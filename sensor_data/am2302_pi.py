import Adafruit_DHT  # Adafruit library fro RPi
import time


class AmSensor(object):

    '''
    A class to get data from Am2302 sensor connected
    to a raspberi pi.  
    '''
    # pinout location
    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN = 18

    # getting data from sensor
    def read_sensor_data(self) -> tuple:
        try:
            humidity, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            return humidity, temp
        except Exception as e:
            print(f'Problem has appeared with the exception {e}')

    # transforming data to the nearest second number after the decimal
    def transform_sensor_data(self, data: float) -> float:
        return round(data, 2)
