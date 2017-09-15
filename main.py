from logger import Logger
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    clan_tag = '2UQ2JJC'
    logger = Logger(clan_tag)
    logger.log_donations()
    logger.log_crowns()
