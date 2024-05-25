# ==================================================       /     IMPORT LIBRARY    /      =================================================== #
#[Data Transformation]
import numpy as np
import pandas as pd
import base64

#[Dashboard]
import plotly.graph_objects as go
import streamlit as st
from streamlit_extras.stylable_container import stylable_container


# ==================================================       /     CUSTOMIZATION    /      =================================================== #
# Streamlit Page Configuration
st.set_page_config(
    page_title = "Customer Clustering",
    page_icon= "Image/shopping-cart.png",
    layout = "centered",
    initial_sidebar_state= "expanded"
    )

# Title
st.header(":blue[Clustering E-Commerce Customers by Search Interests] :shopping_bags:")


# ==================================================       /     INTRO    /      =================================================== #
# Overview
st.subheader("Overview")

st.write("""
        Clustering unlocks valuable insights from datasets. First, it helps us explore and understood
         the data's structure, unveiling hidden patterns and relationships. Second, clustering empowers us to 
         identify distinct customer segments, a crucial step in covering new business opportunities and improving
         key metrics. \n
         Three clusters were identified from K-Means clustering. \n
         The dataset was from a E-Commerce site generated over a period with a unique ID for customers. The process 
         of clustering is detailed in the Python notebook in the repository. \n
         Now, time to unpack these customer segments!
         """)


# ==================================================       /     CUSTOMER CLUSTERS    /      =================================================== #
# Cluster analysis
st.subheader("Who's Who in Our Customer Clusters?")

clusters_dict = {"Food and Snacks": 0, "Lifestyle and Fashion": 1, "Electronics": 2}

clusters = ["Food and Snacks", "Lifestyle and Fashion", "Electronics"]

selected_cluster = st.selectbox(label= "Select a Cluster", options= clusters, index= 0, key= "cluster")


def get_radar_chart(data, selected_cluster):

  input_data = data.drop("Orders", axis=1)
  row_index = clusters_dict.get(selected_cluster)
  input_data = input_data.loc[[row_index], :]

  categories = ['Jordan', 'Gatorade', 'Samsung', 'Asus',
                'Udis', 'Mondelez International', 'Wrangler', 'Vans', 'Fila', 'Brooks',
                'H&M', 'Dairy Queen', 'Fendi', 'Hewlett Packard', 'Pladis', 'Asics',
                'Siemens', 'J.M. Smucker', 'Pop Chips', 'Juniper', 'Huawei', 'Compaq',
                'IBM', 'Burberry', 'Mi', 'LG', 'Dior', 'Scabal', 'Tommy Hilfiger',
                'Hollister', 'Forever 21', 'Colavita', 'Microsoft', 'Jiffy mix',
                'Kraft']

  # Scale the values between 0 and 1
  scaler = pd.Series(data=input_data.min(axis=0), index=input_data.columns)
  scaler = scaler.append(pd.Series(data=input_data.max(axis=0), index=input_data.columns))
  scaled_data = (input_data - scaler.min()) / (scaler.max() - scaler.min())

  fig = go.Figure()

  fig.add_trace(go.Scatterpolar(
      r=scaled_data.iloc[0].tolist(), 
      theta=categories,
      fill='toself',
      name='brands'
  ))

  fig.update_layout(
      polar=dict(
          radialaxis=dict(
              visible=True,
              range=[0, 1]
          )
      ),
      showlegend=True
  )

  return fig

data = pd.read_csv("Data/clustered_data.csv")

chart = get_radar_chart(data, selected_cluster)
st.plotly_chart(chart)


# ==================================================       /     CONCLUSION    /      =================================================== #
# Cluster analysis
st.subheader("Inference")

st.write("""
- In this case study, we have grouped customer dataset into 3 clusters based on the brands they have searched in the e-commerce website. 
- We have used Silhouette score to find the optimum number of clusters and decided k=3 as the best pick after analysing the Silhouette score.
- On applying K-means algorithm with 3 number of clusters, we have segmented the customers under
    - Food and snacks
    - Lifestyle and Fashion
    - Electronics

- These clusters give the information about the interest of the customer in the different brands. 
- This type of segmentation can help the e-commerce companies , to know the customer choices and they can provide more accurate recommendation to the customers.

""")


# streamlit run app.py
