# Merge Two Sorted Lists

n1 = int(input("Enter size of first waitlist: "))
list1 = []

print("Enter elements of first sorted waitlist:")
for i in range(n1):
    list1.append(int(input()))

n2 = int(input("Enter size of second waitlist: "))
list2 = []

print("Enter elements of second sorted waitlist:")
for i in range(n2):
    list2.append(int(input()))

i = 0
j = 0
merge = []

while i < n1 and j < n2:
    if list1[i] < list2[j]:
        merge.append(list1[i])
        i += 1
    else:
        merge.append(list2[j])
        j += 1

while i < n1:
    merge.append(list1[i])
    i += 1

while j < n2:
    merge.append(list2[j])
    j += 1

print("Merged Waitlist:", merge)