class Party:
    def __init__(self):
        self.people = []


name_or_end_command = input()
party = Party()

while name_or_end_command != "End":
    party.people.append(name_or_end_command)
    name_or_end_command = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
