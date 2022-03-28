**Brownie**
    install
        python3 -m pip install --user pipx
        python3 -m pipx ensurepath
        reopen terminal
        pipx install eth-brownie *for some reason pipx is not recognized*
        python3 -m pipx install eth-brownie *so use this instedI* **worked but had to restart pc**
        **or go to env path of python3 and enter the appropriate path** 
        *it goes to all lower case for some reason*
        brownie --version *its not showing*
        pip install eth-brownie *dont know if it worked or didnt work*

        brownie --version
**worked after restarting pc**
        brownie
        brownie init => for creating new brownie project
        *didnt work because readme.md was there*delete readme after init create readme

contacts > SimpleStorage.sol
        brownie compile *for compiling the contract it .jason will be on build/contracts*

create a script deploy.py
        brownie run filename *for running scripts*

brownie set a local blockchain if dont define one
and you can use accounts to get the address

another way to add your accounts is through cmd.exe
        brownie accounts new name
                add metamask privatekey
                set password
        brownie accounts list *to list accounts*
        brownie accounts delete name*to delete accounts*

        this is one of best ways to store your keys

create .env and export private for testing 

to pull .env file directly from brownie
        create a file *brownie-config.yaml*
        brownie always looks for .yaml file to grab info about where 
        you are going to buid/deploy/grabthings
        dotenv: .env ////grabbing .env file
        wallets:
                from_key: ${PRIVATE_KEY} ////here ${} will add it into environment variable no need to import os

create test_simple_storage.py in test folder for automating tests
        brownie test *to test it*
        brownie test -k functionname *to test just one function*
        brownie test --pdb *if there is error we will be put into a python shell to find out whats wrong*
        brownie test -s *to print the lines of test*
        brownie networks list *for listing the networks*
                look at pytest doc for more brownie test stuff

connecting to a test net
        goto *infura* and copy *project id* from project settings
        export a new variable in .env for project id
        
        brownie run deploy.py --network rinkeby to run in rinkeby network through infura

create a new file read_value.py in scripts
        brownie run read_value.py --network rinkeby

we write scripts to do somting over and over again
we can use **brownie console** to do somting ad hoc (to do somthing special or immidiate)
and get into a shell where we can actually work with these contracts
        brownie console *it will have everything imported in it*

                SimpleStorage ([]   will get an array as result / there is no simpleStorage contract yet)
                        
                        //there is no contracts deployed because we are in a new local chain so we can do

                account = accounts[0]
                account *now we have an account to work with

                        \\everything in the script is imported to the console so we can copy any line of code from the script
                        \\and paste it to the console it will run just as we run in the script
                        \\So we can deploy the SimpleStorage contract just by pasting the code for deployment in the console
                        remove spaces to avoid errors

                SimpleStorage //we will see a contract 
                len(SimpleStorage) //will be 1
                SimpleStorage //deployed again
                len(SimpleStorage) //2
                         we can everything in python as well like
                print("Hello!")
                a = 1+1
                a //2

        console is a great way to intract with the contract