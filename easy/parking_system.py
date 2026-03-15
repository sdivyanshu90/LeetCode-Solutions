class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.empty = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.empty[carType - 1] > 0:
            self.empty[carType - 1] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

def test_parking_system():
    parkingSystem = ParkingSystem(1, 1, 0)

    # Test case 1
    print(parkingSystem.addCar(1))  # Expected output: True
    print(parkingSystem.addCar(2))  # Expected output: True
    print(parkingSystem.addCar(3))  # Expected output: False
    print(parkingSystem.addCar(1))  # Expected output: False

    # Test case 2
    parkingSystem = ParkingSystem(0, 0, 2)
    print(parkingSystem.addCar(1))  # Expected output: False
    print(parkingSystem.addCar(2))  # Expected output: False
    print(parkingSystem.addCar(3))  # Expected output: True
    print(parkingSystem.addCar(3))  # Expected output: True
    print(parkingSystem.addCar(3))  # Expected output: False

    # Test case 3
    parkingSystem = ParkingSystem(2, 3, 4)
    print(parkingSystem.addCar(1))  # Expected output: True
    print(parkingSystem.addCar(1))  # Expected output: True
    print(parkingSystem.addCar(1))  # Expected output: False
    print(parkingSystem.addCar(2))  # Expected output: True
    print(parkingSystem.addCar(2))  # Expected output: True
    print(parkingSystem.addCar(2))  # Expected output: True
    print(parkingSystem.addCar(2))  # Expected output: False
    print(parkingSystem.addCar(3))  # Expected output: True
    print(parkingSystem.addCar(3))  # Expected output: True
    print(parkingSystem.addCar(3))  # Expected output: True
    print(parkingSystem.addCar(3))  # Expected output: True
    print(parkingSystem.addCar(3))  # Expected output: False

    # Test case 4
    parkingSystem = ParkingSystem(1, 0, 0)
    print(parkingSystem.addCar(1))  # Expected output: True
    print(parkingSystem.addCar(1))  # Expected output: False
    print(parkingSystem.addCar(2))  # Expected output: False
    print(parkingSystem.addCar(3))  # Expected output: False

    # Test case 5
    parkingSystem = ParkingSystem(0, 1, 1)
    print(parkingSystem.addCar(1))  # Expected output: True
    print(parkingSystem.addCar(2))  # Expected output: True
    print(parkingSystem.addCar(2))  # Expected output: False
    print(parkingSystem.addCar(3))  # Expected output: True
    print(parkingSystem.addCar(3))  # Expected output: False

test_parking_system()