from config.settings import settings
from database.sqlite import connect_database
from utils.logger import logger
from ui.menu import MainMenu
from scraper.pubmed import pubmed_search

def main():
    
    logger.info("Starting Medical Research Intelligence")
    database = connect_database()

    menu = MainMenu()

    while True:
        menu.show()
        choice = menu.get_choice()

        if choice == "1":
            logger.info("\nLaunching Literature Search...\n")

        elif choice == "2":
            logger.info("\nLaunching Gene Lookup...\n")
            gene_name = input("Enter gene symbol (e.g. TP53, BRCA1): ")
            organism = input("Enter organism [Homo sapiens]: ") or "Homo sapiens"       
            result = pubmed_search.fetch_gene(gene_name, organism)

        elif choice == "3":
            logger.info("\nLaunching Sequence Search...\n")

        elif choice == "4":
            logger.info("\nLaunching Protein Analysis...\n")

        elif choice == "5":
            logger.info("\nLaunching Disease Research...\n")

        elif choice == "6":
            logger.info("\nLaunching Mutation Analysis...\n")

        elif choice == "7":
            logger.info("\nLaunching Protein Structures...\n")

        elif choice == "8":
            logger.info("\nGenerating Report...\n")

        elif choice == "9":
            logger.info("\nOpening Settings...\n")

        elif choice == "0":
            logger.info("\nGoodbye!")
            break

        else:
            logger.info("\nInvalid selection.\n")
    


if __name__ == "__main__":
    main()
