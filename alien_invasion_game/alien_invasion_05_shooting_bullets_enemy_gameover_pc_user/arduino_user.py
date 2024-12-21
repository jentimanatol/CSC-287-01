import threading
import serial
import pygame

class ArduinoUser:
    """Class to handle Arduino joystick input."""

    def __init__(self, ship, game):
        """Initialize the Arduino user."""
        self.ship = ship
        self.game = game
        self.joystick_data = {'x': 0, 'y': 0, 'button': 0}
        self.previous_button_state = 0
        self.running = True
        self.last_fire_time = 0
        self.fire_cooldown = 100  # Decreased cooldown period in milliseconds

    def start(self):
        """Start the joystick thread."""
        self.joystick_thread = threading.Thread(target=self._read_joystick_data)
        self.joystick_thread.start()

    def join(self):
        """Wait for the joystick thread to finish."""
        self.joystick_thread.join()

    def _read_joystick_data(self):
        """Read joystick data from the serial port."""
        ser = serial.Serial('COM5', 9600, timeout=1)
        while self.running:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8', errors='ignore').rstrip()
                parts = data.split('|')
                self.joystick_data['x'] = int(parts[0].split(':')[1].strip())
                self.joystick_data['y'] = int(parts[1].split(':')[1].strip())
                self.joystick_data['button'] = int(parts[2].split(':')[1].strip())
                print(f"Joystick data read: {self.joystick_data}")  # Debug statement

    def update(self):
        """Update the ship's position based on joystick data."""
        x = self.joystick_data['x']
        y = self.joystick_data['y']
        button = self.joystick_data['button']
        
        # Define dead zone range
        dead_zone = 100

        if x < (512 - dead_zone):
            self.ship.moving_left = True
            self.ship.moving_right = False
        elif x > (512 + dead_zone):
            self.ship.moving_right = True
            self.ship.moving_left = False
        else:
            self.ship.moving_left = False
            self.ship.moving_right = False

        if y < (512 - dead_zone):
            self.ship.moving_up = True
            self.ship.moving_down = False
        elif y > (512 + dead_zone):
            self.ship.moving_down = True
            self.ship.moving_up = False
        else:
            self.ship.moving_up = False
            self.ship.moving_down = False

        # Fire bullet if button is not pressed and cooldown period has passed
        current_time = pygame.time.get_ticks()
        if button == 0 and (current_time - self.last_fire_time) > self.fire_cooldown:
            self.game._fire_bullet(self.ship)
            self.last_fire_time = current_time
        
        # Update the previous button state
        self.previous_button_state = button

        # Debug statement to check joystick data
        print(f"Joystick data: x={x}, y={y}, button={button}")

    def reset(self):
        """Reset joystick data to initial state."""
        self.joystick_data = {'x': 512, 'y': 512, 'button': 0}
        self.last_fire_time = 0
        self.previous_button_state = 0
        print(f"Joystick data reset to initial state: {self.joystick_data}")
