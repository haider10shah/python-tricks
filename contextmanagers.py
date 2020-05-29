# example of context manager
class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# rewriting the above class with context manager as

from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()


# another example of implementing a class with context managers
class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self.level

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('     ' * self.level + text)




if __name__ == '__main__':
    # standard pattern to open a file and write to it
    # automatically closes the file
    with open('hello.txt', 'w') as f:
        f.write('Hello World!')

    # another way to write the above code is
    f = open('hello.txt', 'w')
    try:
        f.write('Hello World!')
    finally:
        f.close()

    # with also typically used with threading to automatically release locks

    # in order to build your own context managers, you need to add __enter__ and __exit__ methods to an object
    # example usage
    with ManagedFile('hello.txt') as f:
        f.write('Hello World!')
        f.write('bye')

    # python calls __enter__ when execution enters the context of the with statement
    # when execution leaves the context again python calls __exit__ to free up the resource

    # contextlib is a built in module the provides more functionality
    # usage of generator based factory function

    with managed_file('hello.txt') as f:
        f.write('Hello World!')
        f.write('bye')

    # managed_file() is a generator that first acquires the resource
    # it temporarily suspends its own execution and yields the resource to be used by the caller
    # when the caller leaves with context, the generator continues to execute and executes remaining clean up

    #Indenter class usage
    with Indenter() as indent:
        indent.print('hi')
        with indent:
            print('hello')

