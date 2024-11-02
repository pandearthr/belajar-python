class person:
    
    def __init__(self, name, address, telephone, idnumber):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.idnumber = idnumber

    def displayperson(self):
        print("name : ", self.name, ", Address : ", self.address, ", Telephone : ", self.telephone, ", ID Number : ", self.idnumber)

    def displayhobby(self):
        print("hobby : Travelling, Shopping")

x = person("Bambang Jeger", "Jakarta", "081321219090", 101)
x.displayperson()
        