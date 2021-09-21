import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

songs  = pd.read_csv('Spotify-2000.csv')
songs_top = songs.head()

def dist_fun(x):
    import seaborn as sns
    plt.style.use('ggplot')
    sns.displot(songs[x], kde=True, rug=False)
    plt.title('Distribution of ' + x + ' among Popular Spotify Tracks')

def scatter_fun(x, y):
    plt.scatter(songs[x], songs[y], alpha=0.15, marker='o')
    plt.ylabel(y)
    plt.xlabel(x)
    plt.title(y + ' and ' + x)

def scatter_fit(x, y):
    plt.scatter(songs[x], songs[y])
    plt.plot(np.unique(songs[y]),
        np.poly1d(np.polyfit(songs[x],
                              songs[y], 1))(np.unique(songs[y])),
         color='Black', linestyle="--", linewidth=2)
    plt.ylabel(y)
    plt.xlabel(x)
    plt.title(y + ' and ' + x)

from mpl_toolkits.mplot3d import Axes3D
def scat_3d(x, y, z):
    fig= plt.figure()
    ax = fig.add_subplot(111, projection ='3d')
    ax.scatter(songs[x], songs[y],
           songs[z], c='r', marker='o', alpha=0.1)
    ax.view_init(elev=50., azim=15)  # to rotate plot for better view
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)
    plt.title(z + " and Relation to " + x + " with " + y)

dist_fun('Danceability')
plt.show()
plt.savefig('dance_hist.png')


scatter_fit('Danceability', 'Popularity')
plt.show()
plt.savefig('dance_pop_scatter.png')

scat_3d('Beats Per Minute (BPM)', 'Valence', 'Popularity')
plt.show()
plt.savefig('3d_tempo_happ_pop.png')