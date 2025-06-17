import os
import json
import requests
from modules.config import SAVE_RESULTS_TO, SAVE_POISONING_TO, JSON_POISONING_STRUCTURE


def executor():
    """Execute requests to the saved links and update the poisoning result JSON."""
    poisoning_result_file = os.path.join(SAVE_RESULTS_TO, SAVE_POISONING_TO)

    # Load existing poisoning results or initialize with the provided structure
    if os.path.exists(poisoning_result_file):
        with open(poisoning_result_file, 'r', encoding='utf-8') as f:
            poisoning_data = json.load(f)
    else:
        poisoning_data = JSON_POISONING_STRUCTURE

    # Iterate through the domains in the poisoning data
    for domain_entry in poisoning_data['data']:
        domain = domain_entry['domain']
        for track in domain_entry['track']:
            t_url = track['t_url']
            t_header = track['t_header']

            # Make the first request
            first_response = make_request(t_url)

            # Prepare the header for the second request
            second_response, content = make_request(t_url, headers=t_header)

            # Update the track information
            track['t_status'] = first_response.status_code
            track['t_header'].append({
                't_payload': t_header,
                'result': [
                    {'first_response': first_response.status_code},
                    {'second_response': second_response.status_code, 'content': content}
                ]
            })

    # Save the updated poisoning results back to the file
    with open(poisoning_result_file, 'w', encoding='utf-8') as f:
        json.dump(poisoning_data, f, indent=4)


def make_request(url: str, headers: dict = None):
    """Make a GET request to the specified URL with optional headers."""
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return response, response.text
    except requests.RequestException as e:
        print(f"Error making request to {url}: {e}")
        return None, ""
