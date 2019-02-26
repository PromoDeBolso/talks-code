

class Pincode:

    _client = None
    _value = None

    def __init__(self, client, _value):
        self._client = client
        self._value = _value

    @property
    def client(self):
        return self._client

    @property
    def value(self):
        return self._value    