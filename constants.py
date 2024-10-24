import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

QUERY_DIR = os.path.join(CURRENT_DIR, 'queries')

API_KEY = 'YOUR_API_KEY'

QUERY_INFO = {
    'wallet-mapping': {
        'query_path': os.path.join(QUERY_DIR, 'wallet-mapping-query.json'),
        'sentio_project': 'fuellabs/accounts_mapping'
    },
    'asset-balance': {
        'query_path': os.path.join(QUERY_DIR, 'asset-balance-query.json'),
        'sentio_project': 'fuellabs/accounts_allocations'
    }
}

SHOW_LOGS = True
