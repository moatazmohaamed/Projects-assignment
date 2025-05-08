class User:
    def __init__(self, user_id, name, email, status="Available"):
        self.__user_id = user_id  
        self.name = name
        self.email = email
        self.status = status
        self.teams = []
        self.contacts = []

    def update_status(self, new_status):
        self.status = new_status
        print(f"{self.name}'s status updated to {self.status}.")

    def add_contact(self, user):
        if user not in self.contacts:
            self.contacts.append(user)
            print(f"{user.name} has been added to your contacts.")
        else:
            print(f"{user.name} is already in your contacts.")

    def join_team(self, team):
        if self not in team.members_list:
            team.add_member(self)
            self.teams.append(team)
        else:
            print(f"You are already a member of {team.team_name}.")

    def send_message(self, recipient, content):
        print(f"{self.name} to {recipient.name}: {content}")

    def display_userInfo(self):
        print(f"User ID: {self.__user_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Status: {self.status}")
        print("Teams:", [team.team_name for team in self.teams])
        print("Contacts:", [user.name for user in self.contacts])

class Team:
    organization = "Faculty of Commerce" 
    def __init__(self, team_id, team_name, team_description, team_owner):
        self.team_id = team_id
        self.team_name = team_name
        self.team_description = team_description
        self.team_owner = team_owner 
        self.members_list = [team_owner]
        self.channels_list = []

    def add_member(self, user):
        if user not in self.members_list:
            self.members_list.append(user)

    def remove_member(self, user):
        if user in self.members_list:
            self.members_list.remove(user)
            user.teams.remove(self)

    def create_channel(self, channel_name):
        self.channels_list.append(channel_name)

    def list_members(self):
        print(f"Members of {self.team_name}:")
        for user in self.members_list:
            if user == self.team_owner:
                print(f"- {user.name} (Owner)")
            else:
                print(f"- {user.name}")


print("========================== Welcome to the Microsoft Teams Application! ==========================")

userOne = User(5, 'Moataz', "moataz@gmail.com" , "Away")
userTwo = User(6, 'Mostafa', "Mostafa@gmail.com" , "busy")
userThree = User(7, 'mourad', "mourad@gmail.com" , "Available")


print("======== User Information: ========")
userOne.display_userInfo()
print("=================================== \n")


team1 = Team(131, "Programming-2", "Make a OOP projects", userOne)
print(f"\n{userOne.name} created team: {team1.team_name}")

userTwo.join_team(team1)
userThree.join_team(team1)
print(f"\n{userTwo.name} and {userThree.name} joined team: {team1.team_name}")

team1.list_members()
team1.create_channel("General")

print("======== Team Chat ========")
userOne.send_message(userTwo, "3amel ehh ya Mostafa?👋")
userTwo.send_message(userOne, "Ana kwayis enta 3amel eh👋")
print("=================================== \n")

userOne.update_status("Available")

print("======== Contacts : ========")
userTwo.add_contact(userThree)
userOne.add_contact(userTwo)
userThree.add_contact(userOne)
print("=================================== \n")

team1.remove_member(userTwo)
print(f"\n{userTwo.name} has been removed from the team: {team1.team_name}")
team1.list_members()

print("======== Updated User Information: ========")
userOne.display_userInfo()
print("=================================== \n")
userTwo.display_userInfo()
print("=================================== \n")
userThree.display_userInfo()
print("=================================== \n")


