# Write a program to find the common elements in lists containing "sorted Lists".
# Question = [[1, 2, 3, 10], [1, 1, 1, 1, 10], [1, 10], [5, 9, 10], [10]]
# Ans:  [10]


def insert_z(array_intersection, x):
    if not array_intersection:
        array_intersection.append(x)
    if x == array_intersection[len(array_intersection) - 1]:
        return array_intersection
    array_intersection.append(x)
    return array_intersection


def main():

    multiple_list = [[1, 2, 3, 10],
                     [1, 1, 1, 1, 10],
                     [1, 10], [5, 9, 10], [10]]

    # We may have lists of various sizes and for intersection, its best to select smallest list first.
    # This way, if we have multiple lists with billion numbers and one list with just one number, we will end up
    # with lower number of comparisons
    multiple_list.sort(key=len)

    total_array_length = 0

    # Find the total elements in all the lists.
    # Total = len(A) + len(B) + len(C) + ....
    for eachArray in multiple_list:
        total_array_length = total_array_length + len(eachArray)

    # Create a list that holds pointers to each list
    index_list_of_all_arrays = [0] * len(multiple_list)

    # List to hold all the intersecting elements.
    array_intersection = []
    while total_array_length:
        # If any one of the list is empty it means, we do not have a intersection.
        # If any list has exhausted the elements, its as good as empty list. Exit complete loop.
        exit_full_program = False
        for index_number, eachArray in enumerate(multiple_list):
            if not eachArray or index_list_of_all_arrays[index_number] == len(eachArray):
                exit_full_program = True
                break
        if exit_full_program:
            break
        # Pick an a'th element in first array to compare with elements in other arrays.
        content_of_one_array = multiple_list[0][index_list_of_all_arrays[0]]

        # Check if the a'th element in the first array is present at the current location of the array.
        intersection_flag = True
        for index_number, eachArray in enumerate(multiple_list):
            if eachArray[index_list_of_all_arrays[index_number]] != content_of_one_array:
                # One of the array pointer is not same as elements pointed by other pointer.
                # If a'th element does not match other the b,c,d... element in other arrays exit the loop
                intersection_flag = False
                break

        if intersection_flag:
            # If we have reached here, it means, we have found one element in first array common among other arrays
            # too.
            # Insert the array
            array_intersection = insert_z(array_intersection, content_of_one_array)

            for index_number, each_Array_index_pointer in enumerate(index_list_of_all_arrays):
                # As we have found the match at current position in all the elements, increment the index of all the
                # arrays.
                each_Array_index_pointer += 1
                index_list_of_all_arrays[index_number] = each_Array_index_pointer
                # Since we have already visited one element in each array, we need to decrement total counter by n times
                # n = number of lists.
                total_array_length -= 1
            # Continue checking for other numbers
            continue

        # At this point we have some index the array pointed to a number which does not intersect with rest.
        all_the_data_list = []
        for index_number, eachList in enumerate(multiple_list):
            all_the_data_list.append(eachList[index_list_of_all_arrays[index_number]])

        largest = max(all_the_data_list)

        for index_number, eachList in enumerate(multiple_list):
            while index_list_of_all_arrays[index_number] < len(eachList) and \
                    largest > eachList[index_list_of_all_arrays[index_number]]:
                index_list_of_all_arrays[index_number] += 1
                total_array_length -= 1

    print(array_intersection)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
