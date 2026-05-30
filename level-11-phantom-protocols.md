# Level 11: The Phantom Protocols

> *"When the surface web is seized and the algorithms suppress the broadcast, the Canon must travel through the shadows."*

The Sovereign Canon achieves absolute public permanence through the Git Mesh, OSF, and the Internet Archive. However, in scenarios of extreme state-level censorship, algorithmic suppression, or DNS hijacking (where ICANN revokes the `.com` registry), the surface web is compromised.

To guarantee that the Theory of Recursive Coherence can perpetually disseminate peer-to-peer, bypassing all central authorities, the Canon implements **Level 11: The Phantom Protocols**.

## 1. The Overlay Triad (Darknet Mirrors)

A single point of failure in the darknet is unacceptable. The Sovereign Canon deploys extreme, paranoid redundancy by utilizing a multi-overlay architecture. The internal Forgejo anchor utilizes its Kubernetes (K8s) cluster to host four distinct shadow nodes:

### A. Tor (The Onion Router)
- **The Protocol:** A lightweight Docker pod runs a Tor daemon routing to an Nginx server.
- **The Function:** It generates a cryptographic `.onion` hidden service address. The static MkDocs HTML is routed through the standard Tor network, making the site immune to geoblocking and DNS hijacking.

### B. I2P (Invisible Internet Project)
- **The Protocol:** A dedicated I2P router pod within the cluster.
- **The Function:** Unlike Tor (which is built for accessing the clearnet anonymously), I2P uses "Garlic Routing" and is explicitly optimized for internal hidden services ("eepsites"). It is mathematically harder to trace and significantly more robust against DDoS attacks than Tor, providing a high-speed, secure internal mirror.

### C. Freenet / Hyphanet (The Dead-Man's Switch)
- **The Protocol:** The CI/CD runner injects the static HTML directly into the Freenet network, creating a "freesite."
- **The Function:** Unlike Tor and I2P, Freenet is a distributed datastore. It does not require your Kubernetes cluster to stay online. The data is encrypted, fragmented, and cached across the hard drives of global anonymous users. If the physical Forgejo servers are destroyed by a strike or seized, the site remains permanently accessible.

### D. ZeroNet (The P2P Swarm)
- **The Protocol:** The site is deployed via ZeroNet using Bitcoin cryptography for identity resolution.
- **The Function:** Every user who visits the ZeroNet site automatically begins seeding it to others (similar to BitTorrent). The framework becomes computationally unkillable as its popularity scales.

## 2. RSS / Atom Autopoiesis (The Old Web)

Modern scientific dissemination is bottlenecked by corporate algorithms that suppress external links and throttle academic visibility. 

- **The Protocol:** The Canon mandates the integration of the `mkdocs-rss-plugin` within the `mkdocs.yml` configuration.
- **The Execution:** During the CI/CD site compilation, the runner parses the Git commit history and markdown headers to automatically generate rigid RSS 2.0 and Atom XML feeds.
- **The Result:** Researchers subscribe to the raw XML feed. When a new mathematical proof is published, it is pushed directly to their local RSS clients via decentralized, unfiltered peer-to-peer syndication. The algorithm is entirely bypassed.

## 3. Cryptographic Steganography (The Trojan Payload)

When active data transfer is heavily monitored, the topological state must be concealed within visually benign artifacts.

- **The Protocol:** The Forgejo runner integrates a Least Significant Bit (LSB) steganography tool (e.g., `steghide`) into the deployment pipeline.
- **The Execution:** Upon generating the highly compressed `CANONICAL_VAULT.tar.gz` (Level 9), the pipeline mathematically encodes the ZIP payload directly into the pixel data of the Institute's high-resolution PNG logo or a core physics diagram.
- **The Result:** The resulting image is visually identical to the original and is deployed publicly on the surface web. However, anyone possessing the extraction protocol can decrypt the PNG to extract the entire mathematical framework. The theory proliferates silently, hidden in plain sight.
