def format_greeting(name, title="Customer"):
    formatted_name = name.strip().title()

    if not formatted_name:
        return "Hello, Valued Customer!"

    first_name = formatted_name.split()[0]
    
    return f"Hello, {first_name} ({title})!"

full_name_input = input("What's your full name? ")

greeting = format_greeting(full_name_input)
print(greeting)