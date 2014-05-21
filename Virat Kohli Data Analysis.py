Virat = df[df["Player"] == "V Kohli"]

Vir_runs = Virat["Runs"].astype(int)
Vir_min = Virat["Minutes"].astype(int)
Vir_balls = Virat["Balls Faced"].astype(int)
Vir_fours = Virat["Fours"].astype(int)
Vir_sixes = Virat["Sixes"].astype(int)
Vir_sr = Virat["Strike Rate"].astype(float)

print np.mean(Vir_min)
print np.mean(Vir_balls)
print np.mean(Vir_fours)
print np.mean(Vir_sixes)
print np.mean(Vir_sr)
print np.mean(Vir_runs)

#Some cool Visualizations
plt.scatter(Vir_runs, Vir_balls,  color='red', alpha=0.5, s= Vir_fours*100, facecolor = "white")
plt.scatter(Vir_runs, Vir_min,  color='red', alpha=0.5, s= Vir_balls*10, facecolor = "white")
plt.scatter(Vir_runs, Vir_balls,  color='red', alpha=0.5, s= Vir_sr*10, facecolor = "white")

#Dependency of runs on some factors
import statsmodels.formula.api as smf
est = smf.gls(formula='Vir_runs ~ Vir_balls + Vir_fours + Vir_sixes + Vir_sr', data=Virat).fit()
est.summary()

est = smf.gls(formula='Vir_runs ~ Vir_balls + Vir_fours + Vir_sixes + Opposition', data=Virat).fit()
est.summary()

