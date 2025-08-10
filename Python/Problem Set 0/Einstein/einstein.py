# einstein.py - By Charan Katyal

# Define the speed of light (in meters per second)
c = 300000000  # m/s

# Prompt the user for mass input
m = int(input("Enter mass in kilograms: "))

# Calculate the energy using Einstein's equation (E = mc^2)
E = m * c ** 2

# Output the equivalent energy in Joules
print(E)
