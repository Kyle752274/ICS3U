def mergeSort(arr1, arr2, arr3, arr4, left, right):
    if left < right:
        mid = left + (right - left) // 2
        mergeSort(arr1, arr2, arr3, arr4, left, mid)
        mergeSort(arr1, arr2, arr3, arr4, mid + 1, right)
        merge(arr1, arr2, arr3, arr4, left, mid, right)

def merge(arr1, arr2, arr3, arr4, left, mid, right):
    size1, size2 = mid - left + 1, right - mid
    temp1, temp2, temp3, temp4 = [0] * size1, [0] * size1, [0] * size1, [0] * size1
    temp5, temp6, temp7, temp8 = [0] * size2, [0] * size2, [0] * size2, [0] * size2

    for i in range(size1):
        temp1[i], temp2[i], temp3[i], temp4[i] = arr1[left + i], arr2[left + i], arr3[left + i], arr4[left + i]
    for j in range(size2):
        temp5[j], temp6[j], temp7[j], temp8[j] = arr1[mid + 1 + j], arr2[mid + 1 + j], arr3[mid + 1 + j], arr4[mid + 1 + j]

    i, j, k = 0, 0, left
    while i < size1 and j < size2:
        if temp1[i] <= temp5[j]:
            arr1[k], arr2[k], arr3[k], arr4[k] = temp1[i], temp2[i], temp3[i], temp4[i]
            i += 1
        else:
            arr1[k], arr2[k], arr3[k], arr4[k] = temp5[j], temp6[j], temp7[j], temp8[j]
            j += 1
        k += 1

    while i < size1:
        arr1[k], arr2[k], arr3[k], arr4[k] = temp1[i], temp2[i], temp3[i], temp4[i]
        i += 1
        k += 1

    while j < size2:
        arr1[k], arr2[k], arr3[k], arr4[k] = temp5[j], temp6[j], temp7[j], temp8[j]
        j += 1
        k += 1

file_name = "data.dat"
file_handle = open(file_name, 'r')

name_list, card_numbers, card_types, expiry_list = [], [], [], []

lines = file_handle.readlines()
lines.pop(0) 

for line in lines:
    first_name, last_name, card_type, card_number, month, year = line.strip().split(',')
    full_name = first_name + ' ' + last_name
    name_list.append(full_name)
    card_types.append(card_type)
    card_numbers.append(card_number)
    month = month.zfill(2)
    expiry_list.append(int(year + month))

file_handle.close()

mergeSort(expiry_list, name_list, card_numbers, card_types, 0, len(expiry_list) - 1)

with open("output.txt", "w") as output_file:
    for idx in range(len(expiry_list)):
        if expiry_list[idx] > 202501:
            break
        status = "EXPIRED" if expiry_list[idx] < 202501 else "RENEW IMMEDIATELY"
        output_line = "%-35s %-15s %-20s %-8s %-15s\n" % (name_list[idx], card_types[idx], card_numbers[idx], expiry_list[idx], status)
        print(output_line.strip())
        output_file.write(output_line)
