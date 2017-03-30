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
    
    dict_teams.update({allTeams[i]: [teams2014[allTeams[i]], teams2015[allTeams[i]]]})
    
    if allTeams[i] == 'St. Louis Rams':
        allTeams[i] = 'Los Angeles Rams'
        dict_teams['St. Louis Rams'].append(teams2016[allTeams[i]])
    else:
        dict_teams[allTeams[i]].append(teams2016[allTeams[i]])

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
    else:
        x = float(dict_teams[allTeams[i]][0])
        y = float(dict_teams[allTeams[i]][1])
        z = float(dict_teams[allTeams[i]][2])
        j = x + y + z
        teams_total_values.update({allTeams[i]: j})

packers = teams_total_values['Green Bay Packers']
steelers = teams_total_values['Pittsburgh Steelers']
patriots = teams_total_values['New England Patriots']
falcons = teams_total_values['Atlanta Falcons']

falcons = falcons + 0.5
patriots = patriots + 0.5
pack_w = 0
fac_w = 0
stee_w = 0
pats_w = 0
if packers > falcons:
	print('Packers wins NFC Championship')
	pack_w = 1
else:
	print('Falcons wins NFC Championship')
	fac_w = 1

if steelers > patriots:
	print('Steelers wins NFC Championship')
	stee_w = 1
else:
	print('Patriots wins NFC Championship')
	pats_w = 1

if pack_w == 1 and pats_w == 1:
	print('Super Bowl sera entre Packers x Patriots')
	if packers > patriots:
		print('Packers e mais novo canpeao do SuperBowl')
	else:
		print('Patriots e o mais novo campeao do SuperBowl')
elif pack_w == 1 and stee_w == 1:
	print('Super Bowl sera entre Packers x Steelers')
	if packers > steelers:
		print('Packers e mais novo campeao do SuperBowl')
	else:
		print('Steelers e o mais novo campeao do SuperBowl')
elif fac_w == 1 and pats_w == 1:
	print('Super Bowl sera entre Falcons x Patriots')
	if falcons > patriots:
		print('Falcons e mais novo canpeao do SuperBowl')
	else:
		print('Patriots e o mais novo campeao do SuperBowl')
else:
	print('Super Bowl sera entre Falcons x Steelers')