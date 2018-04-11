class Dog():
  def __init__(self, name):
    self.name = name
    self.ate = False
    self.walked = False  

  def __repr__(self):
    return "name: " + self.name + ", ate today: " + str(self.ate) + ", walked today: " + str(self.walked)

  def feed(self):
    self.ate = True

  def walk(self):
    self.walked = True

class DogCare():
  def __init__(self):
    self.dogs = []

  def report(self):
    report = ""
    numberOfDogs = len(self.dogs)
    print("\n===========================================\n              Dog report\n===========================================")
    if (numberOfDogs==0):
      print("You have no dogs yet")
    else:
      i = 1
      for dog in self.dogs:
        print(str(i) + ") " + str(dog))
        i+= 1
    print("\n")

  def add_dog(self,dog):
    self.dogs.append(dog)

  def get_dog(self,dogName):
    for dog in self.dogs:
      if (dog.name == dogName):
        return dog
    print("Error: there is no dog named " + dogName + " in your dog care!" )
    return None

if (__name__ == "__main__"):
  myDogCare = DogCare()
  myDogCare.report()

  myDogCare.add_dog(Dog('Hershey'))
  myDogCare.add_dog(Dog('Ginger'))
  myDogCare.report()

  # Try to find dog named Bob, should return error
  Bob = myDogCare.get_dog('Bob')
  
  # Feed Hershey, walk Ginger
  Hershey = myDogCare.get_dog('Hershey')
  Hershey.feed()
  myDogCare.get_dog('Ginger').walk()
  myDogCare.report()
  

