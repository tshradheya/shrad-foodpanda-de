import google.auth
import pandas
import util
from haversine import haversine

def task3():

    lat_port, long_port = 32.610982, -38.706256

    df = util.get_dataset()
    df1 = df.loc[(df["provisions"]) & (df['water']) & df['fuel_oil'] & df['diesel']][['country', 'port_name', 'port_latitude', 'port_longitude']]

    distances_arr = []

    for row in df1.itertuples(index=False):
        distances_arr.append(haversine((lat_port, long_port), (row.port_latitude, row.port_longitude)))

    df1['distance_from_distress'] = distances_arr

    final = df1.sort_values(by='distance_from_distress').head(1)
    final = final[['country', 'port_name', 'port_latitude', 'port_longitude']]

    print(final)


if __name__ == "__main__":
    # execute only if run as a script
    task3()
