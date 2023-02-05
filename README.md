# mqtt_envir

Read envir smart meter and send it via mqtt

export BROKER_URL="192.168.0.200"

export BROKER_PORT="1883"

export BROKER_USER="usermqtt"

export BROKER_PWD="pwdmqtt"


sudo docker run -d -e "USER=root" -e "BROKER_PORT=1883" -e "BROKER_URL=192.168.0.200" -e "BROKER_USER=usermqtt" -e "BROKER_PWD=pwdmqtt" --device=/dev/ttyUSB0  mqtt_envir:1.0.0

