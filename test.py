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
        self.balances[sender] -= amount
        self.total_supply = total_liquidity - amount
        return eth_amount, token_amount

    def sell_eth_buy_token(self, eth):
        pass

    def sell_tokens_buy_eth(self, token):
        pass

    def print(self):
        print('-' * 10)
        print('balance       = ' + str(self.balance))
        print('token_reserve = ' + str(self.token_reserve))
        print('total_supply  = ' + str(self.total_supply))
        print(self.balances)

if __name__ == '__main__':
    uniswap = Uniswap()
    uniswap.add_liquidity(10, 200, "alice")
    uniswap.print()
    uniswap.add_liquidity(1, 20, "bob")
    uniswap.print()
    uniswap.add_liquidity(10, 200, "carol")
    uniswap.print()
    print(uniswap.remove_liquidity(10, "alice"))
    uniswap.print()


    
    
