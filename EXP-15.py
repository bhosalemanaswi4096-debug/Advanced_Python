
import gc
import tracemalloc

# Start tracking memory
tracemalloc.start()

def create_objects():
    objects = []
    for i in range(1000):
        obj = []
        obj.append(obj)  # Create a reference cycle
        objects.append(obj)
    return objects

# Initial memory usage
gc.collect()
before = tracemalloc.get_traced_memory()[0]
print("Memory before creating objects:", before, "bytes")

# Create objects
objects = create_objects()
print("Objects created:", len(objects))

# Delete references to objects
del objects

# Memory before garbage collection
before_gc = tracemalloc.get_traced_memory()[0]
print("Memory before garbage collection:", before_gc, "bytes")

# Manually collect garbage
collected = gc.collect()
print("Garbage collected:", collected, "objects")

# Memory after garbage collection
after_gc = tracemalloc.get_traced_memory()[0]
print("Memory after garbage collection:", after_gc, "bytes")

tracemalloc.stop()
