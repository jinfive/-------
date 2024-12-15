import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15


# Create an ADS1115 ADC (16-bit) instance.
#adc = Adafruit_ADS1x15.ADS1115()

# Or create an ADS1015 ADC (12-bit) instance.
#adc = Adafruit_ADS1x15.ADS1015()

# Note you can change the I2C address from its default (0x48), andor the I2C
# bus by passing in these optional parameters
adc1 = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)
GAIN = 1

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print(' {06}  {16}  {26}  {36} '.format(range(4)))
print('-'  37)
# Main loop.
while True
    # Read all the ADC channel values in a list.
    values1 = [0]4
    for i in range(4)
        # Read the specified ADC channel using the previously set gain value.
        values1[i] = adc1.read_adc(i, gain=GAIN)
    print(' {06}  {16}  {26}  {36} '.format(values1))
    # Pause for half a second.
    time.sleep(0.1)