import util

"""
Function which gets ports having cargo_wharf and saves into table the number of such ports for each country
"""
def task2():

    df = util.get_dataset_from_bq()

    ports_by_ctry = df.where(df["cargo_wharf"]).groupby('country')['index_number']\
        .count().reset_index(name='port_count')\
        .sort_values(by='port_count', ascending=False)
    print(ports_by_ctry)

    print("Starting writing to table...")
    util.write_to_bq(ports_by_ctry, 'cargo_wharf_port_by_ctry')
    print("Finished writing to table")


if __name__ == "__main__":
    # execute only if run as a script
    task2()
