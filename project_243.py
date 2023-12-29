from web3 import Web3

url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'

web3 = Web3(Web3.HTTPProvider(url))


latest_block = web3.eth.get_block('latest')
print('Block data:', latest_block)

block_transaction_count = web3.eth.get_block_transaction_count(18891784)

print('number of transactions happening in the block',block_transaction_count)

transaction_fee = web3.eth.fee_history(4,'latest',None)
print('transaction fee history in the block',transaction_fee)