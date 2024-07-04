import os

def collect_student_data():
    # Collects student data from the user and returns a dictionary
    num_students = int(input("Enter the number of students: "))
    if num_students <= 0:
        raise ValueError("Number of students should be positive")

    student_data = {}
    for i in range(num_students):
        name = input(f"Enter name of student {i+1}: ")
        if not name.isalpha() and not name.isspace():
            raise ValueError("Name should contain only letters and spaces")
        if name in student_data:
            raise ValueError("Duplicate student names are not allowed")
        student_data[name] = {}
    return student_data

def collect_module_data():
    # Collects module data from the user and returns a list
    num_modules = int(input("Enter the number of course modules: "))
    if num_modules <= 0:
        raise ValueError("Number of modules should be positive")

    module_data = []
    for i in range(num_modules):
        module_name = input(f"Enter name of module {i+1}: ")
        if not module_name.isalpha() and not module_name.isspace():
            raise ValueError("Module name should contain only letters and spaces")
        if module_name in module_data:
            raise ValueError("Duplicate module names are not allowed")
        module_data.append(module_name)
    return module_data

def collect_marks_data(student_data, module_data):
    # Collects marks data from the user and updates the student_data dictionary
    for name in student_data:
        marks = []
        for module in module_data:
            mark = input(f"Enter mark of {module} for {name}: ")
            if not mark.isdigit():
                raise ValueError("Marks should be integers between 0 and 100")
            mark = int(mark)
            if mark < 0 or mark > 100:
                raise ValueError("Marks should be integers between 0 and 100")
            marks.append(mark)
        student_data[name]["marks"] = marks

def process_data(student_data, module_data):
    # Processes the collected data and returns a dictionary with summary information
    summary_data = {"batch_avg": None, "highest_mark": None, "best_student": None}

    for name, data in student_data.items():
        total = sum(data["marks"])
        avg = total / len(module_data)
        student_data[name]["total"] = total
        student_data[name]["avg"] = avg

        if summary_data["highest_mark"] is None or total > summary_data["highest_mark"]:
            summary_data["highest_mark"] = total
            summary_data["best_student"] = name

    total_marks = sum(student_data[name]["total"] for name in student_data)
    batch_avg = total_marks / (len(student_data) * len(module_data))
    summary_data["batch_avg"] = batch_avg

    return summary_data

def save_results(student_data, summary_data,module_data):
    # Saves the results to separate text files
    for name, data in student_data.items():
        filename = name.replace(" ", "_") + ".txt"
        with open(filename, "w") as f:
            f.write(f"Name: {name}\n")
            for i, module in enumerate(module_data):
                f.write(f"{module}: {data['marks'][i]}\n")
            f.write(f"Total: {data['total']}\n")
            f.write(f"Average: {data['avg']}\n")

    with open("summary.txt", "w") as f:
        f.write(f"Batch average: {summary_data['batch_avg']}\n")
        f.write(f"Best performing student: {summary_data['best_student']}")
    
    
    if name == "main":
        try:
            student_data = collect_student_data()
            module_data = collect_module_data()
            collect_marks_data(student_data, module_data)
            summary_data = process_data(student_data, module_data)
            save_results(student_data, summary_data)
        except Exception as e:
            print("Error:", e)
            exit(1)
    else:
        print("Results saved successfully")
        exit(0)

