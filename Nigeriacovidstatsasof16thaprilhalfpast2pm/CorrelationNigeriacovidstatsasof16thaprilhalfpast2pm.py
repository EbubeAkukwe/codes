'''
Nigeria's Covid19 stats as of April 16th Half Past 2PM

Data Source: https://covid19.ncdc.gov.ng/
Credit: Akukwe Ebube
'''

import pandas as pd
import matplotlib.pyplot as plt

dataset = (r"C:\Users\USER\Desktop\Storage\codes\datascience\datavisual\Nigeriacovidstatsasof16thaprilhalfpast2pm\Nigeriacovidstatsasof16thaprilhalfpast2pm.csv")
df = pd.read_csv(dataset)
type(df)
pd.core.frame.DataFrame
pd.set_option("display.max.columns", None)
df.head()

try :
    df.plot(x="StatesAffected", y = ["No.ofCases(LabConfirmed)","No.ofCases(onadmission)","No.Discharged","No.ofDeaths"], kind="bar", rot=100, fontsize=6)
    plt.show()
except KeyError as e :
    print("You did not input the required selection. \n Try replacing "+comp+" with the correct requirement in your input \n Program Stopped!! Please Run Again.")
