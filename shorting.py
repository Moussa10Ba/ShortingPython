
import algorithm

myArray = [13, 27, 19, 30, 2, 16, 3, 7]

sort_type = int(input("What shorting method do you want to try Today ? (1: Bubble, 2: Merge, 3: Insertion, 4: Selection): "))

while sort_type < 1 or sort_type > 4:
        print('Invalid Selection, Please chose a valid entry')
        sort_type = int(input("What shorting method do you want to try Today ? (1: Bubble, 2: Merge, 3: Insertion, 4: Selection): "))


if sort_type == 1:
    sorted_arr = algorithm.bubble_sort(myArray)
elif sort_type == 2:
    sorted_arr = algorithm.merge_sort(myArray)
elif sort_type == 3:
    sorted_arr = algorithm.insertion_sort(myArray)
elif sort_type == 4:
    sorted_arr = algorithm.selection_sort(myArray)
else:
    print("Invalid input. Please enter a number between 1 and 4.")


print("Sorted array:", sorted_arr)