print("Hello World")

checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)

checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    def destroy(index):
        checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# def mark_completed(index):
    # for list_item in checklist:
    # print("\033[1;32;45m read(1) \n")
    
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    list_all_items()

test()
