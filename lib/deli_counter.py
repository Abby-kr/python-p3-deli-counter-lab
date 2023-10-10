katz_deli = []

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    elif len(katz_deli) > 0:
        string = ""
        index = 1
        for customer in katz_deli:
            string += f" {index}. {customer}"
            index += 1
        print("The line is currently:" + string)

def take_a_number(list,name):
    if len(list) == 0:
        list.append(name)
        print(f"Welcome, {name}. You are number 1 in line.")
    elif len(list) > 0:
        list.append(name)
        position = len(list) 
        print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(list):
    if len(list) > 0:
        print(f"Currently serving {list[0]}.")
        list.pop(0)
    else:
        print("There is nobody waiting to be served!")
