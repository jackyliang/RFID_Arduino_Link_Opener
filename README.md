# RFID and Arduino Browser Navigator

A simple Python proof-of-concept on how to control the computer using the Arduino and a RFID shield + tags. This proof of concept allows you to control your web browser using pre-defined RFID tags. One of my first programming projects, circa 2012. 

## Installation: 

1. Download the Arduino IDE
2. Download [PySerial](http://pyserial.sourceforge.net/pyserial.html) (this allows Python to speak with the Arduino's serial port)
3. Install the latest version of Python
3. Load `RFID.ino` into the Arduino IDE and upload to the Arduino
4. Navigate to the path of `TagRecognition.py`, i.e. `cd /Users/Jacky/Desktop/TagRecognition.py`
5. `python TagRecognition.py`
6. Raise tag to the RFID module
7. Use the Omega tag to quit the program (important)

Important: Please define the correct serial port `default_arduino_port =` within `TagRecognition.py`

To find the correct port:

Under the `Arduino IDE` -> `Tools` -> `Serial Port` (It's usually `/dev/tty.usbmodemXXX`)

## License

MIT license. 
