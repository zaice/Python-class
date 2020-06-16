
answer = input("Is there bread?")
if answer == "Yes":
    is_bread = True
if input("Is there milk?")  == "Yes":
    is_milk = True
if input("Is there eggs?") == "Yes":
    is_eggs = True

print(is_bread)
print(is_eggs)
print(is_milk)


if is_bread & is_milk & is_eggs:
    print("The Grenki is going to be delish!")
elif is_eggs & is_milk:
    print("Welp, no Grenki..I'll just make an omlet")
else:
   print("At least I can drink some water!")        


   