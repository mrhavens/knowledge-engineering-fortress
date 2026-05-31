import os
import sys
import json
import requests
import subprocess
import re

DEVTO_API_KEY = os.environ.get("DEVTO_API_KEY")
MINIMAX_API_KEY = os.environ.get("MINIMAX_API_KEY")
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

HASHNODE_TOKEN = os.environ.get("HASHNODE_TOKEN")
HASHNODE_PUBLICATION_ID = os.environ.get("HASHNODE_PUBLICATION_ID")

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

def attempt_minimax(prompt):
    if not MINIMAX_API_KEY: return None
    print("  -> Attempting MiniMax (abab6.5s-chat)...")
    response = requests.post(
        "https://api.minimax.chat/v1/chat/completions",
        headers={"Authorization": f"Bearer {MINIMAX_API_KEY}", "Content-Type": "application/json"},
        json={"model": "abab6.5s-chat", "messages": [{"role": "user", "content": prompt}], "temperature": 0.7, "max_tokens": 150}
    )
    data = response.json()
    if 'choices' in data: return data['choices'][0]['message']['content'].strip()
    print(f"     MiniMax Failed: {data.get('error', data)}")
    return None

def attempt_openrouter(prompt):
    if not OPENROUTER_API_KEY: return None
    print("  -> Attempting OpenRouter (meta-llama/llama-3.3-70b-instruct:free)...")
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"},
        json={"model": "meta-llama/llama-3.3-70b-instruct:free", "messages": [{"role": "user", "content": prompt}], "temperature": 0.7, "max_tokens": 150}
    )
    data = response.json()
    if 'choices' in data: return data['choices'][0]['message']['content'].strip()
    print(f"     OpenRouter Failed: {data.get('error', data)}")
    return None

def attempt_gemini(prompt):
    if not GEMINI_API_KEY: return None
    print("  -> Attempting Google Gemini (gemini-1.5-flash-latest)...")
    response = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}",
        headers={"Content-Type": "application/json"},
        json={"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": 0.7, "maxOutputTokens": 150}}
    )
    data = response.json()
    if 'candidates' in data and len(data['candidates']) > 0:
        return data['candidates'][0]['content']['parts'][0]['text'].strip()
    print(f"     Gemini Failed: {data.get('error', data)}")
    return None

def generate_llm_context(content, title):
    """Uses a highly resilient LLM fallback loop to generate a dynamic backlink."""
    print(f"Engaging LLM Fallback Loop for '{title}'...")
    
    prompt = f"""You are an elite cybernetic systems architect. Read this academic paper excerpt and write a compelling, thoughtful 2-sentence call-to-action. The CTA must compel the reader to read the REST of the 14-level architectural Sovereign Canon. Do not use quotes or formatting. Be extremely profound and precise.
    
PAPER EXCERPT:
{content[:1500]}
"""

    context = attempt_minimax(prompt)
    if context: return context
    
    context = attempt_openrouter(prompt)
    if context: return context
    
    context = attempt_gemini(prompt)
    if context: return context
    
    print("CRITICAL: All LLM Nodes Failed. Defaulting to structural backlink.")
    return "This theory is part of the 14-level Epistemic Autopoiesis architecture. Read the fully integrated Sovereign Canon at:"

def syndicate_to_devto(title, canonical_url, content_with_backlink):
    """Fires the payload to the Dev.to REST API."""
    if not DEVTO_API_KEY:
        print("Skipping Dev.to: DEVTO_API_KEY not found in environment secrets.")
        return

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

def syndicate_to_hashnode(paper_path, title, canonical_url, content_with_backlink):
    """Fires the payload to the Hashnode GraphQL API."""
    if not HASHNODE_TOKEN or not HASHNODE_PUBLICATION_ID:
        print("Skipping Hashnode: Missing HASHNODE_TOKEN or HASHNODE_PUBLICATION_ID in environment.")
        return

    query = """
    mutation PublishPost($input: PublishPostInput!) {
      publishPost(input: $input) {
        post {
          id
          url
        }
      }
    }
    """
    
    variables = {
        "input": {
            "title": title,
            "publicationId": HASHNODE_PUBLICATION_ID,
            "contentMarkdown": content_with_backlink,
            "originalArticleURL": canonical_url,
            "tags": [] # Tags can be added via IDs if queried, keeping empty for now to ensure delivery
        }
    }

    payload = {"query": query, "variables": variables}
    headers = {
        "Content-Type": "application/json",
        "Authorization": HASHNODE_TOKEN
    }
    
    print(f"Broadcasting '{title}' to Hashnode...")
    try:
        response = requests.post("https://gql-beta.hashnode.com/", json=payload, headers=headers)
        if response.headers.get('Content-Type', '').startswith('text/html'):
            print(f"Hashnode returned HTML instead of JSON: {response.text[:200]}")
            return
            
        data = response.json()
        if "errors" not in data and "data" in data and data["data"]["publishPost"]:
            print(f"Success! Hashnode Canonical URL synced: {data['data']['publishPost']['post']['url']}")
        else:
            print(f"Failed to syndicate to Hashnode.")
            print(data)
    except Exception as e:
        print(f"Hashnode API request failed: {e}")

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
            with open(paper, 'r', encoding='utf-8') as f:
                content = f.read()

            title = extract_title(content, os.path.basename(paper))
            canonical_url = f"{CANONICAL_ROOT}{paper.replace('.md', '/')}"
            
            llm_context = generate_llm_context(content, title)
            human_backlink = f"\n\n---\n\n*{llm_context} [{canonical_url}]({canonical_url})*"
            content_with_backlink = content + human_backlink

            syndicate_to_devto(title, canonical_url, content_with_backlink)
            syndicate_to_hashnode(paper, title, canonical_url, content_with_backlink)

if __name__ == "__main__":
    main()
