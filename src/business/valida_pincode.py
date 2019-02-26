from business.pincode import Pincode


class ValidaPincode:

    def valida(self, pincode: Pincode):
        
        if pincode.client == 'atacadao':
            return self.__valida_atacadao(pincode)
        elif pincode.client == 'torratorra':
            return self.__valida_torra(pincode)

        raise Exception('INVALID PINCODE TYPE')    

    @staticmethod
    def __valida_atacadao(pincode):
        if(len(pincode.value)) != 27:
            return False
        return True

    @staticmethod
    def __valida_torra(pincode):
        if(len(pincode.value)) != 10:
            return False
        return True        
