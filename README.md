# LST Queries POC

## Background

Fuel is working with OpenBlock (OBL) and Sentio to run its points program. OpenBlock has designed the methodology and Sentio is indexing the data on behalf of all participating protocols.

This project builds on top of Sentio's indexing solution and allows partners to query Sentio's APIs to get the data they need to understand the state of assets on the network, insofar as Fuel has visibiliy based on its own points program.

## Note on Usage

With the exception of new wallet relationships via bridging, data updates only occur once per hour. So you will not see real-time data. The data is updated at the top of the hour.

Please be polite with API call frequency. We are not currently rate limiting, but that or API key revocation may occur if there is abuse.

## Project Setup

### Obtaining an API Key

Only specific partners will be given access to the API. Please reach out to the Fuel team to get an API key.

### Set Up Python Environment

Follow one of many online tutorials to do this. You can use `virtualenv`, `conda`, or Docker to do this.

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

In constants.py, you have the following variables:
	
```python
# To access Sentio API
# As protocols expand, we may have to move API keys inside the
# QUERY_INFO dictionary to grant access to multiple projects.
API_KEY = "YOUR_API_KEY"

# If you generate any custom SQL for your own needs, you will have to
# store the sql in the queries directory and add references to the project
# and the query here.
QUERY_INFO = {...}
```

You are welcome to use any method you wish to keep private data private - secrets managers, local environment varibles, etc.

### Getting Data

You can run the following command to get data from Sentio's API:

```bash
python3 example.py
```

It will run through multiple types of queries and print the results to the console.

Example data is like this:

```python
{
  "asset-balance": {
    "columnTypes": {
      "block_date": "STRING",
      "chain_id": "STRING",
      "timestamp": "TIME",
      "token_address": "STRING",
      "token_amount": "NUMBER",
      "token_symbol": "STRING",
      "user_address": "STRING"
    },
    "rows": [
      {
        "block_date": "2024-10-19",
        "chain_id": "9889",
        "timestamp": "2024-10-19T12:00:00Z",
        "token_address": "0xf8f8b6283d7fa5b672b530cbb84fcccb4ff8dc40f8176ef4544ddb1f1952ad07",
        "token_amount": "0.0902355",
        "token_symbol": "ETH",
        "user_address": "0x00017a92ed054f04c6dc7594a58974993569156f02f8de16b9d10c472bcf0546"
      },
      {
        "block_date": "2024-10-19",
        "chain_id": "9889",
        "timestamp": "2024-10-19T21:00:00Z",
        "token_address": "0xf8f8b6283d7fa5b672b530cbb84fcccb4ff8dc40f8176ef4544ddb1f1952ad07",
        "token_amount": "0.005",
        "token_symbol": "ETH",
        "user_address": "0x000197cf361a202c3c17b8efd740d1df58967798a24a0b42b9725b2f8ca0e18d"
      },
	  ...
	]
  },
  "<query-type-2>": {
  	# Same format as above
  },
  ...
}

```

Raw hourly data for `asset-balance` queryies will become large, so we recommend running transformations and points calculations via code rather than SQL to enable easier batching and scalability. Sentio's API will time out for queries that are too large.

The python [pandas library resampling](https://pandas.pydata.org/docs/user_guide/timeseries.html#resampling) can be useful to convert the data to the periodicity of your choosing.

## Notes:

This repo is provided as is and with all faults. The user of the repo assumes the entire risk as to the quality and performance of the repo. Fuel is not responsible for any damages of any kind, including consequential damages, arising from the use of the repo.

## License

This repo is licensed under the `Apache-2.0` license. See [`LICENSE`](./LICENSE) for more information.
