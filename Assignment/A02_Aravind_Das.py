#r: networkx
#r: matplotlib

import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore

#create a Graph
G = nx.Graph()

#add nodes
G.add_node('node1')
G.add_node('node2')
G.add_node('node3')
G.add_node('node4')

#add edges
G.add_edge('node1', 'node2')
G.add_edge('node1', 'node3')
G.add_edge('node3', 'node4')

#add position to display
pos = nx.spring_layout(G)

#draw serttings
fig = plt.figure(figsize=(10,10))
ax = plt.subplot()
ax.set_title('Graph', fontsize=12)
nx.draw(G, pos, node_size=1500, with_labels=True, node_color='red', font_size=10, font_color='white')

#draw the graph
plt.tight_layout()


#plot
path= r"E:\MPDA\Python2\New ASsignement - VS\images\hfhfhf.png"
plt.savefig(path, format="PNG")

import networkx as nx
import matplotlib.pyplot as plt

# Create a Graph
G = nx.Graph()

# Add nodes
G.add_node('Aruldas')
G.add_node('Parimala')
G.add_node('arvinddas')
G.add_node('archanat')
G.add_node('ananddas')
G.add_node('anushaA')
G.add_node('Kiandas')
G.add_node('Ashokdas')
G.add_node('JinnyJacob')
G.add_node('Avinash')


# Add edges
G.add_edge('Aruldas','Parimala')
G.add_edge('arvinddas', 'archanat')
G.add_edge('ananddas', 'anushaA',)
G.add_edge('Kiandas', 'anushaA',)
G.add_edge('Ashokdas', 'JinnyJacob')
G.add_edge('Avinash', 'x')


# Add position to display
pos = nx.spring_layout(G,k=3)

# Draw settings
fig, ax = plt.subplots(figsize=(10, 10))  # Using subplots to get figure and axis together
ax.set_title('Graph', fontsize=12)
nx.draw(G, pos, node_size=1500, with_labels=True, node_color='red', font_size=10, font_color='white')

# Draw the graph
plt.tight_layout()

# Save the plot
path = r"E:\MPDA\Python2\New ASsignement - VS\images\hfhfhf.png"
plt.savefig(path, format="PNG")

# Display the plot
plt.show()