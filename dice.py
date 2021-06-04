import csv
import pandas as pd
from plotly.figure_factory.utils import list_of_options 
import plotly_express as px
import plotly.figure_factory as ff
import random
import statistics as stx
import plotly.graph_objects as go

dice_result=[]
for i in range(1,1000) :
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1  + dice2)

#calculate mean median made and standard deviation 

mean=sum(dice_result)/len(dice_result)
standard_deviation =stx.stdev(dice_result)
median=stx.median(dice_result)
mode=stx.mode(dice_result)

print(mean)
print(median)
print(mode)
print(standard_deviation)



# finding one,2,3 standard deviation start and end values
first_std_deviation_start,first_std_deviation_end =mean-standard_deviation,mean+standard_deviation
second_std_deviation_start,second_std_deviation_end =mean-(2*standard_deviation),mean+(2*standard_deviation)
third_std_deviation_start,third_std_deviation_end =mean-(3*standard_deviation),mean+(3*standard_deviation)
fig=ff.create_distplot([dice_result],["Result"] ,show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="standard deviation 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="standard deviation 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="standard deviation 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="standard deviation 2"))
fig.show()
# print the findings
list_of_data_within_1_std_deviation=[result for result in dice_result if result>first_std_deviation_start and result<first_std_deviation_end]
list_of_data_within_2_std_deviation=[result for result in dice_result if result>second_std_deviation_start and result<second_std_deviation_end]
list_of_data_within_3_std_deviation=[result for result in dice_result if result>third_std_deviation_start and result<third_std_deviation_end] 

print("{}% of data lies within one standard deviation".format(len(list_of_data_within_1_std_deviation)*100/len(dice_result)))
print("{}% of data lies within second standard deviation".format(len(list_of_data_within_2_std_deviation)*100/len(dice_result)))
print("{}% of data lies within third standard deviation".format(len(list_of_data_within_3_std_deviation)*100/len(dice_result)))