#example of a python inbuilt iterator
iterable_value = 'Hello World'
iterable_obj = iter(iterable_value)
 
while True:
    try:
 
        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:
 
        break