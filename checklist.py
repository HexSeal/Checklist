
import subprocess
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
    update(index, "\u001b[32m√ " + checklist[index] + "\u001b[0m")

def unmark(index):
    new_item = checklist[index].replace("√ ","\u001b[0m")
    update(index, new_item)

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
    function_code = function_code.lower()

    try:

        if function_code == "c":
            subprocess.run("clear")
            input_item = user_input("Input item: ")
            create(input_item)
            return True

        elif function_code == "r":
            subprocess.run("clear")
            item_index = user_input("Index Number: ")
            print(read(int(item_index)))
            return True

        elif function_code == "p":
            subprocess.run("clear")
            list_all_items()
            return True

        elif function_code == "q":
            return False

        elif function_code == "d":
            subprocess.run("clear")
            item_index = user_input("Index Number: ")
            destroy(int(item_index))
            return True

        elif function_code == "m":
            subprocess.run("clear")
            item_index = user_input("Index Number: ")
            mark_completed(int(item_index))
            return True

        elif function_code == "u":
            subprocess.run("clear")
            item_index = user_input("Index Number: ")
            item_input = user_input("Item to replace with: ")
            update(int(item_index), str(item_input))
            return True

        elif function_code == "y":
            subprocess.run("clear")
            item_index = user_input("Index Number: ")
            unmark(int(item_index))
            return True

        else:
            print("Unknown Option")
            return True

    except IndexError:
        print("That is not a valid index, please try again: ")
        return True
    
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
    selection = user_input("C: add to list \nR: Read from list \nP: display list \nD: Delete an item \nU: Update \nM: Mark as complete \nY: Unmark as complete \nQ: quit: \n")
    running = select(selection)