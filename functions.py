FILENAME= "tasks.txt"

def read_tasks(file=FILENAME):
    """Open and read tasks file"""
    with open(file,"r") as local_file:
        local_tasks = local_file.readlines()
    return local_tasks

def write_tasks(tasks_arg, file=FILENAME):
    """Open and write on tasks file"""
    with open(file,"w") as local_file:
        local_file.writelines(tasks_arg)