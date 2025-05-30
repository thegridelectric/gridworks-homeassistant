# Getting started

This guide explains how to set up GridWorks' API within Home Assistant. The API can receive and process data from connected devices, and will make the data accessible as variables in Home Assistant. The guide also covers how to automatically publish updates to this data to other devices via MQTT.

## 1 - Installing the GridWorks API

The GridWorks API can be installed directly through the Home Assistant Community Store (HACS). If you don’t already have HACS installed, follow the [official HACS installation guide](https://www.hacs.xyz/docs/use/).

### Download the "GridWorks API" integration in HACS
- In Home Assistant, navigate to HACS, click on the three dots at the top right of the page, and choose "Custom repositories"
- Enter the link to this repository (https://github.com/thegridelectric/gridworks-homeassistant) and set the Type to "Integration" before adding the repository
- Click the three-dot menu for the GridWorks API entry in HACS and select Download

### Restart Home Assistant
- Go to Settings, click the three-dot menu in the top right corner, and select "Restart Home Assistant"
- GridWorks API should now appear in your installed repositories list in HACS

### Add GridWorks API as an integration
- Go to Settings → Devices & Services → Add Integration
- Search for GridWorks API and select it

## 2 - Publishing Sensor Data via MQTT

### Add and configure the MQTT integration
- Go to Settings → Devices & Services → Add Integration
- Search for MQTT and select it
- Choose "Manually enter the MQTT broker connection details", and enter the MQTT broker details (IP adress, port, etc.)
- To test the integration, type the following command in the Home Assistant CLI (replace `broker_ip_address`)
```
nc -zv broker_ip_address 1883
```
Note: you might need to add the following lines to the end of `mosquito.conf` on the machine that is running the broker:
```
listener 1883
allow_anonymous true
```

### Create automations to publish data via MQTT

- Go to Setting → Automations & scenes → Create Automation
- Create a new automation from scratch
- Click on the thee-dot menu in the top right and select "Edit in YAML"
- Paste the content of [send_mqtt_on_change.yaml](https://github.com/thegridelectric/gridworks-homeassistant/blob/main/blueprints/automation/send_mqtt_on_change.yaml) in the YAML editor
- Adapt the name of the variable to publish as needed