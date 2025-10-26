class Bank:

    def __init__(self, balance: List[int]):
        self.bal = balance
        self.d = {i:self.bal[i] for i in range(len(self.bal))}

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1-1 in self.d and account2-1 in self.d and self.d[account1-1] >= money:
            self.bal[account1-1]-=money
            self.bal[account2-1]+=money
            self.d[account1-1]-=money
            self.d[account2-1]+=money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account-1 in self.d:
            self.bal[account-1]+=money
            self.d[account-1]+=money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        
        if account-1 in self.d and money<=self.d[account-1]:
            self.bal[account-1]-=money
            self.d[account-1]-=money
            return True
        return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)