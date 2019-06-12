import pandas as pd


def split_cat_features(df, cat_vars, max_cardinality=10):
    """
    Split categorical features by cardinality
    """

    if not isinstance(df, pd.DataFrame):
        raise ValueError('df needs to be a DataFrame')

    if not isinstance(cat_vars, list):
        raise ValueError('cat_vars needs to be a list')

    cardinality = df[cat_vars].apply(lambda x: x.nunique())

    low_card = list(cardinality.loc[cardinality < max_cardinality].index)
    high_card = list(cardinality.loc[cardinality >= max_cardinality].index)

    return low_card, high_card
