from datetime import datetime

def print_all_task(tasks):
    if len(tasks) > 0:
        j = 1
        print("id. name\t    status\tcreated on")
        for key, value in tasks.items():
            status = value["isdone"]
            status_text = "not complate"
            if status == True:
                status_text = "complated"
            created_on = value["created_on"]
            print(f"{j}.  {key}    {status_text}       {created_on}")
            j+=1
    else:
        print("You don't have any task")

def success_msg(msg_type):
    print(f"Your task succesfuly {msg_type}")

def get_current_datetime():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def error_msg(error_str):
    print(f"Error: {error_str}")