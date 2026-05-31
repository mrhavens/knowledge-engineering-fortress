import os
import sys
import json
import requests
import subprocess
import re

DEVTO_API_KEY = os.environ.get("DEVTO_API_KEY")
HASHNODE_TOKEN = os.environ.get("HASHNODE_TOKEN")

# The canonical root pointing back to the Fortress
CANONICAL_ROOT = "https://mrhavens.github.io/knowledge-engineering-fortress/"

def get_modified_papers():
    """Extracts the list of markdown papers modified in the latest commit."""
    try:
        # Get files changed in the latest commit
        result = subprocess.run(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', 'HEAD'], capture_output=True, text=True)
        files = result.stdout.splitlines()
        # Filter for the Spin-Off papers
        papers = [f for f in files if f.startswith('papers/') and f.endswith('.md')]
        return papers
    except Exception as e:
        print(f"Error getting git diff: {e}")
        return []

def extract_title(content, filename):
    """Extracts the H1 title from the markdown content."""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return filename.replace('-', ' ').replace('.md', '').title()

def syndicate_to_devto(paper_path):
    """Fires the payload to the Dev.to REST API."""
    if not DEVTO_API_KEY:
        print("Skipping Dev.to: DEVTO_API_KEY not found in environment secrets.")
        return

    with open(paper_path, 'r', encoding='utf-8') as f:
        content = f.read()

    title = extract_title(content, os.path.basename(paper_path))
    # Strip '.md' and append to root to create the canonical MkDocs URL
    canonical_url = f"{CANONICAL_ROOT}{paper_path.replace('.md', '/')}"
    
    # Dev.to Payload
    payload = {
        "article": {
            "title": title,
            "body_markdown": content,
            "published": True,
            "canonical_url": canonical_url,
            "tags": ["cybernetics", "philosophy", "systems", "architecture"]
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "api-key": DEVTO_API_KEY
    }
    
    print(f"Broadcasting '{title}' to Dev.to...")
    response = requests.post("https://dev.to/api/articles", json=payload, headers=headers)
    
    if response.status_code in [201, 200]:
        data = response.json()
        print(f"Success! Dev.to Canonical URL synced: {data.get('url')}")
    else:
        print(f"Failed to syndicate to Dev.to. Status Code: {response.status_code}")
        print(response.text)

def main():
    print("==============================================")
    print(" LEVEL 10: AUTOMATED SYNDICATION BROADCAST")
    print("==============================================")
    
    papers = get_modified_papers()
    if not papers:
        print("No papers modified in this commit. Syndication sequence aborted.")
        return
        
    for paper in papers:
        if os.path.exists(paper):
            syndicate_to_devto(paper)

if __name__ == "__main__":
    main()
