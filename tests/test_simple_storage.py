from brownie import SimpleStorage, accounts

# testing is in 3 catagories
# Arrange Act Assert

# 1st test to check if starting value in retrieve is 0
def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


# 2nd test to check if the the updated value is stored correctly
def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    simple_storage.store(15, {"from": account})
    # Assert
    assert expected == simple_storage.retrieve()
