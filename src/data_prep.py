import pandas as pd
import numpy as np

def load_data(path):
    return pd.read_csv(path)

def clean_ingredients(ingredients_str):
    return [x.strip() for x in ingredients_str.split(',')]

def compute_ingredient_score(ingredients, ref_df):
    scores = []
    for ing in ingredients:
        match = ref_df[ref_df['chemical_name'].str.lower() == ing.lower()]
        if not match.empty:
            scores.append(match.iloc[0]['eco_rating'])
        else:
            scores.append(5)  # neutral score
    return round(np.mean(scores), 2)

def map_packaging_score(packaging):
    packaging_map = {
        'Recyclable Plastic': 9,
        'Glass Jar': 8,
        'Plastic Tube': 5,
        'Recycled PET Bottle': 8,
        'Biodegradable Pouch': 9
    }
    return packaging_map.get(packaging, 6)
