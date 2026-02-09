from decimal import Decimal, getcontext
from mpmath import mp
    
getcontext().prec = 100                         #set decimal precision to 100 to override native float precision

#using cylinder area formula 2(pi)r(r+h)
def TcalcAtPrecision(precision : int):          #truncated pi
    r = 10
    h = 20     

    mp.dps = precision+2                        #set pi precision
    pi = Decimal(str(mp.pi)[:-1])
    return 2*pi*r*(r*h)

def RcalcAtPrecision(precision : int):          #rounded off pi
    r = 10
    h = 20     

    mp.dps = precision+1                       #set pi precision
    return 2*mp.pi*r*(r*h)


print(f"truncated pi precision at 20: {TcalcAtPrecision(20)}")
print(f"truncated pi precision at 40: {TcalcAtPrecision(40)}")
print(f"truncated pi precision at 60: {TcalcAtPrecision(60)}")
print(f"truncated pi precision at 100: {TcalcAtPrecision(100)}\n")

print(f"rounded pi precision at 20: {RcalcAtPrecision(20)}")
print(f"rounded pi precision at 40: {RcalcAtPrecision(40)}")
print(f"rounded pi precision at 60: {RcalcAtPrecision(60)}")
print(f"rounded pi precision at 100: {RcalcAtPrecision(100)}\n")

print(f"difference of result with rounded and truncated pi at 20th decimal: {abs(RcalcAtPrecision(20)-TcalcAtPrecision(20))}")
print(f"difference of result with rounded and truncated pi at 40th decimal: {abs(RcalcAtPrecision(40)-TcalcAtPrecision(40))}")
print(f"difference of result with rounded and truncated pi at 60th decimal: {abs(RcalcAtPrecision(60)-TcalcAtPrecision(60))}")
print(f"difference of result with rounded and truncated pi at 100th decimal: {abs(RcalcAtPrecision(100)-TcalcAtPrecision(100))}")