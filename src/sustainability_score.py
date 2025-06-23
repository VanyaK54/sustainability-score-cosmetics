import pandas as pd
from .data_prep import clean_ingredients, compute_ingredient_score, map_packaging_score

def score_product_row(row, ref_df):
    ingredients = clean_ingredients(row['ingredients_list'])
    ing_score = compute_ingredient_score(ingredients, ref_df)
    pkg_score = map_packaging_score(row['packaging_material'])
    sustainability_score = round((ing_score + pkg_score) / 2, 2)

    return pd.Series([ing_score, pkg_score, sustainability_score], index=['ingredient_score', 'packaging_score', 'sustainability_score'])

def score_dataset(raw_df_path, ref_df_path):
    df = pd.read_csv(raw_df_path)
    ref = pd.read_csv(ref_df_path)

    scores = df.apply(lambda row: score_product_row(row, ref), axis=1)
    final_df = pd.concat([df, scores], axis=1)
    return final_df
