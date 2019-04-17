import sys



def get_size(*ptrs):
    total_size = 0
    print('* MEMORY USAGE INFORMATION')
    print('FOR OBJECTS:', ptrs)


    for o in ptrs:
        print('object', o)
        print('Checking object contains', sys.getsizeof(o), 'of type',str(type(o)),' with size', sys.getsizeof(o))
        total_size += sys.getsizeof(o)

        if hasattr(o, '__iter__'):
            if hasattr(o, 'items'):
                for item, val in o.items():
                    print(f'Checking object contains {sys.getsizeof(o)} of type {str(type(o))} with size {sys.getsizeof(item)}')
                    total_size += sys.getsizeof(item)
                    if hasattr(item, '__iter__'):
                        print('WARNING. Has deeper level!')

            elif not isinstance(o, str):
                for item in o:
                    print(f'Checking object contains {sys.getsizeof(o)} of type {str(type(o))} with size {sys.getsizeof(item)}')
                    total_size += sys.getsizeof(item)
                    if hasattr(item, '__iter__'):
                        print('WARNING. Has deeper level!')

    print('* TOTAL MEMORY USED:',  total_size)
