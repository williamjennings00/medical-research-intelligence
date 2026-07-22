class MainMenu:
    def __init__(self):
        self.options = {
            "1": "Search Scientific Literature",
            "2": "Gene Lookup",
            "3": "DNA/RNA Sequence Search",
            "4": "Protein Analysis",
            "5": "Disease Research",
            "6": "Mutation Analysis",
            "7": "Protein Structures",
            "8": "Generate Research Report",
            "9": "Settings",
            "0": "Exit"
        }

    def show(self):
        print("\n" + "=" * 60)
        print("      Medical Research Intelligence")
        print("=" * 60)

        for key, value in self.options.items():
            print(f"[{key}] {value}")

        print("=" * 60)

    def get_choice(self):
        return input("Select an option: ").strip()
