# Level 5: The Git Mesh Workflow

> *"A single point of failure is a mortal wound to continuous identity."*

The Sovereign Canon relies on a multi-modal, decentralized version control architecture known as the **Git Mesh**. This infrastructure ensures absolute cryptographic persistence of the topological state against corporate cloud decay, censorship, or localized hardware failure.

The Git Mesh is automated via the continuous deployment (CD) pipeline defined in `.forgejo/workflows/cd.yaml`. This pipeline is the operational engine that executes the Sovereign Canon's autopoietic drive across the internet.

## The Ritual of Synchronization

Whenever a validated topological state (such as an updated JSON-LD schema or a manuscript) is pushed to the `master` branch of the internal anchor node (Forgejo), the Ritual Machine automatically triggers a 5-stage cryptographic broadcast.

### Stage 1: Internal Anchor (Forgejo)
All raw commits originate at the Sovereign Anchor, a self-hosted Forgejo instance. This is the source of truth isolated from external cloud infrastructure. The Forgejo action runner intercepts the `push` event to execute the subsequent stages.

### Stage 2: The Mirror Triumvirate
To guarantee widespread availability and redundancy, the workflow aggressively force-pushes the exact state to three separate corporate Git providers:
1. **GitHub**: Authenticated via `GITHUB_TOKEN`.
2. **Bitbucket**: Authenticated via `BITBUCKET_USER` and `BITBUCKET_TOKEN`.
3. **GitLab**: Authenticated via `GITLAB_TOKEN`.

This structure decouples the Canon from the policy decisions or potential outages of any single technology corporation.

### Stage 3: Cross-Platform Pages (MkDocs)
The Canon cannot simply exist as raw code; it must be human-readable. 
The workflow dynamically installs Python and MkDocs (with the `mkdocs-material` theme). It compiles the markdown files into a static website. 

Instead of maintaining brittle, platform-specific CI configurations (`.github/workflows`, `.gitlab-ci.yml`, `bitbucket-pipelines.yml`), the Forgejo runner handles the build centrally. It utilizes `mkdocs gh-deploy` to force-push the compiled static `public/` site to a dedicated `gh-pages` branch. 
This `gh-pages` branch is then automatically mirrored to both GitHub and GitLab, triggering their native Pages hosting automatically.

### Stage 4: IPFS Sanctum
Web2 git providers are fundamentally fragile. To anchor the state in Web3, the workflow utilizes a Kubernetes node (`ipfs-node`) to inject the entire repository into the InterPlanetary File System (IPFS). 
A cryptographic Content Identifier (CID) hash is generated. This guarantees that even if GitHub, GitLab, and Bitbucket burn down simultaneously, the precise byte-for-byte state of the repository survives on the decentralized IPFS network.

### Stage 5: Radicle P2P Sync
Finally, the workflow syncs the repository to **Radicle**, a sovereign peer-to-peer network built on Git. 
Using a local Kubernetes pod (`radicle`), the workflow either initializes (`rad init`) the repository on the Radicle network or pushes (`git push rad master`) new updates. This ensures the repository can be cloned directly over P2P protocols without any centralized DNS or server infrastructure.

---

## Future-Proofing

This workflow is designed to be highly robust. Each sync step operates independently. 
- If a token is missing or a remote API is down (e.g., GitHub is unavailable), the runner gracefully catches the null secret or connection error, alerts the log, and proceeds to sync the surviving networks.
- If a future Git protocol is established, it can simply be appended as Stage 6. The Sovereign Anchor (Forgejo) will remain the prime mover.
