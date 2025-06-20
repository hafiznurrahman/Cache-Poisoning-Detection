# TODO List - Cache Poisoning Detection

```markdown
Add `x` to `[ ]` to mark a task as completed.
Example: `[x] Task xxxxxxxxxxx`

Or add `<<<` after the task name to mark a task as in progress.
Example: `[ ] Task xxxxx <<<`
```

## 🚀 main.py

-   [x] Soon...

## 🕷️ crawler.py

-   [ ] Crawl every domain in the domains.txt file 
-   [ ] Allow redirects if they are still within the same domain
-   [ ] Do not crawl if the domain/subdomain has already been crawled
-   [ ] Only crawl within a single domain or relative paths (./, ../), absolute paths (/, //), or scheme://
-   [ ] Filter paths like \\+, /+ to /
-   [x] Decode paths containing Unicode or double encoding
-   [ ] Filter schemes that are not http/https and retrieve the entire path
-   [ ] Make the crawler recursive
-   [ ] Add the scheme + domain to each path to make it a complete path
-   [ ] Filter duplicate paths
-   [ ] Save all complete URLs for each domain to crawling_result.json

## 💥 executor.py

-   [x] Soon...

## 🌐 view/

-   [x] Creating a GUI
