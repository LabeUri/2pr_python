def dict_to_tuples(dictionary):
    return [(key, value) for key, value in dictionary.items()]

sample_dict = {'a': 1, 'b': 2, 'c': 3}
tuple_list = dict_to_tuples(sample_dict)
print("Список кортежів, отриманий зі словника:")
print(tuple_list)
