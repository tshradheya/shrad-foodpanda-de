import util
from haversine import haversine

"""
Function which gets the SG Jurong Island Port.
And then adds a column which contains distance to this port and saves top 5 closest ones
"""
def task1():

    df = util.get_dataset_from_bq()

    sg_jurong_port = df.loc[(df["country"] == 'SG') & (df['port_name'] == 'JURONG ISLAND')][['port_latitude', 'port_longitude']]
    if sg_jurong_port.shape[0] != 1:
        print("The mentioned port is not in data")
        return
    lat_port, long_port = float(sg_jurong_port['port_latitude']), float(sg_jurong_port['port_longitude'])

    # Calculate distance and add as column
    distances_arr = []
    for row in df.itertuples(index=False):
        distances_arr.append(haversine((lat_port, long_port), (row.port_latitude, row.port_longitude)))

    df['distance_in_meters'] = distances_arr

    # Get Top 5 excluding that port itself
    distance_from_jurong_island_port = df.where(df['distance_in_meters'] > 0.0).sort_values(by='distance_in_meters').head(5)
    distance_from_jurong_island_port = distance_from_jurong_island_port[['port_name', 'distance_in_meters']]

    print(distance_from_jurong_island_port)

    print("Starting writing to table...")
    util.write_to_bq(distance_from_jurong_island_port, 'closest_ports_to_jurong_island')
    print("Finished writing to table")


if __name__ == "__main__":
    # execute only if run as a script
    task1()
