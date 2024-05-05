bill_amount=int(input())
if(bill_amount<10000):
    print("no discount")
elif(bill_amount>=10000 and bill_amount<25000):
    print("10% of discount")
    discount_price=0.1*bill_amount
    final_bill_amount=bill_amount-discount_price
    print(final_bill_amount)
elif(bill_amount>=25000 and bill_amount<50000):
    print("30% of discont")
    discount_price=0.3*bill_amount
    final_bill_amount=bill_amount-discount_price
    print(final_bill_amount)
else:
    print("50% discont")
    
    discount_price=0.5*bill_amount
    final_bill_amount=bill_amount-discount_price
    print(final_bill_amount)
