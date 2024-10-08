# Pickle

The [`pickle`](https://docs.python.org/3/library/pickle.html) module in Python
is used for serializing and de-serializing Python objects. Serialization is the
process of converting an object into a representation that can be stored or
transmitted, and de-serialization is the process of converting a serialized
representation back into an object.

## Methods

The `pickle` module provides the following functions:

- `pickle.dump(obj, file, *, protocol=None, *, fix_imports=True)`: This
  function is used to serialize an object and write it to a file.

- `pickle.dumps(obj, *, protocol=None, *, fix_imports=True)`: This function is
  used to serialize an object and return the serialized representation as a
  bytes object.

- `pickle.load(file, *, fix_imports=True, encoding='ASCII', errors='strict')`:
  This function is used to de-serialize a serialized representation read from a
  file and return the corresponding object.

- `pickle.loads(data, *, fix_imports=True, encoding='ASCII', errors='strict')`:
  This function is used to de-serialize a serialized representation contained
  in a bytes object and return the corresponding object.

## Example

```python
import pickle

data = {'a': [1, 2.0, 3, 4+6j],
        'b': ('string', u'Unicode string'),
        'c': None}

# Serialize the object and write it to a file
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# De-serialize the object from the file and print it
with open('data.pkl', 'rb') as f:
    deserialized_data = pickle.load(f)

print(deserialized_data)
```
