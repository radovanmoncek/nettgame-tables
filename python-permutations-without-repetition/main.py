from random import randrange


def main():

    print("permutations calculator launched")

    inputValue = input("Input a value to calculate possible permutations of: ")

    inputValue = [char for char in inputValue]

    for i in inputValue:

        if inputValue.count(i) > 1:

            print("input value must not contain duplicite items")

            exit()

    def factorial(value):
        
        if value == 0: 

            return 1 

        else:
            
            return value * factorial((value - 1)) #check how exactly does it work

    def permutationsFor(list):

        return factorial(len(list))

    def getPermutationsWithoutRepetition(list, permutationsCount):
      
      knownConmbs = []
  
      permutation = ""

      index = 0

      while len(knownConmbs) != permutationsCount:

        for i in range(len(list)):
              
            permutation += list[i]

            if len(permutation) == len(list):
              
              break

        if (knownConmbs.count(permutation) == 0):

            knownConmbs.append(permutation)

            print("permutation found! " + permutation)

        if index > len(list): index = 0   

        list.insert(index, list.pop()) 

        index += 1

        permutation = ""

      return permutationsCount

    print("Resolving all possible permutations!")

    getResult = str(getPermutationsWithoutRepetition(inputValue, permutationsFor(inputValue)))

    if int(getResult) == 1:

        print(("Your value can be sorted in " + getResult + " different way (" + getResult + "!)"))

    else:

        print(("Your value can be sorted in " + getResult + " different ways (" + getResult + "!)")) 

if __name__ == "__main__":

    main()