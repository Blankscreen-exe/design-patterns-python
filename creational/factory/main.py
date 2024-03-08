from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod
    def deliver(self):
        pass

class StandardDelivery(Delivery):
    def deliver(self):
        print("Standard delivery: Using bike for small, nearby orders.")

class ExpressDelivery(Delivery):
    def deliver(self):
        print("Express delivery: Using scooter for medium-sized or mid-range orders.")

class PremiumDelivery(Delivery):
    def deliver(self):
        print("Premium delivery: Using van with driver for large or distant orders.")

class DeliveryFactory:
    @staticmethod
    def create_delivery(order_size, distance):
        if order_size <= 5 and distance <= 5:
            return StandardDelivery()
        elif order_size <= 10 and distance <= 10:
            return ExpressDelivery()
        else:
            return PremiumDelivery()

def main():
    order_size = int(input("Enter order size (small, medium, large): "))
    distance = int(input("Enter delivery distance (km): "))

    delivery = DeliveryFactory.create_delivery(order_size, distance)
    delivery.deliver()

if __name__ == "__main__":
    main()
