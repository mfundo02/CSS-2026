# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 12:15:03 2026

@author: mfund
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
- Cross-matching MeerKLASS with KiDS, GALEX, VIKING, and WISE using a pipline I'm developing
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

    fig, ax = plt.subplots()

    sc = ax.scatter(
        df['zbest'],
        df['L'],
        c=df['bayes.agn.fracAGN_stripe82'],
        s=5,
        cmap='jet',
        vmin=0,
        vmax=1
    )

    cbar = fig.colorbar(sc, ax=ax, orientation="vertical", fraction=0.02, pad=0.04)
    cbar.set_label(r"$AGNfraction_{CIGALE, Stripe82}$")

    ax.axhline(y=1e24, color='black', linestyle='--', linewidth=2)
    ax.set_ylabel(r'$L_{1.4GHz} (W\,Hz^{-1})$')
    ax.set_xlabel(r'Redshift (z)')
    ax.set_xlim(0, 2.5)
    ax.set_yscale('log')

    st.pyplot(fig)
    st.caption('Figure: Radio luminosity at 1.4 GHz ($L_{1.4,\mathrm{GHz}}$) as a function of redshift for MeerKLASS radio-selected sources. Points are colour-coded by the AGN fraction estimated from CIGALE SED fitting (Stripe 82), indicating the relative contribution of AGN emission to the total spectral energy distribution. The horizontal dashed line marks $L_{1.4,\mathrm{GHz}} = 10^{24},\mathrm{W,Hz^{-1}}$, commonly used as an approximate division between star-forming galaxies and radio-loud AGN, as only AGN will likely be the source of such powerful emission ')

except Exception as e:
    st.warning("Plot could not be generated. Make sure css.csv is uploaded to the repo.")
    st.text(str(e))

# Add a contact section
st.header("Contact Information")
email = "mfundoshabalala709@gmail.com"
st.write(f"You can reach {name} at {email}.")



