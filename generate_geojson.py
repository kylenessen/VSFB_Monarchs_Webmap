import geopandas as gpd
from pyproj import CRS
deployments_path = "/Users/kylenessen/Documents/Code/masters/VSFB_Monarchs/deployments.gpkg"

df = gpd.read_file(deployments_path)

# Check if the CRS is WGS84
if df.crs != CRS.from_epsg(4326):
    # Project the dataframe to WGS84
    df = df.to_crs(epsg=4326)


df = df[df['youtube_url'].notnull() & (df['youtube_url'] != '')]


geojson_path = "data/deployment_pts.geojson"

# Save the DataFrame as GeoJSON
df.to_file(geojson_path, driver='GeoJSON')
