'''
Created on Sep 6, 2017

@author: idolchevic
'''
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.misc import imread
import pandas as pd
import matplotlib.cbook as cb

df_cies_by_latlong = pd.read_csv('allbylatandlong.csv')

lat = list(df_cies_by_latlong.lat.map(float))
long = list(df_cies_by_latlong.long.map(float))

# Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Vega10, Vega10_r, Vega20, Vega20_r, Vega20b, Vega20b_r, Vega20c, Vega20c_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, icefire, icefire_r, inferno, inferno_r, jet, jet_r, magma, magma_r, mako, mako_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, rocket, rocket_r, seismic, seismic_r, spectral, spectral_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, viridis, viridis_r, vlag, vlag_r, winter, winter_r
# Create new Figure and an Axes which fills it.
xmin,xmax = (np.array(long).min() - 0.2, np.array(long).max() + 0.2)
ymin,ymax = (np.array(lat).min() - 0.2, np.array(lat).max()+0.2)
color = (1,1,1,0.1)

fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(xmin, xmax), ax.set_xticks([])
ax.set_ylim(ymin, ymax), ax.set_yticks([])
plt.title('Toulouse : 40 ans de créations d\'entreprises')
# Create rain data
n_drops = 1000
rain_drops = np.zeros(n_drops, dtype=[('position', float, 2),
                                      ('size',     float, 1),
                                      ('growth',   float, 1),
                                      ('color',    float, 4)])

# Initialize the raindrops in random positions and with
# random growth rates.
#rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
all_positions = list(zip(long,lat))
all_years = list(df_cies_by_latlong.year)
#rain_drops['position'] = list(zip(lat[:n_drops], long[:n_drops]))
rain_drops['position'] = all_positions[:n_drops]
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)

# Construct the scatter which we will update during animation
# as the raindrops develop.
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
                  facecolors=color)


text = ax.text(0.4, 43.9, '0', bbox=dict(facecolor='white', alpha=0.5))
text_year = ax.text(0.4,44, '0', fontsize='30')


def update(frame_number):
    window_size = 200
    # Get an index which we can use to re-spawn the oldest raindrop.
    current_index = (frame_number * window_size) % n_drops
        

    # Make all colors more transparent as time progresses.
    rain_drops['color'][:, 3] -= 1.0/len(rain_drops)
    rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)


    # Make all circles bigger.
    rain_drops['size'] += rain_drops['growth']
    rain_drops['size'] = [200 if size >= 300 else size for size in rain_drops['size']]    

    # Pick a new position for oldest rain drop, resetting its size,
    # color and growth factor.
    #rain_drops['position'][current_index] = np.random.uniform(0, 1, 2)
    limit = window_size
    
    if frame_number * window_size + window_size > len(all_positions) -1:        
        limit = len(all_positions) -1 - frame_number * window_size
        print(limit)
         
    for i in range(limit):
        rain_drops['position'][current_index + i] = all_positions[frame_number * window_size + i]
        rain_drops['size'][current_index + i] = 1
        rain_drops['color'][current_index + i] = color
        rain_drops['growth'][current_index + i] = np.random.uniform(10, 40)

    
    # Update the scatter collection, with the new colors, sizes and positions.
    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])   
    text.set_text(str(frame_number * window_size) + ' sociétés créées')
    text_year.set_text(str(all_years[frame_number * window_size]))    


# Construct the animation, using the update function as the animation
# director.
animation = FuncAnimation(fig, update, interval=2)


#plt.imshow(img, zorder=90, extent=[0, 1, 0, 1])
plt.margins(0.02)

datafile = cb.get_sample_data('/home/idolchevic/eclipse-workspace/datacamp/PracticeToulouseAgglomerationCompanies/departement-31.png')
img = imread(datafile)
plt.imshow(img, extent=(xmin+0.27, xmax-0.1, ymin+0.05, ymax-0.23), zorder=0)

plt.show()



