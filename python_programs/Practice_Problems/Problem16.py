# # Write a program that will determine weather when the value of 
# temperature and humidity is provided by the user.
# TEMPERATURE(C)      HUMIDITY(%)       WEATHER

#       >= 30         >=90              Hot and Humid
#       >= 30         < 90              Hot
#       <30           >= 90             Cool and Humid
#       <30           <90               Cool

class WeatherPredictor:
    def weather_prediction(self, Humidity, Temperature):
        self.Temperature = Temperature
        self.Humid = Humidity
        
        if Temperature >= 30 and Humidity >= 90:
            print("Weather is Hot and Humid")
        elif Temperature >= 30 and Humidity < 90:
            print("Weather is Hot")
        elif Temperature < 30 and Humidity >= 90:
            print("Weather is Cool and Humid")    
        elif Temperature < 30 and Humidity < 90:
            print("Weather is Cool")
        else:
            print("Invalid Inputs")

# Creating an instance of the class
weather_predictor_instance = WeatherPredictor()

# Calling the method using the instance
weather_predictor_instance.weather_prediction(90, 30)


# def weather_prediction(Humidity, Temperature):
#     if Temperature >= 30 and Humidity >= 90:
#         print("Weather is Hot and Humid")
#     elif Temperature >= 30 and Humidity < 90:
#         print("Weather is Hot")
#     elif Temperature < 30 and Humidity >= 90:
#         print("Weather is Cool and Humid")    
#     elif Temperature < 30 and Humidity < 90:
#         print("Weather is Cool")
#     else:
#         print("Invalid Inputs")

# # Calling the function
# weather_prediction(90, 30)

