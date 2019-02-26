from business.pincode import Pincode
from business.valida_pincode import ValidaPincode

if __name__ == '__main__':
    p = Pincode('torratorra', 'TOR64321EW') 
    ValidaPincode().valida(p)
    