from utils.logger import logger

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
        logger.info("\n" + "=" * 60)
        logger.info("      Medical Research Intelligence")
        logger.info("=" * 60)

        for key, value in self.options.items():
            logger.info(f"[{key}] {value}")

        logger.info("=" * 60)

    def get_choice(self):
        return input("Select an option: ").strip()
