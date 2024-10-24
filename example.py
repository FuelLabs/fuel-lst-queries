import json

import fetch


if __name__ == '__main__':

    # Get all wallet mappings
    print(f"Fetching wallet mapping data...")
    data = fetch.get('wallet-mapping')
    print(json.dumps(data, indent=2))

    # Get all asset balances
    print(f"Fetching asset balance data...")
    data = fetch.get('asset-balance')
    print(json.dumps(data, indent=2))

    # Get all data
    print(f"Fetching all data...")
    data = fetch.get()
    print(json.dumps(data, indent=2))
