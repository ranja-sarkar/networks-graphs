
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

data = pd.read_csv('FlightsUSA.csv')
df = nx.from_pandas_edgelist(data, source = 'Origin', target = 'Dest', edge_attr = True)

#df.nodes()
#df.edges()

plt.figure(figsize = (18,12))
nx.draw_networkx(df, with_labels = True)

shortest_dist = nx.dijkstra_path(df, source = 'LAS', target = 'PBI', weight = 'Distance')
shortest_airtime = nx.dijkstra_path(df, source = 'LAS', target = 'PBI', weight = 'AirTime')

print(shortest_dist,shortest_airtime)


