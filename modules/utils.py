import unicodedata
import json
import signal
import sys
import re
import os
from urllib.parse import unquote, urlparse
from modules.config import RESET

# clear text
def clear_cli():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
# EXIT PROGRAM
def signal_handler(sig, frame):
        print()
        sys.exit(0)
signal.signal(signal.SIGINT,signal_handler)

# print text
def ptxt(color, info, text):
    print(f"{color}[{info}]{RESET} {text}")
    
# print redirect
def prdr(color, from_domain, to_domain):
    print(f"{color}[REDIRECT]{RESET} {from_domain} {color}->{RESET} {to_domain}")
    
# filter path
def filter_path(path: str) -> str:
    while True:
        decoded = unquote(path)
        if decoded == path:
            break
        path = decoded

    parsed = urlparse(path)
    if parsed.scheme and parsed.scheme not in ('http', 'https'):
        path = parsed.path
    
    if parsed.scheme in ('http', 'https'):
        get_scheme = parsed.scheme
        get_domain = parsed.netloc
        get_path = re.sub(r'[\\/]+', '/', parsed.path)
        get_query = parsed.query
        get_fragment = parsed.fragment
        
        path = get_scheme + '://' + get_domain + get_path + get_query + get_fragment
        
    else:    
        path = re.sub(r'[\\/]+', '/', path)

    if not path.startswith(('http','https','/')):
        path = '/' + path

    return path

# track domain
def is_domain_tracked(domain: str, result_path: str) -> bool:
    if not os.path.exists(result_path):
        return False
    try:
        with open(result_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return any(entry['domain'] == domain for entry in data)
    except json.JSONDecodeError:
        return False
