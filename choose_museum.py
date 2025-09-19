import geopandas as gpd
import os 

PATH = "./data/liste_des_musees_franciliens.geojson"

def read_data(): 

    if not os.path.exists(PATH):
        raise FileNotFoundError(f"Fichier {PATH} introuvable")

    usecols = ["nom_officiel_du_musee", "url", "latitude", "longitude"] 

    return gpd.read_file(PATH)[usecols]

def choose_random_museum(gdf):
    """Choisit un musée au hasard"""
    n_museum = len(gdf)
    return gdf.sample(1)

def main(): 
    return read_data().pipe(choose_random_museum)

if __name__ == "__main__":
    main()