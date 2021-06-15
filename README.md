# Cranky (CrankDB Python Driver)

Cranky is the database driver for CrankDB for python applications.

# Pre requisites
Setup [CrankDB](https://github.com/shreybatra/crankdb) and get it started.


# Documentation

```python
from cranky import Cranky

// setup a new connection

conn = Cranky()

// Cranky follows almost similar API methods as Crank CLI.

// You can set any type of JSON seriable value at any key.
conn.set(key, value)

// Get a key
conn.get(key)
// Returns a tuple (value, found: bool)

if found:
    print(value)

// delete a key
conn.delete(key)
// Returns a tuple (value, found: bool)

if found:
    print("Key successfully deleted.")

// Find multiple JSON documents using Find
conn.find({key: value}) //Applies a search and returns every key having JSON obj with key=value.
// Returns a tuple (value, found: bool)
```