import scrapy
from bs4 import BeautifulSoup


class MlbDailyLineupSpider(scrapy.spiders.CrawlSpider):
    name = 'mlb-daily-lineup'
    start_urls = ['https://www.rotowire.com/baseball/daily-lineups.php/']

    def parsePitcher(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        self.log('Pitcher Page')
        return soup.prettify()
        # with open('player.html', 'w') as f:
        #     f.write(soup.prettify())

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        lineups = soup.find_all('div', class_='lineup')
        date = soup.find('div', class_='page-title__secondary').getText()[25:-33]
        # self.log(date)
        for lineup in lineups:
            try:
                time = lineup.find('div', class_='lineup__time').getText()
                # self.log(time)

                awayTeam = lineup.find('div', class_='lineup__mteam is-visit').getText().split('(')[0].strip()
                homeTeam = lineup.find('div', class_='lineup__mteam is-home').getText().split('(')[0].strip()
                # self.log(f'{away} vs {home}')


                awayPitcher = lineup.find('ul', class_='lineup__list is-visit').find('div', class_='lineup__player-highlight-name').find('a').getText()
                awayPitcherStats = response.follow(lineup.find('ul', class_='lineup__list is-visit').find('div', class_='lineup__player-highlight-name').find('a')['href'], callback=self.parsePitcher)
                self.log(awayPitcherStats)

                homePitcher = lineup.find('ul', class_='lineup__list is-home').find('div', class_='lineup__player-highlight-name').find('a').getText()
                # self.log(f'{awayPitcher} vs {homePitcher}')

                awayBattingLineup = lineup.find('ul', class_='lineup__list is-visit').find_all('li', class_='lineup__player')
                homeBattingLineup = lineup.find('ul', class_='lineup__list is-home').find_all('li', class_='lineup__player')
                
                awayLineUp = []
                for player in awayBattingLineup:
                    position = player.find('div').getText()
                    handedness = player.find('span').getText()
                    playerName = player.find('a')['title']
                    awayLineUp.append({
                        "player": playerName,
                        "position": position,
                        "handedness": handedness
                    })
                # self.log(awayLineUp)

                homeLineUp = []
                for player in homeBattingLineup:
                    position = player.find('div').getText()
                    handedness = player.find('span').getText()
                    playerName = player.find('a')['title']
                    homeLineUp.append({
                        "player": playerName,
                        "position": position,
                        "handedness": handedness
                    })
                # self.log(homeLineUp)

                away = {
                    "team": awayTeam,
                    "pitcher": awayPitcher,
                    'batters': awayLineUp
                }
                home = {
                    "team": homeTeam,
                    "pitcher": homePitcher,
                    "batters": homeLineUp
                }
                yield {
                    "date": date,
                    "time": time,
                    "away": away,
                    "home": home
                }
            except:
                continue
