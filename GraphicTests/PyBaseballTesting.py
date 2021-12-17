from pybaseball import plotting as pl, datasources, retrosheet, statcast_pitcher as sp, statcast_batter, statcast
import statsapi as sapi
from matplotlib import pyplot
import numpy
import scipy
from BackgroundFunctions import Get_MLB_ID, GetPyBaseballTeamID

# for pl.plot_stadium: two word teams use underscore; 'generic' acceptable
# pl.spraychart

import numpy as np
import matplotlib.pyplot as plt
from StatcastScrape import statcast_player



if __name__ == '__main__':
    errormessage = "Didn't work"
    # print(statcast('2021-11-02','2021-11-02'))

    # pl.plot_stadium(GetPyBaseballTeamID('WSN'),'Test Stadium')
    
    # pyplot.show()
    # sapi.get('highlow','team')
    # print(Get_MLB_ID('guerrero'))
    pl.plot_bb_profile(statcast_player(MLBID= 665489))
    pl.spraychart(statcast_player(MLBID = 665489),'Blue_Jays')
    pyplot.show()