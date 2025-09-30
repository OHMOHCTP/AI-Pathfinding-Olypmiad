// consider void... i forgot postman handles this, working on implementing postman - mcrtbp2006


var mqtt;
var reconnectTimeout = 2000;
var host = "172.17.217.194";
var port = 9001;

function onConnect(){
    console.log("Connected successfully!");
    message = new Paho.MQTT.Message("hi");
    message.destinationName = "testing";
    mqtt.send(message);
};

function onMessageArrived(msg) {
    output_msg = "Message recieved: " + msg.payloadString + "<br>";
    output_msg = "Message recieved, topic " + msg.destinationName;
    console.log(output_msg)
}

function onFailure() {
    console.log("Connection attempt to host " + host + " failed.");
    setTimeout(MQTTconnect, reconnectTimeout);
};

function MQTTconnect() {
    console.log("connecting to " + host + " " + port + "...");
    var clientId = "clientjs-" + Math.floor(Math.random() * 10000);
    mqtt = new Paho.MQTT.Client(host, port, "client.js");
    var options = {
        timeout: 3,
        onSuccess: onConnect,
        onFailure: onFailure,
    };

    mqtt.onMessageArrived = onMessageArrived
    mqtt.connect(options);
};
