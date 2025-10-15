# Multi-Bibliography System Guide

## Overview

The site supports multiple bibliography files for efficient organization and management of references. This system allows you to organize sources by topic, testament, or book while maintaining fast performance.

## System Architecture

### Bibliography File Organization

**Recommended Structure:**
```
data/
├── nt-commentary.json          # New Testament commentaries
├── ot-commentary.json          # Old Testament commentaries  
├── systematic-theology.json    # Systematic theology works
├── biblical-theology.json      # Biblical theology sources
├── general-references.json     # Background, lexicons, etc.
├── church-history.json         # Historical sources
└── book-specific/
    ├── genesis.json           # Genesis-specific sources
    ├── philippians.json       # Philippians-specific sources
    └── romans.json            # Romans-specific sources
```

### Performance Guidelines

**Optimal Bibliography File Sizes:**
- **50-200 entries per file**: Excellent performance
- **200-500 entries per file**: Good performance  
- **500+ entries per file**: May slow down builds

## Usage in Commentary Files

### 1. Specify Bibliography Files in Front Matter

```yaml
---
title: "Philippians 1:1-11 - Greeting and Thanksgiving"
book: "Philippians"
bibliography_files: ["nt-commentary", "systematic-theology", "general-references"]
---
```

### 2. Use Citations Normally

```markdown
Paul's emphasis on partnership{{< note "fee1999:63-65" >}}{{< /note >}} reflects deep theological commitment.
```

### 3. Search Order

The system searches bibliography files in the order specified:
1. First file (`nt-commentary.json`)
2. Second file (`systematic-theology.json`)  
3. Third file (`general-references.json`)
4. Returns first match found

## Bibliography File Format

Each JSON file contains an array of sources:

```json
[
  {
    "id": "fee1999",
    "type": "commentary",
    "title": "Paul's Letter to the Philippians",
    "author": [
      {
        "family": "Fee",
        "given": "Gordon D."
      }
    ],
    "issued": {
      "date-parts": [
        [
          "1999"
        ]
      ]
    },
    "publisher": "Eerdmans",
    "collection-title": "New International Commentary on the New Testament"
  }
]
```

## Best Practices

### 1. Logical Grouping
- Group sources by topic or testament
- Keep related sources together
- Use descriptive file names

### 2. Citation Key Consistency
- Use author-year format: `fee1999`, `grudem1994`
- Keep keys short but descriptive
- Avoid special characters in keys

### 3. File Management
- Start with 3-5 bibliography files
- Add new files as collection grows
- Keep each file under 500 entries

### 4. Performance Optimization
- Put most-used sources in first file listed
- Order files by frequency of use
- Use book-specific files for large commentaries

## Example Configurations

### Basic Commentary Setup
```yaml
bibliography_files: ["nt-commentary", "general-references"]
```

### Comprehensive Study
```yaml
bibliography_files: ["philippians", "nt-commentary", "systematic-theology", "biblical-theology", "general-references"]
```

### Topical Study
```yaml
bibliography_files: ["systematic-theology", "biblical-theology", "church-history"]
```

## Migration from Single Bibliography

1. **Split existing bibliography** into logical topic-based files
2. **Update front matter** in existing commentaries
3. **Test citations** to ensure proper lookup
4. **Optimize file order** based on usage patterns

## Troubleshooting

### Citation Not Found
1. Check citation key spelling
2. Verify source is in specified bibliography files
3. Confirm bibliography file names in front matter
4. Check JSON syntax in bibliography files

### Slow Performance
1. Reduce file sizes (split large files)
2. Put frequently-used sources first
3. Limit number of bibliography files per page
4. Check for JSON parsing errors in Hugo logs

## Zotero Integration

When exporting from Zotero:
1. **Export by collection** to create topic-based files
2. **Use Better BibTeX** plugin for consistent formatting
3. **Convert to simplified JSON** using provided scripts
4. **Split large exports** into manageable files

This system provides excellent scalability while maintaining performance for reference-heavy biblical commentary sites.