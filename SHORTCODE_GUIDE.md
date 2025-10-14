# Shortcode Reference Guide

This guide explains how to use all available shortcodes in the biblical commentary system. Use this as a reference when writing commentary content.

## Table of Contents
- [Note System (Citations & Footnotes)](#note-system-citations--footnotes)
- [Greek Words](#greek-words)
- [Hebrew Words](#hebrew-words)
- [Cross-References](#cross-references)
- [Academic Notes](#academic-notes)
- [Expandable Sections](#expandable-sections)
- [Reading Modes](#reading-modes)
- [Best Practices](#best-practices)

---

## Note System (Citations & Footnotes)

The unified `{{< note >}}` shortcode handles all footnotes and citations. It auto-numbers and provides popup functionality.

### Basic Syntax
```markdown
{{< note "source:pages" >}}Optional commentary text{{< /note >}}
```

### Usage Examples

#### 1. Citation Only
```markdown
Paul's understanding of partnership{{< note "fee1999:123-125" >}}{{< /note >}} shapes this greeting.
```
**Result:** Numbered footnote showing "Fee, Commentary on Philippians (1999), 123-125."

#### 2. Commentary Only
```markdown
This phrase is significant{{< note "" >}}It appears over 160 times in Paul's letters, emphasizing the believer's new identity.{{< /note >}} in Pauline theology.
```
**Result:** Numbered footnote with just your commentary.

#### 3. Citation + Commentary
```markdown
The Greek term is complex{{< note "martin1983:87-90" >}}Martin's analysis shows how koinonia implies deep spiritual partnership beyond mere association.{{< /note >}} in its implications.
```
**Result:** Numbered footnote with citation followed by your commentary (properly spaced).

#### 4. Multiple Sources
```markdown
This interpretation is widely supported{{< note "fee1999:63-65,martin1983:45,grudem1994:789" >}}{{< /note >}} in recent scholarship.
```
**Result:** All sources listed in one footnote.

### Important Notes
- **Punctuation:** Always place periods and commas OUTSIDE the shortcode: `{{< /note >}}.`
- **Empty content:** For citation-only footnotes, use empty quotes: `{{< note "source:pages" >}}{{< /note >}}`
- **Spacing:** The system automatically adds proper spacing between commentary and citations

---

## Greek Words

Use `{{< greek >}}` for Greek words with hover tooltips and Strong's numbers.

### Syntax
```markdown
{{< greek "greek_text" "transliteration" "strongs_number" "definition" >}}
```

### Examples
```markdown
Paul identifies himself as {{< greek "δοῦλοι" "douloi" "G1401" "slaves/servants" >}} of Christ.

The concept of {{< greek "κοινωνίᾳ" "koinonia" "G2842" "fellowship, participation, sharing" >}} is central here.

This refers to {{< greek "ἁγίοις" "hagiois" "G40" "holy ones" >}} set apart for God's purposes.
```

### Best Practices
- Include the Strong's number for precision
- Keep definitions concise but accurate
- Use standard transliteration conventions

---

## Hebrew Words

Use `{{< hebrew >}}` for Hebrew words (primarily for Old Testament commentary).

### Syntax
```markdown
{{< hebrew "hebrew_text" "transliteration" "strongs_number" "definition" >}}
```

### Examples
```markdown
The Hebrew concept of {{< hebrew "שָׁלוֹם" "shalom" "H7965" "peace, wholeness" >}} goes beyond mere absence of conflict.

God's {{< hebrew "חֶסֶד" "chesed" "H2617" "steadfast love, loving-kindness" >}} is central to the covenant.
```

---

## Cross-References

Use `{{< crossref >}}` to link to other passages or commentary sections.

### Syntax
```markdown
{{< crossref "passage_reference" "url_path" >}}
```

### Examples
```markdown
Compare {{< crossref "Ephesians 2:8-10" "/commentary/new-testament/ephesians/02-01-10/" >}} for similar language.

See also {{< crossref "2 Corinthians 8:4" "/commentary/new-testament/2-corinthians/08-01-15/" >}} on partnership.

This echoes {{< crossref "Romans 1:1" "/commentary/new-testament/romans/01-01-07/" >}} where Paul uses similar servant language.
```

### Best Practices
- Use standard biblical reference format
- Ensure the URL path matches your site structure
- Link to relevant passages that illuminate the text

---

## Academic Notes

Use `{{< academic-note >}}` for content that appears only in Study and Academic reading modes.

### Syntax
```markdown
{{< academic-note >}}
Content for advanced readers only
{{< /academic-note >}}
```

### Examples
```markdown
{{< academic-note >}}
The choice to use δοῦλοι rather than ἀπόστολοι is significant. Paul reserves his apostolic authority for situations requiring correction{{< note "fee1999:63-65" >}}{{< /note >}}.
{{< /academic-note >}}

{{< academic-note >}}
Koinōnia in the Hellenistic world often referred to business partnerships, indicating deep mutual commitment{{< note "martin1983:87-90" >}}{{< /note >}}.
{{< /academic-note >}}
```

### Best Practices
- Use for technical discussions
- Include scholarly citations
- Avoid overwhelming casual readers
- Can contain other shortcodes (notes, Greek words, etc.)

---

## Expandable Sections

Use `{{< expandable >}}` to create collapsible content sections.

### Syntax
```markdown
{{< expandable title="Section Title" level="2" >}}
Content goes here
{{< /expandable >}}
```

### Examples
```markdown
{{< expandable title="Verse-by-Verse Analysis" level="2" >}}
### Verses 1-2: Greeting
Detailed analysis here...
{{< /expandable >}}

{{< expandable title="Word Studies" level="2" >}}
### Koinōnia (κοινωνία)
Detailed word study...
{{< /expandable >}}
```

### Best Practices
- Use descriptive titles
- Set appropriate level (1-3) for nesting
- Structure content logically inside
- Can contain all other shortcodes

---

## Reading Modes

The system supports three reading modes that control content visibility:

### Quick Mode
- Shows basic content only
- Hides academic notes and complex expandable sections
- Target: General readers

### Study Mode  
- Shows academic notes
- Displays all expandable content
- Target: Serious Bible students

### Academic Mode
- Shows all content
- Full scholarly apparatus
- Target: Pastors, scholars, seminary students

### Controlling Visibility
```markdown
<!-- Always visible -->
Basic commentary text

<!-- Study and Academic only -->
{{< academic-note >}}
Technical discussion
{{< /academic-note >}}

<!-- Academic only (level 3 expandable) -->
{{< expandable title="Advanced Analysis" level="3" >}}
Highly technical content
{{< /expandable >}}
```

---

## Best Practices

### Punctuation and Formatting
```markdown
✅ CORRECT:
Text{{< note "source:pages" >}}{{< /note >}}.
Text{{< note "" >}}Commentary here.{{< /note >}}.

❌ WRONG:
Text{{< note "source:pages" >}}.{{< /note >}}
Text{{< note "" >}}Commentary here{{< /note >}}.
```

### Citation Format
```markdown
✅ CORRECT:
{{< note "fee1999:123-125" >}}{{< /note >}}
{{< note "fee1999:123-125,martin1983:45" >}}{{< /note >}}

❌ WRONG:
{{< note "fee1999" "123-125" >}}{{< /note >}}
{{< note "fee1999:123-125, martin1983:45" >}}{{< /note >}}
```

### Content Organization
1. **Structure logically:** Use expandable sections for major divisions
2. **Layer content:** Quick → Study → Academic progression
3. **Link extensively:** Use cross-references to connect ideas
4. **Define terms:** Use Greek/Hebrew shortcodes for key words
5. **Cite sources:** Use note shortcodes for scholarly backing

### Reading Flow
- Write for the Quick mode reader first
- Add Study mode content for deeper engagement  
- Include Academic mode content for scholarly completeness
- Ensure each mode provides a complete reading experience

---

## Quick Reference

| Shortcode | Purpose | Example |
|-----------|---------|---------|
| `{{< note >}}` | Citations & footnotes | `{{< note "source:pages" >}}{{< /note >}}` |
| `{{< greek >}}` | Greek words | `{{< greek "δοῦλοι" "douloi" "G1401" "servants" >}}` |
| `{{< hebrew >}}` | Hebrew words | `{{< hebrew "שָׁלוֹם" "shalom" "H7965" "peace" >}}` |
| `{{< crossref >}}` | Cross-references | `{{< crossref "Rom 1:1" "/path/" >}}` |
| `{{< academic-note >}}` | Study/Academic only | `{{< academic-note >}}Content{{< /academic-note >}}` |
| `{{< expandable >}}` | Collapsible sections | `{{< expandable title="Title" level="2" >}}{{< /expandable >}}` |

## File Location
Save this guide as `SHORTCODE_GUIDE.md` in your project root for easy reference while writing commentary.