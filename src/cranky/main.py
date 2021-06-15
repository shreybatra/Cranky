import json
import socket


class Cranky:

    _socket = None

    def __init__(self, host="localhost", port=9876):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((host, port))

    def _send(self, data):
        ok = self._socket.send(data.encode("utf-8"))
        if not ok:
            raise Exception("Socker connection broken.")
        response = self._socket.recv(4096)

        return response

    def set(self, key: str, value):

        if len(key) > 128:
            raise Exception("Length of key should be within 128 bytes.")

        try:
            value = json.dumps(value)
            if len(value) > 3968:
                print("Size of value should be within 3968 bytes.")
            msg = "set {} {}".format(key, value)
        except:
            raise Exception("{} Value is not JSON serializable.".format(value))

        response = self._send(msg)

        if response == "Invalid value":
            raise Exception(response)

        return response.decode("utf-8")

    def get(self, key):
        msg = "get {}".format(key)

        response = self._send(msg)

        if response == "Not found":
            return None, False

        return json.loads(response.decode("utf-8")), True

    def find(self, filters={}):

        for key, _ in filters:
            if type(key) != str:
                raise Exception("Filter keys can only have String values.")

        msg = "find {}".format(json.dumps(filters))
        response = self._send(msg)

        return json.loads(response.decode("utf-8")), True

    def delete(self, key):
        msg = "del {}".format(key)

        response = self._send(msg)

        if response == "Not found":
            return None, False

        return json.loads(response.decode("utf-8")), True
