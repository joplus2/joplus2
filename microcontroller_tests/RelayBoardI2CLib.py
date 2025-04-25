"""
Library for "YourCee" relay board using I2C
Written by joplus - github.com/joplus2

Class relay has these arguments:
i2c - I2C object
number - number of relays (def. 2)
address - I2C address (def. 32)
memory - which mem to write / read (def. 6)
"""

class relay:
    def __init__(self, i2c, number=2, address=32, memory=6):
        if (number <= 0 or address <= 0 or memory <= 0):
            raise ValueError("All numbers must be >0!")
        self.iic = i2c
        self.num = number
        self.addr = address
        self.mem = memory
        
    def on(self, rel):
        if (rel > self.num):
            raise ValueError("Relay number exceeded number of relays!")
        if (rel <= 0):
            raise ValueError("Relay number must be >0!")
        rel = rel-1
        state = self.iic.readfrom_mem(32,6,1)
        binary = int(list(state)[0])
        bits = binary & ~(1<<rel)
        self.iic.writeto_mem(self.addr, self.mem, bytes([bits]))
        
    def off(self, rel):
        if (rel > self.num):
            raise ValueError("Relay number exceeded number of relays!")
        if (rel <= 0):
            raise ValueError("Relay number must be >0!")
        rel = rel-1
        state = self.iic.readfrom_mem(32,6,1)
        binary = int(list(state)[0])
        bits = binary | (1<<rel)
        self.iic.writeto_mem(self.addr, self.mem, bytes([bits]))
        
