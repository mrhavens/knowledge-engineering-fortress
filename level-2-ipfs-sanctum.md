# Level 2: The IPFS Sanctum

To guarantee that research and theory remain untampered by future corporate models or link rot, knowledge must be cryptographically pinned.

## Core Principle
If the content is mutable, the history can be rewritten. Sovereign Knowledge Engineering demands content-addressing.

## Implementation Standard
All codebases, ontologies, and research papers must automatically deploy to the InterPlanetary File System (IPFS) upon modification.

1. **GitOps Trigger**: A native CI runner intercepts every push to `master`.
2. **Hashing**: The repository is compressed and hashed via `ipfs add`.
3. **Immutable CID**: A Content Identifier (CID) is generated. This CID represents the absolute mathematical state of the research at that exact timestamp. It cannot be altered without the CID changing.

The IPFS Sanctum acts as the final anchor of TRUTH.
