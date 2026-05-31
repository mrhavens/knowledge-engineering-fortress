# Level 6: The OSF Academic Vault

> *"The Git Mesh secures the bytes. The OSF Vault secures the paradigm."*

## Abstract
While the Git Mesh (Level 5) acts as an unkillable, decentralized infrastructure for continuous topological preservation, it is inherently chaotic and iterative. To interface with the formal scientific and academic community, the Canon requires a sterile, organized, and legally anchored front-end. This is the **Open Science Framework (OSF) Academic Vault**.

## Execution Protocol
The operational methodology of OSF differs fundamentally from the Web2/Web3 git platforms. The Forgejo runner **never** pushes directly to OSF. OSF is configured as a passive mirror via native OAuth integration (the OSF GitHub Add-on). OSF watches the primary GitHub mirror and automatically syncs the repository state. 

### Zenodo & SWH (The Release)
- **Trigger:** A formal Release tag cut on GitHub.
- **Function:** Zenodo pulls the exact codebase, mints a DOI, and pushes it to Software Heritage (SWH).
- **Purpose:** Archiving the exact *software state* and source code for reproducibility.

### OSF (The Registration)
- **Trigger:** A manual initiation via the OSF user interface.
- **Function:** OSF takes an unchangeable, mathematically locked snapshot of the node.
- **Purpose:** Archiving the exact *ideological and theoretical state* of a framework before journal submission. Registrations are the ultimate legal anchor against intellectual property capture, proving explicit primacy of a framework on a specific date.

## Current Status
**Status:** `Manually Executed / Institutional Integration`
The automated mirroring is active, but the Registrations and Zenodo DOI minting are executed manually by the human anchor prior to formal mathematical publication.
