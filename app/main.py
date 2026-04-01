def interaktywne_menu():
    """Główna pętla gry pozwalająca na interaktywne rzucanie kośćmi."""
    print("\n" + "="*30)
    print(" WITAJ W SYMULATORZE KOŚCI ")
    print("="*30)
    
    while True:
        print("\nDostępne kości: 4, 6, 20")
        wybor = input("Którą kością rzucamy? (wpisz liczbę lub 'koniec'): ").strip().lower()

        if wybor == 'koniec':
            print("\n[!] Zamykanie symulatora. Do widzenia!")
            break

        if wybor in ['4', '6', '20']:
            kod_kosci = f"K{wybor}"
            
            try:
                wynik = rzut_koscia(kod_kosci)
                
                print("-" * 20)
                print(f"  WYLOSOWANO: [ {wynik} ]")
                print("-" * 20)
            except Exception as e:
                print(f"Błąd podczas losowania: {e}")
        else:
            print(">>> BŁĄD: Wybierz 4, 6 lub 20. Jeśli chcesz wyjść, wpisz 'koniec'.")

if __name__ == "__main__":
    interaktywne_menu()
