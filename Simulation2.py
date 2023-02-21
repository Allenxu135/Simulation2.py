import random

def simulate_system(num_iterations, success_prob, disturbance_prob, adaptation_prob):
    print("Starting system simulation...")
    environment_state = "stable"
    system_state = "success"
    for i in range(num_iterations):
        print(f"Iteration {i+1}: Environment state - {environment_state}, System state - {system_state}")
        if system_state == "success":
            if random.uniform(0, 1) > success_prob:
                system_state = "failure"
                print("System failure detected!")
                if random.uniform(0, 1) <= disturbance_prob:
                    print("Disturbance detected!")
                    environment_state = "disturbed"
        else:
            if random.uniform(0, 1) <= adaptation_prob:
                system_state = "success"
                print("System adapted to failure and returned to stable ")
                if environment_state == "disturbed":
                    environment_state = "stable"
        if i == num_iterations - 1:
            print(f"Final iteration: Environment state - {environment_state}, System state - {system_state}")

def main():
    num_iterations = int(input("Enter the number of iterations to simulate: "))
    success_prob = float(input("Enter the probability of system success in each iteration (between 0 and 1): "))
    disturbance_prob = float(input("Enter the probability of disturbance occurrence (between 0 and 1): "))
    adaptation_prob = float(input("Enter the probability of environment adaptation (between 0 and 1): "))
    simulate_system(num_iterations, success_prob, disturbance_prob, adaptation_prob)

# mian running
if __name__ == "__main__":
    main()


