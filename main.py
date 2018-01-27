from logger import Logger
import logging
import sys

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        logging.error('Usage: python3 main.py clan_id')
        sys.exit(1)

    # Insert your key in the next line
    key = '<YOUR KEY>'

    clan_tag = sys.argv[1]
    logger = Logger(key, clan_tag)
    logger.log_donations()
    logger.log_crowns()
