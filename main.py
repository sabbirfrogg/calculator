#calculator

#add
def add(n1, n2):
  return n1+n2
#subtract
def subtract(n1,n2):
  return n1 -n2
#multiply
def multiply(n1, n2):
  return n1*n2
  #devide
def devide(n1,n2):
  return n1/n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : devide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second nubmber?: "))

for symbol in operations:
  print(symbol)

operation_symbol = input("Pick an operation symbol from the line above: ")

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")