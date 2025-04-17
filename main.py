# main.py

from pet import Pet  # Import the Pet class from pet.py

# Create a pet object
my_pet = Pet("Sparrow")

# Test the functionality
print("Initial Status:")
my_pet.get_status()  # Get initial status

print("\nFeeding the pet:")
my_pet.eat()  # Feed the pet

print("\nLetting the pet sleep:")
my_pet.sleep()  # Let the pet sleep

print("\nPlaying with the pet:")
my_pet.play()  # Play with the pet

# Teach the pet a few tricks
print("\nTraining the pet...")
my_pet.train("Sit")
my_pet.train("Roll over")

# Show the tricks the pet has learned
print("\nTricks learned:")
my_pet.show_tricks()

# Get updated status of the pet
print("\nUpdated Status:")
my_pet.get_status()  # Get updated status after all activities
