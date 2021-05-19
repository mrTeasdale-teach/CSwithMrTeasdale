#check digit program
#calculates check digit for a 5-character code
#to create a 6-digit product code
productCode = []
weight = 6
weightedSum = 0
productCode = input("Enter product code without check digit: ")

for number in range (5):

     print(productCode[number])
     weightedDigit = int(productCode[number]) * weight
     print("weighted digit = ",weightedDigit)
     weightedSum = weightedSum + weightedDigit
     weight = weight - 1
     print("weightedSum",weightedSum,"weight",weight)
 
#ENDFOR

remainder = weightedSum % 10
if remainder == 0:
    checkDigit = 0
else:
    checkDigit = 10 - remainder
#ENDIF
        
productCode = productCode + str(checkDigit)
print ("Product code = ",productCode)



#To check a product code is valid:
print("This program checks that a product code is valid")

productCode = []
weight = 6
weightedSum = 0
productCode = input("Enter product code, including check digit: ")

for number in range (6):

 print(productCode[number])
 weightedDigit = int(productCode[number]) * weight
 print("weighted digit = ",weightedDigit)
 weightedSum = weightedSum + weightedDigit
 weight = weight - 1
#ENDFOR    
remainder = weightedSum % 10

print ("Remainder = ",remainder)
if remainder == 0:
    print("Product code is valid")
else:
    print ("Product code is invalid")