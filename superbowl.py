from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    #takes in a user input year and validates it
    validYear = False
    print('NFL Superbowl winner by year!')
    while not validYear:
        year = input("What year would you like(1967-2025)")
        if (2025 - int(year)) > 58 or (2025 - int(year)) < 0:
            print("Not a valid year")
        else:
            validYear = True
            print('Scraping ',year,' Superbowl winner...')

    #creates the url from the given year
    url = 'https://www.pro-football-reference.com/super-bowl/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #finds the winner from the mvp table
    table = soup.find('table', {'id': 'super_bowls'})
    rows = table.find_all('tr')
    row = 2026 - int(year)
    team_cell = rows[row].find('td', {'data-stat': 'sb_winner'})
    team_name = team_cell.get_text(strip=True)
    
    #output
    print("The", year, "Superbowl winner was the", team_name)



