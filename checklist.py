checklist = list()
checklist.append('Blue')
checklist.append('Orange')

checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
        checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    update(index, "√ "+checklist[index])

def select(function_code):
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)
        return True

    elif function_code == "R":
        item_index = user_input("Index Number: ")
        print(read(int(item_index)))
        return True

    elif function_code == "P":
        list_all_items()
        return True

    elif function_code == "Q":
        return False

    elif function_code == "D":
        item_index = user_input("Index Number: ")
        destroy(int(item_index))
        return True

    else:
        print("Unknown Option")
        return True
    
def user_input(prompt):
    user_input = input(prompt)
    return user_input

def test():
    create("purple socks")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    list_all_items()
    mark_completed(0)

    select("C")
    # View the results
    list_all_items()

    select("R")

    list_all_items()
 
    user_value = user_input("Please enter a value:")
    print(user_value)

running = True
while running:
    selection = user_input("C: to add to list R: Read from list P: display list, Q: quit: ")
    running = select(selection)