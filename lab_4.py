class Process:
    def __init__(self, p_id, process_name, start_time, priority):
        self.p_id = p_id
        self.process_name = process_name
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def __init__(self):
        self.processes = []
        
    def add_process(self, process):
        self.processes.append(process)
        
    def sort_by_p_id(self):
        self.processes.sort(key=lambda process: process.p_id)
        
    def sort_by_start_time(self):
        self.processes.sort(key=lambda process: process.start_time)
        
    def sort_by_priority(self):
        priority_order = {'High': 3, 'MID': 2, 'Low': 1}
        self.processes.sort(key=lambda process: priority_order[process.priority], reverse=True)
        
    def display_table(self):
        print("{:<5} {:<10} {:<15} {:<8}".format("P_ID", "Process", "Start Time (ms)", "Priority"))
        print("="*40)
        for process in self.processes:
            print("{:<5} {:<10} {:<15} {:<8}".format(process.p_id, process.process_name,
                                                    process.start_time, process.priority))

def main():
    flight_table = FlightTable()
    
    flight_table.add_process(Process("P1", "VSCode", 100, "MID"))
    flight_table.add_process(Process("P23", "Eclipse", 234, "MID"))
    flight_table.add_process(Process("P93", "Chrome", 189, "High"))
    flight_table.add_process(Process("P42", "JDK", 9, "High"))
    flight_table.add_process(Process("P9", "CMD", 7, "High"))
    flight_table.add_process(Process("P87", "NotePad", 23, "Low"))
    
    while True:
        print("\n[1. Sort by P_ID], \n[2. Sort by Start Time], \n[3. Sort by Priority],\n[ 4. Quit]")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            flight_table.sort_by_p_id()
        elif choice == '2':
            flight_table.sort_by_start_time()
        elif choice == '3':
            flight_table.sort_by_priority()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
            continue
        
        flight_table.display_table()

if __name__ == "__main__":
    main()
