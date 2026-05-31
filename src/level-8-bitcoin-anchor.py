#!/usr/bin/env python3
"""
Level 8: Bitcoin OP_RETURN Anchor
This script generates an irreversible cryptographic timestamp on the Bitcoin blockchain.
By default, it uses the Bitcoin Testnet (free). 
Set the environment variable BTC_NETWORK="mainnet" to etch this permanently into history.
"""

import os
import sys
import subprocess
try:
    from bit import PrivateKeyTestnet, PrivateKey
except ImportError:
    print("ERROR: The 'bit' library is required.")
    print("Please install it by running: pip install bit")
    sys.exit(1)

def get_git_hash():
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()
    except Exception as e:
        print(f"Error getting git hash: {e}")
        sys.exit(1)

def main():
    use_mainnet = os.environ.get('BTC_NETWORK', 'testnet').lower() == 'mainnet'
    pk_env = os.environ.get('BTC_PRIVATE_KEY')
    
    if not pk_env:
        print("ERROR: BTC_PRIVATE_KEY environment variable is not set.")
        print("To generate a testnet key for testing, use a testnet wallet generator.")
        sys.exit(1)
        
    git_hash = get_git_hash()
    payload = f"SOVEREIGN_CANON:{git_hash}"
    payload_bytes = payload.encode('utf-8')
    
    if len(payload_bytes) > 80:
        print("ERROR: Payload exceeds 80 bytes for OP_RETURN.")
        sys.exit(1)
        
    print("==============================================")
    print(" LEVEL 8: ON-CHAIN IMMUTABLE LEDGER INJECTION")
    print("==============================================")
    print(f"Anchoring payload : {payload}")
    print(f"Payload size      : {len(payload_bytes)} bytes\n")
    
    if use_mainnet:
        print("NETWORK: MAINNET (REAL FUNDS WILL BE USED)")
        print("WARNING: This action is mathematically irreversible.")
        key = PrivateKey(pk_env)
    else:
        print("NETWORK: TESTNET (Free Testnet Coins)")
        key = PrivateKeyTestnet(pk_env)
        
    print(f"Wallet Address    : {key.address}")
    balance = key.get_balance('btc')
    print(f"Current Balance   : {balance} BTC\n")
    
    if float(balance) == 0:
        print("ERROR: Wallet has no balance. Fund it before running.")
        sys.exit(1)
        
    print("Crafting and sending OP_RETURN transaction...")
    
    try:
        # The 'message' parameter natively creates an OP_RETURN output in the bit library
        txid = key.send([], message=payload_bytes)
        print("\n=== ANCHOR SUCCESSFUL ===")
        print(f"Transaction ID: {txid}")
        if use_mainnet:
            print(f"View on block explorer: https://mempool.space/tx/{txid}")
        else:
            print(f"View on block explorer: https://mempool.space/testnet/tx/{txid}")
    except Exception as e:
        print(f"Transaction failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
