#!/bin/bash
set -e

echo "=============================================="
echo " LEVEL 8: ARWEAVE BLOCKWEAVE DEPLOYMENT"
echo "=============================================="

if [ -z "$ARWEAVE_WALLET_JSON" ]; then
    echo "ERROR: ARWEAVE_WALLET_JSON environment variable is not set."
    echo "Provide the absolute path to your Arweave wallet JSON file."
    exit 1
fi

if ! command -v arkb &> /dev/null; then
    echo "ERROR: 'arkb' is not installed."
    echo "Please install it via: npm install -g arkb"
    exit 1
fi

TARBALL="sovereign-canon-archive.tar.gz"
echo "[1/3] Packaging repository for deployment..."
# Exclude git, node_modules, and any existing tarball to keep it clean
tar -czf "$TARBALL" --exclude='.git' --exclude='node_modules' --exclude="$TARBALL" .
echo "Created: $TARBALL"

echo "[2/3] Calculating cost and deploying to Arweave..."
# Using arkb to deploy the tarball to the permaweb
arkb deploy "$TARBALL" --wallet "$ARWEAVE_WALLET_JSON" --tag-name "App-Name" --tag-value "Sovereign-Canon"

echo "[3/3] Deployment Complete"
echo "The payload is now physically etched into the blockweave for 200+ years."
