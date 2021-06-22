import util

"""
Function which gets ports having cargo_wharf and saves into table the number of such ports for each country
"""
def task2():

    df = util.get_dataset_from_bq()

    ports_by_ctry = df.where(df["cargo_wharf"]).groupby('country')['index_number']\
        .count().reset_index(name='port_count')

    highest_num_of_ports = ports_by_ctry['port_count'].max()
    ctry_with_highest_ports = ports_by_ctry[ports_by_ctry['port_count'] == highest_num_of_ports]
    print(ctry_with_highest_ports)

    print("Starting writing to table...")
    util.write_to_bq(ctry_with_highest_ports, 'cargo_wharf_port_by_ctry')
    print("Finished writing to table")


if __name__ == "__main__":
    # execute only if run as a script
    task2()
