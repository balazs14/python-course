
from pprint import pprint
import pandas as pd
import numpy as np

from tardis_client import TardisClient, Channel
from tardis_dev import datasets


def example_download_of_a_dataset():

    datasets.download(
        exchange="binance-european-options",
        data_types=[
        #    'book_snapshot_25'
        'trades'
        ],
        from_date="2025-05-01",
        to_date="2025-05-01",
        symbols=['OPTIONS'],
        api_key="YOUR API KEY (optionally)",
    )

if __name__ == '__main__':
    example_download_of_a_dataset()