import time

def zmierz_czas(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = funkcja(*args, **kwargs)
        koniec = time.time()
        print(f"Funkcja {funkcja.__name__} wykonała się w {koniec-start:.4f} sekund")
        return wynik
    return wrapper