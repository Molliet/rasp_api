
# This file will be used when deploying to Raspberry Pi
# Uncomment and implement when you have the hardware

class GPIOController:
    def __init__(self):
        # import RPi.GPIO as GPIO
        # GPIO.setmode(GPIO.BCM)
        pass
    
    def setup_pin(self, pin: int, mode: str):
        """Setup GPIO pin as input or output"""
        # GPIO.setup(pin, GPIO.OUT if mode == "output" else GPIO.IN)
        pass
    
    def set_pin_high(self, pin: int):
        """Set pin to HIGH"""
        # GPIO.output(pin, GPIO.HIGH)
        pass
    
    def set_pin_low(self, pin: int):
        """Set pin to LOW"""
        # GPIO.output(pin, GPIO.LOW)
        pass
    
    def read_pin(self, pin: int):
        """Read pin value"""
        # return GPIO.input(pin)
        pass
    
    def cleanup(self):
        """Cleanup GPIO"""
        # GPIO.cleanup()
        pass

gpio_controller = GPIOController()

