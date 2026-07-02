# Binary Search - Lower Bound

n = int(input("Enter number of laptop prices: "))

price = []

for i in range(n):
    p = int(input("Enter price: "))
    price.append(p)

target = int(input("Enter target price: "))

low = 0
high = n - 1
ans = -1

while low <= high:
    mid = (low + high) // 2

    if price[mid] >= target:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

if ans != -1:
    print("First laptop price >=", target, "is", price[ans], "at position", ans + 1)
else:
    print("No laptop found")