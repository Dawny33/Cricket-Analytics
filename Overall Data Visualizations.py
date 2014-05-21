%pylab inline

import matplotlib.pyplot as plt


#Plot b|w Fours and Strike Rate
plt.scatter(Sixes, Strike_Rate)
plt.xlabel('No. of Sixes')
plt.ylabel('Strike-Rate')
numpy.corrcoef(Sixes, Strike_Rate)

#Plot b|w Sixes and Strike Rate
plt.scatter(Sixes, Strike_Rate)
plt.xlabel('No. of Sixes')
plt.ylabel('Strike-Rate')
numpy.corrcoef(Sixes, Strike_Rate)

#Plot b|w Fours and Balls Faced
plt.scatter(Fours, Balls_Faced, color='black', alpha=0.5)
plt.xlabel('No. of Balls Faced')
plt.ylabel('Strike-Rate')
numpy.corrcoef(Balls_Faced, Fours)
