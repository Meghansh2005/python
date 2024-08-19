def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def sort_switch_case(choice, arr):
    # Dictionary to simulate switch-case functionality
    switch = {
        1: bubble_sort,
        2: merge_sort,
        3: selection_sort,
        4: insertion_sort
    }

    # Get the sorting function from the dictionary
    sort_function = switch.get(choice, lambda arr: "Invalid choice")

    # Execute the sorting function
    return sort_function(arr)

# Example usage
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)

choice = int(input("Choose sorting algorithm:\n1. Bubble Sort\n2. Merge Sort\n3. Selection Sort\n4. Insertion Sort\nEnter your choice: "))

sorted_arr = sort_switch_case(choice, arr.copy())
print("Sorted array:", sorted_arr)
