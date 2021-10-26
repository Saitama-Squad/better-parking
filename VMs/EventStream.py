import wiotp.sdk.application
from wiotp.sdk.api.services import EventStreamsServiceBindingCredentials, EventStreamsServiceBindingCreateRequest
import json


def eventCallback(event):
    str = "%s event '%s' received from device [%s]: %s"
    print(str % (event.format, event.eventId,
          event.device, json.dumps(event.data)))


config = {
    "identity": {
        "appId": "app1"
    },
    "auth": {
        "key": "a-ev8xy3-rqfbn1jvy2",
        "token": "t_tSdBG-HVwcyOujtl"
    }
}

client = wiotp.sdk.application.ApplicationClient(config=config)
client.connect()
client.deviceEventCallback = eventCallback
client.subscribeToDeviceEvents(typeId="Camera")

while True:
    pass
