# Alien Invasion Game

## Overview

Welcome to **Alien Invasion**, an engaging two-player game where one player uses an Arduino joystick and the other uses keyboard controls. Your mission is to defend against incoming enemy ships and their bullets. The game keeps track of the number of times each player fires and how many times each player dies. Challenge your friends and see who comes out on top!

---

## Features

- **Dual Control Modes**: One player uses an Arduino joystick and the other uses keyboard controls.
- **Enemy Ships**: Randomly appearing enemy ships that fire bullets at the player.
- **Score Tracking**: Keep track of how many times each player fires and dies.
- **Game Over Display**: See the final scores and deaths for both players at the end of the game.
- **Restart Game**: After the game ends, return to the start screen and play again.

---

## Game Controls

### Player 1 (Arduino Joystick)
- **Move**: Control the ship movement using the joystick.
- **Fire**: Press the joystick button to fire bullets.

### Player 2 (Keyboard)
- **Move**: Use the arrow keys (`Up`, `Down`, `Left`, `Right`) to move the ship.
- **Fire**: Press the `Space` bar to fire bullets.
- **Exit**: Press `ESC` to end the game and return to the start screen.

---

## Installation

### Prerequisites

Ensure you have the following installed:
- **Python 3.13.0**: [Download Python](https://www.python.org/downloads/)
- **Pygame**: Install Pygame using the following command:
  ```sh
  pip install pygame
  ```
- **Arduino IDE**: [Download Arduino IDE](https://www.arduino.cc/en/software)
- **Arduino Drivers**: Install the necessary drivers for the Arduino board you are using.

### Setting Up Arduino Environment

1. **Connect Your Arduino Board**: Connect your Arduino board to your computer using a USB cable.
2. **Install Arduino IDE**: Download and install the Arduino IDE.
3. **Install Joystick Library**:
   - In the Arduino IDE, go to `Sketch > Include Library > Manage Libraries...`.
   - Search for "Joystick" and install the library.
4. **Upload Joystick Code to Arduino**:
   - Create a new sketch in the Arduino IDE and paste the following code:
     ```cpp
     #include <Joystick.h>

     const int xPin = A0;
     const int yPin = A1;
     const int buttonPin = 2;

     void setup() {
         Serial.begin(9600);
         pinMode(buttonPin, INPUT_PULLUP);
     }

     void loop() {
         int xValue = analogRead(xPin);
         int yValue = analogRead(yPin);
         int buttonValue = digitalRead(buttonPin);

         Serial.print("x:");
         Serial.print(xValue);
         Serial.print(" | y:");
         Serial.print(yValue);
         Serial.print(" | button:");
         Serial.println(buttonValue);
         delay(100);
     }
     ```
   - Upload the code to your Arduino board.

### Running the Game

1. **Clone the Repository**: Clone or download the repository to your local machine.
2. **Navigate to the Project Directory**: Open a terminal or command prompt and navigate to the project directory.
3. **Run the Game**: Execute the following command to start the game:
   ```sh
   python alien_invasion.py
   ```

---

## Code Overview

### Main Game File: `alien_invasion.py`
This file initializes and runs the game. It handles the main game loop, event checking, and screen updates.

```python
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
```

### Arduino User: `arduino_user.py`
This file handles the input from the Arduino joystick.

```python
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
```

### PC User: `pc_user.py`
This file handles the input from the keyboard.

```python
def check_keydown_events(self, event):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True
    elif event.key == pygame.K_UP:
        self.ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        self.ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        self.game._fire_bullet(self.ship)
```

### Start Screen: `start_screen.py`
The start screen displays the welcome message and game results.

```python
def show(self, results=None):
    """Display the start screen."""
    self.screen.fill(self.settings.bg_color)
    self._draw_text("Welcome to Alien Invasion", 48, self.screen_rect.centerx, self.screen_rect.centery - 50)
    self._draw_text("Press 'Enter' to start", 24, self.screen_rect.centerx, self.screen_rect.centery)
    self._draw_text("Press 'ESC' to exit", 24, self.screen_rect.centerx, self.screen_rect.centery + 30)

    # Display results if provided
    if results:
        self._draw_text(f"Ship1 fired: {results['fire_count1']} times", 24, self.screen_rect.centerx, self.screen_rect.centery + 60)
        self._draw_text(f"Ship2 fired: {results['fire_count2']} times", 24, self.screen_rect.centerx, self.screen_rect.centery + 90)
        self._draw_text(f"Ship1 deaths: {results['ship1_deaths']}", 24, self.screen_rect.centerx, self.screen_rect.centery + 120)
        self._draw_text(f"Ship2 deaths: {results['ship2_deaths']}", 24, self.screen_rect.centerx, self.screen_rect.centery + 150)

    pygame.display.flip()
    self._wait_for_key()
```

---

## Adjusting Game Settings

The `settings.py` file contains various settings to customize the game experience:

```python
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 3.0

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Enemy ship settings
        self.enemy_speed = 1.0

        # Enemy bullet settings
        self.enemy_bullet_speed = 3.0
        self.enemy_bullet_interval = 2000
```

### Customizable Settings
- **Screen Resolution**: Adjust `screen_width` and `screen_height`.
- **Ship Speed**: Modify `ship_speed` to change player movement speed.
- **Bullet Properties**: Customize `bullet_speed`, `bullet_width`, and `bullet_height`.
- **Enemy Ship**: Change `enemy_speed` to adjust their movement.
- **Enemy Bullet**: Tweak `enemy_bullet_speed` and `enemy_bullet_interval`.

---

## Additional Information

Feel free to modify the game settings and code to enhance or customize the experience. If you encounter any issues or have any questions, reach out or open an issue on the repository.

Enjoy the game and good luck defending against the alien invasion!

