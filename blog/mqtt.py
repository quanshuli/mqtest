import paho.mqtt.client as paho
import json
import time
import random
import django
django.setup()

broker="192.168.0.11"
port= 9001
sub_topic="test"

 
def on_message(client, userdata, message):
    print("message received  "  ,str(message.payload.decode("utf-8")))


client= paho.Client("receive-socks",transport='websockets')       #create client object
#client= mqtt.Client("receive-socks") # no websocket

client.connect(broker,port)           #establish connection


client.loop_start()
client.subscribe(sub_topic)
client.on_message = on_message        #assign function to callback



client= paho.Client("publish-socks",transport='websockets')       #create client object

client.connect(broker,port)           #establish connection

while True:
    rand_int = random.randint(1, 100)
    client.publish(sub_topic,rand_int)    #publish
    print('publishing: '+str(rand_int))
    time.sleep(1)
