from wrap import wrap_lines

text = input("text:\n")

number = input("\nnumber:\n")

justify = input("\njustify?(y/n)\n")

if justify == "y":
    justify = True
    print("\n" + wrap_lines(text, number, justify))
elif justify == "n":
    justify == False
    print("\n" + wrap_lines(text, number, justify))
else:
    print("The value needs to be y or n...")