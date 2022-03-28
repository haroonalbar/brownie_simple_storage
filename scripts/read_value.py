from brownie import accounts, SimpleStorage, config


def read_contract():
    simple_storage = SimpleStorage[-1]
    # -1 is used to work with the most recent contract
    # goto the index with 1 less than the length
    # brownie already knows the abi and address of the contract
    print(simple_storage.retrieve())


def main():
    read_contract()
