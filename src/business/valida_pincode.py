
class ValidaPincode:
    
    @staticmethod
    def valida(value):
        raise NotImplementedError


class ValidaPincodeTorraTorra(ValidaPincode):

    @staticmethod
    def valida(value):
        if(len(value)) != 10:
            return False
        return True   

class ValidaPincodeAtacadao(ValidaPincode):

    @staticmethod
    def valida(value):
        if(len(value)) != 27:
            return False
        return True


class ValidaPincodeConti(ValidaPincode):
    
    @staticmethod
    def valida(value):
        if(len(value)) != 12:
            return False
        return True

