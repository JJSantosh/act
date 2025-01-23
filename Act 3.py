n1=float(input("Enter the n1:"))
n2=float(input("Enter the n2:"))
while (n2!=0):
    t=n2
    n2=n1%n2
    n1=t
HCF=n1
print("HCF is:",HCF)