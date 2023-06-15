import logging
import sqlite3

logging.basicConfig(
    filename="basic.log",
    level=logging.DEBUG,
    format="%(levelname)s %(name)s %(asctime)s %(filename)s %(lineno)d %(message)s",
    datefmt="%x-%X",
)


file_path = "DATA/wombats.txt"

try:
    logging.debug("Opening %s", file_path)
    with open(file_path) as file_in:
        for raw_line in file_in:
            line = raw_line.rstrip()
            print(line)
except (FileNotFoundError, PermissionError) as err:
    logging.critical(err)

logging.info("Hi, Mom!")

with open('DATA/breakfast.txt') as file_in:
    all_food = file_in.read().splitlines()
    try:
        print(all_food[99])
    except IndexError as err:
        logging.exception(err)

numbers = [8, -3, 4.9, 0, 18, 37]
for n in numbers:
    try:
        logging.debug("Dividing %s by %s", 1000, n)
        result = 1000 / n
    except ZeroDivisionError as err:
        logging.error(err)
    except Exception as err:
        logging.error("HUH!! %s", err)
    else:
        print(result)


conn = None
try:
    conn = sqlite3.connect('foom.db')
except sqlite3.DatabaseError as err:  # specified exception was raised
    logging.error(err)
else:  # no exception was raised
    cur = conn.cursor()
    cur.execute("select 5 = 5")
    print(cur.fetchall())
    exit()
finally:  # whether or not there was an exception
    if conn is not None:
        conn.close()




logging.info("All done.")

