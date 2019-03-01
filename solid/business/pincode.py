from enum import Enum

from business.valida_pincode import ValidaPincodeTorraTorra
from business.valida_pincode import ValidaPincodeAtacadao
from business.valida_pincode import ValidaPincodeConti

class Pincode():

    _validation_class = None

    def __init__(self, validation):
        self._validation_class = validation 

    @property
    def validation_class(self):
        return self._validation_class   


class PincodeType(Enum):
    TORRATORRA = Pincode(ValidaPincodeTorraTorra())
    ATACADAO = Pincode(ValidaPincodeAtacadao())
    CONTI = Pincode(ValidaPincodeConti())