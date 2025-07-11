from abc import ABC, abstractmethod
class Vehicle(ABC):
    SERVICE_THRESHOLD_KM = 10000
    def __init__(self, brand: str, fuel_capacity: float, fuel_efficiency: float):
        self._brand = brand
        self._fuel_capacity = fuel_capacity
        self._fuel_efficiency = fuel_efficiency
        self._fuel = 0.0
        self._km_run = 0.0
    def get_brand(self):
        return self._brand
    def get_fuel(self):
        return self._fuel
    def get_km_run(self):
        return self._km_run
    def refuel(self, amount: float):
        if self._fuel + amount > self._fuel_capacity:
            print(f"{self._brand}: Cannot refuel beyond fuel capacity.")
        else:
            self._fuel += amount
            print(f"{self._brand}: Refueled {amount}L. Current fuel: {self._fuel}L")
    def take_trip(self, distance: float):
        fuel_needed = distance / self._fuel_efficiency
        self._fuel -= fuel_needed
        self._km_run += distance
        print(f"{self._brand}: Trip of {distance} km completed.")
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def display_info(self):
        pass
    def needs_service(self):
        return self._km_run >= self.SERVICE_THRESHOLD_KM
class Car(Vehicle):
    def start(self):
        print(f"{self._brand} Car is starting...")
    def stop(self):
        print(f"{self._brand} Car is stopping...")
    def display_info(self):
        print(f"Car - Brand: {self._brand}, Fuel: {self._fuel}L, KM Run: {self._km_run}")
class Bike(Vehicle):
    def start(self):
        print(f"{self._brand} Bike is starting...")
    def stop(self):
        print(f"{self._brand} Bike is stopping...")
    def display_info(self):
        print(f"Bike - Brand: {self._brand}, Fuel: {self._fuel}L, KM Run: {self._km_run}")
class Truck(Vehicle):
    def start(self):
        print(f"{self._brand} Truck is starting...")
    def stop(self):
        print(f"{self._brand} Truck is stopping...")
    def display_info(self):
        print(f"Truck - Brand: {self._brand}, Fuel: {self._fuel}L, KM Run: {self._km_run}")
class FleetManager:
    def __init__(self):
        self.vehicles = []
    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)
    def summary(self):
        print("\n=== Fleet Summary ===")
        for vehicle in self.vehicles:
            vehicle.display_info()
            print(f"{vehicle.get_brand()} is a {vehicle.__class__.__name__}")
            print("Needs Service" if vehicle.needs_service() else " Does Not Need Service")
            print()
def main():
    fleet = FleetManager()
    toyota = Car("Toyota", 50, 10.6)
    yamaha = Bike("Yamaha", 15, 35)
    volvo = Truck("Volvo", 120, 5)
    fleet.add_vehicle(toyota)
    fleet.add_vehicle(yamaha)
    fleet.add_vehicle(volvo)
    toyota.start()
    toyota.refuel(30)
    toyota.take_trip(200)
    toyota.display_info()
    toyota.stop()
    toyota._km_run = 10200
    yamaha.start()
    yamaha.refuel(30)
    yamaha.display_info()
    yamaha.stop()
    volvo.start()
    volvo.refuel(30)
    volvo.take_trip(200)
    volvo.display_info()
    volvo.stop()
    fleet.summary()
if __name__ == "__main__":
    main()
