
# Customer Segmentation Using K-Means Clustering

This project, hosted on [GitHub](https://github.com/mourvijoshi/PRODIGY_ML_02.git), demonstrates customer segmentation using K-Means clustering on a dataset of mall customers. The script involves preprocessing, clustering, and visualizing the data to extract meaningful insights.

---

## Features
- **Data Preprocessing:**
  - Cleaned column names to ensure consistency.
  - Selected relevant features: `Annual Income (k$)` and `Spending Score (1-100)`.
  - Standardized features using `StandardScaler`.

- **Clustering:**
  - Applied K-Means clustering to segment customers into 3 clusters.
  - Computed distances to cluster centroids for analysis.

- **Visualization:**
  - Scatter plot of clusters based on features.
  - Distribution of customers across clusters.
  - Histograms of distances to centroids for each cluster.

- **Output:**
  - Updated dataset saved as `mall_with_distances.csv`, which includes:
    - Cluster assignments.
    - Distances to centroids.

---

## Installation

### 1. Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/mourvijoshi/PRODIGY_ML_02.git
```

### 2. Install Required Libraries
Install dependencies using `pip`:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

---

## Dataset
The project uses the `Mall_Customers.csv` dataset. Ensure this file is located in the root directory.

### Sample Dataset Columns:
| CustomerID | Gender | Age | Annual Income (k$) | Spending Score (1-100) |
|------------|--------|-----|--------------------|-------------------------|
| 1          | Male   | 19  | 15                 | 39                      |
| 2          | Female | 21  | 15                 | 81                      |

---

## How to Run
1. Place `Mall_Customers.csv` in the same folder as the script.
2. Execute the script:

   ```bash
   python task2.py
   ```

3. The output file `mall_with_distances.csv` will be generated in the project directory.
4. View the generated visualizations for insights into clustering results.

---

## Visualizations
1. **Customer Segments:** A scatter plot showing clusters of customers based on income and spending score.
2. **Cluster Distribution:** A bar chart representing the number of customers in each cluster.
3. **Distances to Centroids:** Histograms showing the distribution of distances to centroids for each cluster.

---

## Project Structure
```
.
├── Mall_Customers.csv        # Input dataset
├── mall_with_distances.csv   # Output dataset with cluster data
├── task2.py                 # Python script for clustering
├── README.md                 # Project documentation
```

---

## Contributing
Feel free to contribute! Fork the repository, create a branch for your feature, and submit a pull request.

---

### Repository Link:
Access the project on GitHub: [PRODIGY_ML_02](https://github.com/mourvijoshi/PRODIGY_ML_02.git)

---
