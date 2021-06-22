from google.cloud import bigquery
from google.oauth2 import service_account
import pandas_gbq

project_id = 'shrad-foodpanda-test'
bq_dataset = 'shrad-foodpanda-test.tasks'

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

def write_to_bq(output, table_name, ):
    credentials = service_account.Credentials.from_service_account_file('./config/shrad-foodpanda-test-9a162656d6ba.json')
    pandas_gbq.to_gbq(output, bq_dataset + '.' + table_name, if_exists='replace', project_id=project_id, credentials=credentials)

