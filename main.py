class flight:

    def __init__(self, origin,destination,duration):
        self.origin=origin
        self.destination=destination
        self.duration=duration

def main():

    f=flight("Mumbai","Delhi",200)


    print(f.__dict__)
    print(f.origin)

    f.duration += 10

    print(f.__dict__)

if __name__ == "__main__":
    main()

