def dodawanie(a: float, b: float) -> float:
    """Funkcja dodawania"""
    wynik = a + b
    print(f"Wynik dodawania: {wynik}")

def odejmowanie(a: float, b: float) -> float:
    """Funkcja odejmowania"""
    wynik = a - b
    print(f"Wynik odejmowania: {wynik}")

def mnozenie(a: float, b: float) -> float:
    """Funkcja mnożenia"""
    wynik = a * b
    print(f"Wynik mnożenia: {wynik}")

def dzielenie(a: float, b: float) -> float:
    """Funkcja dzielenia"""
    try:
        wynik = a / b
        print(f"Wynik dzielenia: {wynik}")
    except ZeroDivisionError:
        print("Nie dziel przez 0")

def kalkulator() -> None:
    """Funkcja wyboru opcji liczenia"""
    while True:
        print("1 - dodawanie")
        print("2 - odejmowanie")
        print("3 - mnożenie")
        print("4 - dzielenie")
        print("9 - koniec")

        a = None
        b = None

        try:

            wybor = int(input("Wybierz opcje: "))
            
            if wybor not in [1, 2, 3, 4]:
                print("****Błędny numer!****")
                continue
            a = float(input("pierwsza liczba: "))
            b = float(input("druga liczba: "))

            if wybor == 1:
                dodawanie(a, b)
            elif wybor == 2:
                odejmowanie(a, b)
            elif wybor == 3:
                mnozenie(a, b)
            elif wybor == 4:
                dzielenie(a, b)
            elif wybor == 9:
                print("Dalej liczysz sam")
                break

        except ValueError:
            print("Błędne dane - podaj LICZBĘ")

kalkulator()