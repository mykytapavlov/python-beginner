p = input("Enter items:")
p = p.split(",")

quotient, remainder = divmod(len(p), 2)
res_first = p[:quotient + remainder]
res_second = p[quotient + remainder:]

print(f"The first part of string :{res_first}")
print(f"The second part of string :{res_second}")