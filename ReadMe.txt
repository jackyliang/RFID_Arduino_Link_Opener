1. Download the Arduino IDE
2. Download PySerial @ http://pyserial.sourceforge.net/pyserial.html (this allows Python to speak with the Arduino's serial port)
3. Install Python if your computer does not have it
3. Load RFID.ino into the Arduino IDE and "Upload" it onto the Arduino with the USB cord
4. In Terminal, type "cd <path of TagRecognition.py>" (for example: "cd /Users/Jacky/Desktop/"
5. In Terminal, type in "python TagRecognition.py". This will load the piece of code that reads the tag values and spit out site URLs.
6. Raise tag to the RFID module
7. Use the Omega tag to quit the program (important)

Important: Please configure "default_arduino_port =" in TagRecognition.py

To find the correct port:

Under the Arduino IDE -> "Tools" -> "Serial Port" (It's usually /dev/tty.usbmodemXXX)