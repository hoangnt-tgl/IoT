import paho.mqtt.client as mqttclient
import time
import json
import geocoder     # thư viện để lấy kinh độ, vĩ độ
import random
BROKER_ADDRESS = "demo.thingsboard.io"
PORT = 1883
THINGS_BOARD_ACCESS_TOKEN = "PmV9G4AwiZ6nojbbKSAd"


def subscribed(client, userdata, mid, granted_qos):
    print("Subscribed...")

def recv_message(client, userdata, message):
    print("Received: ", message.payload.decode("utf-8"))
    temp_data = {'value': True}
    try:
        jsonobj = json.loads(message.payload)
        if jsonobj['method'] == "setValue":
            temp_data['value'] = jsonobj['params']
            client.publish('v1/devices/me/attributes', json.dumps(temp_data), 1)
    except:
        pass

def connected(client, usedata, flags, rc):
    if rc == 0:
        print("Thingsboard connected successfully!!")
        client.subscribe("v1/devices/me/rpc/request/+")
    else:
        print("Connection is failed")


client = mqttclient.Client("Gateway_Thingsboard")
client.username_pw_set(THINGS_BOARD_ACCESS_TOKEN)

client.on_connect = connected
client.connect(BROKER_ADDRESS, 1883)
client.loop_start()

client.on_subscribe = subscribed
client.on_message = recv_message


while True:
    
    # random nhiệt độ, độ ẩm
    temp = round(random.uniform(-50,50), 2)
    humi = round(random.uniform(0,100), 2)
    
    # lấy thông tin tọa độ
    c = geocoder.ip('me')
    latitude = c.latlng[0]
    longitude = c.latlng[1]
    city = c.city
    country = c.country
    
    collect_data = {'country': country,
                    'city': c.city,
                    'latitude': latitude,
                    'longitude': longitude,
                    'temperature': temp,
                    'humidity': humi}
    
    client.publish('v1/devices/me/telemetry', json.dumps(collect_data), 1)
    time.sleep(10)