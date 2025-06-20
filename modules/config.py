# ANSI color codes
RED = "\033[1;91m"
GREEN = "\033[1;92m"
YELLOW = "\033[1;93m"
BLUE = "\033[1;94m"
MAGENTA = "\033[1;95m"
RESET = "\033[0m"

# file naming     
TARGET_LIST_FILE = "domains.txt"
SAVE_RESULTS_TO = "data"
SAVE_CRAWLING_TO = "crawling_result.json"
SAVE_POISONING_TO = "poisoning_result.json"

# for crawling requests 
REQUEST_HEADER = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/123.0.0.0 Safari/537.36"}

# test unkeyed header
PAYLOADS = [
    {"key": "X-Forwarded-Host", "value": "evil.com"},
    {"key": "X-Host", "value": "evil.com"},
    {"key": "X-Forwarded-Scheme", "value": "http"},
    {"key": "X-Forwarded-Proto", "value": "http"},
    {"key": "X-Original-URL", "value": "/malicious"},
    {"key": "X-Rewrite-URL", "value": "/malicious"},
    {"key": "X-Forwarded-Port", "value": "8080"},
    {"key": "X-Forwarded-Server", "value": "evil.com"},
    {"key": "X-Real-IP", "value": "127.0.0.1"},
    {"key": "Forwarded", "value": "host=evil.com;proto=http"},
    {"key": "Host", "value": "evil.com"},
    {"key": "X-Custom-IP-Authorization", "value": "127.0.0.1"},
    {"key": "X-Original-Host", "value": "evil.com"},
    {"key": "X-Client-IP", "value": "127.0.0.1"},
    {"key": "X-Remote-IP", "value": "127.0.0.1"},
    {"key": "X-Originating-IP", "value": "127.0.0.1"},
    {"key": "X-Remote-Addr", "value": "127.0.0.1"},
    {"key": "X-Forwarded-For", "value": "127.0.0.1"},
    {"key": "Via", "value": "evil.com"},
    {"key": "True-Client-IP", "value": "127.0.0.1"},
    {"key": "X-HTTP-Host-Override", "value": "evil.com"}
]

# data crawling structure
JSON_CRAWLING_STRUCTURE = [
    {
        "domain":"",
        "data":[]
    }
]

#STATUS: NONE | POTENTIAL | VULNERABLE
#CONTENT: ZLIB COMPRESS
JSON_POISONING_STRUCTURE = {
  "data": [
    {
      "domain_name": "",
      "endpoints": [
        {
          "url": "",
          "payload_tests": [
            {
              "status": "",
              "payload": "",
              "result": {
                "original_response": {
                  "header": ""
                },
                "modified_response": {
                  "header": "",
                  "content": ""
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
