import random


class System:
    def __init__(self, environment):
        self.environment = environment
        self.behavior = self.do_behavior()

    def do_behavior(self):
        # Define the normal behavior of the system in the environment
        if self.environment == "A":
            return "Behavior A"
        elif self.environment == "B":
            return "Behavior B"
        else:
            return "Behavior C"

    def disturb(self):
        # Randomly trigger a disturbance in the system
        self.environment = random.choice(["A", "B", "C"])
        self.behavior = self.do_behavior()

    def adapt(self):
        # Adjust the system to restore normal behavior after a disturbance
        if self.behavior == "Behavior A":
            self.environment = "A"
        elif self.behavior == "Behavior B":
            self.environment = "B"
        else:
            self.environment = "C"

# Initialize the system with environment A
def run_simulation(num_iterations):
 system = System("A")

# Run the simulation for x iterations
 for i in range(num_iterations):
    print(f"Iteration {i + 1}: System is in environment {system.environment} and is doing {system.behavior}")

    # Randomly disturb the system in some iterations
    if random.random() < 0.3:
        print("Disturbance!")
        system.disturb()

    # Check if the system is still behaving normally
    if system.behavior != system.do_behavior():
        print("Adapting...")
        system.adapt()

    print(f"System is now in environment {system.environment} and is doing {system.behavior}")
    print("-" * 20)

num_iterations = int(input("Enter the number of iterations: "))
run_simulation(num_iterations)

