from Team import Team
from selenium import webdriver
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://kenpom.com/')
driver.maximize_window()

client = MongoClient('mongodb+srv://navirzi:E2e6AQqE4rAVGDqk@march-madness-data.1efkla5.mongodb.net/?retryWrites=true&w=majority&appName=March-Madness-Data', server_api=ServerApi('1'))
teamDataTable = client['teamData']
teams = []

driver.implicitly_wait(2)
table = driver.find_elements(By.CSS_SELECTOR, '#ratings-table > tbody > tr > td')

for tr in driver.find_elements(By.CSS_SELECTOR, '#ratings-table > tbody > tr'):
    tableData = tr.find_elements(By.TAG_NAME, 'td')
    team = Team(tableData[1].find_element(By.TAG_NAME, 'a').text)

    try: team.seed = tableData[1].find_element(By.TAG_NAME, 'span').text
    except: team.seed = None

    if team.teamName[len(team.teamName) - 1] == ".": team.teamName = team.teamName[:-1]

    team.kpRank = tableData[0].text
    team.conf = tableData[2].text
    team.record = tableData[3].text
    team.eff = tableData[4].text
    team.offEff = tableData[5].text
    team.offEffRk = tableData[6].text
    team.defEff = tableData[7].text
    team.defEffRk = tableData[8].text
    team.tempo = tableData[9].text
    team.tempoRk = tableData[10].text
    team.luck = tableData[11].text
    team.luckRk = tableData[12].text
    team.oppEff = tableData[13].text
    team.oppEffRk = tableData[14].text
    team.oppOffEff = tableData[15].text
    team.oppOffEffRk = tableData[16].text
    team.oppDefEff = tableData[17].text
    team.oppDefEffRk = tableData[18].text
    team.nonConOppEff = tableData[19].text
    team.nonConOppEffRk = tableData[20].text

    teamData = teamDataTable[team.teamName]
    if teamData.find_one({'teamName':team.teamName}): teamData.find_one_and_replace({'teamName':team.teamName}, team.__dict__)
    else: teamData.insert_one(team.__dict__)
    teams.append(team)
    del team