# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 19:35:40 2018

@author: AbhiMan
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 18:03:47 2018

@author: AbhiMan
"""
# Loading lib
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#conda install c anaconda seaborn
# loading excel file
mpl.use('agg')
df_file = pd.read_excel("C:\\Users\\AbhiMan\\Documents\\UTDALLAS\\Compition\\Election\\code fix\\2014 naraingarh vidhan.xlsx")
df_2014 = df_file[['Station Name','INLD','BJP','INC','BSP','TOTAL VOTES']]
df_2014.set_index('Station Name',inplace = True)
df_cur = df_file.groupby('Station Name')['INLD','BJP','INC','BSP'].sum()

df_cur2014 = df_cur[df_cur.index != "Total Valid Votes Polled"]
del df_2014; del df_file; del df_cur;
inld = (df_cur2014['INLD'].values)
bjp = (df_cur2014['BJP'].values)
inc = (df_cur2014['INC'].values)
bsp = (df_cur2014['BSP'].values)
#total = (df_cur['TOTAL VOTES'].values)
fig = plt.figure()
ax = fig.add_subplot(111)
com_list = [inld, bjp, inc,bsp]
x_lbl = ['INLD', 'BJP', 'INC','BSP']
ax.boxplot(com_list, patch_artist=True)
ax.set_xticklabels(x_lbl)
ax.set_title("Box Plot for 2014")
ax.set(ylim=(0, 1000))

plt.show()

" Getting summary for 2014 voting data"
df_cur2014.describe()

"Finding Corelation matrix"
corr = df_cur2014.corr()
print(corr.style.background_gradient().set_precision(2))

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,4,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_title("Correlation Matrix")
ax.set_xticklabels(x_lbl)
ax.set_yticklabels(x_lbl)

plt.show()

" Finding top and bottom station for each party"
for i in range( 0,len(x_lbl)):

    party = eval('[x_lbl[i]]')
    top5 = df_cur2014.nlargest(5,party)
    bottom5 = df_cur2014.nsmallest(5,party)
    bar_val = (top5[party].values).tolist()
    flattened  = [val for sublist in bar_val for val in sublist]
#    val1 = [1,2,2,3,3,4,55,66,44,8,77,98]
    " creating bar graph for top 10 station for INLD"
    y_pos = np.arange(len(top5))
    plt.bar(y_pos, flattened, align='center', alpha=.5)
    plt.xticks(y_pos, top5.index)
    plt.ylabel('Votes')
    plt.title('Top 5 Station for ' +" ".join(party))
    plt.show()
    
    " creating bar graph for Bottom 10 station for INLD"
    y_pos = np.arange(len(bottom5))
    bar_val2 = (bottom5[party].values).tolist()
    flattened_b  = [val for sublist in bar_val2 for val in sublist]
    plt.bar(y_pos, flattened_b, align='center', color = "Orange", alpha=.5)
    plt.xticks(y_pos, bottom5.index)
    plt.ylabel('Votes')
    plt.title('Bottom 5 Station for ' +" ".join(party))
    plt.show()


"Creating Pie chart for % coverage"
labels = x_lbl
sizes = [sum(df_cur2014.INLD), sum(df_cur2014.BJP), sum(df_cur2014.INC), sum(df_cur2014.BSP)]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice
# 
## Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
ax.set_title("Party share for Votes")
plt.axis('equal')
plt.show()

del flattened_b; del sizes; del explode; del labels; del top5; del bottom5;


