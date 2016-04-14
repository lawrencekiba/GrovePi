#!/usr/bin/env python
#
# GrovePi Example for using the Grove Dry Reed Relay (http://www.seeedstudio.com/wiki/Grove_-_Dry-Reed_Relay)
#
#
# GrovePi is an electronics board designed by Dexter Industries that you can connect to hundreds of 
# different sensors, so you can program them to monitor, control, and automate devices in your life.  
# See more about the GrovePi here:  http://www.dexterindustries.com/grovepi/
#
#
# Have a question about this example?  Ask on the forums here:  http://www.dexterindustries.com/forum/?forum=grovepi
#

'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2016  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import time
import grovepi

# Connect the Grove Dry Reed Relay to digital port D4
# SIG,NC,VCC,GND
relay = 4

# Relay is normally open. LED will illuminate when closed and there is no clicking sound

grovepi.pinMode(relay,"OUTPUT")

while True:
    try:
        # switch on for 5 seconds
        grovepi.digitalWrite(relay,1)
        print ("on")
        time.sleep(5)

        # switch off for 5 seconds
        grovepi.digitalWrite(relay,0)
        print ("off")
        time.sleep(5)

    except KeyboardInterrupt:
        grovepi.digitalWrite(relay,0)
        break
    except IOError:
        print ("Error")
