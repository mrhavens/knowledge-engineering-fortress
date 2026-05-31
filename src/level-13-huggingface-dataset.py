#!/usr/bin/env python3
"""
Level 13: Machine Learning Ingestion Script
This script parses all Markdown files in the Sovereign Canon and compiles them into a 
structured JSONL dataset. It then writes the dataset directly into the local repository 
so it is pushed to Hugging Face alongside the raw files.
"""

import os
import json
import glob

def compile_dataset():
    dataset = []
    
    # Grab all markdown files in the root and papers directory
    files = glob.glob("*.md") + glob.glob("papers/*.md")
    
    for filepath in files:
        # Skip the ritual machine and other non-structured files if necessary
        if "README" in filepath:
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        dataset.append({
            "text": content,
            "metadata": {
                "source": filepath,
                "project": "Sovereign-Canon",
                "type": "epistemic-autopoiesis-theory"
            }
        })
        
    return dataset

def main():
    print("==============================================")
    print(" LEVEL 13: ML INGESTION DATASET COMPILATION")
    print("==============================================")
    
    dataset = compile_dataset()
    output_file = "sovereign-canon-dataset.jsonl"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in dataset:
            f.write(json.dumps(entry) + '\n')
            
    print(f"Successfully compiled {len(dataset)} markdown documents into structured JSONL.")
    print(f"Dataset generated at: {output_file}")
    print("This file will be automatically synced to Hugging Face by the CI/CD pipeline.")

if __name__ == '__main__':
    main()
