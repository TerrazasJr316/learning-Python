# maketrans and translate

example_maketrans = "Josue Terrazas1"
result_maketrans = example_maketrans.maketrans("1", " ")

print(example_maketrans.translate(result_maketrans))

example_two_maketrans = "Josue Terrazas1234"
example_num = "1234"
example_num_change = "    "
result_two_maketrans = example_maketrans.maketrans(example_num, example_num_change)

print(example_maketrans.translate(result_maketrans))