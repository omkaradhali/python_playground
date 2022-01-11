def hello(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

if __name__ == "__main__":
    hello("world!!")
    # Output
    # world!!

    hello("world!!", 1, 2, 3)
    # output
    # world!!
    # (1,2,3)

    hello("world!!", 1, 2, 3, key1="key1", key2="key2")
    # output
    # world!!
    # (1,2,3)
    # {'key1': 'key1', 'key2': 'key2'}