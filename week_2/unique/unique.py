import collections

p = input("Enter numbers:")
p = [int(i) for i in p.split(",")]
a = sorted(set(p))
print("Unique:", a)
counted = dict(collections.Counter(p))
print("Amount of occurrences of each unique number in sequence:", counted)
