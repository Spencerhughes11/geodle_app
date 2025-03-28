import osgeo.ogr
import shapely.wkt

def main():
    shapefile = osgeo.ogr.Open("TM_WORLD_BORDERS-0.3.shp")
    layer = shapefile.GetLayer(0)

    countries = {} # Maps country name to Shapely geometry.

    for i in range(layer.GetFeatureCount()):
        feature = layer.GetFeature(i)
        country = feature.GetField("NAME")
        outline = shapely.wkt.loads(feature.GetGeometryRef().ExportToWkt())

        countries[country] = outline

    print ("Loaded %d countries" % len(countries))

if __name__ == "__main__":
    main()