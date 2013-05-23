// Arduino Internet Gizmo: instructable by talk2bruce
// This program reads RFID card tag id from a Parallax RFID card reader 
// and send that information to a PC connected using a serial connection (USB).
// A program on the PC looks up the tag id in a table to find the name of the
// web site associated with this tag.  The PC program then opens that web site
// in a new tab on the browser.

#include <SoftwareSerial.h>  // library used to read from the RFID reader

#define NO_SUCH_PIN 255      // non-existent pin
#define RFID_OUT_PIN 2       // (YELL 2) pin used to read data from the RFID reader
#define RFID_ENABLE_PIN 4    // (BLU to 4) pin used to tell RFID reader to read tags

SoftwareSerial rfid_reader(RFID_OUT_PIN, NO_SUCH_PIN); // Setup the serial port for the RFID reader
int val = 0;                 // used for holding the byte just read from the reader
char code[10];               // used for holding the entire tag id that was just read 
int bytes_read = 0;          // used for counting the number of tag bytes read          
int tags_read = 0;           // used to count the number of tags read
unsigned long time;          // used to remember the time that the tag was read
                             // the time is milliseconds since the Arduino was last reset
//
// Intialize the Arduino Internet Gizmo
//
void setup() {
  Serial.begin(9600);                     // initialize the serial port used to write to the PC
  rfid_reader.begin(2400);                // initialize the serial port for reading RFID tags              
  pinMode(RFID_ENABLE_PIN, OUTPUT);       // set the pin to enable the RFID reader to output    
  digitalWrite(RFID_ENABLE_PIN, LOW);     // tell the RFID reader to start reading tags 
}  

//
// Loop forever reading tags and sending data to the PC
//
void loop() { 
  if(rfid_reader.available() > 0) {         // check to see if data is available from the reader    
    if((val = rfid_reader.read()) == 10) {  // check for a "start of data" byte
      bytes_read = 0; 
      while(bytes_read < 10) {              // if less than 10 bytes have been read, keep reading 
        if( rfid_reader.available() > 0) {  // if a new byte has been read
          val = rfid_reader.read();         // read the byte
          if((val == 10)||(val == 13)) {    // if header or stop bytes before the 10 digit reading 
            break;                          // stop reading 
          } 
          code[bytes_read] = val;           // add the data read to the tag variable          
          bytes_read++;                     // increment the number of bytes read and keep reading  
        } 
      } 
      if(bytes_read == 10) {                // if all of the bytes in the tag have been read 
        tags_read++;                        // increment the number of tags read
        time = millis();                    // record the time the tag was read
        Serial.print(tags_read);            // send the number of tags read to the PC
        Serial.print(",");                  // send a comma
        Serial.print(time);                 // send the time the tag was read
        Serial.print(",");                  // send a comma
        Serial.print(code);                 // send the RFID card tag       
      } 
      bytes_read = 0;                       // reset the number of bytes read
      digitalWrite(RFID_ENABLE_PIN, HIGH);  // deactivate the RFID reader for a moment
      digitalWrite(RFID_ENABLE_PIN, LOW);   // re-enable the RFID reader to read tags
    } 
  } 
}

