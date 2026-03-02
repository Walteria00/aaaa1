wiek=int(input("Podaj swój wiek: "))

if wiek >= 18 and wiek < 35:
    print("Możesz głosować.")
elif wiek >= 35:
    print("Możesz nawet zostać prezydentem.")
else:
    print("Nie możesz głosować.")
