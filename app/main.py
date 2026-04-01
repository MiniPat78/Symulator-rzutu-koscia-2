import random

DOZWOLONE_KOSCI = [4, 6, 20]

def rzut_koscia(typ_kosci):
    """Symuluje pojedynczy rzut kością (K4, K6 lub K20)."""
    if typ_kosci not in DOZWOLONE_KOSCI:
        raise ValueError(f"Niedozwolony typ kości. Wybierz jedną z: {DOZWOLONE_KOSCI}")
    return random.randint(1, typ_kosci)

def oblicz_statystyki(wyniki):
    """Oblicza sumę, średnią oraz wartości skrajne (min, max) dla rzutów."""
    if not wyniki:
        return {"suma": 0, "srednia": 0.0, "min": None, "max": None}
    return {
        "suma": sum(wyniki),
        "srednia": round(sum(wyniki) / len(wyniki), 2),
        "min": min(wyniki),
        "max": max(wyniki)
    }

def symulacja_masowa(typ_kosci, liczba_rzutow):
    """Przeprowadza masową symulację rzutów."""
    if liczba_rzutow <= 0:
        raise ValueError("Liczba rzutów musi być większa niż 0.")
    return [rzut_koscia(typ_kosci) for _ in range(liczba_rzutow)]

def tryb_gry(typ_kosci, prog_zwyciestwa):
    """
    Tryb gry: rzucasz wybraną kością, aż suma Twoich rzutów 
    osiągnie lub przekroczy wyznaczony próg zwycięstwa.
    """
    historia_rzutow = []
    suma_punktow = 0
    
    while suma_punktow < prog_zwyciestwa:
        wynik = rzut_koscia(typ_kosci)
        historia_rzutow.append(wynik)
        suma_punktow += wynik
        
    return {
        "liczba_rund": len(historia_rzutow),
        "historia_rzutow": historia_rzutow,
        "koncowa_suma": suma_punktow
    }
    
if __name__ == "__main__":
    print("=" * 40)
    print(" WITAJ W SYMULATORZE RZUTU KOŚCIĄ! ")
    print("=" * 40)
    
    try:
        wybrana_kosc = int(input(f"Wybierz kość z dostępnych {DOZWOLONE_KOSCI}: "))
        wybrany_prog = int(input("Podaj próg punktów do wygranej (np. 50): "))
        
        print("\nRozpoczynam grę...")
        
        wynik = tryb_gry(wybrana_kosc, wybrany_prog)
        
        print("-" * 40)
        print("WYNIKI GRY:")
        print(f"Liczba rund: {wynik['liczba_rund']}")
        print(f"Historia rzutów: {wynik['historia_rzutow']}")
        print(f"Końcowa suma punktów: {wynik['koncowa_suma']}")
        print("-" * 40)
        
    except ValueError as e:
        print(f"\nBłąd: {e}")
        print("Uruchom program ponownie i podaj poprawne dane (tylko liczby całkowite).")
