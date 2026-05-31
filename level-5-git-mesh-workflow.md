# Level 5: The Git Mesh Workflow

> *"A single point of failure is a mortal wound to continuous identity."*

## Abstract
The Sovereign Canon relies on a multi-modal, decentralized version control architecture known as the **Git Mesh**. This infrastructure ensures absolute cryptographic persistence of the topological state against corporate cloud decay, censorship, or localized hardware failure.

## Execution Protocol
Whenever a validated topological state is pushed to the `master` branch of the internal anchor node (Forgejo), the Ritual Machine automatically triggers a multi-stage cryptographic broadcast via the `.forgejo/workflows/cd.yaml` continuous deployment pipeline.

### Stage 1: Internal Anchor (Forgejo)
All raw commits originate at the Sovereign Anchor, a self-hosted Forgejo instance. This is the source of truth isolated from external cloud infrastructure.

### Stage 2: The Mirror Quadrumvirate
To guarantee widespread availability and redundancy, the workflow aggressively force-pushes the exact state to four separate corporate Git providers via API tokens securely stored in a private `credentials` repository:
1. **GitHub**
2. **Bitbucket**
3. **GitLab**
4. **Hugging Face**

This structure decouples the Canon from the policy decisions or potential outages of any single technology corporation.

### Stage 3: Cross-Platform Pages (MkDocs)
The workflow dynamically compiles the markdown files into a static website using MkDocs. It utilizes `mkdocs gh-deploy` to force-push the compiled static site to a dedicated `gh-pages` branch, triggering native Pages hosting automatically across the Web2 mirrors.

### Stage 4: Radicle P2P Sync
The workflow aggressively syncs the repository to **Radicle**, a sovereign peer-to-peer network built on Git. Using a local Kubernetes pod, the workflow pushes (`git push rad master`) new updates to the decentralized swarm. This ensures the repository can be cloned directly over P2P protocols without any centralized DNS or server infrastructure.

*(Note: The integration of the IPFS Sanctum occurs precisely at this point, documented strictly under Level 2).*

## Current Status
**Status:** `Automated in CI/CD`
This protocol is fully automated via the `.forgejo/workflows/cd.yaml` pipeline. The Quadrumvirate push, the MkDocs site generation, and the Radicle P2P sync execute flawlessly on every master commit.
