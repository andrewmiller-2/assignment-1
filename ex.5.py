# --- Main Program ---

product_name_input = input("What's the product name? ")

processed_name = product_name_input.strip().lower()

match processed_name:
    case i if processed_name.startswith("tech"):
        category = "High Margin"
    
    case "electronics" | "gadget":
        category = "High Margin"
    case "clothing" | "apparel":
        category = "Medium Margin"
    case "food" | "grocery":
        category = "Low Margin"

    case i:
        category = "Uncategorized - Review Needed"

print(f"Product: {processed_name} | Category: {category}")