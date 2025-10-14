#!/usr/bin/env python3
"""
Convert Zotero Better BibTeX JSON export to Hugo bibliography YAML format.
"""

import json
import yaml
import sys
import os
from pathlib import Path

def convert_item_type(zotero_type):
    """Map Zotero item types to our bibliography categories."""
    type_mapping = {
        'book': 'systematic_theology',
        'bookSection': 'commentary',
        'journalArticle': 'journal_article',
        'conferencePaper': 'conference_paper',
        'thesis': 'thesis',
        'webpage': 'online_resource'
    }
    return type_mapping.get(zotero_type, 'systematic_theology')

def clean_author_name(creators):
    """Extract and format author names from Zotero creators."""
    if not creators:
        return "Unknown Author"
    
    authors = []
    for creator in creators:
        if creator.get('creatorType') in ['author', 'editor']:
            if 'name' in creator:
                authors.append(creator['name'])
            else:
                first = creator.get('firstName', '')
                last = creator.get('lastName', '')
                if first and last:
                    authors.append(f"{first} {last}")
                elif last:
                    authors.append(last)
    
    if len(authors) == 1:
        return authors[0]
    elif len(authors) == 2:
        return f"{authors[0]} and {authors[1]}"
    elif len(authors) > 2:
        return f"{authors[0]} et al."
    else:
        return "Unknown Author"

def convert_zotero_to_yaml(json_file_path, yaml_file_path):
    """Convert Zotero JSON export to Hugo YAML bibliography."""
    
    # Read Zotero JSON
    with open(json_file_path, 'r', encoding='utf-8') as f:
        zotero_data = json.load(f)
    
    # Convert to our format
    sources = {}
    
    for item in zotero_data:
        # Skip if no citation key
        if 'citationKey' not in item:
            continue
            
        citation_key = item['citationKey']
        
        # Extract fields
        source = {
            'type': convert_item_type(item.get('type', 'book')),
            'author': clean_author_name(item.get('creators', [])),
            'title': item.get('title', 'Unknown Title'),
            'year': item.get('date', '').split('-')[0] if item.get('date') else None
        }
        
        # Add optional fields if they exist
        if item.get('publisher'):
            source['publisher'] = item['publisher']
        
        if item.get('place'):
            source['city'] = item['place']
        
        if item.get('series'):
            source['series'] = item['series']
        
        if item.get('ISBN'):
            source['ISBN'] = item['ISBN']
        
        if item.get('DOI'):
            source['DOI'] = item['DOI']
        
        if item.get('url'):
            source['url'] = item['url']
        
        # Remove None values
        source = {k: v for k, v in source.items() if v is not None}
        
        sources[citation_key] = source
    
    # Create final structure
    bibliography = {'sources': sources}
    
    # Write YAML file
    with open(yaml_file_path, 'w', encoding='utf-8') as f:
        yaml.dump(bibliography, f, default_flow_style=False, allow_unicode=True, sort_keys=True)
    
    print(f"Converted {len(sources)} sources from {json_file_path} to {yaml_file_path}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python convert_zotero_to_yaml.py <input.json> <output.yaml>")
        print("Example: python convert_zotero_to_yaml.py zotero_export.json data/bibliography.yaml")
        sys.exit(1)
    
    json_file = sys.argv[1]
    yaml_file = sys.argv[2]
    
    if not os.path.exists(json_file):
        print(f"Error: Input file {json_file} not found!")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    output_dir = Path(yaml_file).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    convert_zotero_to_yaml(json_file, yaml_file)

if __name__ == "__main__":
    main()