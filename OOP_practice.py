class Person:
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.dateofbirth = None
        self.address = None

    def printidentity(self):
        self.firstname = input("Enter your Forename:\n")
        self.lastname = input("Enter your Surname:\n")
        self.dateofbirth = input("Enter your Date of birth:\n")
        self.address = input("Enter your home address:\n")

        print(f"""
        First name: {self.firstname}
        Last name: {self.lastname}
        DOB: {self.dateofbirth}
        Home Address: {self.address}
        """)

usr1 = Person()

usr1.printidentity()