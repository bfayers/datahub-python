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

        #Weather codes = 
        weather_codes = {
            0: "Clear night",
            1: "Sunny day",
            2: "Partly cloudy (night)",
            3: "Partly cloudy (day)",
            4: "Not used",
            5: "Mist",
            6: "Fog",
            7: "Cloudy",
            8: "Overcast",
            9: "Light rain shower (night)",
            10: "Light rain shower (day)",
            11: "Drizzle",
            12: "Light rain",
            13: "Heavy rain shower (night)",
            14: "Heavy rain shower (day)",
            15: "Heavy rain",
            16: "Sleet shower (night)",
            17: "Sleet shower (day)",
            18: "Sleet",
            19: "Hail shower (night)",
            20: "Hail shower (day)",
            21: "Hail",
            22: "Light snow shower (night)",
            23: "Light snow shower (day)",
            24: "Light snow",
            25: "Heavy snow shower (night)",
            26: "Heavy snow shower (day)",
            27: "Heavy snow",
            28: "Thunder shower (night)",
            29: "Thunder shower (day)",
            30: "Thunder"
        }
        #Format incoming response
        self.days = []
        for day in self.response['features'][0]['properties']['timeSeries']:
            self.days.append({
                "time": day['time'],
                "daySignificantWeather": weather_codes[day['daySignificantWeatherCode']],
                "nightSignificantWeather": weather_codes[day['nightSignificantWeatherCode']]
            })