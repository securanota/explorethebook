#!/usr/bin/env python3
"""
Convert Zotero Better BibTeX JSON export to Hugo simple JSON bibliography format.
"""

import json
import sys
import os
from pathlib import Path

def extract_author_name(creators):
    """Extract and format the first author's name from Zotero creators."""
    if not creators:
        return "Unknown Author"
    
    for creator in creators:
        if creator.get('creatorType') in ['author', 'editor']:
            if 'name' in creator:
                # Single name field
                return creator['name']
            else:
                # Separate first/last name fields
                first = creator.get('firstName', '').strip()
                last = creator.get('lastName', '').strip()
                if first and last:
                    return f"{first} {last}"
                elif last:
                    return last
                elif first:
                    return first
    
    return "Unknown Author"

def extract_year(date_field):
    """Extract year from various Zotero date formats."""
    if not date_field:
        return None
    
    # Handle different date formats
    if isinstance(date_field, str):
        # Try to extract year from string like "2023-01-01" or "2023"
        year = date_field.split('-')[0].strip()
        if year.isdigit() and len(year) == 4:
            return year
    
    return None

def convert_zotero_to_simple_json(zotero_json_path, output_json_path):
    """Convert Zotero JSON export to Hugo simple JSON bibliography."""
    
    # Read Zotero JSON
    with open(zotero_json_path, 'r', encoding='utf-8') as f:
        zotero_data = json.load(f)
    
    # Convert to simple format
    simple_bibliography = {}
    
    for item in zotero_data:
        # Skip if no citation key
        if 'citationKey' not in item:
            print(f"Warning: Item '{item.get('title', 'Unknown')}' has no citation key, skipping")
            continue
            
        citation_key = item['citationKey']
        
        # Build simple entry
        entry = {
            'author': extract_author_name(item.get('creators', [])),
            'title': item.get('title', 'Unknown Title')
        }
        
        # Add year if available
        year = extract_year(item.get('date') or item.get('issued'))
        if year:
            entry['year'] = year
        
        # Add optional fields
        if item.get('publisher'):
            entry['publisher'] = item['publisher']
        
        if item.get('series') or item.get('seriesTitle'):
            entry['series'] = item.get('series') or item.get('seriesTitle')
        
        if item.get('ISBN'):
            entry['isbn'] = item['ISBN']
        
        if item.get('DOI'):
            entry['doi'] = item['DOI']
        
        if item.get('url'):
            entry['url'] = item['url']
        
        # Store in bibliography
        simple_bibliography[citation_key] = entry
    
    # Write output
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(simple_bibliography, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Converted {len(simple_bibliography)} sources")
    print(f"📝 Output written to: {output_json_path}")
    
    # Show sample entries
    if simple_bibliography:
        print("\n📋 Sample entries:")
        for i, (key, entry) in enumerate(simple_bibliography.items()):
            if i >= 3:  # Show only first 3
                break
            print(f"   {key}: {entry['author']} - {entry['title']} ({entry.get('year', 'no year')})")

def main():
    if len(sys.argv) != 3:
        print("Usage: python convert_zotero_simple.py <zotero_export.json> <output_bibliography.json>")
        print("\nSteps to use:")
        print("1. In Zotero, right-click your collection")
        print("2. Choose 'Export Collection'")
        print("3. Select 'Better BibTeX JSON' format")
        print("4. Save as 'zotero_export.json'")
        print("5. Run this script to convert to Hugo format")
        sys.exit(1)
    
    zotero_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(zotero_file):
        print(f"❌ Error: Zotero export file not found: {zotero_file}")
        sys.exit(1)
    
    # Create output directory if needed
    output_dir = Path(output_file).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        convert_zotero_to_simple_json(zotero_file, output_file)
        print(f"\n🎉 Conversion completed successfully!")
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()