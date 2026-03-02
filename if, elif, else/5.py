try:
    wiek=int(input("Podaj swój wiek: "))
except:
    print("Nie to, matma u ma być, nie umiesz w liczby.")
if wiek is not None:
    if wiek >= 18 and wiek < 35:
        print("Umiesz w liczby i możesz głosować.")
    elif wiek >= 35:
        print("Umiesz w liczby i możesz teraz zostać prezydentem.")
    else:
        print("U miesz w liczby ale nie możesz głosować.")
