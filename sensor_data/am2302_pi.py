import Adafruit_DHT 
#from manual_exceptions import TooLowHighTempError
import manual_exceptions
import time


class AmSensor(object):

    '''
    A class to get data from Am2302 sensor connected
    to a raspberi pi.  
    '''
    # pinout location
    # getting data from sensor
    def read_sensor_data(self) -> tuple:
        DHT_SENSOR = Adafruit_DHT.DHT22
        DHT_PIN = 18
        try:
            humidity, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            humidity = self.transform_sensor_data(humidity)
            temp = self.transform_sensor_data(temp)
            print(humidity, temp)
            if int(temp) < -30 or int(temp) > 60:
                raise manual_exceptions.TooLowHighTempError(temp)
            return humidity, temp
        except Exception as e:
            print(f'Problem has appeared with the exception {e}')


    # transforming data to the nearest second number after the decimal
    def transform_sensor_data(self, data: float) -> float:
        return round(data, 2)




if __name__==__main__:
    s = AmSensor()
    print('fuck you')
