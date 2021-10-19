import numpy as np
from pandas import DataFrame
from pyproj import Proj
import simplekml
import csv
import sys

def main():

    myProj = Proj(Proj("epsg:31983").definition_string())

    path = sys.argv[1]
            
    with open(path, 'r') as f:
        reader = csv.reader(f, delimiter = ' ')
        data = list(reader)

    lista = data

    label, x, y = [], [], []

    for row in lista:
        label.append(row[0])
        x.append(row[1])
        y.append(row[2])

    df = DataFrame(np.c_[x, y], columns=['East', 'North'])

    lon, lat = myProj(df['East'].values, df['North'].values, inverse=True)
    
    E, N = myProj(lon, lat)

    df = DataFrame(np.c_[E, N, lon, lat], columns=['E', 'N', 'Lon', 'Lat'])

    df['Name'] = label
    kml = simplekml.Kml()

    fileindex = path.index('.txt')
                
    filename = path[:fileindex] + '.kml'

    for row in df.itertuples():
        kml.newpoint(name = row.Name,
        coords = [(row.Lon, row.Lat)])
        kml.save(filename)

if __name__ == '__main__':
    
    main()