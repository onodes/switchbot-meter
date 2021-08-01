import json
import requests

class SwitchBot:
    """ SwitchBot Client"""

    API_ENDPOINT = 'https://api.switch-bot.com'

    def __init__(self, tokens:str=None) -> None:
        self._tokens = tokens
    
    def devices(self) -> str:
        url = "/v1.0/devices"
        response = self._api_request_body(method="GET", url=url)
        return response
    
    def device(self, device_id:str):
        return Device(self, device_id)

    def status(self, device_id:str) -> str:
        url = f"/v1.0/devices/{device_id}/status"
        response = self._api_request_body(method="GET", url=url)
        return response

    def _api_request_body(self, method:str, url:str) -> str:
        response = self._api_request(method=method, url=url)
        text_body = json.loads(response)["body"]
        return text_body

    def _api_request(self, method:str, url:str) -> str:
        header = {"Authorization": self._tokens}
        if method == "GET":
            response = requests.get(SwitchBot.API_ENDPOINT + url, headers=header)
        elif method == "POST":
            response = requests.post(SwitchBot.API_ENDPOINT + url, headers=header)
        else:
            raise NotImplementedError
        
        if response.status_code != requests.codes.ok:
            response.raise_for_status()

        return response.text

class Device:
    """ SwitchBot device"""

    def __init__(self, switchbot:SwitchBot, device_id:str) -> None:
        self._switchbot = switchbot
        self._device_id = device_id
        self._device_name = None
        self._device_type = None

    def status(self) -> str:
        return self._switchbot.status(self._device_id)
    
    def update(self) -> str:
        status = self.status()
        self._device_type = status["deviceType"]
        return status

class Meter(Device):
    """ SwitchBot Meter"""

    def __init__(self, switchbot: SwitchBot, device_id: str) -> None:
        super().__init__(switchbot, device_id)
        self._humidity = None
        self._temperature = None
    
    def update(self) -> str:
        status = super.update()
        self._humidity = status["humidity"]
        self._temperature = status["temperature"]
        return status


