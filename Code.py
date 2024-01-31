keys = ['a', 'b', 'c']
values = [1, 2, 3]

make_dict = dict(zip(keys, values))

make_dict.get(' ')
del make_dict
# for indexing ---make list--- list(make_dict.key()[ i ]
# for popint in dect : make_dict.popitem()

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Remove and return the value associated with the key 'b'
removed_value = my_dict.pop('b')

# Dicionary in Dictionary
outer_dict = {
    'key1': {'inner_key1': 'value1', 'inner_key2': 'value2'},
    'key2': {'inner_key3': 'value3', 'inner_key4': 'value4'},
    'key3': {'inner_key5': 'value5', 'inner_key6': 'value6'}
}

# Accessing values
print(outer_dict['key1']['inner_key1'])  # Output: 'value1'
print(outer_dict['key2']['inner_key4'])  # Output: 'value4'


