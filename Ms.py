import paho.mqtt.client as mqtt
BROKER = "86.97.118.3" 
PORT   = 1883
TOPICS = {
    "motor": "Robot/Motor/Status",
    "light": "Robot/LineSens/5",
    "path":  "Robot/Path/Status",
}
def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(BROKER, PORT, 60)
    print(f"Connected to MQTT broker at {BROKER}:{PORT}")
    print("Type 'exit' to quit.\n")
    while True:
        comp = input("Component (motor/light/path/custom/exit): ").strip().lower()
        if comp in ("exit", "quit"):
            print("Exiting...")
            break
        if comp == "custom":
            topic = input("Enter custom topic: ").strip()
        elif comp in TOPICS:
            topic = TOPICS[comp]
        else:
            print("Unknown component, try again.")
            continue
        msg = input(f"Message for {topic}: ").strip()
        if msg.lower() in ("exit", "quit"):
            print("Exiting...")
            break
        client.publish(topic, msg, qos=1)
        print(f"Sent '{msg}' → {topic}")
if __name__ == "__main__":
    main()
