import collections

class Uniswap:
    def __init__(self):
        self.balance = 0
        self.token_reserve = 0
        self.total_supply = 0
        self.balances = collections.defaultdict(float)

    def add_liquidity(self, eth, token, sender):
        self.balance += eth
        total_liquidity = self.total_supply
        if total_liquidity > 0:
            eth_reserve = self.balance - eth
            token_reserve = self.token_reserve
            token_amount = eth * (1.0 * token_reserve/eth_reserve) + 1
            self.token_reserve += token_amount
            liquidity_minted = eth * (1.0 * total_liquidity) / eth_reserve
            self.balances[sender] += liquidity_minted
            self.total_supply = total_liquidity + liquidity_minted
            return liquidity_minted
        else:
            token_amount = token
            initial_liquidity = self.balance
            self.total_supply = initial_liquidity
            self.balances[sender] = initial_liquidity
            self.token_reserve = token
            return initial_liquidity

    def remove_liquidity(self, amount, sender):
        total_liquidity = self.total_supply
        token_reserve = self.token_reserve
        eth_amount = amount * (1.0 * self.balance) / total_liquidity
        token_amount = amount * (1.0 * token_reserve) / total_liquidity
        self.balance -= eth_amount
        self.token_reserve -= token_amount
        self.balances[sender] -= amount
        self.total_supply = total_liquidity - amount
        return eth_amount, token_amount

    # fee goes from 0.0 to 1.0. 
    def sell_x_and_buy_y(self, x, x_reserve, y_reserve, fee = 0.01):
        k = x_reserve * y_reserve
        new_x = x_reserve + x
        new_y = k * 1.0/new_x
        y_to_give_sans_fees = y_reserve - new_y
        y_to_give = y_to_give_sans_fees * (1 - fee)
        y_reserve = y_reserve - y_to_give
        return y_to_give, new_x, y_reserve

    def sell_eth_buy_token(self, eth):
        token_to_give, new_eth_balance, new_token_reserve = self.sell_x_and_buy_y(eth, self.balance, self.token_reserve)
        self.balance = new_eth_balance
        self.token_reserve = new_token_reserve
        return token_to_give

    def sell_token_buy_eth(self, token):
        eth_to_give, new_token_reserve, new_eth_balance = self.sell_x_and_buy_y(token, self.token_reserve, self.balance)
        self.balance = new_eth_balance
        self.token_reserve = new_token_reserve
        return eth_to_give

    def print(self):
        print('-' * 10, 'Uniswap Internals', '-' * 10)
        print('balance       = ' + str(self.balance))
        print('token_reserve = ' + str(self.token_reserve))
        print('total_supply  = ' + str(self.total_supply))
        print(self.balances)
        print('-' * 10)

if __name__ == '__main__':
    uniswap = Uniswap()
    print("Alice added liquidity and got", uniswap.add_liquidity(10, 200, "alice"), "tokens")
    uniswap.print()
    print("Bob added liquidity and got", uniswap.add_liquidity(1, 20, "bob"), "tokens")
    uniswap.print()
    print("Carol added liquidity and got", uniswap.add_liquidity(3, 300, "carol"), "tokens")
    uniswap.print()
    print("ETH Bought for 10 tokens:", uniswap.sell_token_buy_eth(10))
    uniswap.print()
    print("Alice removed liquidity:", uniswap.remove_liquidity(10, "alice"))
    uniswap.print()



    
    
