class Contact():
    def __init__(self , name :str , email : str , phone : str) -> None:
        self.name = name
        self.email = email
        self.phone = phone
    def Adding (self):
        pass
    def Editing (self) :
        pass
    def Deleting(self):
        pass

class User():
    def __init__(self , username : str , password : str) -> None:
        self.username =username
        self.password =password
    def Creating(self):
        pass
    def Authenticating(self):
        pass
    def Modifying(self):
        pass