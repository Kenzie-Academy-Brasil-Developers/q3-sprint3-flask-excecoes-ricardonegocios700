class FieldTypeError(Exception):
    def __init__(self, type_nome, type_email):
        self.message = {"wrong fields": []}
        self.code    = 400
        
        if type_nome != "str":
            self.message["wrong fields"].append({"nome": type_nome})

        if type_email != "str":
            self.message["wrong fields"].append({"email": type_email})