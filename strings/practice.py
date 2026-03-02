# name = input("Enter your Name: ")

# print(f"Good After Noon {name}")

letter = '''Dear <|Name|>, you are selected <|Date|> '''

print(letter.replace('<|Name|>', 'Shahzad').replace('<|Date|>', '24 Sep 2026'))