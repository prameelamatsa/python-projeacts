import requests
import streamlit as st

st.title("Weather App")

col1, col2 = st.columns([3, 1])
with col1:
  city_name = st.text_input(
      "Enter city name:", placeholder="e.g. London, Tokyo, New York"
  )
with col2:
  unit_choice = st.radio("Select unit:", ("Celsius", "Fahrenheit"))

units_parmeter = "metric" if unit_choice == "Celsius" else "imperial"
units_symbol = "°C" if unit_choice == "Celsius" else "°F"
API_KEY = "85e5299774e7959ba5eac3a357ed6e56"

if st.button("get weather"):
  if city_name.strip() == "":
    st.error("Please enter a city name.")
  else:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units={units_parmeter}"
    try:
      response = requests.get(url, timeout=5)
      if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        icon_code = data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"

        st.success(f"Weather in {city_name}:")

        # Display Metrics in columns
        m_col1, m_col2 = st.columns(2)
        with m_col1:
          st.metric(label="Temperature", value=f"{temperature} {units_symbol}")
        with m_col2:
          st.metric(label="Humidity", value=f"{humidity} %")

        st.info(f"Weather Description: {description}")
        st.image(icon_url, caption="Weather Icon", width=100)

        # Forecast Request
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units={units_parmeter}"
        forecast_response = requests.get(forecast_url, timeout=5)

        if forecast_response.status_code == 200:
          st.markdown("---")
          st.subheader("5-Day Forecast (Next 12 Hours):")
          forecast_data = forecast_response.json()
          forecast_list = forecast_data["list"][:4]

          # Create columns for the forecast items
          f_cols = st.columns(len(forecast_list))

          for idx, item in enumerate(forecast_list):
            time_txt = item["dt_txt"].split(" ")[1][:5]
            f_temperature = item["main"]["temp"]
            f_icon_code = item["weather"][0]["icon"]
            f_icon_url = f"http://openweathermap.org/img/wn/{f_icon_code}.png"

            with f_cols[idx]:
              st.caption(f"⏰ {time_txt}")
              st.image(f_icon_url, width=50)
              st.write(f"**{f_temperature} {units_symbol}**")
        else:
          st.error("Could not retrieve forecast data.")

      elif response.status_code == 404:
        st.error("City not found. Please check the city name and try again.")
      else:
        st.error("API request failed.")

    except requests.exceptions.RequestException as e:
      st.error(f"An error occurred: {e}")


