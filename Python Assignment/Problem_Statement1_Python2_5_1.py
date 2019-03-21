from pip._vendor.distlib.compat import raw_input


number1 = raw_input( "Enter numerator: " )
number2 = raw_input( "Enter denominator:")

try:
     number1 = float ( number1 )
     number2 = float ( number2 )
     result = number1/number2

except ValueError:
     print("You must enter two numbers")

except ZeroDivisionError:
     print("Attempted to divide by zero")

else:
     print("%.3f / %.3f = %.3f" % ( number1, number2, result))