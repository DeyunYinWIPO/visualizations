import pandas as pd
from matplotlib import pyplot as plt
import os
from mpl_toolkits.basemap import Basemap
import matplotlib.patches as mpatches
import matplotlib.colors as colors
%matplotlib inline 


df=pd.read_stata('Chart 4.4_Crops_cluster_data')


def colormap():
    cdict = ['limegreen','orange']
    return colors.ListedColormap(cdict, 'indexed')

my_cmap = colormap()

my_dpi=200
plt.figure(figsize=(6000/my_dpi, 4000/my_dpi), dpi=my_dpi)

# Make the background map
m=Basemap(llcrnrlon=-180, llcrnrlat=-65,urcrnrlon=180,urcrnrlat=80)
m.drawmapboundary(fill_color='1', linewidth=0)
m.fillcontinents(color='0.8', alpha=0.3)
m.drawcoastlines(linewidth=0.1, color="white")

# prepare a color for each point depending on the continent.
# transform categorical to dummy 
df['labels_enc'] = pd.factorize(df['cluster_type'])[0]

# Add a point per position
m.scatter(df['lng'], df['lat'], s=df['clus_num']/5, alpha=0.8, 
          c=df['labels_enc'], cmap=my_cmap)

#create legend
leg_int = mpatches.Patch(color='limegreen', label='International Crop Biotech Clusters')
leg_nat = mpatches.Patch(color='orange', label='National Crop Biotech Clusters')
plt.legend(handles=[leg_int,leg_nat],loc='lower left',ncol=1,prop={'size': 20})

plt.title("Geographical Distribution of Crop Biotech Clusters",size=20)
# Save as png
plt.savefig('./charts/6.6 Maps/crops_clusters_bubble.png', bbox_inches='tight',dpi=1000)
print("Done!!!")

plt.show()
