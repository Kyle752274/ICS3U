# Recursive merge sort function to sort multiple parallel arrays
def mergeSort(arr1, arr2, arr3, arr4, left, right):
    if left < right:
        # Find the middle point to divide the array into two halves
        mid = left + (right - left) // 2

        # Recursively sort the first half
        mergeSort(arr1, arr2, arr3, arr4, left, mid)

        # Recursively sort the second half
        mergeSort(arr1, arr2, arr3, arr4, mid + 1, right)

        # Merge the sorted halves
        merge(arr1, arr2, arr3, arr4, left, mid, right)

# Function to merge two sorted halves of arrays
def merge(arr1, arr2, arr3, arr4, left, mid, right):
    # Calculate sizes of the two subarrays
    size1, size2 = mid - left + 1, right - mid

    # Create temporary arrays to hold the subarray elements
    temp1, temp2, temp3, temp4 = [0] * size1, [0] * size1, [0] * size1, [0] * size1
    temp5, temp6, temp7, temp8 = [0] * size2, [0] * size2, [0] * size2, [0] * size2

    # Copy data to temporary arrays
    for i in range(size1):
        temp1[i], temp2[i], temp3[i], temp4[i] = arr1[left + i], arr2[left + i], arr3[left + i], arr4[left + i]
    for j in range(size2):
        temp5[j], temp6[j], temp7[j], temp8[j] = arr1[mid + 1 + j], arr2[mid + 1 + j], arr3[mid + 1 + j], arr4[mid + 1 + j]

    # Merge the temporary arrays back into the original arrays
    i, j, k = 0, 0, left
    while i < size1 and j < size2:
        if temp1[i] <= temp5[j]:
            arr1[k], arr2[k], arr3[k], arr4[k] = temp1[i], temp2[i], temp3[i], temp4[i]
            i += 1
        else:
            arr1[k], arr2[k], arr3[k], arr4[k] = temp5[j], temp6[j], temp7[j], temp8[j]
            j += 1
        k += 1

    # Copy any remaining elements of the first subarray
    while i < size1:
        arr1[k], arr2[k], arr3[k], arr4[k] = temp1[i], temp2[i], temp3[i], temp4[i]
        i += 1
        k += 1

    # Copy any remaining elements of the second subarray
    while j < size2:
        arr1[k], arr2[k], arr3[k], arr4[k] = temp5[j], temp6[j], temp7[j], temp8[j]
        j += 1
        k += 1

# File containing the data
file_name = "data.dat"
file_handle = open(file_name, 'r')

# Lists to store data from the file
name_list, card_numbers, card_types, expiry_list = [], [], [], []

# Read all lines from the file and remove the header line
lines = file_handle.readlines()
lines.pop(0)  # Remove header

# Parse each line and extract data into corresponding lists
for line in lines:
    first_name, last_name, card_type, card_number, month, year = line.strip().split(',')
    full_name = first_name + ' ' + last_name
    name_list.append(full_name)
    card_types.append(card_type)
    card_numbers.append(card_number)
    month = month.zfill(2)  # Ensure the month is 2 digits
    expiry_list.append(int(year + month))  # Combine year and month as an integer

file_handle.close()

# Sort all lists by expiry date using merge sort
mergeSort(expiry_list, name_list, card_numbers, card_types, 0, len(expiry_list) - 1)

# Write the sorted data to an output file
with open("output.txt", "w") as output_file:
    for idx in range(len(expiry_list)):
        # Check the status of each card based on expiry date
        if expiry_list[idx] > 202501:
            break
        status = "EXPIRED" if expiry_list[idx] < 202501 else "RENEW IMMEDIATELY"

        # Format the output line
        output_line = "%-35s %-15s %-20s %-8s %-15s\n" % (name_list[idx], card_types[idx], card_numbers[idx], expiry_list[idx], status)

        # Print and write the output line to the file
        print(output_line.strip())
        output_file.write(output_line)
