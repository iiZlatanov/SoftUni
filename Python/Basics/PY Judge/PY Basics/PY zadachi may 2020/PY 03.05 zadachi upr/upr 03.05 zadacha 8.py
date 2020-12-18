length = int(input())
width = int(input())
height = int(input())
percent_of_volume = float(input())

volume_of_aquarium = length * width * height
litres_the_aquarium_can_contain = volume_of_aquarium * 0.001
percent = percent_of_volume * 0.01

litres_we_will_need = litres_the_aquarium_can_contain * (1 - percent)
print(litres_we_will_need)