calculate_grades = int(input("Enter your mark"))

match calculate_grades:

     case grades if 90 <= grades <= 100:
               print ("Grade A - extraordinary")
     case grades if 80 <= grades  <= 89:
               print ("Grade B - Excellent")
     case grades if 70 <=grades   <= 79:
               print ("Grade C- Very Good")
     case grades if 60 <= grades  <= 69:
               print("Grade D - Good")
     case grades if 0 <= grades  <= 59:
               print("Grade F - Need focus")
     case _:
           print ( "Enter yor marks from 0 to 100 only")





             
