import machine
import utime

# Configure the servo motor pin
servo_pin = machine.Pin(15)
servo = machine.PWM(servo_pin)

# Set the frequency of the servo (50 Hz is commonly used)
servo.freq(50)

# Define the pulse width range for the servo motor
# These values may need to be adjusted for your specific servo
min_width = 600  # Minimum pulse width
max_width = 2400  # Maximum pulse width

# Configure the potentiometer pin
potentiometer_pin = machine.ADC(26)

# Function to map a value from one range to another
def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# Function to move the servo based on the potentiometer input
def move_servo_by_potentiometer():
    pot_value = potentiometer_pin.read_u16()
    angle = map_value(pot_value, 0, 65535, 0, 180)
    pulse_width = int((angle / 180) * (max_width - min_width) + min_width)
    servo.duty_u16(pulse_width)

# Move the servo based on the potentiometer input
while True:
    move_servo_by_potentiometer()
    utime.sleep_ms(20)  # Adjust the delay as needed
