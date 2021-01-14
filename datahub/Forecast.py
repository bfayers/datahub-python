from datahub.Helpers import weather_codes, split_days
from datetime import datetime

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
        if frequency == "daily":
            #Format for daily frequency
            for day in self.response['features'][0]['properties']['timeSeries']:
                self.days.append({
                    "time": day['time'],
                    "daySignificantWeather": weather_codes[day['daySignificantWeatherCode']],
                    "nightSignificantWeather": weather_codes[day['nightSignificantWeatherCode']],
                    #Wind Speed
                    #Midday
                    "middayWindSpeed": day['midday10MWindSpeed'],
                    "middayWindDirection": day['midday10MWindDirection'],
                    "middayWindGust": day['midday10MWindGust'],
                    #Midnight
                    "midnightWindSpeed": day['midnight10MWindSpeed'],
                    "midnightWindDirection": day['midnight10MWindDirection'],
                    "midnightWindGust": day['midnight10MWindGust'],
                    #Visibility
                    #Midday
                    "middayVisibility": day['middayVisibility'],
                    #Midnight
                    "midnightVisibility": day['midnightVisibility'],
                    #Relative Humidity
                    "middayRelativeHumidity": day['middayRelativeHumidity'],
                    "midnightRelativeHumidity": day['midnightRelativeHumidity'],
                    #Pressure (divided by 100 o make it into hPa)
                    "middayPressure": day['middayMslp']/100,
                    "midnightPressure": day['midnightMslp']/100,
                    #UV
                    "maxUVIndex": day['maxUvIndex'],
                    #Temperatures
                    "maxTemperature": day['dayMaxScreenTemperature'],
                    "minTemperature": day['nightMinScreenTemperature'],
                    "maxFeelsLike": day['dayMaxFeelsLikeTemp'],
                    "minFeelsLike": day['nightMinFeelsLikeTemp'],
                    #Precipitation
                    #Day
                    "dayProbabilityOfPrecipitation": day['dayProbabilityOfPrecipitation'],
                    "dayProbabilityOfSnow": day['dayProbabilityOfSnow'],
                    "dayProbabilityOfHeavySnow": day['dayProbabilityOfHeavySnow'],
                    "dayProbabilityOfRain": day['dayProbabilityOfRain'],
                    "dayProbabilityOfHeavyRain": day['dayProbabilityOfHeavyRain'],
                    "dayProbabilityOfHail": day['dayProbabilityOfHail'],
                    #Night
                    "nightProbabilityOfPrecipitation": day['nightProbabilityOfPrecipitation'],
                    "nightProbabilityOfSnow": day['nightProbabilityOfSnow'],
                    "nightProbabilityOfHeavySnow": day['nightProbabilityOfHeavySnow'],
                    "nightProbabilityOfRain": day['nightProbabilityOfRain'],
                    "nightProbabilityOfHeavyRain": day['nightProbabilityOfHeavyRain'],
                    "nightProbabilityOfHail": day['nightProbabilityOfHail']
                })
        else:
            #Split hourly and three hourly time series into days
            time_series = self.response['features'][0]['properties']['timeSeries']
            self.days = split_days(time_series)

            #Convert mslp to hPa
            for day in self.days:
                for hour in day:
                    #Change "significantWeatherCode" to "significantWeather"
                    hour['mslp'] = hour.pop('mslp')/100
                    
                    if frequency == "hourly":
                        #Change "significantWeatherCode" to "significantWeather"
                        hour['significantWeather'] = weather_codes[hour.pop('significantWeatherCode')]