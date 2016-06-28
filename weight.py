

class Weight():


    MEASUREMENTS = {
        'lb': 'pounds'
    }

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def convert(self, measurement):
        #return Weight(converted_value, measurement)
        pass

    def measurement(self):
        return Weight.MEASUREMENTS[self.type]


