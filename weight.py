class Weight():


    MEASUREMENTS = {
        'lb': 'pounds(lb)'
    }

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def convert(self, measurement):
        conversion_table = {
            'lb': {
                'kg': self.value * 0.45359237,
                'lb': self.value
            },
            'kg': {
                'lb': self.value / 0.45359237,
                'kg': self.value
            }
        }

        return Weight(conversion_table[self.type][measurement], measurement)

    def measurement(self):
        return Weight.MEASUREMENTS[self.type]
