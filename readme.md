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
        brownie accounts list *to list accounts*
        brownie accounts delete name*to delete accounts*
