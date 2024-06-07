import openmeteo_requests
import datetime
import requests_cache
import pandas as pd
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": -21.325613,
    "longitude": -46.366999,
    "hourly": ["temperature_2m", "apparent_temperature"],
    "daily": ["temperature_2m_max", "temperature_2m_min", "apparent_temperature_max", "apparent_temperature_min"],
    "timezone": "America/Sao_Paulo",
    "forecast_days": 1
}
responses = openmeteo.weather_api(url, params=params)

response = responses[0]

hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
hourly_apparent_temperature = hourly.Variables(1).ValuesAsNumpy()

hourly_data = {
    "date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )
}
hourly_data["temperature_2m"] = hourly_temperature_2m
hourly_data["apparent_temperature"] = hourly_apparent_temperature

hourly_dataframe = pd.DataFrame(data=hourly_data)
hourly_dataframe['date'] = hourly_dataframe['date'].dt.tz_convert('America/Sao_Paulo')

hora_atual = datetime.datetime.now().replace(minute=0, second=0, microsecond=0).astimezone(datetime.timezone(datetime.timedelta(hours=-3)))

temperatura_atual = hourly_dataframe.loc[hourly_dataframe['date'] == hora_atual]

daily = response.Daily()
daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
daily_apparent_temperature_max = daily.Variables(2).ValuesAsNumpy()
daily_apparent_temperature_min = daily.Variables(3).ValuesAsNumpy()

print("Temperatura atual:")
if not temperatura_atual.empty:
    print(f"Temperatura: {temperatura_atual['temperature_2m'].values[0]:.2f}°C")
    print(f"Sensação Termica: {temperatura_atual['apparent_temperature'].values[0]:.2f}°C")
else:
    print("No temperature data available for the current hour.")

print("\nTemperaturas diárias:")
print(f"Temperatura Maxima: {daily_temperature_2m_max[0]:.2f}°C")
print(f"Temperatura Minima: {daily_temperature_2m_min[0]:.2f}°C")
print(f"Sensação Termica Maxima: {daily_apparent_temperature_max[0]:.2f}°C")
print(f"Sensação Termica Maxima: {daily_apparent_temperature_min[0]:.2f}°C")
