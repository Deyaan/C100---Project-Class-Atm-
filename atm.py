class atm(object):
    def __init__(self,card_number,pin):
        self.card_number=card_number
        self.pin=pin
        
    def CashWithdrawl(self):
        print("CashWithdrawl")
        
    def BalanceEnquiry (self):
        print("BalanceEnquiry ")
        
  
card=atm("123","789")        
print(card.card_number)              