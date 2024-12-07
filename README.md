Here’s a well-structured **README.md** file for your GitHub repository based on the given Python script:

---

# Customer Segmentation Using K-Means Clustering

This project demonstrates customer segmentation using K-Means clustering on a dataset of mall customers. The script performs data preprocessing, applies clustering, calculates distances to centroids, and visualizes the results with insightful plots.

---

## Features
- **Data Preprocessing:**
  - Cleaned column names.
  - Selected relevant features: `Annual Income (k$)` and `Spending Score (1-100)`.
  - Standardized features using `StandardScaler`.

- **Clustering:**
  - Applied K-Means clustering with 3 clusters.
  - Computed distances to cluster centroids and appended them to the dataset.

- **Visualization:**
  - Scatter plot of clusters.
  - Distribution of customers per cluster.
  - Histogram of distances to centroids for each cluster.

- **Output:**
  - Updated dataset with cluster assignments and distances saved as `mall_with_distances.csv`.

---

## Installation

### **1. Clone the repository**
```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

### **2. Install required libraries**
Ensure you have Python installed. Install dependencies using:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

---

## Dataset
The project uses the `Mall_Customers.csv` dataset. Ensure the file is placed in the root folder of the project.

### Sample Structure of `Mall_Customers.csv`:
| CustomerID | Gender | Age | Annual Income (k$) | Spending Score (1-100) |
|------------|--------|-----|--------------------|-------------------------|
| 1          | Male   | 19  | 15                 | 39                      |
| 2          | Female | 21  | 15                 | 81                      |

---

## How to Run
1. Place the dataset (`Mall_Customers.csv`) in the same directory as the script.
2. Execute the script:

   ```bash
   python script.py
   ```

3. View the generated visualizations and inspect the output file `mall_with_distances.csv`.

---

## Visualizations
### **1. Customer Segments**
Scatter plot showing customer segments based on annual income and spending score.

### **2. Cluster Distribution**
Bar chart of the number of customers in each cluster.

### **3. Distances to Centroids**
Histograms representing the distribution of distances to centroids for each cluster.

---

## Project Structure
```
.
├── Mall_Customers.csv        # Input dataset
├── mall_with_distances.csv   # Output dataset with cluster assignments and distances
├── task2.py                 # Main Python script
└── README.md                 # Project documentation
```

---

## Contributing
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Let me know if you'd like me to adjust anything! 😊
