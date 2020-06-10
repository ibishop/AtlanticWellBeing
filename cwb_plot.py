import data.load as dl
import plotly.graph_objects as go
import pandas as pd
import numpy as np
# Load Dataset

df = dl.comm_well_being(2001)

fig = go.Figure()

fig.add_trace(go.Scatter(x= np.log(df['2A Population / Population 2A 2001']+1),
                         y= df['Education / Scolarité 2001'],
                         mode='markers',
                         text=df['CSD Name / Nom de la SDR 2001'])
              )

fig.add_trace(go.Scatter(x= np.log(df['2A Population / Population 2A 2001']+1),
                         y= df['Income / Revenu 2001'],
                         mode='markers',
                         visible=False,
                         text=df['CSD Name / Nom de la SDR 2001'])
              )

fig.add_trace(go.Scatter(x= np.log(df['2A Population / Population 2A 2001']+1),
                         y= df['Housing / Logement 2001'],
                         mode='markers',
                         visible=False,
                         text=df['CSD Name / Nom de la SDR 2001'])
              )


fig.add_trace(go.Scatter(x= np.log(df['2A Population / Population 2A 2001']+1),
                         y= df['Labour Force Activity / Activité sur le marché du travail 2001'],
                         mode='markers',
                         visible=False,
                         text=df['CSD Name / Nom de la SDR 2001'])
              )


fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="Education",
                     method="update",
                     args=[{"visible": [True, False, False, False]},
                           {"title": "Education"}]),

                dict(label="Income",
                     method="update",
                     args=[{"visible": [True, False, False, False]},
                           {"title": "Income"}]),

                dict(label="Housing",
                     method="update",
                     args=[{"visible": [False, False, True, False]},
                           {"title": "Housing"}]),

                dict(label="LFA",
                     method="update",
                     args=[{"visible": [False, False, False, True]},
                           {"title": "LFA"}]),

            ]),
        )
    ])

# Set title
fig.update_layout(title_text="CWB Data")

fig.show()
