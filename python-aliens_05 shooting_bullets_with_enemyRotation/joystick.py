import serial

def read_joystick_data(ai_game):
    """Read joystick data from the serial port."""
    ser = serial.Serial('COM3', 9600, timeout=1)
    while ai_game.running:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8', errors='ignore').rstrip()
            parts = data.split('|')
            ai_game.joystick_data['x'] = int(parts[0].split(':')[1].strip())
            ai_game.joystick_data['y'] = int(parts[1].split(':')[1].strip())
            ai_game.joystick_data['button'] = int(parts[2].split(':')[1].strip())
            print(f"Joystick data read: {ai_game.joystick_data}")  # Debug statement
