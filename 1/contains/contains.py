print("Add your letter: ")
l=str(input())
print("Add your word: ")
w=str(input())
if l in w:
    print('The word', w,  'contains letter', l)
else:
    print('The word', w,  'does not contain letter', l)
