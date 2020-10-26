from function import print_all_task, get_current_datetime, success_msg, error_msg


data = {}

task = ""
helper_static = {"isdone": False, "created_on": ""}

while True:
    action = input("Your action ('create', 'read' 'update', 'delete') (if exit enter 'x' ): : ")
    if action == 'x':
        break
    if action == "create":
        task = input("Add task : ")
        tasks_list = list(data.keys())
        if task in tasks_list:
            error_msg("your task has already created")
        else:
            helper_static["created_on"] = get_current_datetime()
            helper_static["isdone"] = False
            data[task] = helper_static
            
            success_msg("created")

    elif action == "read":
        print_all_task(data)
    elif action == "update":
        task = input("Enter task name which you want to update: ")
        tasks_list = list(data.keys())
        if task in tasks_list:
            data[task] = {"isdone": True, "created_on": data[task]["created_on"]}
            
            success_msg("updated")
        else:
            error_msg("your task isn't in database")

    elif action == "delete":
        task = input("Enter task name which you want to delete: ")
        tasks_list = list(data.keys())
        if task in tasks_list:
            del data[task]
            success_msg("deleted")
        else:
            error_msg("your task isn't in database")
      
    else:
        print("I don't have this action please try again !!!")

# print_all_task(data)