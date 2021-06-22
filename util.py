from google.cloud import bigquery

def get_dataset_from_bq():
    bqclient = bigquery.Client.from_service_account_json('./config/shrad-foodpanda-test-9a162656d6ba.json')

    df = bqclient.list_rows('bigquery-public-data.geo_international_ports.world_port_index').to_dataframe()

    return df

def write_to_bq(output, table_name):
    bqclient = bigquery.Client.from_service_account_json('./config/shrad-foodpanda-test-9a162656d6ba.json')
    dataset = bqclient.get_dataset('shrad-foodpanda-test.tasks')

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE"
    )

    job = bqclient.load_table_from_dataframe(
        output, dataset.table(table_name), job_config=job_config
    )

    job.result()

