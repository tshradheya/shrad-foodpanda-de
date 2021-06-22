import util
from haversine import haversine

"""
Function which gets closest port based on location and having required resources 
"""
def task3(resources, lat_disaster, long_disaster):

    df = util.get_dataset_from_bq()
    # To filter ports containing all
    for resource in resources:
        df = df[df[resource] == True]

    df = df[['country', 'port_name', 'port_latitude', 'port_longitude']]
    suitable_ports = df

    distances_arr = []
    for row in suitable_ports.itertuples(index=False):
        distances_arr.append(haversine((lat_disaster, long_disaster), (row.port_latitude, row.port_longitude)))

    suitable_ports['distance_from_distress'] = distances_arr

    # Get closest port
    closest_port = suitable_ports.sort_values(by='distance_from_distress').head(1)
    closest_port = closest_port[['country', 'port_name', 'port_latitude', 'port_longitude']]

    print(closest_port)

    print("Starting writing to table...")
    util.write_to_bq(closest_port, 'closest_port_to_distress')
    print("Finished writing to table")


if __name__ == "__main__":
    # execute only if run as a script
    disaster_lat, disaster_long = 32.610982, -38.706256
    required_resources = ['provisions', 'water', 'fuel_oil', 'diesel']
    task3(required_resources, disaster_lat, disaster_long)
