![cache_poisoning_detection](./assets/icon.png)

# Cache Poisoning Detection

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![License](https://img.shields.io/github/license/hafiznurrahman/Cache-Poisoning-Detection)
![Last Commit](https://img.shields.io/github/last-commit/hafiznurrahman/Cache-Poisoning-Detection)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Repo Size](https://img.shields.io/github/repo-size/hafiznurrahman/Cache-Poisoning-Detection)
![PRs](https://img.shields.io/github/issues-pr/hafiznurrahman/Cache-Poisoning-Detection)
![Stars](https://img.shields.io/github/stars/hafiznurrahman/Cache-Poisoning-Detection?style=social)

**Cache Poisoning Detection** is a semi-automated Python-based tool that focuses on detecting and exploiting cache poisoning vulnerabilities through HTTP header manipulation. This tool automates the process of crawling and sending specially designed headers to identify misconfigured caching behavior, particularly targeting header-based poisoning without keys.

## Development Status
> 🚧 This tool is under active development.
Please refer to `TODO.md` for upcoming features and progress tracking.

## Features

-   Crawl domains and subdirectories
-   Run payloads along with cache busters
-   Output stored in JSON structure
-   Display results in graphical user interface (GUI)

## Project structure

```bash
.
├── LICENSE
├── README.md
├── TODO.md
├── assets
│   └── icon.png
├── data
│   ├── crawling_result.json
│   └── poisoning_result.json
├── domains.txt
├── index.html
├── main.py
├── modules
│   ├── config.py
│   ├── crawler.py
│   ├── executor.py
│   └── utils.py
├── requirements.txt
└── src
    ├── script.js
    └── style.css
```

## Installation

Copy and paste it into your terminal

```bash
git clone https://github.com/hafiznurrahman/Cache-Poisoning-Detection.git
cd Cache-Poisoning-Detection
pip install -r requirements.txt
```

## How To Use

1. Enter the domain list into `domains.txt`
2. Run the `main.py` script

    ```bash
    python3 main.py
    ```
3. The results are stored in `data/`
4. Open the `index.html` file in your browser to see the results.

## Licence

This project is licensed under the [MIT License](./LICENSE).
