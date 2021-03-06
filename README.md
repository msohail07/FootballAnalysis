# FootballAnalysis
## Summary
For NFL defenses, predicting the opponents’ offensive plays can mean the difference between a win and a loss. In this project, I use NFL play-by-play data from 2009-2016 to predict if the offensive team executes a run or a pass. 

## Modeling
I focus on two game-time settings. First, the coach’s booth, where coaches have time to interpret a more complex yet highest possible accuracy model. My most successful model here was a Random Forest Classifier with an accuracy of 61%.  Second, the players on the field when a quick, interpretable model is needed in rushed situations. Here I used a shallow decision tree classifier, which achieved 57% accuracy.

## Results
Although the Random Forest and Decision Tree models accuracy was not extremely high, both were able to achieve predictions better than random and thus provide some utility. These scores show a fundamental limit to the model’s performance given the discrete, play-summary dataset where each row only contains information regarding what the final outcome was of a given play. More fine-grained data including players positioning and movement is needed to improve the predictive performance of these models. A computer-vision, neural-network approach seems promising as a future model to explore.
