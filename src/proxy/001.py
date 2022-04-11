class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f'Car is being driven by {self.driver}')

# Say for example that you want to modify the drive() method so it has extra functionality, like checking driver's age before allowing the driver to drive.
# For this end you build a Proxy
class CarProxy:
    def __init__(self, driver: 'Driver'):
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print('Driver too young')

class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} whom is {self.age}yo'


if __name__ == '__main__':
    driver = Driver('Jane', 15)
    car = Car(driver)
    car.drive()  # this driver is too young

    driver = Driver('Jane', 16)
    car = CarProxy(driver)
    car.drive() # this driver should be able to drive

    driver = Driver('Jane', 15)
    car = CarProxy(driver)
    car.drive() # this driver is too young