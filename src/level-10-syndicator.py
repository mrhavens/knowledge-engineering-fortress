import os
import sys
import json
import requests
import subprocess
import re

DEVTO_API_KEY = os.environ.get("DEVTO_API_KEY")
MINIMAX_API_KEY = os.environ.get("MINIMAX_API_KEY")

# The canonical root pointing back to the Fortress
CANONICAL_ROOT = "https://mrhavens.github.io/knowledge-engineering-fortress/"

def get_modified_papers():
    """Extracts the list of markdown papers modified in the latest commit."""
    try:
        result = subprocess.run(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', 'HEAD'], capture_output=True, text=True)
        files = result.stdout.splitlines()
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

def generate_llm_context(content, title):
    """Uses MiniMax API to generate a dynamic contextual backlink."""
    if not MINIMAX_API_KEY:
        print("No MiniMax API key found. Defaulting to static backlink.")
        return "This theory is part of the 14-level Epistemic Autopoiesis architecture. Read the fully integrated Sovereign Canon at:"
        
    print(f"Asking MiniMax to analyze '{title}' and generate a thoughtful context...")
    
    prompt = f"""You are an elite cybernetic systems architect. Read this academic paper excerpt and write a compelling, thoughtful 2-sentence call-to-action. The CTA must compel the reader to read the REST of the 14-level architectural Sovereign Canon. Do not use quotes or formatting. Be extremely profound and precise.
    
PAPER EXCERPT:
{content[:1500]}
"""

    try:
        response = requests.post(
            "https://api.minimax.chat/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {MINIMAX_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "abab6.5s-chat",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 150
            }
        )
        data = response.json()
        if 'choices' not in data:
            print(f"MiniMax API returned an error: {data}")
            return "This theory is part of the 14-level Epistemic Autopoiesis architecture. Read the fully integrated Sovereign Canon at:"
            
        context = data['choices'][0]['message']['content'].strip()
        return context
    except Exception as e:
        print(f"MiniMax API failed: {e}")
        return "This theory is part of the 14-level Epistemic Autopoiesis architecture. Read the fully integrated Sovereign Canon at:"

def syndicate_to_devto(paper_path):
    """Fires the payload to the Dev.to REST API."""
    if not DEVTO_API_KEY:
        print("Skipping Dev.to: DEVTO_API_KEY not found in environment secrets.")
        return

    with open(paper_path, 'r', encoding='utf-8') as f:
        content = f.read()

    title = extract_title(content, os.path.basename(paper_path))
    canonical_url = f"{CANONICAL_ROOT}{paper_path.replace('.md', '/')}"
    
    # Generate the Dynamic LLM Context
    llm_context = generate_llm_context(content, title)
    human_backlink = f"\n\n---\n\n*{llm_context} [{canonical_url}]({canonical_url})*"

    content_with_backlink = content + human_backlink
    
    # Dev.to Payload
    payload = {
        "article": {
            "title": title,
            "body_markdown": content_with_backlink,
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
    print(" LEVEL 10: AUTOMATED SYNDICATION BROADCAST (LLM HOOK)")
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
