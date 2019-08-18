import os
import sys
import time
import logging

import click

from model.iris import Iris
from model.setting import session
import pandas as pd

app_home = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ""))
log_format = logging.Formatter("%(asctime)s [%(levelname)8s] %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# 標準出力へのハンドラ
# stdout_handler = logging.StreamHandler(sys.stdout)
# stdout_handler.setFormatter(log_format)
# logger.addHandler(stdout_handler)
# ログファイルへのハンドラ
file_handler = logging.FileHandler(os.path.join(app_home, "log", "sample.log"), "a+")
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)


def insert(data):
    """
    Iris Table Inserts
    :rtype: object
    """
    session.bulk_save_objects(
        [Iris(sepal_length=row.sepal_length,
              sepal_width=row.sepal_width,
              petal_length=row.petal_length,
              petal_width=row.petal_width,
              species=row.species)
         for row in data.itertuples()], return_defaults=True)
    session.commit()


@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):
    try:
        print(filename)
        start = time.time()
        logger.info("main():start")
        insert(pd.read_csv(filename))
        logger.info(f"main():end[{time.time() - start}s]")
    except Exception as e:
        logger.exception(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
