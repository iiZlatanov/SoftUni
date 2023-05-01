number_of_invitations = int(input())
list_of_invitations = []

for _ in range(number_of_invitations):
    invitation = input()
    list_of_invitations.append(invitation)

command = input()
while command != "END":
    list_of_invitations.remove(command)
    command = input()

print(len(list_of_invitations))
print("\n".join(sorted(list_of_invitations)))
