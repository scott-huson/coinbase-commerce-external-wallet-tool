
import binascii
from bip_utils import Bip39EntropyGenerator, Bip39MnemonicGenerator, Bip39WordsNum, Bip39EntropyBitLen, Bip39SeedGenerator, Bip32, Bip44, Bip44Coins, Bip44Changes, P2PKH, P2SH, P2WPKH
from bitcoinutils.setup import setup
from bitcoinutils.script import Script
from bitcoinutils.keys import P2wpkhAddress, P2wshAddress, P2shAddress, PrivateKey, PublicKey

# Arguments
verbose = True # Print out the generated addresses in the console in addition to saving them.
privates = False # Generate individual private keys and save them WARNING (make sure no one is looking)
number = 50 # Number of addresses to generate
output_dest = "ExportKeys.csv" # Default place for saving the keys
compare = "" # If you want to look for a certain address put it here

# WARNING!!! LEAVE THIS BLANK UNTIL ON A COLD MACHINE!
mnemonic_phrase = ""

def generate():
  # Tells the library what network we are using
  setup() 

  if not mnemonic_phrase:
    # Generate mnemonic from random 192-bit entropy
    entropy_bytes = Bip39EntropyGenerator(Bip39EntropyBitLen.BIT_LEN_192).Generate() 
    mnemonic = Bip39MnemonicGenerator.FromEntropy(entropy_bytes)
    print("Generated random mnemonic:\n"+mnemonic)
  else: 
    print("Using included mnemonic.")
    mnemonic = mnemonic_phrase
  
  # Get seed bytes from mnemonic
  seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
  bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN) # Could add in multi currency support
  
  # Derive account 0 for Bitcoin: m/44'/0'/0'
  bip44_acc = bip44_mst.Purpose() \
                      .Coin()    \
                      .Account(0)

  # Derive the external chain: m/44'/0'/0'/0
  bip44_change = bip44_acc.Change(Bip44Changes.CHAIN_EXT)
  
  with open(output_dest, 'w') as output_file: # Open the output file
    output_file.write("address, public_key" + (", private_key" if privates else "") + "\n")
    # Go through each address
    for i in range(number):
      bip44_addr = bip44_change.AddressIndex(i)
        
      # create segwit address
      addr3 = PrivateKey.from_wif(bip44_addr.PrivateKey().ToWif()).get_public_key().get_segwit_address()
      # wrap in P2SH address
      addr4 = P2shAddress.from_script(addr3.to_script_pub_key())
      
      if addr4.to_string() == compare: 
        print("Found it!")
        print("Path: m/44'/0'/0'/0/"+str(i))
        break
      #print("P2SH(P2WPKH):", addr4.to_string())
      if (i%int(number/10)) == 0:
        print('Finished {}'.format(i))
      
      out = "{0}, {1}".format(addr4.to_string(), bip44_addr.PublicKey().ToExtended()) # Public addresses not including private
      if (privates): # Include the private keys
        out = "{0}, {1}, {2}".format(addr4.to_string(), bip44_addr.PublicKey().ToExtended(), bip44_addr.PrivateKey().ToExtended())
        #bip44_addr.PublicKey().ToAddress() # This is the regular address (not P2SH(P2WPKH))
      
      # Print extended keys and address
      if (verbose):
        print(out)
      
      output_file.write(out+"\n")
      
    

if __name__ == "__main__":
  generate()


