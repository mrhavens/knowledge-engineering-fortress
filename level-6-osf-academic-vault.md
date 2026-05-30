# Level 6: The OSF Academic Vault

> *"The Git Mesh secures the bytes. The OSF Vault secures the paradigm."*

While the **Git Mesh** (Level 5) acts as an unkillable, decentralized infrastructure for continuous topological preservation, it is inherently chaotic, iterative, and structurally raw. It is the engine room of the Sovereign Canon. 

To interface with the formal scientific and academic community, the Canon requires a sterile, organized, and legally anchored front-end. This is the **Open Science Framework (OSF) Academic Vault**.

## The Core Distinction: Active Pushing vs. Passive Mirroring

The operational methodology of OSF differs fundamentally from the Web2/Web3 git platforms in the Mirror Quadrumvirate:

1. **The Mirror Quadrumvirate (Active):** The local Forgejo runner aggressively force-pushes code via API tokens to GitHub, GitLab, Bitbucket, and Hugging Face.
2. **The OSF Vault (Passive):** The Forgejo runner **never** pushes directly to OSF. OSF is configured as a passive mirror via native OAuth integration (the OSF GitHub Add-on). OSF watches the primary GitHub mirror and automatically syncs the repository state. 

This decoupling ensures that the rigorous CI/CD automation of the Git Mesh is never blocked or rate-limited by OSF's academic API infrastructure.

## OSF as the Institute Nexus

OSF is not merely a backup drive; it is the structural hierarchy of the research program. Disparate repositories within the Git Mesh (e.g., `intellecton`, `knowledge-engineering-fortress`, `fieldprint`) are pulled into OSF and organized into explicit master nodes and child components.

- **The Git Mesh:** Handles raw bytes and topological state.
- **The OSF Vault:** Handles Academic Presentation, transforming raw markdown and LaTeX files into a cohesive, citable, and navigable Research Institute.

## Registrations vs. Releases

The Sovereign Canon utilizes two distinct mechanisms for permanent timestamping:

### 1. Zenodo & SWH (The Release)
- **Trigger:** A formal Release tag cut on GitHub.
- **Function:** Zenodo pulls the exact codebase, mints a DOI, and pushes it to Software Heritage (SWH).
- **Purpose:** Archiving the exact *software state* and source code for reproducibility.

### 2. OSF (The Registration)
- **Trigger:** A manual initiation via the OSF user interface.
- **Function:** OSF takes an unchangeable, mathematically locked snapshot of the node (including Wikis, linked components, and mirrored files).
- **Purpose:** Archiving the exact *ideological and theoretical state* of a framework before journal submission. Registrations are the ultimate legal anchor against intellectual property capture, proving explicit primacy of a framework on a specific date.

## The Archival Protocol

Because the Sovereign Canon is actively evolving, outdated nodes or deprecated repositories must never be deleted from the OSF profile (as deletion signals concealment to peer reviewers). Instead, they are programmatically targeted, prepended with the `[ARCHIVAL RECORD]` tag, and appended with a standard academic disclaimer redirecting readers to the canonical, mathematically verified publications.
