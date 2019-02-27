import sys

from business.pincode import Pincode
from business.valida_pincode import ValidaPincode

if __name__ == '__main__':
    args = sys.argv
    p = Pincode(args[1], args[2]) 
    is_valid = ValidaPincode().valida(p)
    print(f'Pincode is valid: {is_valid}.')
