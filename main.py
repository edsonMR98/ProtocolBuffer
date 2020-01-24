import addressBook_pb2

person = addressBook_pb2.Person() # Creates a Person instance

# Fills the fields with Person information
person.id = 1234
person.name = "Edson"
person.email = "edson@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressBook_pb2.Person.HOME