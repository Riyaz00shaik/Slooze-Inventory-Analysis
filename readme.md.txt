# Slooze Inventory Optimization Project

## Project Overview
This project analyzes sales, purchases, and inventory data to improve stock management, reduce financial loss, and optimize supplier performance.

## Objectives
- Demand Forecasting
- ABC Inventory Classification
- Economic Order Quantity (EOQ)
- Reorder Point Calculation
- Lead Time Analysis
- Inventory Turnover Analysis
- Dead Stock Identification

## Approach

1. Data Cleaning
   - Standardized date formats
   - Removed missing values
   - Created revenue metrics

2. Sales Analysis
   - Monthly revenue trend analysis
   - Top-performing products identification

3. ABC Analysis
   - Classified products into A, B, C categories
   - Prioritized high-revenue inventory

4. Inventory Optimization
   - Calculated EOQ
   - Determined reorder points
   - Evaluated inventory turnover

5. Supplier Performance
   - Lead time analysis
   - Vendor efficiency comparison

6. Demand Forecasting
   - Time-series forecasting using historical sales

## Key Insights
- A small percentage of products generate majority of revenue.
- Certain suppliers have significantly higher lead times.
- Slow-moving items tie up working capital.
- Forecasting improves purchasing planning and reduces stockouts.

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the analysis:
   python inventory_analysis.py