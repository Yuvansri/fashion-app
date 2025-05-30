class FitnessTracker:
    def __init__(self):
        self.activities = []

    def add_activity(self, activity, duration):
        self.activities.append((activity, duration))

    def view_activities(self):
        if not self.activities:
            print("No activities logged yet.")
        else:
            for i, (act, dur) in enumerate(self.activities, 1):
                print(F"{i}. {act} - {dur} mins")

    def total_time(self):
        total = sum(d for _, d in self.activities)
        print(f"Total time spent exercising: {total} minutes")

def menu():
    tracker = FitnessTracker()
    while True:
        print("\nFitness Tracker Menu:")
        print("1. Add Activity")
        print("2. View Activities")
        print("3. Show Total Time")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            act = input("Enter activity name: ")
            try:
                dur = int(input("Enter duration (in minutes): "))
                tracker.add_activity(act, dur)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '2':
            tracker.view_activities()
        elif choice == '3':
            tracker.total_time()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

menu()                



                                     


       

