import pandas as pd
from matplotlib import pyplot as plt
import os
from mpl_toolkits.basemap import Basemap
import matplotlib.patches as mpatches
import matplotlib.colors as colors
%matplotlib inline 

os.chdir(r'C:/Users/Yin_d/Bordeaux-WIPO Dropbox/Shared/Chapter_2/Agbio/crops/Indicators/charts/chart 4.5/')

agbio=pd.read_stata('chart 4.5_agbio_cluster.dta')

# Plooting 

def colormap():
    cdict = ['limegreen','cornflowerblue']
    return colors.ListedColormap(cdict, 'indexed')

my_cmap = colormap()

for i in agbio.year_dmy.unique():
    agbio_yeardmy = agbio[agbio.year_dmy==i]
    # Set the dimension of the figure
    my_dpi=200
    plt.figure(figsize=(6000/my_dpi, 4000/my_dpi), dpi=my_dpi)
    
    # Make the background map
    m=Basemap(llcrnrlon=-180, llcrnrlat=-65,urcrnrlon=180,urcrnrlat=80)
    m.drawmapboundary(fill_color='1', linewidth=0)
    m.fillcontinents(color='0.8', alpha=0.5)
    m.drawcoastlines(linewidth=0.1, color="white")

    # prepare a color for each point depending on the continent.
    # transform categorical to dummy 
    agbio_yeardmy['labels_enc'] = pd.factorize(agbio_yeardmy['pat_wos'])[0]

    # Add a point per position
    m.scatter(agbio_yeardmy['lng'], agbio_yeardmy['lat'], s=agbio_yeardmy['num_points']/2, alpha=0.5, 
              c=agbio_yeardmy['labels_enc'], cmap=my_cmap)

    #create legend
    leg_pat = mpatches.Patch(color='limegreen', label='Patents')
    leg_wos = mpatches.Patch(color='cornflowerblue', label='Scientific Publications')
    plt.legend(handles=[leg_pat,leg_wos],loc='lower left',ncol=1,prop={'size': 20})

    plt.title("Geographical distribution of global crops patents and publications in "+i,size=20)
    # Save as png
    plt.savefig('chart4.5_crops_cluster_bubble'+i+'.png', bbox_inches='tight',dpi=1000)
    print(i,"finished")
print("Done!!!")

plt.show()