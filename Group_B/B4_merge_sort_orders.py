def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


n = int(input("Enter number of orders: "))
orders = []

for i in range(n):
    oid = input("Enter order id: ")
    time = int(input("Enter delivery time (minutes): "))
    orders.append([oid, time])

print("\nBefore sorting")
for o in orders:
    print("Order", o[0], "-", o[1], "min")

merge_sort(orders)

print("\nAfter sorting")
for o in orders:
    print("Order", o[0], "-", o[1], "min")
