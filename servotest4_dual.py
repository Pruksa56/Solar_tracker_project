import machine
import utime

# Configure servo motor pins
servo1_pin = machine.Pin(15)  # GPIO 31 (ADC0)
servo2_pin = machine.Pin(16)  # GPIO 32 (ADC1)

# Configure ADC pins
adc1 = machine.ADC(machine.Pin(26))  # GPIO 26 (ADC1)
adc2 = machine.ADC(machine.Pin(27))  # GPIO 27 (ADC2)

# Set the frequency of the servo motors (50 Hz is commonly used)
servo_freq = 55

# Define the pulse width range for the servo motors
# These values may need to be adjusted for your specific servos
min_width = 600  # Minimum pulse width
max_width = 2400  # Maximum pulse width

# Function to move a servo to a specific angle
def move_servo(servo, angle):
    # Map the angle to a pulse width value
    pulse_width = int((angle / 90) * (max_width - min_width) + min_width)
    servo.duty_u16(pulse_width)

# Create servo objects
servo1 = machine.PWM(servo1_pin)
servo2 = machine.PWM(servo2_pin)
servo1.freq(servo_freq)
servo2.freq(servo_freq)

# Rotate the servo motors based on analog input readings
while True:
    # Read analog inputs
    input1 = adc1.read_u16()
    input2 = adc2.read_u16()

    # Convert analog readings to servo angles (0-180 degrees)
    angle1 = int((input1 / 65535) * 360)
    angle2 = int((input2 / 65535) * 360)

    # Move servo1 to angle1 and servo2 to angle2
    move_servo(servo1, angle1)
    move_servo(servo2, angle2)

    # Delay between servo movements
        
    print("Angle1:",angle1)
    print("Angle2:",angle2)
    
    utime.sleep_ms(50)
