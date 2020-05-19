# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:12:42 2020

@author: roger
"""


from nba_api.stats.static.teams import find_teams_by_city
#from nba_api.stats.static.players import 

raptorsid = find_teams_by_city("Toronto")[0]['id']
print(raptorsid)

from nba_api.stats.endpoints import drafthistory

raptors_drafthistory = drafthistory.DraftHistory(team_id_nullable = raptorsid)

raptors_drafthistory_df = raptors_drafthistory.get_data_frames()

print(raptors_drafthistory_df)




    




