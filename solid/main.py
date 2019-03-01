import sys

from business.pincode import PincodeType
from business.valida_pincode import ValidaPincode

if __name__ == '__main__':
    args = sys.argv
    _type = args[1].upper()
    _value = args[2]

    p = PincodeType[_type]
    is_valid = p.value.validation_class.valida(_value)
    print(f'Pincode is valid: {is_valid}.')
