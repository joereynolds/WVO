class Weight():


    def __init__(self, value, _type):
        self.value = value
        self.type = _type

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

    def __add__(self, other):
        """Adds two weights together. Note that the unit of measurement
        is not important, i.e. you can add 'lb' and 'kg' together.
        When you add a 'lb' and 'kg together, it will convert
        the 'kg' to 'lb' and add them together"""
        return Weight(
            other.convert(self.type).value + self.value,
            self.type
        )

    def __sub__(self, other):
        """Same as __add__ but subtracts"""
        return Weight(
            self.value - other.convert(self.type).value,
            self.type
        )

    def __repr__(self):
        return str(self.value) + self.type
