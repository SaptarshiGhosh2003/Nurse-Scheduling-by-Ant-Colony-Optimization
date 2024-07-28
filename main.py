import random

class Nurse:
    def __init__(self, id, availability):
        self.id = id
        self.availability = availability
        self.shifts = [0] * 7  # 7 days of the week

class Problem:
    def __init__(self, nurses, time_distribution):
        self.nurses = nurses
        self.time_distribution = time_distribution
        self.best_solution = None
        self.best_fitness = 0

    def schedule_shift(self, nurse, time_slot):
        if nurse.availability >= self.time_distribution[time_slot]:
            nurse.shifts[time_slot] = 1
            nurse.availability -= self.time_distribution[time_slot]

    def pheromone_solution(self):
        for time_slot in range(len(self.time_distribution)):
            for nurse in self.nurses:
                if nurse.shifts[time_slot] == 0:  # Check if the shift is not already assigned
                    self.schedule_shift(nurse, time_slot)

    def calculate_fitness(self):
        total_shifts = 0
        for nurse in self.nurses:
            total_shifts += nurse.shifts.count(1)
        return total_shifts

    def solve(self):
        self.best_solution = [nurse.shifts[:] for nurse in self.nurses]
        self.best_fitness = 0

        for iteration in range(100):
            self.pheromone_solution()
            current_fitness = self.calculate_fitness()

            if current_fitness > self.best_fitness:
                self.best_solution = [nurse.shifts[:] for nurse in self.nurses]
                self.best_fitness = current_fitness

            # Reset availability for the next iteration
            #for nurse in self.nurses:
                #nurse.availability = random.randint(0, 200)  # 6Reset to original availability range

        return self.best_solution

def get_nurse_availabilities(num_nurses):
    nurses = []
    for i in range(num_nurses):
        while True:
            try:
                availability = int(input(f"Enter availability for Nurse {i}: "))
                if availability < 0:
                    raise ValueError("Availability must be a non-negative integer.")
                nurses.append(Nurse(i, availability))
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid integer.")
    return nurses

def main():
    # Get user input for the number of nurses
    num_nurses = int(input("Enter the number of nurses: "))

    # Get user input for each nurse's availability
    nurses = get_nurse_availabilities(num_nurses)

    # Define the time distribution (can be changed as needed)
    time_distribution = [10, 20, 15, 25, 10, 20, 15]  # Sample time slots

    # Create and solve the problem
    problem = Problem(nurses, time_distribution)
    solution = problem.solve()

    # Print the results
    print("\nBest solution:")
    for i, nurse in enumerate(problem.best_solution):
        print(f"Nurse {i}: {nurse}")
    print(f"Best fitness: {problem.best_fitness}")

if __name__ == '__main__':
    main()
