import user


class Founder(User):

    def __init__(self, username, password, name, gender, address, phone):
        super().__init__(username, password, name, gender, address)