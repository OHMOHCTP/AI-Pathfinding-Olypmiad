import paho.mqtt.client as mqtt
from datetime import datetime
BROKER = "86.97.118.3"
PORT   = 1883
SUB_TOPICS = [("Robot/#", 0)]
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"[{datetime.now()}] Connected (rc={rc})")
    for topic, qos in SUB_TOPICS:
        client.subscribe(topic, qos)
def on_message(client, userdata, msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = msg.payload.decode("utf-8", errors="replace")
    if msg.topic == "Robot/Motor/Tel/Speed":
        print(f"{ts} | MOTOR SPEED = {payload}")
    else:
        print(f"{ts} | {msg.topic} -> {payload}")
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, keepalive=60)
status_msg = "Motor running OK"
client.publish("Robot/Motor/Status", status_msg, qos=1)
print(f"Published to Robot/Motor/Status: {status_msg}")
client.loop_forever()
