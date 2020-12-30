# Coinbase Commerce External Wallet Tool

### This tool helps to derive and find the addresses and keys of a seed used by Coinbase Commerce
This was made in response to the lack of support provided by Coinbase and the development team.

For other questions on support, contact [Coinbase](https://help.coinbase.com/).

## WARNING: USE THIS SCRIPT AT YOUR OWN RISK

While not initially configured to handle wallets with funds (default is random), enter your real seed phrase at your own risk!
The reccomended configuration for using this script is on a cold (offline) [Tails](https://tails.boum.org/) boot or equivalent. 
Be aware that any machine you type your seed into may be compromised and **all precautions should be taken** to minimize this risk. 

The writer of this script is not liable for the loss of funds as a result of the use of this script.

## Requirements

To run this you'll need a Python 3 environment with the following packages included. I used Python 3.7 I reccomend using [conda](https://docs.conda.io/en/latest/) for managing the install and versioning.

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

## Ongoing Work

This script is a work in progress. The list below include the upcoming features that I will add. Depending on community response I may add other features:

1. Scanning generated addresses for funds: Not every address that Coinbase Commerce generates is used (due to incomplete or unused charges). Therefore it is important to know which addresses to import to withdraw your funds. I've already written a script that scans a list of addresses for funds, but would like to make it simpler and find a blockchain API that is not rate limited. I'll include it later. 
2. Multi-currency support (LTC is currency also broken by the derivation path change, ETH could follow).
3. Remove/include dependencies for convinience (Make it easier to use on an offline system). 
4. Include basic protection on exported files. 

Please reach out for feedback on which features your care about most. 

## Contributions

I obviously am doing this because I am fed up with Coinbase, but if you'd like to tip me some shitcoins you have lying around, it would definitely make my day. :) 
BTC: 1L1rwapFYPbDie4sAQ24v8fbdtAWCcGmQ8

