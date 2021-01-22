import bluetooth
import Adafruit_DHT
import time

serverMACAddress = 'B8:27:EB:C8:8E:2E'
#serverMACAddress = 'B8:27:EB:97:CB:E1' # for the threadingserver .199
port = 2
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))


sensor = Adafruit_DHT.DHT22

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
#pin = 'P8_11'

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
while True:
    #humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    th= 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
    print(th)
    #text = input()
    s.send(th)
    time.sleep(1)
s.close()
    
    
    
    


# while 1:



