class Weight():

    def __init__(self, value, _type):
        self.value = value
        self.type = _type

    def convert(self, measurement):
        """
        Converts one unit of measurement to another, i.e.
        Weight(5, 'lb').convert('kg') -> Weight(2.2679618500000003, 'kg')
        """
        conversion_table = {
            'lb': {
                'kg': self.value * 0.45359237,
                'lb': self.value,
                'oz': self.value * 16
            },
            'g' : {
                'kg': self.value / 1000,
                'lb': self.value * 0.0022046
            },
            'kg': {
                'lb': self.value / 0.45359237,
                'kg': self.value,
                'g': self.value / 0.0010000
            },
            'oz': {
                'oz': self.value
            }
        }

        return Weight(conversion_table[self.type][measurement], measurement)

    def __add__(self, other):
        """
        Weight(5, 'lb') + Weight(6, 'kg') -> Weight(18.227735731092654, 'lb')
        Weight(6, 'kg') + Weight(5, 'lb') -> Weight(8.26796185, 'kg')
        """
        return Weight(
            other.convert(self.type).value + self.value,
            self.type
        )

    def __sub__(self, other):
        """Same as addition."""
        return Weight(
            self.value - other.convert(self.type).value,
            self.type
        )
