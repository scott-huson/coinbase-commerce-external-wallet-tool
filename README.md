# Coinbase Commerce External Wallet Tool

### This tool helps to derive and find the addresses and keys of a seed used by Coinbase Commerce
This was made in response to the lack of support provided by Coinbase and the development team. 

## WARNING: USE THIS SCRIPT AT YOUR OWN RISK

While not initially configured to handle wallets with funds (default is random), enter your real seed phrase at your own risk!
The reccomended configuration for using this script is on a cold (offline) Tails boot or equivalent. 
Be aware that any machine you type your seed into may be compromised and **all precautions should be taken** to minimize this risk. 

## Requirements

To run this you'll need a Python 3 environment with the following packages included. I used Python 3.7 I reccomend using conda for managing the install and versioning.

 * bitcoinutils
 * bip-utils
 * binascii

## Deriving Addresses

To generate addresses using the new Coinbase Commerce derivation path, you can run the `deriveAddresses.py` script included.

```
python deriveAddresses.py
```

This derive script will generate a number of addresses. The configurable parts of the script are listed at the top of the file and below:

1. Number of addresses generated
2. What mnemonic to use (default is randomly generated)
3. Whether to include the private keys in the output csv (you can generate addresses at first to verify your funds) 
4. Print addresses to console
5. Search for a specific address (handy if you want to verify mnemonic)
6. Output file destination