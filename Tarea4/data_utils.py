import pandas as pd


def import_dataset(filename):
    ds = pd.read_csv(filename + '.csv',
                     parse_dates=[3], infer_datetime_format=True)
    ds['datetime'] = ds['datetime'].sort_index()
    return ds
