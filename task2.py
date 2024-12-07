import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('Mall_Customers.csv')

# Inspect and clean column names
df.columns = df.columns.str.strip()  # Remove extra spaces
print("Available columns:", df.columns)  # Debug: Check column names

# Select features
features = df[['Annual Income (k$)', 'Spending Score (1-100)']]  # Ensure column names are correct

# Standardize the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)  # Explicit n_init for sklearn >= 1.3
df['ClusterAssigned'] = kmeans.fit_predict(scaled_features)

# Calculate distances to centroids
distances = pd.DataFrame()
for i in range(3):
    centroid = kmeans.cluster_centers_[i]
    distances[f'DistanceToCentroid{i + 1}'] = np.linalg.norm(scaled_features - centroid, axis=1)

# Append distances to the DataFrame
df = pd.concat([df, distances], axis=1)

# Save the updated DataFrame
df.to_csv('mall_with_distances.csv', index=False)
print("Updated DataFrame saved as 'mall_with_distances.csv'.")

# Visualization

# 1. Scatter plot of clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='Annual Income (k$)',
    y='Spending Score (1-100)',
    hue='ClusterAssigned',
    data=df,
    palette='viridis',
    legend='full',
    s=100
)
plt.title('Customer Segments (Clustered)', fontsize=15)
plt.xlabel('Annual Income (k$)', fontsize=12)
plt.ylabel('Spending Score (1-100)', fontsize=12)
plt.show()

# 2. Distribution of customers per cluster
plt.figure(figsize=(8, 6))
sns.countplot(x='ClusterAssigned', data=df, palette='viridis')
plt.title('Number of Customers in Each Cluster', fontsize=15)
plt.xlabel('Cluster', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.show()

# 3. Distance to Centroids
for i in range(1, 4):
    plt.figure(figsize=(8, 6))
    sns.histplot(df[f'DistanceToCentroid{i}'], kde=True, color=['blue', 'orange', 'green'][i - 1])
    plt.title(f'Distance to Centroid {i}', fontsize=15)
    plt.xlabel('Distance', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.show()
