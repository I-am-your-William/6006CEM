import HousePricePolynomial  # Assuming this has y_test and y_pred_poly_all
import HousePriceRMSELinear  # Assuming this has y_pred_linear
import pandas as pd

# Create a DataFrame to compare actual and predicted prices
comparison_df = pd.DataFrame({
    'Actual Price': HousePricePolynomial.y_test.values,  # Correct access to y_test
    'Predicted Price (Linear Regression)': HousePriceRMSELinear.y_pred_linear,  # Linear regression predictions
    'Predicted Price (Polynomial)': HousePricePolynomial.y_pred_poly  # Polynomial predictions
})

# Display the comparison DataFrame
print(comparison_df)
