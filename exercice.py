#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import sklearn


def lire_fichier(fichier: str) -> pd.DataFrame:
    return pd.read_csv(fichier, ";")


def separer_variables_x_y(fichier: str) -> (np.array, np.array):

    x = np.array(lire_fichier(fichier).drop(columns=["quality"]))
    y = np.array(lire_fichier(fichier)["quality"])

    return x, y


def generer_sous_ensemble_x_y(fichier: str):

    x = separer_variables_x_y(fichier)[0]
    y = separer_variables_x_y(fichier)[1]

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.3, random_state=34)

    return x_train, x_test, y_train, y_test



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(generer_sous_ensemble_x_y("data/winequality-white.csv"))
    
