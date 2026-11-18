def fractional_knapsack(profit, weight, capacity):
    items = sorted(zip(profit, weight), key=lambda x: x[0] / x[1], reverse=True)

    total = 0

    for p, w in items:
        if capacity >= w:
            total += p
            capacity -= w
        else:
            total += (p / w) * capacity
            break

    return total


n = int(input("Enter number of parcels: "))
profit = []
weight = []

for i in range(n):
    p = int(input("Enter profit of parcel " + str(i + 1) + ": "))
    w = int(input("Enter weight of parcel " + str(i + 1) + ": "))
    profit.append(p)
    weight.append(w)

capacity = int(input("Enter capacity of truck: "))

print("Maximum profit =", fractional_knapsack(profit, weight, capacity))
