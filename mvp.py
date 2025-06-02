from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
    #takes in a user input year and validates it
    validYear = False
    print('NFL AP MVP winner by year!')
    while not validYear:
        year = input("What year would you like(1961-2024)")
        if (2024 - int(year)) > 63 or (2024 - int(year)) < 0:
            print("Not a valid year")
        else:
            validYear = True
            print('Scraping ',year,' NFL AP MVP...')

    #creates the url from the given year
    url = 'https://www.pro-football-reference.com/awards/awards_'+year+'.htm'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #finds the winner from the mvp table
    mvp_table = soup.find('table', {'id': 'voting_apmvp'})
    winner_row = mvp_table.find('tbody').find('tr')
    player_cell = winner_row.find('td', {'data-stat': 'player'})
    player_name = player_cell.get_text(strip=True)
    
    #output
    print("The", year, "AP MVP was", player_name)


