import numpy as np
import pandas as pd
import streamlit as st

import plotly.graph_objects as go

st.beta_set_page_config(layout='wide')

N = 1000

# Generate curve data
t = pd.Series(np.linspace(0, 5, N))
x_e = np.cos(t)
y_e = np.sin(t)

w_m = st.sidebar.slider(
    'Moon orbital speed',
    min_value=1,
    max_value=100,
    value=10
)

d_moon = st.sidebar.slider(
    'Moon-earth distance',
    min_value=0.03,
    max_value=0.5,
    value=0.1,
    step=0.001
)

x_m = x_e + d_moon * np.cos(w_m*t)
y_m = y_e + d_moon * np.sin(w_m*t)

text_e = [
    f"Earth<br>t: {round(val, 1)}<br>X: {round(x_e[idx], 2)}<br>Y: {round(y_e[idx], 2)}"
    for idx, val in t.iteritems()
]

text_m = [
    f"Moon<br>t: {round(val, 1)}<br>X: {round(x_m[idx], 2)}<br>Y: {round(y_m[idx], 2)}"
    for idx, val in t.iteritems()
]

# Create figure
fig = go.Figure(
    data=[
        go.Scatter(
            x=[x_m.iloc[0], x_e.iloc[0]],
            y=[y_m.iloc[0], y_e.iloc[0]],
            marker={'color': "red"},
            name='Moon-Earth distance'
        ),
        go.Scatter(
            x=x_e,
            y=y_e,
            mode="lines",
            line={'color': "blue"},
            name='Earth orbit',
            hoverinfo='text',
            text=text_e
        ),
        go.Scatter(
            x=x_m,
            y=y_m,
            mode="lines",
            line={'color': "grey"},
            name='Moon orbit',
            hoverinfo='text',
            text=text_m
        )
    ],
    layout=go.Layout(
        xaxis=dict(range=[-1.5, 1.5], autorange=False, zeroline=False),
        yaxis=dict(range=[-1.5, 1.5], autorange=False, zeroline=False),
        width=1000,
        height=800,
        title_text="Sun-Moon-Earth orbit",
        hovermode="closest",
        updatemenus=[
            dict(
                type="buttons",
                buttons=[
                    dict(
                        label="Play",
                        method="animate",
                        args=[
                            None,
                            {
                                "frame": {
                                    "duration": 20,
                                    "redraw": False
                                },
                                "fromcurrent": True,
                                "transition": {
                                    "duration": 10,
                                    "easing": "quadratic-in-out"
                                }
                            }
                        ]
                    )
                ]
            )
        ]
    ),
    frames=[
        go.Frame(
            data=[
                go.Scatter(
                    x=[x_m.iloc[idx], x_e.iloc[idx]],
                    y=[y_m.iloc[idx], y_e.iloc[idx]],
                    marker={'color': "red"},
                    name='Moon-Earth distance'
                )
            ]
        )
        for idx, val in t.iteritems()
    ]
)

st.plotly_chart(fig)
