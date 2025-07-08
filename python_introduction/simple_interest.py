# Define the variables
principal = 1000     # Principal amount in currency units
rate = 5             # Rate of interest (as percentage)
time = 3             # Time in years

# Convert rate to a decimal for calculation
rate_decimal = rate / 100

# Calculate simple interest
interest = principal * rate_decimal * time

# Print the result
print(f"Simple Interest for a principal of {principal} at a rate of {rate}% for {time} years is {interest}")
