# Spam Detector - Linear Search (User Defined)

n = int(input("Enter number of blacklisted sender IDs: "))

blacklist = []

for i in range(n):
    sender = input("Enter Sender ID: ")
    blacklist.append(sender)

search = input("Enter Sender ID to search: ")

found = 0

for i in blacklist:
    if i == search:
        found = 1
        break

if found == 1:
    print("Spam Sender Detected")
else:
    print("Sender is Safe")