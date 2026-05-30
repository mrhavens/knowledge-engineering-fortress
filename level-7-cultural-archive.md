# Level 7: The Cultural Archive

> *"The Git Mesh secures the bytes. The OSF Vault secures the paradigm. The Cultural Archive secures the memory."*

The Sovereign Canon utilizes multiple distinct topological layers for persistence:
- **Web2 / Git Mesh (Level 5):** Secures the raw source code bytes (GitHub, GitLab, Bitbucket).
- **Web3 / IPFS (Level 5):** Secures the decentralized hash and peer-to-peer distribution.
- **Academic / OSF & Zenodo (Level 6):** Secures the theoretical timeline, academic primacy, and DOI generation.

However, if corporate Git infrastructure fails or is censored, the *visual, human-readable presentation* of the Canon (e.g., the compiled MkDocs site) is lost to the surface web. The raw bytes on IPFS require technical literacy to reassemble. 

To solve this, the Sovereign Canon integrates **The Internet Archive (Archive.org & The Wayback Machine)** as the ultimate Web1 cultural preservation layer.

## Dual-Pronged Archival Strategy

The Forgejo runner integrates two automated subroutines to permanently cache the visual and raw outputs of the Canon into the Internet Archive.

### 1. The Automated Wayback Ping (Visual Preservation)
The Canon's primary interface is its static website, compiled via MkDocs and deployed to `gh-pages`.
To ensure the visual structure is preserved identically to how it was experienced by users on a given date:
- Immediately following a successful deployment to `gh-pages`, the CI/CD runner executes an automated API ping to the Wayback Machine `save` endpoint.
- **Mechanism:** `curl -s "https://web.archive.org/save/https://<your-domain>"`
- **Result:** The Wayback Machine instantly crawls and permanently caches the fully rendered HTML/CSS state of the theory.

### 2. The Archive.org Item Dump (Raw Artifacts)
While Zenodo handles formal academic software preservation, Archive.org serves as the public library, completely immune to academic gatekeeping or corporate cloud decay.
- When a major milestone is reached (e.g., the publication of a core physics preprint), the runner utilizes the official `ia` command-line tool.
- The pipeline zips the compiled LaTeX PDFs, the markdown source, and the schema topologies.
- **Mechanism:** `ia upload <item-name> <payload.zip> --metadata="title:The Sovereign Canon" --metadata="mediatype:texts"`
- **Result:** The raw artifacts are indexed globally by the Internet Archive, establishing an indestructible Web1 mirror. 

## The Absolute Perimeter
With the integration of Level 7, the Sovereign Canon achieves absolute topological persistence. The framework exists simultaneously as raw versioned code, a decentralized cryptographic hash, a registered academic theory, and a permanent cultural artifact.
