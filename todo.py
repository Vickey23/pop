import json
import atexit

zadania = []
ostatnie_id = 0

def zaladuj_zadania():
    try:
        with open('Zadania.json', 'r') as f:
            zadania.extend(json.load(f))
    except FileNotFoundError:
        print("Nie znaleziono pliku")
        pass

def zapisz_zadania():
    with open('Zadania.json', 'w') as f:
        json.dump(zadania, f)

def wyswietl_zadania():
    if len(zadania) == 0:
        print("Brak zadań.")
    else:
        for zadanie in zadania:
            print("ID zadania: ", zadanie['id'])
            print("Tytuł zadania: ", zadanie['tytul'])
            print("Data wykonania: ", zadanie['data'])
            print("")

def wyswietl_szczegoly(zadanie):
    print("Opis zadania: ", zadanie['opis'])
    print("")

def aktualizacja_ostatniego_id():
    global ostatnie_id
    if len(zadania) > 0:
        ostatnie_id = max(zadanie['id'] for zadanie in zadania)

def dodaj_zadanie():
    global ostatnie_id

    tytul = input("Tytuł zadania: ")
    opis = input("Opis zadania: ")
    data = input("Termin wykonania zadania: ")

    ostatnie_id += 1
    zadanie = {
        'id': ostatnie_id,
        'tytul': tytul,
        'opis': opis,
        'data': data
    }

    zadania.append(zadanie)
    print("Twoje zadanie zostało dodane.")
    print("")

def prawidlowy_input(komunikat, typ):
    while True:
        try:
            input_uzytkownika = typ(input(komunikat))
            return input_uzytkownika
        except ValueError:
            print("Nieprawidłowe dane.")

def usun_zadanie():
    zadanie_id = prawidlowy_input("Podaj ID zadania do usunięcia: ", int)
    for zadanie in zadania:
        if zadanie['id'] == zadanie_id:
            zadania.remove(zadanie)
            print("Zadanie usunięte.")
            print("")
            return
    print("Brak zadania o podanym ID!")
    print("")

def zaktualizuj_zadania():
    zadanie_id = prawidlowy_input("Podaj ID zadania do aktualizacji: ", int)

    for zadanie in zadania:
        if zadanie['id'] == zadanie_id:
            tytul = input("Podaj nowy tytuł zadania: ")
            opis = input("Podaj nowy opis zadania: ")
            data = input("Podaj nowy termin wykonania zadania: ")

            zadanie['title'] = tytul
            zadanie['description'] = opis
            zadanie['due_date'] = data

            print("Zadanie zaktualizowane.")
            print("")
            return

        print("Brak zadania o podanym ID!")
        print("")

def zapisz_do_pliku():
    zapis = input("Czy chcesz zapisać zadania do pliku? T/N ")
    if zapis.upper() == 'T':
        print("Zadania zostały zapisane do pliku.")
        print("")
    else:
        print("Zadania nie zostały zapisane do pliku.")
        print("")

def zamkniecie():
    zapisz_zadania()

def menu():
    zaladuj_zadania()

    if len(zadania) > 0:
        wyswietl_zadania()
    else:
        print("Brak zadań!")
        print("")

    while True:
        print("****menu zadań****")
        print("1 - Dodaj nowe zadanie")
        print("2 - Usuń zadanie")
        print("3 - Zaktualizuj zadanie")
        print("4 - Wyświetl zadania")
        print("5 - Zapisz zadania do pliku")
        print("6 - Wyjście")

        wybor = prawidlowy_input("Wybierz opcję: ", str)

        if wybor == '1':
            dodaj_zadanie()
        elif wybor == '2':
            if len(zadania) == 0:
                print("Brak zadań.")
            else:
                for zadanie in zadania:
                    print("ID zadania: ", zadanie['id'])
                    print("Tytuł zadania: ", zadanie['tytul'])
            usun_zadanie()
        elif wybor == '3':
            zaktualizuj_zadania()
        elif wybor == '4':
            wyswietl_zadania()
            id_zadania = prawidlowy_input("\nPodaj ID zadania, aby wyświetlić jego opis lub 0 aby wrócić do menu: ", int)
            if id_zadania != 0:
                for zadanie in zadania:
                    if zadanie['id'] == id_zadania:
                        wyswietl_szczegoly(zadanie)
        elif wybor == '5':
            zapisz_do_pliku()
            print("Zadania zostały zapisane do pliku.")
        elif wybor == '6':
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie")
            print("")

if __name__ == '__main__':
    atexit.register(zamkniecie)
    menu()