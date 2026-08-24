counter = 0

def process_counter(list_of_elements):
    global counter 
    if list_of_elements:
        
        if len(list_of_elements) <= 3:
            list_of_elements.clear()
            counter = counter + 1
            return counter
        while len(list_of_elements) > 3:
            del list_of_elements[:3]
            counter = counter + 1
            if len(list_of_elements) != len(set(list_of_elements)) or len(list_of_elements) > 3:
                return process_counter(list_of_elements)
            else:
                return counter 
                
    else:
        print("There are no elements in the list")
        return None 


def main():

    print("How many elements do you want in a list")
    num = int(input())

    print(f"Enter {num} elements one by one")
    num_list = []

    for i in range(num):
        element = int(input())
        num_list.append(element)
    
    print(num_list)
    
    total = process_counter(num_list)

    print(f"Toal number of processes are {total}")


if __name__ == "__main__":
    main()