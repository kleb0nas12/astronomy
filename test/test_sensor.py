from sensor_data.am2302_pi import AmSensor
from ecxeptionlist import TooLowHighTempError
import pytest

class TestAmSensor:


    @pytest.mark.parametrize('number, expected',[
        (2.34067,2.34),(32.07256,32.07),(-12.2589,-12.26)
    ])
    def test_transforming_float_data_to_2_decimal(self,number,expected):
        '''Method to reduce float to 2 decimal numbers to
        after the dot'''
        
        sensor = AmSensor()

        result = sensor.transform_sensor_data(number)
        assert result == expected

    def test_abnormal_high_temp_error(self):
        sensor = AmSensor()
        with pytest.raises(TooLowHighTempError) as context:
            result = sensor.transform_sensor_data(50)
    
    def test_abnormal_low_temp_error(self):
        sensor = AmSensor()
        with pytest.raises(TooLowHighTempError) as context:
            result = sensor.transform_sensor_data(-40)


