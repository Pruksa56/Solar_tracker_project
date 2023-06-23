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

# Function to move the servo to a specific angle
def move_servo(angle):
    # Map the angle to a pulse width value
    pulse_width = int((angle / 180) * (max_width - min_width) + min_width)
    servo.duty_u16(pulse_width)

# Move the servo to the initial position (90 degrees)
move_servo(90)

# Rotate the servo motor back and forth until interrupted
try:
    while True:
        for angle in range(0, 180, 10):
            move_servo(angle)
            utime.sleep_ms(500)  # Wait for 500 milliseconds
        for angle in range(180, 0, -10):
            move_servo(angle)
            utime.sleep_ms(500)  # Wait for 500 milliseconds
except KeyboardInterrupt:
    pass  # Continue execution after the KeyboardInterrupt

# Cleanup and stop the servo PWM
servo.deinit()
