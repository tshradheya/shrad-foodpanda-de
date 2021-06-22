from google.cloud import bigquery


def get_dataset():
    bqclient = bigquery.Client.from_service_account_json('./config/shrad-foodpanda-test-9a162656d6ba.json')

    # Download query results.
    query_string = """
        SELECT * FROM `bigquery-public-data.geo_international_ports.world_port_index`
        """
    df = (
        bqclient.query(query_string)
            .result()
            .to_dataframe()
    )

    return df
