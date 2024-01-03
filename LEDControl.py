import time
import network
from machine import Pin
import BlynkLib
 
led1=Pin(1, Pin.OUT)
led2=Pin(2, Pin.OUT)
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("maitraiyee","maitraiyee01")
 
BLYNK_AUTH = 'VGUWwpYC6Vr0eDfh-kfpLpL5cQ74hH1y'
 
# connect the network       
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    ip=wlan.ifconfig()[0]
    print('IP: ', ip)
    
 
"Connection to Blynk"
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
 
# Register virtual pin handler
@blynk.on("V0") #virtual pin V0
def v0_write_handler(value): #read the value
    if int(value[0]) == 1:
        led1.value(1) #turn the led on        
    else:
        led1.value(0)    #turn the led off
        
@blynk.on("V1") #virtual pin V0
def v1_write_handler(value): #read the value
    if int(value[0]) == 1:
        led2.value(1) #turn the led on        
    else:
        led2.value(0)    #turn the led off        
while True:
    blynk.run()