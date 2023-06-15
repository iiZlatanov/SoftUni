from collections import deque

elves_list = deque(int(x) for x in input().split())
materials_list = [int(x) for x in input().split()]
index = 1
total_energy_spent = 0
toys_counter = 0

while elves_list and materials_list:
    if index % 5 == 0:#Clumsy time
        if elves_list[0] < 5:  # Elf takes day off
            elves_list.popleft()
            index -= 1
        else:  # Create another if/else to check if it is a creative time as well
            if index % 3 == 0:#Creative & clumsy
                current_elf_energy = elves_list.popleft()  # Take the current elf
                double_the_energy = materials_list[-1] * 2  # Doubling the energy since it is creative time
                if current_elf_energy >= double_the_energy:  # If the elf has equal or more energy, and can create the toy
                    total_energy_spent += double_the_energy  # Adding the energy to the total spent, since the elf crafted the toy
                    current_elf_energy -= double_the_energy  # Remove the energy from the elfs energy
                    elves_list.append(current_elf_energy)  # Adding the elf back at the end of the line
                    materials_list.pop()  # Remove the materials, since they were used already, but we do not add to the toys, since its clumsy time
                else:  # When the elf does not have the energy to create the toy
                    elves_list.append(current_elf_energy * 2)

            else:#Normal & clumsy
                current_elf_energy = elves_list.popleft()  # Take the current elf
                if current_elf_energy >= materials_list[-1]:  # If the elf has equal or more energy, and can create the toy
                    total_energy_spent += materials_list[-1]  # Adding the energy to the total spent, since the elf crafted the toy
                    current_elf_energy -= materials_list[-1]  # Remove the energy from the elfs energy
                    elves_list.append(current_elf_energy)  # Adding the elf back at the end of the line
                    materials_list.pop()  # Remove the materials, since they were used already, but we do not add to the toys, since its clumsy time
                else:  # When the elf does not have the energy to create the toy
                    elves_list.append(current_elf_energy * 2)


    elif index % 3 == 0:#Creative time
        if elves_list[0] < 5:#Elf takes day off
            elves_list.popleft()
            index -= 1
        else:#Check if elf can or cannot craft the toy
            current_elf_energy = elves_list.popleft()#Take the current elf
            double_the_energy = materials_list[-1] * 2#Doubling the energy since it is creative time
            if current_elf_energy >= double_the_energy:#If the elf has equal or more energy, and can create the toy
                total_energy_spent += double_the_energy#Adding the energy to the total spent, since the elf crafted the toy
                current_elf_energy -= double_the_energy#Remove the energy from the elfs energy
                current_elf_energy += 1#Add 1 energy for the cookie reward after creating a toy
                elves_list.append(current_elf_energy)#Adding the elf back at the end of the line
                toys_counter += 2#Adding 2 toys, since it is creative time
                materials_list.pop()#Remove the materials, since they were used already
            else:# When the elf does not have the energy to create the toy
                elves_list.append(current_elf_energy * 2)


    else:
        if elves_list[0] < 5:#Elf takes day off
            elves_list.popleft()
            index -= 1
        else:#Check if elf can or cannot craft the toy
            current_elf_energy = elves_list.popleft()#Take the current elf
            if current_elf_energy >= materials_list[-1]:#If the elf has equal or more energy, and can create the toy
                total_energy_spent += materials_list[-1]#Adding the energy to the total spent, since the elf crafted the toy
                current_elf_energy -= materials_list[-1]#Remove the energy from the elfs energy
                current_elf_energy += 1#Add 1 energy for the cookie reward after creating a toy
                elves_list.append(current_elf_energy)#Adding the elf back at the end of the line
                toys_counter += 1#Adding a toy, since a toy was made
                materials_list.pop()#Remove the materials, since they were used already
            else:# When the elf does not have the energy to create the toy
                elves_list.append(current_elf_energy * 2)


    index += 1

print(f"Toys: {toys_counter}\n"
      f"Energy: {total_energy_spent}")
if elves_list:
    print(f"Elves left: {', '.join(str(elf) for elf in elves_list)}")
if materials_list:
    print(f"Boxes left: {materials_list}")
