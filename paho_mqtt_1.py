# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 20:03:18 2016

@author: OldzieMa
"""

import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnectthen subscriptions will be renewed.
    
    client.subscribe("$SYS/#")
    #subscribe to the topic test123
    client.subscribe("test123")
    #print "on connect"

# The callback for when a PUBLISH message is received from the server.
data = []
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    data.append([msg.topic, str(msg.payload)])
    #print "on message"
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.connect("iot.eclipse.org", 1883, 60)
client.connect("192.168.1.142", 8883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

# the loop below will block any other funcitons
#client.loop_forever()

# This loop os cool because it works in the background and only calls the on message funciton when there is new message sent be broker
client.loop_start()

import time

while 1:
   
    print time.asctime()
    time.sleep(2)
    
    