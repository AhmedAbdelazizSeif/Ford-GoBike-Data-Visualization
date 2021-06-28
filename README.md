# Ford GoBike Visualization
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.
This dataset is supposed to be for bikeshare in Feb 2019 with 16 rows explaining each bikeshare event by users.

# Overview
This dataset is supposed to be for bikeshare in Feb 2019 with 16 rows explaining each bikeshare event by users. Mainly in this project, I discussed reasons affecting each of the following:<br>
- Why people might not use the bikeshare for their whole trip
- Crowded Stations around the state mentioned in the dataset
- Ages using bikeshare systems
- Peak Times when people use to bikeshare
- Gender affection on different criteria over the dataset

# Key Insights
I started looking through the data based on some questions I wrote before the beginning of exploratory analysis, some resulted into further question I already put them into the 'Questions' section in the main notebook. These questions included the following: <br>
## Questions 
1. What are the most crowded stations in terms of start and end stations in bikeshare?
2. what conditions are affected by subscription?
3. Who're the most subscribers?
4. What are the peak times of bikeshare?
5. Is there any factor that affects a Simpson-Paradox throughout these times?!!
6. Which ages share bikes the most?
7. Are subscriptions affected by either of gender or age?
8. Why some users may not use bikeshare for their whole trip?
9. What is the most appearing round trip?
10. Is age a factor affecting share duration?
11. What ages affect bikeshare for all trip?

Answering such questions resulted in seeing observations as mentioned below in the Main Findings section: <br>

# Main Findings
1. Most crowded stations are San Francisco Caltrain Station 2 and Market St
2. Most trips go around Berry St 4th and Harry Bridges Plaza
3. Most Bikesharers are of age 30
4. Peak times are on morning go to work and afternoon return
5. Most Bikesharers are males
6. Age doesn't affect share duration
6. Although most bikesharers are males and most bikesharers are of age 30 but females are the most subscribers of age 30
7. Simpson's paradox could happen assuming that most bikesharers of age 30 males are subscribers while its inversed here
7. Since most bikesharers are males so it's expected to see most subscribers as males as we see in the dataset
8. Bikeshare for all trip is affected by subscription
9. Most bike sharers under 30 are the most to use bikeshare for their whole trip
10. Age doesn't really affect share duration 

# Resources
https://stackoverflow.com/questions/48145924/different-colors-for-points-and-line-in-seaborn-regplot <br>
To see how to change the best fit line color<br>
https://seaborn.pydata.org/generated/seaborn.catplot.html?highlight=catplot#seaborn.catplot<br>
Since I didn't use the violinplot seaborn function<br>
https://online.stat.psu.edu/stat200/lesson/3/3.2#:~:text=We%20can%20use%20the%20IQR,add%20this%20value%20to%20Q3<br>
To deal with age and duration outliers<br>
http://centruldecariera.ase.ro/wp-content/iukzsd0v/6cff29-matplotlib-barh-descending-order<br>
Tried to reach out for a way to make horizontal barplots go descendingly
