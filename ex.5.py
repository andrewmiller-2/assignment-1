# --- Main Program ---

# Prompt the user for the product name
product_name_input = input("What's the product name? ")

# .strip() removes leading and trailing whitespace.
# .lower() converts the entire string to lowercase for case-insensitive matching.
processed_name = product_name_input.strip().lower()

# The match statement correctly categorizes the product.
match processed_name:
    # This case now specifically checks if the name starts with "tech".
    # This is a wildcard `_` with a specific `if` guard.
    case i if processed_name.startswith("tech"):
        category = "High Margin"
    
    # These cases handle specific keywords for other categories.
    case "electronics" | "gadget":
        category = "High Margin"
    case "clothing" | "apparel":
        category = "Medium Margin"
    case "food" | "grocery":
        category = "Low Margin"

    # The underscore (_) is a wildcard pattern that acts as a default or 'else' case.
    case i:
        category = "Uncategorized - Review Needed"

# Print the final output, showing both the processed name and the assigned category.
print(f"Product: {processed_name} | Category: {category}")