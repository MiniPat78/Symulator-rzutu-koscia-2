def interaktywne_menu():
    print("\n" + "="*40)
    print(" PROFESJONALNY SYMULATOR KOŚCI RPG ")
    print("="*40)
    
    while True:
        print("\n[1] Pojedynczy rzut")
        print("[2] Symulacja masowa + Statystyki")
        print("[0] Wyjście")
        
        tryb = input("\nWybierz opcję: ").strip()

        if tryb == '0':
            print("Zamykanie... Powodzenia na sesji RPG!")
            break

        if tryb in ['1', '2']:
            kosc = input("Wybierz kość (4, 6, 20): ").strip()
            if kosc not in ['4', '6', '20']:
                print("BŁĄD: Obsługujemy tylko kości 4, 6 i 20!")
                continue
            
            kod_kosci = f"K{kosc}"

            if tryb == '1':
                wynik = rzut_koscia(kod_kosci)
                print(f"\n>>> WYNIK RZUTU: [ {wynik} ]")

            elif tryb == '2':
                ile = int(input("Ile rzutów wykonać w symulacji? "))
                wyniki = symulacja_masowa(kod_kosci, ile)
                
                stats = oblicz_statystyki(wyniki)
                
                print(f"\n--- WYNIKI SYMULACJI ({ile} rzutów) ---")
                print(f"Średnia: {stats['srednia']:.2f}")
                print(f"Minimum: {stats['min']}")
                print(f"Maximum: {stats['max']}")
                print(f"Historia (pierwsze 10 rzutów): {wyniki[:10]}...")

        else:
            print("Niepoprawny wybór, spróbuj ponownie.")

if __name__ == "__main__":
    interaktywne_menu()
