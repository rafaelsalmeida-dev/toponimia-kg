import sys, pandas as pd, geopandas as gpd

p = sys.argv[1]

if p.endswith((".geojson", ".shp", ".gpkg")):
    df = gpd.read_file(p)
else:
    df = pd.read_csv(p)
print(len(df), "registros")
print(df.dtypes)
print(df.isna().mean().round(2))
print(df.head(10).to_string())