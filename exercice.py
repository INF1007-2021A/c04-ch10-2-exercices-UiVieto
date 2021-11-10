#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd
import sklearn


def lire_fichier(fichier: str) -> pd.DataFrame:
    return pd.read_csv(fichier)


def separer_variables_x_y(fichier: str) -> (pd.DataFrame, pd.DataFrame):

    x = lire_fichier(fichier).drop(columns=["quality"])
    y = lire_fichier(fichier)["quality"]
    
    return x, y


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    pass
