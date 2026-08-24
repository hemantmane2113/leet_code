def process_counter(list_of_elements):
    global counter

    # ✅ STOP condition FIRST
    if len(list_of_elements) == len(set(list_of_elements)):
        return counter

    # If list is empty
    if not list_of_elements:
        return counter

    # Perform one operation
    counter += 1

    if len(list_of_elements) <= 3:
        list_of_elements.clear()
        return counter

    # Remove first three elements
    del list_of_elements[:3]

    # Recurse
    return process_counter(list_of_elements)

def main():
    global counter
    counter = 0   # ✅ reset for each test case

    print("How many elements do you want in a list")
    num = int(input())

    print(f"Enter {num} elements one by one")
    num_list = []

    for i in range(num):
        element = int(input())
        num_list.append(element)

    total = process_counter(num_list)
    print(f"Total number of processes are {total}")

