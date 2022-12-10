from datetime import datetime
from time import sleep
import serial
import re
import random
import time
import paho.mqtt.client as mqtt
#Para el log
import time
import os


#Escribir fichero de log
f = open ('lee_potmqtt.log','w')
f.write(time.ctime(time.time()) + ' Ejecutado script desde ' +os.getenv("USER")+'\n' )
f.close()

#config broker
broker_url = "IP_BROKER"
broker_port = 1883  

client = mqtt.Client()
client.username_pw_set(username="usuariomqtt",password="passwordmqtt")
client.connect(broker_url, broker_port) 

now = datetime.utcnow()
print(now)

f = open ('lee_potmqtt.log','a')
f.write(time.ctime(time.time()) + ' Conectado a broker '+ str(broker_url) + ' en puerto ' + str(broker_port)  +  '\n')
f.close()



while True:
    try:
        now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
   
        cc128 = serial.Serial("/dev/ttyUSB0", 57600, timeout=6)
        cc128xml = cc128.readlines(6)

        texto=re.sub('<.*?>', '', str(cc128xml))

        print (texto)

        tmpr=texto[27:31]
        watts=texto[39:43]
        print ("Temperatura " + str(tmpr) + "C, Potencia " + str(watts) + "watios")
#        f = open ('lee_potmqtt.log','a')
#        f.write(time.ctime(time.time()) + ' Temperatura ' + str(tmpr) + 'C, Potencia ' + str(watts) + 'watios' + '\n')
#        f.close()
        print (cc128xml)
#	if float(tmpr)<50 and float(tmpr)>10:
        if float(tmpr)<50 and float(tmpr)>10 and float(watts)<8000 and float(watts)>50:

          client.publish(topic="home-assistant/envir/temperatura", payload=str(tmpr), qos=0, retain=False)
          client.publish(topic="home-assistant/envir/potencia", payload=str(watts), qos=0, retain=False)

        sleep(10)
    except:
        sleep(10)


f.close()
