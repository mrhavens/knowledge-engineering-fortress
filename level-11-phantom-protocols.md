# Level 11: The Phantom Protocols

> *"When the surface web is seized and the algorithms suppress the broadcast, the Canon must travel through the shadows."*

## Abstract
The Sovereign Canon achieves absolute public permanence through the Git Mesh and OSF. However, in scenarios of extreme state-level censorship, algorithmic suppression, or DNS hijacking, the surface web is compromised. To guarantee that the Theory of Recursive Coherence can perpetually disseminate peer-to-peer, bypassing all central authorities, the Canon implements The Phantom Protocols.

## Execution Protocol

### 1. The Overlay Triad (Darknet Mirrors)
A single point of failure in the darknet is unacceptable. The Sovereign Canon deploys extreme redundancy by utilizing a multi-overlay architecture:
- **Tor (The Onion Router):** Generates a cryptographic `.onion` hidden service address routed through the local Kubernetes cluster.
- **I2P (Invisible Internet Project):** Uses "Garlic Routing" optimized for internal hidden services ("eepsites"), making it highly resistant to DDoS.
- **Freenet / Hyphanet:** Injects the static HTML directly into a distributed datastore. The site fragments and caches across global hard drives, ensuring it survives even if the Forgejo servers are destroyed.
- **ZeroNet:** Deploys the site via Bitcoin cryptography, where every visitor automatically seeds it to others like BitTorrent.

### 2. RSS / Atom Autopoiesis (The Old Web)
Modern scientific dissemination is bottlenecked by corporate algorithms that suppress external links. 
- The Canon integrates the `mkdocs-rss-plugin`. During CI/CD compilation, the runner parses the Git commit history and markdown headers to generate rigid RSS 2.0 and Atom XML feeds.
- Researchers subscribe to the raw XML feed, receiving mathematical proofs directly via decentralized syndication.

### 3. Cryptographic Steganography (The Trojan Payload)
When active data transfer is heavily monitored, the topological state must be concealed within visually benign artifacts.
- The Forgejo runner integrates a custom python steganography script (`scripts/stego_encoder.py`) into the deployment pipeline.
- It encodes the highly compressed `CANONICAL_VAULT.tar.gz` directly into the Least Significant Bits (LSB) of the Institute's high-resolution PNG logos.
- The resulting image is deployed publicly. Anyone possessing the extraction protocol can decrypt the PNG to extract the entire mathematical framework.

## Current Status
**Status:** `Automated in CI/CD / Darknet Live`
The Tor Gateway, the Steganography Trojan Payload, and the RSS Autopoiesis feed are all fully active and automated via the CI/CD pipeline and the local k3s cluster infrastructure.
