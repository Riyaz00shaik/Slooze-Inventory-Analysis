# Slooze Inventory Analysis

## Project Overview
This project performs inventory, sales, and purchase analysis for a retail wine & spirits company.

The goal is to:
- Optimize inventory levels
- Perform ABC analysis
- Forecast demand
- Calculate EOQ
- Analyze supplier lead time
- Improve procurement efficiency

---

## Dataset
Sample dataset is included (reduced size for GitHub upload).

Original dataset was large and trimmed for repository size compliance.

---

## Analysis Performed

### 1. Demand Forecasting
- Time-series based monthly sales aggregation
- Revenue trend visualization

### 2. ABC Analysis
- Inventory categorized into A, B, C classes
- Prioritization based on contribution

### 3. EOQ Calculation
- Economic order quantity optimization
- Holding vs ordering cost comparison

### 4. Reorder Point
- Safety stock consideration
- Lead time based reorder strategy

### 5. Lead Time Analysis
- Supplier efficiency evaluation

---

## Project Structure

data/ → Input datasets  
src/ → Python analysis script  
outputs/ → Generated results and visualizations  
notebooks/ → Optional exploration  

---

## How to Run

1. Install dependencies:
   pip install -r requirement.txt

2. Run:
   python inventory_analysis.py
