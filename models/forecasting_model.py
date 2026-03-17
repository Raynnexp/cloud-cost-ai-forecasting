# Cloud Cost Predictive Model
# Using Linear Regression concepts to forecast next month's spend

def predict_next_month_cost(current_avg, growth_rate):
    """
    Simulates a Predictive Analytics model.
    Input: Current average spend and month-over-month growth.
    """
    predicted_cost = current_avg * (1 + growth_rate)
    return round(predicted_cost, 2)

# Data from our Databricks billing
current_monthly_avg = 3200.00 # USD
growth_observed = 0.05 # 5% increase

forecast = predict_next_month_cost(current_monthly_avg, growth_observed)

print(f"--- AI Cloud Cost Forecast ---")
print(f"Current Avg Spend: ${current_monthly_avg}")
print(f"Predicted Spend for Next Month: ${forecast}")
