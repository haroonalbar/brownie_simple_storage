# import accounts to work with address and privatekey
from brownie import accounts


def deploy_simple_storage():
    # account = accounts[0]
    # print(account)

    # to work with the the account you created
    account = accounts.loadl("dog")


def main():
    deploy_simple_storage()
