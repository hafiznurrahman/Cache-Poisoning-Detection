import os
import json
from modules.utils import clear_cli, signal_handler, ptxt
from modules.crawler import crawler
from modules.executor import executor
from modules.config import YELLOW as color
from modules.config import RESET
from modules.config import SAVE_RESULTS_TO
from modules.config import SAVE_CRAWLING_TO
from modules.config import SAVE_POISONING_TO
from modules.config import TARGET_LIST_FILE
from modules.config import JSON_CRAWLING_STRUCTURE
from modules.config import JSON_POISONING_STRUCTURE

def main():
    # clear interface
    clear_cli()
    
    # Create a folder to store output files
    if not os.path.exists(SAVE_RESULTS_TO):
        os.makedirs(SAVE_RESULTS_TO)
        ptxt(color,"+",f"THE {color+SAVE_RESULTS_TO+RESET} FOLDER WAS CREATED\n")
    
    # Create a file crawling_result.json
    CRAWLING_RESULT_JSON_FILE = f"{SAVE_RESULTS_TO}/{SAVE_CRAWLING_TO}"
    if not os.path.exists(CRAWLING_RESULT_JSON_FILE):
        with open(CRAWLING_RESULT_JSON_FILE,'w') as file:
            ptxt(color,"+",f"{color+CRAWLING_RESULT_JSON_FILE+RESET} ADDED")
            
            # add json structure
            json.dump(JSON_CRAWLING_STRUCTURE,file,indent=4)
            ptxt(color,"W",f"JSON STRUCTURE ADDED TO {color+CRAWLING_RESULT_JSON_FILE+RESET}\n")
    else:
        # check & add json structure
        with open(CRAWLING_RESULT_JSON_FILE,'r') as file:
            content = file.read().strip()
            if not content:
                with open(CRAWLING_RESULT_JSON_FILE,'w') as file:
                        json.dump(JSON_CRAWLING_STRUCTURE,file,indent=4)
                        ptxt(color,"W",f"JSON STRUCTURE ADDED TO {color+CRAWLING_RESULT_JSON_FILE+RESET}")
        
    # Create a file poisoning_result.json
    POISONING_RESULT_JSON_FILE = f"{SAVE_RESULTS_TO}/{SAVE_POISONING_TO}"
    if not os.path.exists(POISONING_RESULT_JSON_FILE):
        with open(POISONING_RESULT_JSON_FILE,'w') as file:
            ptxt(color,"+",f"{color+POISONING_RESULT_JSON_FILE+RESET} ADDED")
            
            # add json structure
            json.dump(JSON_POISONING_STRUCTURE,file,indent=4)
            ptxt(color,"W",f"JSON STRUCTURE ADDED TO {color+POISONING_RESULT_JSON_FILE+RESET}\n")
    else:
        # check & add json structure
        with open(POISONING_RESULT_JSON_FILE,'r') as file:
            content = file.read().strip()
            if not content:
                with open(POISONING_RESULT_JSON_FILE,'w') as file:
                    json.dump(JSON_POISONING_STRUCTURE,file,indent=4)
                    ptxt(color,"W",f"JSON STRUCTURE ADDED TO {color+POISONING_RESULT_JSON_FILE+RESET}")
    
    # Create a file for the target list
    if not os.path.exists(TARGET_LIST_FILE):
        with open(TARGET_LIST_FILE,'w') as file:
            ptxt(color,"+",f"THE {color+TARGET_LIST_FILE+RESET} FILE WAS CREATED")
            ptxt(color,"WARN!",f"ENTER DOMAINS ONE PER LINE INTO {color+TARGET_LIST_FILE+RESET}\n")
    else:
        # check target list
        with open(TARGET_LIST_FILE, 'r') as file:
            content = file.read().strip()
            if not content:
                ptxt(color,"WARN!",f"ENTER DOMAINS ONE PER LINE INTO {color+TARGET_LIST_FILE+RESET}\n")
            else:
                ptxt(color,"RUN",f"CRAWLING...")
                ptxt(color,"+",f"SAVED TO {color+CRAWLING_RESULT_JSON_FILE+RESET}")
                
                # read per line & crawling
                with open(TARGET_LIST_FILE, 'r') as file:
                    for domain in file:
                        domain_url = "https://"+domain.strip()
                        print() #new line
                        ptxt(color,"DOMAIN", domain.strip())
                        crawler(domain_url)
                        
                print() #new line
                
               # executor()
                
if __name__=="__main__":
    main()