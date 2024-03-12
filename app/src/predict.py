import sys
import os

from catboost import CatBoostRanker
import numpy as np
import pandas as pd


def get_predictions(data: pd.DataFrame) -> np.array:
    """
    :param data: dataFrame with 0..78 features
    :return:
    """
    model = CatBoostRanker()
    model.load_model(
        os.path.join(os.path.dirname(sys.argv[0]), "model", "vk_ranker.cbm")
    )

    predictions = model.predict(data)
    return predictions
