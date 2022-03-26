# import accounts to work with address and privatekey
# import SimpleStorage contract
# import network to work with diffrent networks
from brownie import accounts, config, SimpleStorage, network


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallet"]["from_key"])


def deploy_simple_storage():
    account = get_account()
    # in brownie in transcation we have to specify the account we are transactining from
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transcation = simple_storage.store(15, {"from": account})
    transcation.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)
    # print(simple_storage)
    # print(account)

    # to work with the the account you created
    # account = accounts.load("dog")
    # print(account)
    # account = accounts.add(config["wallet"]["from_key"])
    # print(account)


def main():
    deploy_simple_storage()
