# Least Squares Approximation Implementation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use(['ggplot'])

# Load the data
df = pd.read_csv('salary_data.csv')
print("First 4 rows of data:")
print(df.head(4))

# 4. Create scatter plot
print("\n=== Creating Scatter Plot ===")
plt.figure(figsize=(10, 6))
plt.scatter(df['YearsExperience'], df['Salary'], color='blue', alpha=0.7, s=50)
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs Years of Experience')
plt.grid(True, alpha=0.3)
plt.show()

# 5. Implement Least Squares Approximation manually
print("\n=== Implementing Least Squares Approximation ===")

# Extract x (years of experience) and y (salary) from dataframe
x = df['YearsExperience'].values
y = df['Salary'].values

print(f"Number of data points: {len(x)}")
print(f"X range: {x.min():.1f} to {x.max():.1f} years")
print(f"Y range: ${y.min():.0f} to ${y.max():.0f}")

# Create matrix A = [1, X] where:
# - First column is all ones (for θ₀ term)
# - Second column is the x values (for θ₁ term)
n = len(x)
A = np.column_stack([np.ones(n), x])
print(f"\nMatrix A shape: {A.shape}")
print("First few rows of A:")
print(A[:5])

# The target vector b is the salary values
b = y.reshape(-1, 1)  # Make it a column vector
print(f"\nVector b shape: {b.shape}")

# Calculate θ using the normal equation: θ = (A^T A)^(-1) A^T b
print("\n=== Calculating θ parameters ===")

# Step 1: Calculate A^T (A transpose)
A_transpose = A.T
print(f"A^T shape: {A_transpose.shape}")

# Step 2: Calculate A^T * A
AtA = A_transpose @ A
print(f"A^T * A shape: {AtA.shape}")
print("A^T * A:")
print(AtA)

# Step 3: Calculate (A^T * A)^(-1)
AtA_inv = np.linalg.inv(AtA)
print(f"\n(A^T * A)^(-1):")
print(AtA_inv)

# Step 4: Calculate A^T * b
Atb = A_transpose @ b
print(f"\nA^T * b shape: {Atb.shape}")
print("A^T * b:")
print(Atb)

# Step 5: Calculate θ = (A^T * A)^(-1) * A^T * b
theta = AtA_inv @ Atb
print(f"\n=== Final θ parameters ===")
print(f"θ₀ (intercept): {theta[0, 0]:.2f}")
print(f"θ₁ (slope): {theta[1, 0]:.2f}")

# The linear regression equation is: y = θ₀ + θ₁ * x
print(f"\nLinear regression equation: y = {theta[0, 0]:.2f} + {theta[1, 0]:.2f} * x")

# 6. Plot the regression line on top of the scatter plot
print("\n=== Creating Final Plot with Regression Line ===")

# Create prediction points for smooth line
x_pred = np.linspace(x.min(), x.max(), 100)
# Create A matrix for predictions: A_pred = [1, x_pred]
A_pred = np.column_stack([np.ones(len(x_pred)), x_pred])
# Calculate predictions: y_pred = A_pred * θ
y_pred = A_pred @ theta
y_pred = y_pred.flatten()  # Convert to 1D array for plotting

# Create the final plot
plt.figure(figsize=(12, 8))

# Plot scatter points
plt.scatter(df['YearsExperience'], df['Salary'], color='blue', alpha=0.7, s=50, 
           label='Data points', zorder=5)

# Plot regression line
plt.plot(x_pred, y_pred, color='red', linewidth=2, 
         label=f'Linear Regression: y = {theta[0, 0]:.0f} + {theta[1, 0]:.0f}x')

plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs Years of Experience with Linear Regression')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Calculate some statistics
print("\n=== Model Statistics ===")

# Calculate predictions for actual data points
y_pred_actual = A @ theta
y_pred_actual = y_pred_actual.flatten()

# Calculate R-squared
ss_res = np.sum((y - y_pred_actual) ** 2)  # Sum of squares of residuals
ss_tot = np.sum((y - np.mean(y)) ** 2)     # Total sum of squares
r_squared = 1 - (ss_res / ss_tot)
print(f"R-squared: {r_squared:.4f}")

# Calculate Mean Squared Error
mse = np.mean((y - y_pred_actual) ** 2)
print(f"Mean Squared Error: {mse:.2f}")

# Calculate Root Mean Squared Error
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: ${rmse:.2f}")

print(f"\nFor someone with 5 years of experience, predicted salary: ${theta[0, 0] + theta[1, 0] * 5:.2f}")
print(f"For someone with 10 years of experience, predicted salary: ${theta[0, 0] + theta[1, 0] * 10:.2f}")