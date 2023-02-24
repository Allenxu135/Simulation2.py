import random

# Define a function to simulate the system behavior
def simulate_system(num_iterations, success_prob, disturbance_prob, adaptation_prob):
    print("Starting system simulation...")
    #Initialize environment and system states as "normal" and "success", respectively
    environment_state = "stable"
    system_state = "success"
    # Iterate for the specified number of iterations
    for i in range(num_iterations):
        print(f"Iteration {i+1}: Environment state - {environment_state}, System state - {system_state}")
        # Check if the system is currently in a successful state
        if system_state == "success":
            # If the success probability is not met, set the system state to "failure"
            if random.uniform(0, 1) > success_prob:
                system_state = "failure"
                print("System failure detected!")
                # If the disturbance probability is met, set the environment state to "disturbed"
                if random.uniform(0, 1) <= disturbance_prob:
                    print("Disturbance detected!")
                    environment_state = "disturbed"
        # If the system is in a failed state, attempt to adapt
        else:
            # If the adaptation probability is met, set the system state back to "success"
            if random.uniform(0, 1) <= adaptation_prob:
                system_state = "success"
                print("System adapted to failure and returned to stable ")
                # If the environment is currently disturbed, attempt to adapt it back to "normal"
                if environment_state == "disturbed":
                    environment_state = "stable"
        # If this is the final iteration, print the current environment and system states
        if i == num_iterations - 1:
            print(f"Final iteration: Environment state - {environment_state}, System state - {system_state}")

# Define a main function to prompt the user for simulation parameters and call the simulation function
def main():
    num_iterations = int(input("Enter the number of iterations to simulate: "))
    success_prob = float(input("Enter the probability of system success in each iteration (between 0 and 1): "))
    disturbance_prob = float(input("Enter the probability of disturbance occurrence (between 0 and 1): "))
    adaptation_prob = float(input("Enter the probability of environment adaptation (between 0 and 1): "))
    simulate_system(num_iterations, success_prob, disturbance_prob, adaptation_prob)

# main system running
if __name__ == "__main__":
    main()


