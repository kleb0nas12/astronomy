class TooLowHighTempError(Exception):
    def __init__(self, temp):
        self.temp = temp
    
    def __str__(self):
        return f'The temperature has reached abnormal level of {self.temp}! please check the  equipment'

    