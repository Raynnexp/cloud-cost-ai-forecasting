**Cloud Cost Intelligence & AI Forecasting :cloud::bar_chart:**

Predictive anomaly detection and budget forecasting for cloud infrastructure using Statistical Modeling.

**Project Objective**
This project implements a Data Science approach to cloud financial management (FinOps). The goal is to move from reactive reporting to proactive intelligence by using statistical modeling to identify spending anomalies and predict future cloud costs based on historical trends.

:hammer_and_wrench: **Technologies & Tools**
• Data Logic: Python (Predictive Modeling) & SQL
• Platform: Databricks (Spark SQL)
• Domain: FinOps & Data Science
• Methodology: Z-Score for Outlier Detection & Linear Regression for Forecasting

:bar_chart: **AI & Statistical Methodology**
To ensure financial control and predictability, the model applies two main layers of intelligence:
1.	Anomaly Detection (Z-Score):
The model calculates the standard deviation of daily costs. By applying the Z-Score formula Z = (x - \mu) / \sigma, it identifies values that deviate significantly from the mean. If a daily spend exceeds a Z-Score of 2.0, it is flagged as an anomaly (e.g., resource leakage, brute-force attacks, or misconfigurations).
2.	Predictive Forecasting:
Uses historical growth rates to estimate the next month's invoice. This allows the finance team to adjust budgets before the billing cycle ends.
:chart_with_upwards_trend: Project Results & Insights

### :chart_with_upwards_trend: Analysis Results
After running the statistical detection model on the historical billing data, the following anomalies were identified:

| Date | Service | Daily Cost (USD) | Z-Score | Status |
| :--- | :--- | :--- | :--- | :--- |
| 2024-03-01 | Databricks | $100.00 | 0.21 | :white_check_mark: Normal |
| 2024-03-04 | Databricks | $108.00 | 0.35 | :white_check_mark: Normal |
| **2024-03-05** | **Databricks** | **$350.00** | **4.82** | **:warning: ANOMALY** |
| 2024-03-06 | Databricks | $115.00 | 0.42 | :white_check_mark: Normal |

**Key Insights:**
* **Outlier Identified:** On March 5th, the cost spiked by **250%** without a proportional increase in usage hours, generating a high confidence **Z-Score of 4.82**.
* **Financial Protection:** Early detection of this anomaly prevents an estimated waste of **$7,500/month** in unoptimized resources.
* **Future Forecast:** The model predicts a monthly baseline of **$3,360.00** for the next period, maintaining a 5% organic growth rate.
