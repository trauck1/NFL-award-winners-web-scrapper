# NFL-award-winners-web-scrapper

**NFL Awards by Year (IN PROGRESS)**

A command-line application that scrapes and displays NFL award winners and Super Bowl champions by year. The project consists of a C++ menu system that calls Python scripts to retrieve data from Pro Football Reference.
Features

AP MVP Winners (1961-2024): Get Associated Press Most Valuable Player award winners
AP DPOY Winners (1971-2024): Get Associated Press Defensive Player of the Year award winners
Super Bowl Winners (1967-2025): Get Super Bowl championship teams
Interactive menu system with input validation
Web scraping from Pro Football Reference

**Requirements**

C++ Compiler (g++, clang++, or similar)
Python 3.x
Python Libraries:

beautifulsoup4
requests


**Select from the menu options:**

1 - AP MVP winner lookup
2 - AP DPOY winner lookup
3 - Super Bowl winner lookup
4 - In progress (placeholder)
5 - Exit


**Enter a valid year when prompted:**

MVP: 1961-2024
DPOY: 1971-2024
Super Bowl: 1967-2025



**File Structure**


main.cpp        # C++ menu system and program entry point

mvp.py          # AP MVP winner scraper

dpoy.py         # AP DPOY winner scraper

superbowl.py    # Super Bowl winner scraper

**Example Output**

NFL award winners by year!
1. AP MVP
2. AP DPOY
3. SUPERBOWL WINNER
4. IN PROGRESS
5. Exit
1
NFL AP MVP winner by year!
What year would you like(1961-2024)2023
Scraping 2023 NFL AP MVP...
The 2023 AP MVP was Lamar Jackson

**Technical Details**

Data Source: Pro Football Reference (pro-football-reference.com)
Scraping Method: BeautifulSoup HTML parsing
Year Validation: Built-in range checking for each award type
Error Handling: Input validation and retry loops
