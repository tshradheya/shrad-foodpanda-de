import google.auth
import pandas
import util


def task2():

    df = util.get_dataset()

    df1 = df.where(df["cargo_wharf"]).groupby('country')['index_number']\
        .count().reset_index(name='port_count')\
        .sort_values(by='port_count', ascending=False)
    print(df1)


if __name__ == "__main__":
    # execute only if run as a script
    task2()
