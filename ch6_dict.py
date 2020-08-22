# key-value pairs
# dict = {}
# dict = {'key':'value}

embiid_stats = {'team': 'sixers', 'points':28}

#assessing the vales in a dict
print(embiid_stats['team'])
print(embiid_stats['points'])

scoring = embiid_stats['points']
team = embiid_stats['team']
print(f"The average points scored for the season was {scoring} and was on the {team} roster.")

# adding new key-value pairs
embiid_stats['rebound'] = 12
embiid_stats['assists'] = 6

print(embiid_stats)

# sometimes it's more convenient to start with an empty dict
simmons_stats = {}

simmons_stats['team'] = 'sixers'
simmons_stats['points'] = 14
simmons_stats['rebounds'] = 7
simmons_stats['assists'] = 7

print(simmons_stats)

# modifying values
simmons_stats['points'] = 13.6

updated_points = simmons_stats['points']
print(f'We updated the stats for the season and the average points is now {updated_points}')

# practical example
embiid_stats2 = {'team': 'sixers', 'points': 28, 'rebounds':10, 'assists' : 6}
print(f"The regular season output is: {embiid_stats2['points']} points, 
                                       {embiid_stats2['rebounds']} rebounds, {embiid_stats2['assists']} assists.')
#adjust stats according to pre, regular, and post season
if # come back to this

# removing key-value pairs: del()
del embiid_stats2['assists]
print(embiid_stats2)

# a dict of similar objects
favorite_languages = {
        'trap': 'python',
        'mega': 'python',
        'little anthony' : 'c',
        'hoang': 'sql'}
language = favorite_languages['hoang'].title()
print(f"Hoang's favorite langauge is {language}")
favorite_language['mega]
