import pandas as pd

# nflDF = pd.read_csv('data/nflplaybyplay2009to2016/nfl2009_2017.csv')
# columns --> ['Date', 'GameID', 'Drive', 'qtr', 'down', 'time', 'TimeUnder',
       'TimeSecs', 'PlayTimeDiff', 'SideofField', 'yrdln', 'yrdline100',
       'ydstogo', 'ydsnet', 'GoalToGo', 'FirstDown', 'posteam',
       'DefensiveTeam', 'desc', 'PlayAttempted', 'Yards.Gained', 'sp',
       'Touchdown', 'ExPointResult', 'TwoPointConv', 'DefTwoPoint',
       'Safety', 'Onsidekick', 'PuntResult', 'PlayType', 'Passer',
       'Passer_ID', 'PassAttempt', 'PassOutcome', 'PassLength',
       'AirYards', 'YardsAfterCatch', 'QBHit', 'PassLocation',
       'InterceptionThrown', 'Interceptor', 'Rusher', 'Rusher_ID',
       'RushAttempt', 'RunLocation', 'RunGap', 'Receiver', 'Receiver_ID',
       'Reception', 'ReturnResult', 'Returner', 'BlockingPlayer',
       'Tackler1', 'Tackler2', 'FieldGoalResult', 'FieldGoalDistance',
       'Fumble', 'RecFumbTeam', 'RecFumbPlayer', 'Sack',
       'Challenge.Replay', 'ChalReplayResult', 'Accepted.Penalty',
       'PenalizedTeam', 'PenaltyType', 'PenalizedPlayer', 'Penalty.Yards',
       'PosTeamScore', 'DefTeamScore', 'ScoreDiff', 'AbsScoreDiff',
       'HomeTeam', 'AwayTeam', 'Timeout_Indicator', 'Timeout_Team',
       'posteam_timeouts_pre', 'HomeTimeouts_Remaining_Pre',
       'AwayTimeouts_Remaining_Pre', 'HomeTimeouts_Remaining_Post',
       'AwayTimeouts_Remaining_Post', 'No_Score_Prob',
       'Opp_Field_Goal_Prob', 'Opp_Safety_Prob', 'Opp_Touchdown_Prob',
       'Field_Goal_Prob', 'Safety_Prob', 'Touchdown_Prob', 'ExPoint_Prob',
       'TwoPoint_Prob', 'ExpPts', 'EPA', 'airEPA', 'yacEPA',
       'Home_WP_pre', 'Away_WP_pre', 'Home_WP_post', 'Away_WP_post',
       'Win_Prob', 'WPA', 'airWPA', 'yacWPA', 'Season']

def convertDateToDatetime(nflDF):
	nflDF.Date = pd.to_datetime(nflDF.Date)

def createModelingDF():
    nflDF = nflDF[nflDF.PlayType.isin(['Pass', 'Run'])]
    playType = nflDF[['PlayType']]
    playType.replace('Pass', 1, inplace=True)
    playType.replace('Run', 0, inplace=True)
    playType.reset_index(inplace=True, drop=True)

    homeTeamDummy = pd.get_dummies(nflDF.HomeTeam)
    awayTeamDummy = pd.get_dummies(nflDF.AwayTeam)
    qtrDummy = pd.get_dummies(nflDF.qtr)

    modelDF0 = pd.concat([playType, homeTeamDummy, awayTeamDummy, qtrDummy, nflDF[['TimeSecs', 'yrdln', 'ydsnet']]], axis=1)
    modelDF0 = modelDF0.dropna()

if __name__ == '__main__':
    model0Features = ['HomeTeam', 'AwayTeam', 'qtr', 'TimeSecs', 'yrdln', 'ydsnet']

    nflDF = pd.read_csv('data/nflplaybyplay2009to2017/nfl2009_2017.csv')


