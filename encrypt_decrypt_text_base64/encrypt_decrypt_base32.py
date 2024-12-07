

#I like your example. I would import base64. Then add an extra 2 lines for encrypting data.
import base64
import pickle
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        
student = Student("John", 20, "Computer Science")
serialized_student = pickle.dumps(student)
#encript data 
encoded_student = base64.b64encode(serialized_student)
#decript data 
serialized_student = base64.b64decode(encoded_student)

deserialized_student = pickle.loads(serialized_student)

print(f"The deserialized object is: {deserialized_student.name}, {deserialized_student.age}, {deserialized_student.major}")