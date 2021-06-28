# Cranky (CrankDB Python Driver)

Cranky is the database driver for CrankDB for python applications.

# Pre requisites
Setup [CrankDB](https://github.com/shreybatra/crankdb) and get it started.


# Documentation

```python
from cranky import Cranky

# setup a new connection

conn = Cranky(host="localhost", port="9876") # default values

# Cranky follows almost similar API methods as Crank CLI.

# You can set any type of JSON seriable value at any key.
conn.set(key, value)

# Get a key
conn.get(key)
# Returns a DataPacket object with `dataType` attribute and corresponding value field `jsonVal`, `stringVal`, etc.


# Find multiple JSON documents using Find
conn.find({key: value}) #Applies a search and returns every key having JSON obj with key=value.
# Returns a list of DataPackets with dataType and jsonVal attributes.

conn.find({}) # returns all JSON (dict) type key values.
```