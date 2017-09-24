# linkedInScraper
LinkedIn Scraper in Python

DIRECTORY STRUCTURE:
  - scripts: contains the scripts
  - data_source: contains two files
    - links.txt: list of links to scrape
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
	- The program asks if you'dlike to delete files of previous session thrice. Choose accordingly.
	- A browser window pops up. Enter LinkedIn login credentials within 30 seconds.
	- The browser will open the links one by one. 
	- If there are any exceptions, the program will ask if you'd like to reopen the exceptions. To continue with checking exceptions press 'y'; otherwise, press any key.
	- The program creates a file 'output/scraping_exceptions.txt' which contains list of profile link numbers that couldn't be opened.
  - PROCESS
  	- Navigate to scripts folder : 'cd scripts/'.
	- Execute 'python scraper.py'.
	- Files should now be ready to export.
  - EXPORT
  	- Navigate to scripts folder : 'cd scripts/'.
	- Execute 'python scraper.py'.
	- Information will be stored in 'output/export.csv'
