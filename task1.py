import google.auth
import pandas
import util
from haversine import haversine

def task1():

    df = util.get_dataset()
    sg_jurong_port = df.loc[(df["country"] == 'SG') & (df['port_name'] == 'JURONG ISLAND')][['port_latitude', 'port_longitude']]
    if sg_jurong_port.shape[0] != 1:
        return
    lat_port, long_port = float(sg_jurong_port['port_latitude']), float(sg_jurong_port['port_longitude'])

    distances_arr = []

    for row in df.itertuples(index=False):
        distances_arr.append(haversine((lat_port, long_port), (row.port_latitude, row.port_longitude)))

    df['distance_from_jurong_port'] = distances_arr

    final = df.where(df['distance_from_jurong_port'] > 0.0).sort_values(by='distance_from_jurong_port').head(5)
    final = final[['port_name', 'distance_from_jurong_port']]

    print(final)


if __name__ == "__main__":
    # execute only if run as a script
    task1()
