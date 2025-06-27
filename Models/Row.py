
class Row:
    def __init__(self,code_name,real_name,location,status,missions):
        self.id = None
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions = missions
    def val_by_default(self,the_id):
        self.id = the_id
    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Code Name: {self.code_name}\n"
                f"Real Name: {self.real_name}\n"
                f"Location: {self.location}\n"
                f"Status: {self.status}\n"
                f"Missions: {self.missions}\n")
