'''
Here we define Manual Error classes and usuage for abnormal or/and uneven events.
'''


class TooLowHighTempError(Exception):
    '''
    Error to inform about abnormal temperature events.
    '''
    def __init__(self, temp):
        self.temp = temp
    
    def __str__(self):
        return f'The temperature has reached abnormal level of {self.temp}! please check the  equipment'

    