# linkedInScraper
LinkedIn Scraper in Python

LICENSE: 
This code now is open-source. Feel free to use it. :)

DIRECTORY STRUCTURE:
  - scripts: contains the scripts
  - data_source: contains two files
    - links.txt: the list of links to scrape
    - company.txt: list of companies to look for, in experience section
  - output: contains the final output files 
  - other hidden files and folders

SYSTEM REQUIREMENTS:
  - Python 2 / 3
  - Libraries: selenium, time, os, sys

HOW TO USE:
  - SCRAPING
    - Navigate to scripts folder : 'cd scripts/'.
    - Execute 'python scraper.py'.
    - The program asks if you 'd like to delete files of the previous session thrice. Choose accordingly.
    - A browser window pops up. Enter LinkedIn login credentials within 30 seconds.
    - The browser will open the links one by one. 
    - If there are any exceptions, the program will ask if you'd like to reopen the exceptions. To continue with checking exceptions press 'y'; otherwise, press any key.
    - The program creates a file 'output/scraping_exceptions.txt' which contains the list of profile link numbers that couldn't be opened.
  - PROCESS
      - Navigate to scripts folder : 'cd scripts/'.
    - Execute 'python scraper.py'.
    - Files should now be ready to export.
  - EXPORT
      - Navigate to scripts folder : 'cd scripts/'.
    - Execute 'python scraper.py'.
    - Information will be stored in 'output/export.csv'

FOR CHANGING PARAMETERS BASED ON CONNECTIVITY: 
  - Open file 'scraper.py' present in the scripts directory. 
  - Modify the code between lines 10 to 22. Modifying further code would void the guarantee. 
  - Set LOGIN_TIME. If LOGIN_TIME > 5, the browser will wait for those many seconds before continuing, otherwise, the program will wait 'til you press any key. 
  - Set WAIT_GENERAL. The browser will wait for these many seconds before moving on to the next link in general. 
  - Set WAIT_EXCEPTION. The browser will wait for these many seconds before moving on to the next link in case of the exception. 
