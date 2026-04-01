import random

class DiceSimulator:
    def __init__(self):
        self.history = []

    def roll_dice(self, sides=6, num_dice=1):
        """Podstawowy rzut wybraną liczbą kości o określonej liczbie ścianek."""
        if sides < 2 or num_dice < 1:
            raise ValueError("Nieprawidłowe parametry kości")
        
        rolls = [random.randint(1, sides) for _ in range(num_dice)]
        self.history.extend(rolls)
        return rolls

    def get_statistics(self):
        """Zwraca statystyki ze wszystkich dotychczasowych rzutów."""
        if not self.history:
            return {"total_rolls": 0, "message": "Brak historii rzutów."}
        
        return {
            "total_rolls": len(self.history),
            "sum": sum(self.history),
            "average": round(sum(self.history) / len(self.history), 2),
            "min": min(self.history),
            "max": max(self.history)
        }

    def simulate(self, sides=6, num_rolls=100):
        """Tryb symulacji: masowe rzuty do testów statystycznych."""
        return self.roll_dice(sides, num_rolls)

if __name__ == "__main__":
    sim = DiceSimulator()
    print("Rzut 2x k6:", sim.roll_dice(sides=6, num_dice=2))
    print("Rzut 1x k20 (krytyk?):", sim.roll_dice(sides=20, num_dice=1))
    print("Statystyki:", sim.get_statistics())
