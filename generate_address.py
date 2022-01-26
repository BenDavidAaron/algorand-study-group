from algosdk import account, mnemonic

def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print(mnemonic.from_private_key(private_key))

if __name__=="__main__":
    generate_algorand_keypair()

