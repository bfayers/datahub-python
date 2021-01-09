from datahub.Helpers import weather_codes

class Forecast():
    def __init__(self, frequency=None, response=None):
        if frequency is None:
            raise Exception("No frequency provided")
        if response is None:
            raise Exception("No response provided")
        self.frequency = frequency
        if response.status_code != 200:
            raise Exception("Response not OK")
        
        self.response = response.json()

        #Format incoming response
        self.days = []
        for day in self.response['features'][0]['properties']['timeSeries']:
            self.days.append({
                "time": day['time'],
                "daySignificantWeather": weather_codes[day['daySignificantWeatherCode']],
                "nightSignificantWeather": weather_codes[day['nightSignificantWeatherCode']]
            })