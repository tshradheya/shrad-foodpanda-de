# FoodPanda Data Engineering - Shradheya 

This repository is for the solution to take home exam for Foodpanada Data Engineering Position

## Setup

### Environment and Versions

- Python: 3.7 [Install](https://docs.brew.sh/Homebrew-and-Python)
- Google Project ID: `shrad-foodpanda-test`
- Google Project Number: `412359830924`
- Google Service Account: ` query-user@shrad-foodpanda-test.iam.gserviceaccount.com`. Key present in `config/`


### Setup process

- Create Google Cloud account
- Create [Google Service Account](https://cloud.google.com/docs/authentication/production
) for project use and save the keyfile under `config/`
- Add `bigquery-public-data.geo_international_ports` dataset

### Installation Process

- Run `pip install --upgrade pandas 'google-cloud-bigquery[pandas]' haversine`

## Logic and Approach

In order to complete all tasks a decent knowledge of the `geo_international_ports` data is required.
So first step was to inspect the tables and their schema and see sample data for understanding what fields can be used.

Since Python was required for writing script instead of traditional SQL queries, I used pandas data frame to perform all operations

### Task1:

- Get `SG Jurong Island Port` lat and long
- Perform another operation to add a column which contains the [haversine](https://en.wikipedia.org/wiki/Haversine_formula) distance from this port. This algorithm was used as it accounted for earth's sphere shape and gave most accurate results 
- Get top 5 where distance > 0(ignore the port itself)


### Task2:

- This is equivalent of performing a group by `country` and a count(*) aggregate
- Hence I used pandas to mimic the same


### Task3

- This is similar to Task1 and same logic was used
- However, since this was more generic,
 I abstracted the logic for it to be more modifiable and used for other use cases
- Based on analysing schema I found the Geometry data type of big query available and I also explored that but the above seemed a better programmatic solution


## Running Code

- `python task1.py` (Change according to task number)

The Results can be viewed [here](https://console.cloud.google.com/bigquery?project=shrad-foodpanda-test)
