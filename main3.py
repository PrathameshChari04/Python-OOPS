class Flight:

    counter = 1
    def __init__(self,origin,destination,duration):

        self.id = Flight.counter
        Flight.counter += 1

        self.passengers = []

        self.origin=origin
        self.destination=destination
        self.duration=duration

    def details(self):
        print(f"Origin : {self.origin}")
        print(f"Destination : {self.destination}")
        print(f"Duration : {self.duration}")

        print("Passengers :")
        for passenger in self.passengers:
            print(f"{passenger.name}")

    def delay(self,amount):
        self.duration += amount

    def add_passenger(self,p):
        self.passengers.append(p)
        p.flight_id=self.id

class Passenger:
    def __init__(self,name):
        self.name=name


def main():
    f1 = Flight("Delhi","Mumbai",200)
    f2 = Flight("Goa","Mumbai",100)

    rohit = Passenger("Rohit")
    om= Passenger("Om")
    aaya = Passenger("Aaya")

    f1.add_passenger(om)
    f1.add_passenger(aaya)
    f2.add_passenger(rohit)


    f1.details()
    f2.details()



if __name__ == "__main__":
    main()