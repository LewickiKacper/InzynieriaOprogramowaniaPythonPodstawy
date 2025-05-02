"""
Zadanie 1 - Weryfikacja numeru PESEL

Opis zadania:
- Użytkownik wprowadza numer PESEL (ciąg 11 znaków, zakładamy, że długość jest poprawna).
- Program sprawdza, czy ostatnia cyfra (cyfra kontrolna) jest prawidłowa.
- Reguła: znaleźć w internecie.
- Jeśli ostatnia cyfra zgadza się z obliczoną wartością, funkcja ma zwrócić 1, w przeciwnym wypadku 0.

Przykładowe wejście:
    "97082123152"
Przykładowe wyjście:
    0

Wymagania:
- Implementacja funkcji `verify_pesel(pesel: str) -> int`.
- Użycie algorytmu weryfikacji opisanej powyżej.
"""


def verify_pesel(pesel: str) -> int:
    if len(pesel) != 11 or not pesel.isdigit():
        return 0

    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = 0

    for i in range(10):
        iloczyn = int(pesel[i]) * wagi[i]
        suma += iloczyn % 10

    cyfra_kontrolna = (10 - suma % 10) % 10

    return 1 if cyfra_kontrolna == int(pesel[-1]) else 0



# Przykładowe wywołanie:
if __name__ == "__main__":
    pesel_input = "97082123152"
    print(verify_pesel(pesel_input))  # Oczekiwane wyjście: 0