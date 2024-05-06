# E-Commerce Customer Segmentation

## Overview
Leveraging a rich dataset of orders and brand searches from over 30,000 customers, I built a customer segmentation model. This model identifies customer brand preferences, enabling personalized marketing strategies.

## Data
The data was collected from a well-known e-commerce website over a period based on the customer's search profile.
|__Column__| Description |
| :--- |:--- |
|__Cust_ID__| Unique numbering for customers |
|__Gender__| Gender of the customers |
|__Orders__| Number of orders placed by the customer in the past|
|__Others__| Number of times customers have searched the brands |

## Data Exploration

### Distribution of Gender
Gender analysis of the dataset shows that female customers dominate in E-commerce purchases.

![gender](https://github.com/aishwarya-10/e-commerce_customer_segmentation/assets/48954230/6a7ad340-aa40-4d7c-b390-81c6cb8b0c7b)

### Distribution of Orders
The data showcases a range of customer engagement, with some placing orders (1-12) and a significant group (around 5,000) focusing on brand research without converting to purchases. This highlights a potential opportunity for targeted marketing strategies.

![orders](https://github.com/aishwarya-10/e-commerce_customer_segmentation/assets/48954230/0b42f915-938b-4e0d-b8e3-3f4fd010bbce)

### Customer Views vs Brands
The chart visualizes the distribution of browsing activity across different brands. Each brand is represented on the y-axis, while the x-axis shows the corresponding number of times customers browsed that particular brand. This helps understand which brands generate the most customer interest.

![cust_views](https://github.com/aishwarya-10/e-commerce_customer_segmentation/assets/48954230/03aae9dd-8ed6-4518-87c8-4ce3e5ef5c63)

## Cluster analysis
The data is processed by removing irrelevant features and filling in missing values using the `mode` technique. K-means calculates the distance between data points using Euclidean distance. This distance measure is heavily influenced by the scale of the features in your data. 
We have used the Silhouette score to find the optimum number of clusters and decided k=3 as the best pick after analyzing the Silhouette score.
    
![elbow](https://github.com/aishwarya-10/e-commerce_customer_segmentation/assets/48954230/2570c13a-062a-4267-8db0-8abc373e6b07)

On applying the K-means algorithm with 3 number of clusters, we have segmented the customers under
    - **Food and snacks**
    - **Lifestyle and Fashion**
    - **Electronics**

| Cluster | Orders | Frequency |
| :--- |:--- | :--- |
| 1 | 5324 | 1278 |
| 2 | 24359 | 5453 |
| 3 | 95411 | 23269 |

## Conclusion
- The customer segmentation analysis using K-means clustering provides valuable insights into the search behavior and purchase patterns of e-commerce customers.
- These clusters give information about the interest of the customer in the different brands. 
- This type of segmentation can help the e-commerce companies, to know the customer choices and they can provide more accurate recommendations to the customers.

