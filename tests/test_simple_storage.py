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
