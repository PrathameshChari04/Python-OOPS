class flight:
    def __init__(self, origin,destination,duration):
        self.origin=origin
        self.destination=destination
        self.duration=duration

    def details(self):
        print(f"Origin : {self.origin}")
        print(f"Destination : {self.destination}")
        print(f"Duration : {self.duration}")

    def delay(self,amount):
        self.duration += amount

def main():

    f=flight("Goa","Mumabi",200)
    f2=flight("Delhi","Pune",300)

    f.details()
    f.delay(20)
    f2.details()

if __name__ == "__main__":
    main()