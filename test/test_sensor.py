from sensor_data.am2302 import AmSensor


class TestAmSensor:

        '''
        AM2302 sensor testing class
        '''
    def test_transforming_float_data_to_2_decimal(self):
        '''Method to reduce float to 2 decimal numbers to
        after the dot'''
        
        sensor = AmSensor()

        result = sensor.transform_sensor_data(2.34067)
        assert result == 2.34

