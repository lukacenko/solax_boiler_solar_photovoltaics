import RPi.GPIO as GPIO
import time
import requests
channel = 21
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)
def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on
def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off
	
response = requests.get("https://www.solaxcloud.com/proxyApp/proxy/api/getRealtimeInfo.do?tokenId=202207161542249917581112&sn=SXBQKMNEDD")
#response.content()
r = response.json()
vykon = r['result']['acpower']
print("Vykon je: ", vykon, " Watt")
motor_on(channel)
time.sleep(1)
motor_off(channel)
time.sleep(1)
if vykon > 1000:
  print("ZAPNE BOJLER")
  #GPIO.output(11, GPIO.HIGH) 
else: 
  print("VYPNE BOJLER")
  #GPIO.output(11, GPIO.LOW)		

#GPIO.cleanup()
		
		



