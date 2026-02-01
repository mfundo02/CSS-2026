# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 12:15:03 2026

@author: mfund
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page title
st.set_page_config(page_title="Mfundo Shabalala | Research Profile", layout="wide")


# Collect basic information
name = "Mfundo Shabalala"
field = "Astrophysics"
institution = "University of the Western Cape"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")


st.subheader('About me')
st.write("""

I am an MSc student in Astronomy at the University of the Western Cape (UWC), with research experience in radio astronomy and multiwavelength studies of galaxies and AGN. My work focuses on understanding the physical properties and cosmic evolution of radio-selected galaxies using MeerKAT and large optical/infrared surveys.

---

### Research Interests
- Radio galaxy evolution
- Active Galactic Nuclei (AGN)
- Star-forming galaxies
- Multiwavelength astronomy
- Galaxy evolution
- Radio luminosity functions
- Spectral Energy Distribution (SED) fitting

---
""")

st.subheader('Current project')
st.write("""**Multiwavelength counterparts of MeerKLASS radio sources
- Cross-matching MeerKLASS with KiDS, GALEX, VIKING, and WISE using a pipline I'm developing, and it could be found at: https://github.com/mfundo02/cross-matching
- Building a unified multiwavelength catalogue
- Separating AGN and star-forming galaxies
- Performing SED fitting using AGNfitter
- Studying radio and infrared luminosity functions

""")
try:
    st.image('378_mosaic.png', caption='Image of the same source from different surveys with the blue contours representing radio emission from the source. I use these images insure that the crossmatching was valid.')
except Exception as e:
    st.warning("Plot could not be generated. Make sure image is in repo")
    st.text(str(e))
    
st.subheader("Redshift vs Radio Luminosity")



try:
    df = pd.read_csv('css.csv', sep=',')

    fig = px.scatter(
        df,
        x='zbest',
        y='L',
        color='bayes.agn.fracAGN_stripe82',
        color_continuous_scale='Jet',
        range_color=(0, 1),
        labels={
            'zbest': 'Redshift (z)',
            'L': r'L_1.4GHz (W Hz⁻¹)',
            'bayes.agn.fracAGN_stripe82': 'AGN fraction (CIGALE, Stripe82)'
        },
        title='Radio luminosity vs redshift'
    )

    # Add horizontal AGN/SFG division line
    fig.add_hline(
        y=1e24,
        line_dash='dash',
        line_color='black',
        line_width=2,
        annotation_text='AGN/SFG divide',
        annotation_position='top left'
    )

    # Log scale on y-axis and x limits
    fig.update_yaxes(type='log')
    fig.update_xaxes(range=[0, 2.5])

    # Marker size (Plotly handles this differently than matplotlib)
    fig.update_traces(marker=dict(size=5))

    st.plotly_chart(fig, use_container_width=True)

    st.caption(
        'Figure: Radio luminosity at 1.4 GHz ($L_{1.4,\mathrm{GHz}}$) as a function of redshift for MeerKLASS radio-selected sources. '
        'Points are colour-coded by the AGN fraction estimated from CIGALE SED fitting (Stripe 82), indicating the relative contribution '
        'of AGN emission to the total spectral energy distribution. The horizontal dashed line marks '
        '$L_{1.4,\mathrm{GHz}} = 10^{24}\,\mathrm{W\,Hz^{-1}}$, commonly used as an approximate division between star-forming galaxies and '
        'radio-loud AGN.'
    )

except Exception as e:
    st.warning("Plot could not be generated. Make sure css.csv is uploaded to the repo.")
    st.text(str(e))


# Add a contact section
st.header("Contact Information")
email = "mfundoshabalala709@gmail.com"
st.write(f"You can reach {name} at {email}.")

