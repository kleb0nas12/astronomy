from sensor_data.am2302_pi import AmSensor
from ecxeptionlist import TooLowHighTempError
import pytest
from unittest.mock import patch

class TestAmSensor:

    @pytest.mark.parametrize('number, expected', [
        (2.34067, 2.34), (32.07256, 32.07), (-12.2589, -12.26)
    ])
    def test_transforming_float_data_to_2_decimal(self, number, expected):
        '''Method to test reduce float to 2 decimal numbers to
        after the decimal'''

        sensor = AmSensor()

        result = sensor.transform_sensor_data(number)
        assert result == expected

    def test_mock_read_sensor(self, mocker):
        mocker.patch('am2302_pi.Adafruit_DHT.read_retry',
                     return_value=(20.589, 28.689), autospec=True)
        _sensor = AmSensor()
        assert _sensor.read_sensor_data() == (20.59, 28.69)

# #     @patch('sensor_data.am2302_pi.Adafruit_DHT.read_retry', new = mocked_current_reading)
# #     def test_main_function(self):

# #         result = AmSensor.read_sensor_data()
# #         truth = (20.59, 88.69)
# #         assert result == truth
# #     def mocked_current_reading(self):
# #         return (20.589, 88.689)
# def current_reading():
#     return (20.589, 88.689)

# @patch('sensor_data.am2302_pi.Adafruit_DHT.read_retry', new=current_reading)
# def test_main_function():
#     data= AmSensor()
#     result = data.read_sensor_data()
#     truth = (20.59, 88.69)
#     assert result == truth


# def current_reading():
#     return (20.589, 28.689)

# @patch('sensor_data.am2302_pi.read_retry')
# def test_main_function(mock):
#     mock.return_value = current_reading()
#     data= AmSensor()
#     result = data.read_sensor_data()
#     truth = (20.59, 28.69)
#     assert result == truth

