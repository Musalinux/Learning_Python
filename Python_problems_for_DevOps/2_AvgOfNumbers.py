def collect_input(totalNumbers):
      print ("Please enter", totalNumbers, "numbers, and I will calculate the average for you!")
      for i in range (0, totalNumbers):
          ele = float(input())
          mylist.append(ele)

def calculate_average():
    total = 0
    for i in range (0, len(mylist)):
        total = total + mylist[i]
    return (total/totalNumbers)

mylist = []
totalNumbers = int(input("Average of how many numbers?\n "))
collect_input(totalNumbers)

average = calculate_average()
print (f"Average of the {totalNumbers} numbers is {average}")