# import accounts to work with address and privatekey
# import SimpleStorage contract
from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    # print(account)

    # to work with the the account you created
    # account = accounts.load("dog")
    # print(account)
    # account = accounts.add(config["wallet"]["from_key"])
    # print(account)


def main():
    deploy_simple_storage()
