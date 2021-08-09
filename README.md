# switchbot-meter

[SwitchBot Meter](https://github.com/OpenWonderLabs/SwitchBotAPI) client

This Python Script is a client tool that uses the SwitchBot API to display the temperature, humidity, and other data that the SwitchBot device is getting.

Because it uses the SwitchBot API, you need to use the Switchbot Hub or Hub Mini.

You will need
1. python 3.x
1. SwitchBot Temperature and Humidity
1. **SwitchBot Hub or SwitchBot Hub mini**


## Getting Started
To get started, obtain an API Token from the Switchbot smartphone application.
https://github.com/OpenWonderLabs/SwitchBotAPI#getting-started

## Usage

```python
import switchbot
token = "<API Token>"
switchbot_client = switchbot.SwitchBot(token)
```

## Get Device List
```python
switchbot_client.devices()
```

response

The return value is the python dict type.
```
{'deviceList': [{'deviceId': 'xxx',
   'deviceName': 'Power Plug',
   'deviceType': 'Plug',
   'enableCloudService': True,
   'hubDeviceId': '000000000000'},
  {'deviceId': 'xxx',
   'deviceName': 'Bed Room',
   'deviceType': 'Meter',
   'enableCloudService': True,
   'hubDeviceId': 'xxx'},
  {'deviceId': 'xxx',
   'deviceName': 'Hub Mini',
   'deviceType': 'Hub Mini',
   'hubDeviceId': '000000000000'},
  {'deviceId': 'xxx',
   'deviceName': 'Living Room',
   'deviceType': 'Meter',
   'enableCloudService': True,
   'hubDeviceId': 'xxx'},
  {'deviceId': 'xxx',
   'deviceName': Study Room'',
   'deviceType': 'Meter',
   'enableCloudService': True,
   'hubDeviceId': 'xxx'}],
 'infraredRemoteList': []}
 ```

### example
```python
for device in devices["deviceList"]:
    print(device["deviceName"])
```

Response.
```
Power Plug
Bed Room
Living Room
Study Room
```
## Get Device Status

```python
device = switchbot_client.device('<ID>')
device.status()
```

response
```
{'deviceId': 'xxx',
 'deviceType': 'Meter',
 'hubDeviceId': 'xxx',
 'humidity': 62,
 'temperature': 26.6}
```

### example
```python
device = switchbot_client.device('<ID>')
device.status()["temperature"]
```

response
```
26.4
```

## License
The source code is licensed MIT.