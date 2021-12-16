import datafortest.datafortest as data
from models import OwmWeather


class TestModels:
    daily = OwmWeather(data.daily)
    forecast = OwmWeather(data.forecast['list'][0])

    def test_daily_types(self):
        assert isinstance(self.daily.get_daily(), str)

    def test_daily_value(self):
        assert self.daily.location == 'Москва'

    def test_forecast_types(self):
        assert isinstance(self.forecast.get_daily(), str)

    def test_forecast_value(self):
        assert self.forecast.location == 'no name'
