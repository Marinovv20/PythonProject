from autocomplete_model import AddressAutocompleteModel

dummy_addresses = [
    "221 Baker Street, London",
    "10 Downing Street, London",
    "1600 Pennsylvania Avenue, Washington DC",
    "742 Evergreen Terrace, Springfield",
    "12 Grimmauld Place, London",
    "31 Spooner Street, Quahog",
    "124 Conch Street, Bikini Bottom"
]

model = AddressAutocompleteModel(dummy_addresses)

query = "221 Bakr Stree"
suggestions = model.suggest(query)

print("Suggestions for:", query)
for suggestion in suggestions:
    print("-", suggestion)
