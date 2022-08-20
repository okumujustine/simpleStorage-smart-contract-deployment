from solcx import compile_standard, install_solc
import json
from web3 import Web3
from config import (
    provider_url,
    chain_id,
    my_address,
    private_key,
)

install_solc("0.6.0")


with open("./simpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# compile smart contract
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"simpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]},
            }
        },
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get the bytecode
bytecode = compiled_sol["contracts"]["simpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["simpleStorage.sol"]["SimpleStorage"]["abi"]

# network configuration section
w3 = Web3(Web3.HTTPProvider(provider_url))
chain_id = chain_id
my_address = my_address
private_key = private_key

# create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce = w3.eth.getTransactionCount(my_address)

# 1. build a transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce,
    }
)
# 2. sign transaction
signed_trx = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# 3. create/send raw transactiont to node
trx_hash = w3.eth.send_raw_transaction(signed_trx.rawTransaction)

# 4. wait for transaction confirmations
trx_receipt = w3.eth.wait_for_transaction_receipt(trx_hash)
print("contract deployed", trx_receipt)
