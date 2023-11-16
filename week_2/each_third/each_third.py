p = input("Enter items: ")
p = [str(i).strip() for i in p.split(",")]
print(p[2::3])

