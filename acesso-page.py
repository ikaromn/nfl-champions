#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup


nflUrl = urllib.urlopen('http://www.nfl.com/standings?category=league&season=2016-REG&split=Overall').read()
soup = BeautifulSoup(nflUrl, "lxml")
standings = soup.find("div", "span-11")
newStandings = standings.find_all('tr', 'tbdy1')

teams2016 = {}
for i in range(len(newStandings)):

    nflTeamName = newStandings[i].find('a',).text
    lastStandings = newStandings[i].find('td','sorted').text
    strNflTeamName = str(nflTeamName)
    strLastStandings = str(lastStandings)
    stripedNflTeamName = strNflTeamName.strip()
    stripedLastStandings = strLastStandings.strip()
    teams2016[stripedNflTeamName] = stripedLastStandings



nflUrl = urllib.urlopen('http://www.nfl.com/standings?category=league&season=2015-REG&split=Overall').read()
soup = BeautifulSoup(nflUrl, "lxml")
standings = soup.find("div", "span-11")
newStandings = standings.find_all('tr', 'tbdy1')

teams2015 = {}
for i in range(len(newStandings)):

    nflTeamName = newStandings[i].find('a',).text
    lastStandings = newStandings[i].find('td','sorted').text
    strNflTeamName = str(nflTeamName)
    strLastStandings = str(lastStandings)
    stripedNflTeamName = strNflTeamName.strip()
    stripedLastStandings = strLastStandings.strip()
    teams2015[stripedNflTeamName] = stripedLastStandings



nflUrl = urllib.urlopen('http://www.nfl.com/standings?category=league&season=2014-REG&split=Overall').read()
soup = BeautifulSoup(nflUrl, "lxml")
standings = soup.find("div", "span-11")
newStandings = standings.find_all('tr', 'tbdy1')

teams2014 = {}
allTeams = []

for i in range(len(newStandings)):

    nflTeamName = newStandings[i].find('a',).text
    lastStandings = newStandings[i].find('td','sorted').text
    strNflTeamName = str(nflTeamName)
    strLastStandings = str(lastStandings)
    stripedNflTeamName = strNflTeamName.strip()
    stripedLastStandings = strLastStandings.strip()
    allTeams.append(stripedNflTeamName)
    teams2014[stripedNflTeamName] = stripedLastStandings



dict_teams = {}
for i in range(len(allTeams)):
    #print(allTeams[i] + " teve as campanhas:")
    
    dict_teams.update({allTeams[i]: [teams2014[allTeams[i]], teams2015[allTeams[i]]]})
    
    if allTeams[i] == 'St. Louis Rams':
        allTeams[i] = 'Los Angeles Rams'
        dict_teams['St. Louis Rams'].append(teams2016[allTeams[i]])
        #print(dict_teams['St. Louis Rams'])
    else:
        dict_teams[allTeams[i]].append(teams2016[allTeams[i]])
        #print(dict_teams[allTeams[i]])
    #print('\n')

print(dict_teams['Dallas Cowboys'][2])

x = 0
y = 0
z = 0
teams_total_values = {}
for i in range(len(allTeams)):
    if allTeams[i] == 'Los Angeles Rams':
        allTeams[i] = 'St. Louis Rams'
        x = dict_teams[allTeams[i]][0]
        y = dict_teams[allTeams[i]][1]
        z = dict_teams[allTeams[i]][2]
        j = x + y + z
        teams_total_values.update({allTeams[i]: j})
        print('é')
    else:
        x = float(dict_teams[allTeams[i]][0])
        y = float(dict_teams[allTeams[i]][1])
        z = float(dict_teams[allTeams[i]][2])
        j = x + y + z
        teams_total_values.update({allTeams[i]: j})

print(teams_total_values)