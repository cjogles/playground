people = ["Abe", "Bill", "Charles", "Dolly", "David", "Evelyn", "Frank", "Gunther"]

# comp for names that start with D
start_d = [x for x in people if x.startswith("D")]
print(start_d)
# comp for names that end in Y
end_y = [x for x in people if x.endswith("y")]
print(end_y)
# comp for names that start with B through D
start_b_through_d = [x for x in people if x.startswith("B") or x.startswith("C") or x.startswith("D")]
print(start_b_through_d)
# comp for names but in uppercase
uppercase_names = [x.upper() for x in people]
print(uppercase_names)