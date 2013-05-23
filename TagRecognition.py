#!/usr/bin/env python

# python code for the Arduino
# 
# This program receives RFID tag numbers sent from an Arduino connected via USB.
# the tag is number is used to lookup the address of the web site associated
# with the tag. the program then opens a new tab in a web browser for that site.
# if an unknown tag is read, a small HTML file is constructed with an error
# message and the tag number. a new tab is opened in a web browser and the error
# information is displayed.  this error message can be used to for adding new tages:
# the tag number can be copied by the user and added to the dictionary and 
# associated with a new web site.

import sys            # library for system functions
import serial         # library for connecting to the Arduino
import shlex          # library for parsing text data
import webbrowser     # library for opening web pages in a browser

# this dictionary is used to map RFID tag numbers to web sites
# to add a new tag, duplicate the last line and modify the tag and
# web site address (url)

tag_url_dictionary = {  
     '35021C81BD' : 'quit'  
    ,'3501D5CD4F' : 'http://www.workarea.com' 
    ,'35021EC0B7' : 'http://store.americanapparel.net/product/index.jsp?productId=rsabnr&c=rose'
    ,'35021E5DEB' : 'http://www.thenorthface.com/catalog/sc-gear/mens-collections-summit-series-0174/men-39-s-elysium-jacket.html'
    ,'35021E755B' : 'http://www.uniqlo.com/us/store/made-for-all/men-washed-flat-front-chino-pants/072492-57-035'
    ,'35021E68BD' : 'http://store.nike.com/us/en_us/product/lunarglide-4-id-running-shoe/#?mid=406403505&sitesrc=dl_usid'
    ,'35021E8E1E' : 'http://www.gotti.ch/en/collection/LOREN'
    ,'35021ED2EF' : 'http://www.chocoolate.hk/productDetail.php?productID=1379'
    ,'35021E646E' : 'http://www.freepeople.com/shoes-sneakers/americana-chucks/'
  }

# default port for the arduino for my system - update to match your system
default_arduino_port = "/dev/tty.usbmodem621"

# name of the file used for constructing error messages when tags not in the
# dictionary have been read.  this file will be created in the same directory
# as this program is located.
error_file = 'Unknown tag, try adding it to the database.'

# main program for reading and processing tags
def main(arduino = default_arduino_port):      
  print "Connecting to Arduino on port ", arduino
  try:
    ser = serial.Serial(arduino, timeout=1)                 # connect to the Arduino
    print "Successfully connected to Arduino on ", arduino
    arduino_opened = 1
  except:
    print "Failed to connect Arduino on port ", arduino
    arduino_opened = 0

  # if the Arduino was successfully connected, start reading and processing tags    
  if arduino_opened:

    previous_rfid_tag = ''  # used for identifying whether the same tag has been read
  
    while 1:    # loop forever until a "quit" tag is read
  
      ser.flushInput()                    # flush any extra data from the serial port
      rfid_data = ser.readline().strip()  # read the  rfid data 

      # if data has been received
      if len(rfid_data) > 0:

        # parse the rfid data. rfid data contains three values:
        # <number of tags read>, <time in millisconds tag was read>, <tag value>
        parsed_rfid_data = shlex.shlex(rfid_data, posix=True)
        parsed_rfid_data.whitespace += ','
        parsed_rfid_data.whitespace_split = True
        rfid_data_list = list(parsed_rfid_data)
        print rfid_data_list

        # using the tag number, lookup the corresponding web site address
        url = translate_tag_to_url(tag_url_dictionary, rfid_data_list[2]);
        print "tag = ", rfid_data_list[2], " url = ", url

        # check to see if the 'quit' tag was just read and if so stop the program
        if url == 'quit':
          break
        else:
          # if the last tag is different than the last one read, open the web page
          # ignore the tag is it was the same one as the one last read
          if rfid_data_list[2] != previous_rfid_tag:
            webbrowser.open(url)                   # open the web site in a new tab in the default browser
            previous_rfid_tag = rfid_data_list[2]  # remember what tag was just read    

# this function uses the tag number to look up the web site address (url)from the RFID tag number
def translate_tag_to_url(tag_dictionary, tag):

  if tag_dictionary.has_key(tag): # see if the tag is in the dictionary
    return tag_dictionary[tag]    # it's there so return the url associated with the tag
  else:    # tag isn't defined - build a HTML page with the error message in a temporary file
    # build the HTML file for the error message: it will look like "RFID tag not in the dictionary: xxxxxxxxxx"
    # where xxxxxxxxxx is the tag number.
    error_msg = '<html><title>Error Message</title><body><font size="+3">'
    error_msg = error_msg + 'RFID tag not in the dictionary: ' + tag
    error_msg = error_msg + '</font></body></html>'
    f = open(error_file, 'w')   # open the file for writing
    f.writelines(error_msg)     # write the error message
    f.close                     # close the file
    return error_file           # return the file name

# this code enables starting the program from the command line
if __name__ == '__main__':
  if (len(sys.argv) > 1):
    main(sys.argv[1])
  else:
    main()
