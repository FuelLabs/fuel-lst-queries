import time
import json
import requests

import constants


api_key = constants.API_KEY

all_query_types = list(constants.QUERY_INFO.keys())


def get(query_types=all_query_types, show_logs=constants.SHOW_LOGS):
    data = {}

    start_time = time.time()
    for query_type, query_info in constants.QUERY_INFO.items():

        if query_type not in query_types:
            continue

        query_path = query_info['query_path']
        sentio_project = query_info['sentio_project']
        

        with open(query_path) as f:
            query = json.load(f)

        cursor = None

        data[query_type] = {
            "columnTypes": {},
            "rows": []
        }
        while cursor is None or cursor:

            if cursor:
                json_body = {'cursor': cursor}
            else:
                json_body = query

            response = requests.post(
                f'https://app.sentio.xyz/api/v1/analytics/{sentio_project}/sql/execute',
                json=json_body,
                headers={
                    'Api-Key': f'{api_key}',
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }
            )

            if response.status_code != 200:
                print(response.json())
                raise Exception("Error getting data from Sentio.")
            else:
                try:

                    resp_data = response.json()
                    if resp_data['result']['columnTypes']:
                        data[query_type]['columnTypes'].update(resp_data['result']['columnTypes'])

                    data[query_type]['rows'].extend(resp_data['result']['rows'])
                    cursor = resp_data['result'].get('cursor', '')

                    more_results = (cursor is not None and cursor != '')

                    if show_logs:
                        print(f'Fetched {len(data[query_type]["rows"])} rows for {query_type} | more results: {more_results}')

                except:
                    print(response.json())
                    raise Exception("Error getting or parsing data from Sentio.")

    end_time = time.time()

    if show_logs:
        print(f'Time taken: {end_time - start_time} seconds')

    return data
