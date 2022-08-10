import os
from time import sleep

import psycopg2
from loguru import logger
from dotenv import load_dotenv
from colorama import init, Fore

init()

logger.add('log/debug.log', level='DEBUG',
           format='{time} {message} {level}', rotation='10 KB', compression='zip')

dotenv_path = os.path.join(os.path.dirname(__file__), 'env/.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

try:
    conn = psycopg2.connect(
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST')
    )
except Exception as _ex:
    logger.exception(_ex)
else:
    conn.autocommit = True
    print(f'{Fore.GREEN}[INFO] Database is connected...')


@logger.catch
def main():
    sleep(2)
    try:
        conn.close()
    except Exception as _ex:
        logger.exception(_ex)
    else:
        print(f'{Fore.RED}[INFO] Database is disconnected')


if __name__ == '__main__':
    main()
