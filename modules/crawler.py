import os
import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlparse, urljoin
from modules.utils import clear_cli, signal_handler, ptxt, prdr, filter_path, is_domain_tracked
from modules.config import YELLOW as color1
from modules.config import BLUE as color2
from modules.config import RED as color3
from modules.config import RESET
from modules.config import REQUEST_HEADER
from modules.config import SAVE_RESULTS_TO
from modules.config import SAVE_CRAWLING_TO

#ptxt = template print text
#prdr = template print text for redirect
def crawler(crawling_urls):
    # try block
    try:
        PATH_CRAWLING_RESULT = f"{SAVE_RESULTS_TO}/{SAVE_CRAWLING_TO}"
        response = requests.get(crawling_urls, allow_redirects=True, timeout=10, headers=REQUEST_HEADER)
        final_url = response.url
        original_domain = urlparse(crawling_urls).netloc
        current_domain = urlparse(final_url).netloc
        
        # track redirect
        if response.history:
            prdr(color1, crawling_urls, final_url)
            
        print() # new line
        
        # extract url
        soup = BeautifulSoup(response.content,'html.parser')
        found_urls = set()
        for link in soup.find_all('a'):
            href = link.get('href')
            # filter
            if href is not None:
                absolute_path = filter_path(href)
                parsed = urlparse(absolute_path)
                
                if not parsed.scheme:
                    absolute_path = 'https://' + current_domain + absolute_path
                
                if absolute_path not in found_urls:
                    found_urls.add(absolute_path)
                    ptxt(color2, "URL", absolute_path)
                    
                    result = []
                
                    # Load existing file
                    if os.path.exists(PATH_CRAWLING_RESULT):
                        with open(PATH_CRAWLING_RESULT, 'r') as f:
                            try:
                                result = json.load(f)
                            except json.JSONDecodeError:
                                result = []
                
                    # Convert to dict
                    domain_map = {entry["domain"]: entry["data"] for entry in result}
                
                    if current_domain not in domain_map:
                            domain_map[current_domain] = []
                
                    if absolute_path not in domain_map[current_domain]:
                            domain_map[current_domain].append(absolute_path)
                
                    # convert back to list of dict
                    updated_result = [{"domain": d, "data": sorted(domain_map[d])} for d in sorted(domain_map)]
                
                    # save to file
                    with open(PATH_CRAWLING_RESULT, 'w', encoding='utf-8') as f:
                        json.dump(updated_result, f, ensure_ascii=False, indent=4)

    # error block
    except Exception as err:
        print() # new line    
        ptxt(color3,"ERROR",f"{color3}{err}{RESET}")