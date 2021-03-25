import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO
import time
GPIO.setmode( GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

def ejecutar():
	GPIO.output(7, False)
	c="sensor inactivo"
	mqttc.publish("654hector1@gmail.com/test", c)
	print (c)
	
def luz1On():
	GPIO.output(7, True)
	time.sleep(0.5)
	c=("1")
	mqttc.publish("654hector1@gmail.com/test", c)

def luzOff():
	GPIO.output(7, False)
	time.sleep(1)
	c=("0")
	mqttc.publish("654hector1@gmail.com/test", c)


def on_message(client, obj, msg):
	accion=(msg.payload.decode("utf-8"))
	print(accion)
	if accion=="L_ON":
		luz1On()
	if accion== "L_OFF":
		luzOff()
	

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.username_pw_set("654hector1@gmail.com", "naruto798199429")
mqttc.connect("maqiatto.com",1883)
mqttc.subscribe("654hector1@gmail.com/kop", 0)

rc=0
print("conectado..")
i=0
ms="sensor inactivo"
while rc==0:
	time.sleep(2)
	rc = mqttc.loop()
	#es=ejecutar()
	#ime.sleep(10)
	#mqttc.publish("654hector1@gmail.com/test", "sensor  "+str(i))
	i=i+1
	
