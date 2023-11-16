p = input("Enter numbers:")
p = [int(i) for i in p.split(",")]
p.sort()
print(p)

# OR
# p = input("Enter numbers:")
# p = p.split(",")
# p.sort(key = int)
# print(p)
