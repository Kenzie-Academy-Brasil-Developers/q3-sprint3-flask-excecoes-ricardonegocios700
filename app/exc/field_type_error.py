class FieldTypeError(Exception):
    default_message = {
        "wrong fields": [
            {
                "nome": "list"
            },
            {
                "email": "float"
            }
        ]
    }
    default_status_code = 400

    def __init__(self, message = default_message, status_code = default_status_code):
        self.default_message = message
        self.status_code = status_code