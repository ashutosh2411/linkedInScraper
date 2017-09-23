# linkedInScraper
LinkedIn Scraper in Python

Directory structure:
  - scripts: 		contains the scripts
  - data_source:	contains tho files
    - links.txt: 	list of links to scrape
    - company.txt: 	list of companies to look for, in experience section
  - output:			

Prerequisites:
  - Python 2 / 3
  - Libraries: Selenium, time, os, sys

How to use:
  - SCRAPING
	- Navigate to scripts folder : 'cd scripts/'.
	- Execute 'python scraper.py'.
	- The program asks if you'dlike to delete files of previous session thrice. Choose accordingly.
	- A browser window pops up. Enter LinkedIn login credentials within 30 seconds.
	- The browser will open the links one by one. 
	- If there are any exceptions, the program will ask if you'd like to reopen the exceptions. To continue with checking exceptions press 'y'; otherwise, press any key.
  - PROCESS
  	- Navigate to scripts folder : 'cd scripts/'.
	- Execute 'python scraper.py'.
	- Files should now be ready to export.
  - EXPORT
  	- Navigate to scripts folder : 'cd scripts/'.
	- Execute 'python scraper.py'.
	- Information will be stored in 'output/export.csv'
