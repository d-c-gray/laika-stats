# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:07:01 2022

@author: coleg
"""

from scipy import optimize
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats


def fit_exp(x,a1,tau1,const):
    return a1*np.exp(-x/tau1)+const

plt.close('all')

#%% fits
data = pd.read_csv('laikaStats.csv')    
dob = data['Birth Date'].iloc[0]
weeks = data['Age (Weeks)'].to_numpy()
lbs =  data['Weight [lbs]'].to_numpy()
#non linear fit of 2 exp
popt,pcov = optimize.curve_fit(fit_exp,weeks, lbs)
xfit = np.linspace(weeks[0],weeks[-1],100)
yfit = fit_exp(xfit,*popt)
yfit1 = fit_exp(xfit,*(popt+np.sqrt(np.diag(pcov))))
yfit2 = fit_exp(xfit,*(popt-np.sqrt(np.diag(pcov))))
#%% Plots
fig,ax = plt.subplots(1,1)
ax.grid()
ax.plot(weeks/52,lbs,'ko',label = 'Measurements')
ax.plot(xfit/52,yfit,'b-',label = '1 Exp Fit')
ax.plot(xfit/52,yfit1,'r--',label = r'$\pm 1\sigma$ on fit parameters')
ax.plot(xfit/52,yfit2,'r--')
# ax.plot(xfit,y_fo,'g',label = 'first order taylor expansion')
# ax.plot(weeks,ylinreg,'b-',label = 'LinReg: $lbs = '+str(np.round(linreg.slope,1))+'w + '+str(np.round(linreg.intercept,1))+', R^2 = '+str(np.round(linreg.rvalue,3))+'$' )
ax.legend(loc = 'best')
ax.set_xlabel('Age (Years)')
ax.set_ylabel('Weight (lbs)')
ax.set_title(f'Laika\'s Weight with Exponential Fit DOB {dob}')
plt.show()
fig.savefig('laika-weight.png')

#printing

