from sensor_data.am2302_pi import AmSensor
from manual_exceptions import TooLowHighTempError
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
        ''' Test sensor temp and humidy data with pytest-mock'''
        mocker.patch('sensor_data.am2302_pi.Adafruit_DHT.read_retry',
                     return_value=(20.589, 28.689), autospec=True)
        _sensor = AmSensor()
        assert _sensor.read_sensor_data() == (20.59, 28.69)



    def test_mock_read_sensor_raised_exception(self, mocker):
        ''' Code to test abnormal temp level exception'''
        mocker.patch('sensor_data.am2302_pi.Adafruit_DHT.read_retry', return_value=(20.589, 22.689),side_effect = TooLowHighTempError(88.69))
        with pytest.raises(TooLowHighTempError) as excinfo:
            _sensor = AmSensor()
            _sensor.read_sensor_data()
        assert str(excinfo.value) == 'The temperature has reached abnormal level of 88.69! please check the  equipment'
        


    ### Now without pytest-mock , but using unittest-mock.
    def mocked_adafruit_sensor_data(self):
        ''' Mock our adafruit sensor function to return some data values'''
        return 20.589, 28.689


    @patch('sensor_data.am2302_pi.Adafruit_DHT.read_retry', return_value=(20.589, 22.689) )#new = mocked_adafruit_sensor_data)
    def test_that_mock_works(self):
        _sensor = AmSensor() 
        result = _sensor.read_sensor_data()
        truth = (20.59, 28.69)
        assert result == truth


    @patch('sensor_data.am2302_pi.Adafruit_DHT.read_retry', new = TestAmSensor().mocked_adafruit_sensor_data)
    def test_mock_read_sensor_with_unittest(self):
        _sensor = AmSensor()
        assert _sensor.read_sensor_data() == (20.59, 28.69)



