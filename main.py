
from pet import Pet  # Import the Pet class from pet.py


my_pet = Pet("Bosco")


print("Initial Status:")
my_pet.get_status()  

print("\nFeeding the pet:")
my_pet.eat()  

print("\nLetting the pet sleep:")
my_pet.sleep()  

print("\nPlaying with the pet:")
my_pet.play()  

print("\nTraining the pet...")
my_pet.train("Sit")
my_pet.train("Roll over")


print("\nTricks learned:")
my_pet.show_tricks()


print("\nUpdated Status:")
my_pet.get_status()  