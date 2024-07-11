from web3 import Web3
from solcx import compile_standard, install_solc

# Install specific Solidity compiler version
install_solc('0.8.0')

# Solidity source code
with open('src/blockchain/contracts/FakeProfileVerification.sol', 'r') as file:
    source_code = file.read()

# Compile contract
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "FakeProfileVerification.sol": {
            "content": source_code
        }
    },
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
            }
        }
    }
}, solc_version='0.8.0')

# Connect to local Ethereum node
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.eth.default_account = w3.eth.accounts[0]

# Deploy contract
bytecode = compiled_sol['contracts']['FakeProfileVerification.sol']['FakeProfileVerification']['evm']['bytecode']['object']
abi = compiled_sol['contracts']['FakeProfileVerification.sol']['FakeProfileVerification']['abi']

FakeProfileVerification = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = FakeProfileVerification.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f'Contract deployed at address: {tx_receipt.contractAddress}')
