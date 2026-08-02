import pandas as pd
import os
from sqlalchemy import create_engine
import logging


# Logging configuration
log_path = r"D:\Projects\sales analysis\logs\pipeline.log"

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# connect to server
engine = create_engine(
    "postgresql://postgres:12345@localhost:5432/Olist_DB"
)

logger.info("Database connection created")


def load_to_postgres(df, table, engine):
    """Here we load data from dir to SQL"""
    try:
        df.to_sql(
            table,
            con=engine,
            if_exists="replace",
            index=False
        )

        logger.info(
            f"Table {table} loaded successfully | Rows: {df.shape[0]}"
        )

    except Exception as e:
        logger.error(
            f"Error loading table {table}: {e}"
        )


def Load_data():

    folder_path = r"D:\Projects\sales analysis\Dataset"

    try:
        for file in os.listdir(folder_path):

            file_path = os.path.join(folder_path, file)

            df = pd.read_csv(file_path)

            logger.info(
                f"Reading file {file} | Shape: {df.shape}"
            )

            load_to_postgres(
                df,
                file[:-4],
                engine
            )

        logger.info("All data loaded successfully")

        print("all data load succesfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")


if __name__ == "__main__":
    Load_data()