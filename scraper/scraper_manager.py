from utils.logger import logger


class ScraperManager:

    def __init__(self):

        self.scrapers = {}

        logger.info("Scraper Manager initialized")


    def register_scraper(self, name, scraper):

        self.scrapers[name] = scraper

        logger.info(
            f"Registered scraper: {name}"
        )


    def get_scraper(self, name):

        scraper = self.scrapers.get(name)

        if scraper:
            logger.info(
                f"Loading scraper: {name}"
            )

            return scraper

        logger.warning(
            f"Scraper not found: {name}"
        )

        return None


    def close_all(self):

        logger.info(
            "Closing all scrapers"
        )

        for name, scraper in self.scrapers.items():

            scraper.close()

            logger.info(
                f"Closed {name}"
            )
