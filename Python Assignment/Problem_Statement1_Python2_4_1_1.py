from pip._vendor.distlib.compat import raw_input


class Triangle:

      def __init__(self,side1=0,side2=0,side3=0):
          """ Initializes the sides to zero"""
          self.side1 = side1
          self.side2 = side2
          self.side3 = side3
          self.perimeter = (self.side1 + self.side2 + self.side3)
          if ((self.side1 == 0) or (self.side2 == 0) or (self.side3 == 0)):
               self.setSides()

      def getSide1(self):
          return self.side1

      def getSide2(self):
          return self.side2

      def getSide3(self):
          return self.side3

      def setSides(self):
        print("Consider a triangle with three sides")

        try:
            self.side1 = float(raw_input("Enter first integer as the first side of the triangle ? "))
            self.side2 = float(raw_input("Enter second integer as the second side of the triangle ? "))
            self.side3 = float(raw_input("Enter third integer as the third side of the triangle ? "))

        except ValueError:
            print("You must have entered a non numeric value for one of the sides")

        else:
            self.perimeter = float(self.side1 + self.side2 + self.side3)
            self.validateTriangle(self.side1, self.side2, self.side3)


      def validateTriangle(self,side1,side2,side3):
          if (side1 <= (side2 + side3)):
              print("The first side is less than the sum of the second and third side")
              if ( side2 <= (side1 + side3)):
                  print("The second side is less than the sum of the first and third side")
                  if (side3 <= (side1 + side2)):
                     print("The third side is less than the sum of the first and second side")
                     print("This can be a valid triangle")
                     return
                  else:
                     print("This combination of numbers cannot represent a triangle \n")
                     self.__init__()
              else:
                   print("This combination of numbers cannot represent a triangle \n")
                   self.__init__()
          else:
              print("This combination of numbers cannot represent a triangle \n")
              self.__init__()

class derivedTriangle(Triangle):
         
      def __init__(self,*args,**kwargs):
          super(derivedTriangle,self).__init__(*args,**kwargs)
          self.semi_perimeter = (super(derivedTriangle,self).getSide1()+super(derivedTriangle,self).getSide2()+super(derivedTriangle,self).getSide3())/2
          self.difference1 = self.semi_perimeter - super(derivedTriangle,self).getSide1()
          self.difference2 = self.semi_perimeter - super(derivedTriangle,self).getSide2()
          self.difference3 = self.semi_perimeter - super(derivedTriangle,self).getSide3()
          self.area = 0.0
          print(self.difference3)
          print(self.difference2)
          print(self.difference1)

      def printArea(self):
           if (self.difference1 > 0):
               if (self.difference2 > 0):
                   if (self.difference3 > 0):
                       self.area = (self.semi_perimeter * (self.difference1) * (self.difference2) * (self.difference3))
                       self.area = self.area ** 0.5

           return self.area


dt1 = derivedTriangle(3,4,5)
area = dt1.printArea()
print("Area of the triangle is \t")
print (area)

dt2 = derivedTriangle()
area = dt2.printArea()
print("Area of the triangle is \t")
print (area)
