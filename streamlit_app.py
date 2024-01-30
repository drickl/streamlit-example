import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

nodes = []
edges = []
nodes.append( Node(id="Spiderman",
                   label="Peter Parker",
                   size=25,
                   shape="circularImage",
                   image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png")
              ) # includes **kwargs

nodes.append( Node(id="Captain_Marvel",
                   size=25,
                   shape="circularImage",
                   image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png")
              )

edges.append( Edge(source="Captain_Marvel",
                   label="friend_of",
                   target="Spiderman",
                   # **kwargs
                   )
              )

config = Config(width=750,
                height=950,
                directed=True,
                physics=True,
                hierarchical=False,
                # **kwargs
                )

return_value = agraph(nodes=nodes,
                      edges=edges,
                      config=config)


"""
# Drickls first Streamlit app!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

*Hallo Stefan* das ist total cool.

In the meantime, below is an example of what you can do with just a few lines of code:
"""



num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
