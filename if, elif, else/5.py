from os import access

try:
    wiek=int(input("Podaj swój wiek: "))
except:
    print("Nie to, matma u ma byc")
if wiek is not None:
    if wiek >= 18 and wiek < 35:
        print("Możesz głosować.")
    elif wiek >= 35:
        print("Możesz nawet zostać prezydentem.")
    else:
        print("Nie możesz głosować.")
