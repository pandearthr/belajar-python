class Student(person):

    def __init__(self, name, address, telephone, idnumber, year):

        super().__init__(self, name, address, telephone, idnumber)
        self.address = address
        self.graduaionyear = year

y = Student("Nilam Cahya", "Cirebon", "087809291212", 15035, 2019)
y.displayperson()
y.displayhobby()