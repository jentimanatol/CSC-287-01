
#I like your example. I would add an extra 2 lines for encrypting data .
import pickle
import base64
class SwimTeamMember:
 def __init__(self, name, age, position):
  self.name = name
  self.age = age
  self.position = position

def save_swim_team_members(members, filename):
  serialized_members = pickle.dumps(members)
  #encode data then save to file 
  encoded_members = base64.b64encode(serialized_members)
  with open(filename, 'wb') as file:
   pickle.dump(encoded_members, file)


def load_swim_team_members(filename):
  try:
   with open(filename, 'rb') as file:
    encoded_student = pickle.load(file)
    #decode data from file 
    serialized_members = base64.b64decode(encoded_student)

    members = pickle.loads(serialized_members)

    return members
  except FileNotFoundError:
    return []


member1 = SwimTeamMember("John Doe", 20, "Freestyle")
member2 = SwimTeamMember("Jane Smith", 22, "Butterfly")


save_swim_team_members([member1, member2], 'swim_team_members.pickle')


loaded_members = load_swim_team_members('swim_team_members.pickle')


for member in loaded_members:
 print(f"Name: {member.name}, Age: {member.age}, Position: {member.position}")