import time

import dziesiec

@dziesiec.zmierz_czas
def wolna_funkcja(ar=2,ha=[1,2,3]):
    time.sleep(1)
    print("Funkcja zakończona")
    ha.append(ar)
    print(ha)
wolna_funkcja()

if __name__ == "__main__":
    wolna_funkcja()
    wolna_funkcja(1, [])
    wolna_funkcja(1)