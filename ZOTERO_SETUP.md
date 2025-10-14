# Zotero to Hugo Bibliography Setup Guide

This guide shows you how to set up Zotero with Better BibTeX to automatically maintain your Hugo site's bibliography.

## Why This Approach?

Instead of manually maintaining YAML files, you can:
- ✅ Manage all your sources in Zotero (with proper metadata, PDFs, notes)
- ✅ Export directly to a format Hugo can read
- ✅ Keep citations consistent and professional
- ✅ Automatically update your website when you add new sources

## Step 1: Install Better BibTeX in Zotero

1. **Download Better BibTeX:**
   - Go to: https://retorque.re/zotero-better-bibtex/
   - Download the latest `.xpi` file

2. **Install in Zotero:**
   - Open Zotero → Tools → Add-ons
   - Click the gear icon ⚙️ → "Install Add-on From File"
   - Select the downloaded `.xpi` file
   - Restart Zotero

## Step 2: Configure Better BibTeX

1. **Set Citation Key Format:**
   - Zotero → Edit → Preferences → Better BibTeX
   - In "Citation keys" tab, set format to: `[auth:lower][year]`
   - This creates keys like `fee1999`, `martin1983` (matching your current format)

2. **Configure Auto-Export:**
   - Check "On change" for automatic updates
   - This will re-export whenever you modify your library

## Step 3: Set Up Your Bibliography Collection

1. **Create a Collection:**
   - Right-click in Zotero sidebar → "New Collection"
   - Name it "Website Bibliography" or "Hugo Sources"

2. **Add Your Sources:**
   - Drag existing items into this collection
   - Add new sources as needed
   - Ensure each has proper metadata (author, title, year, publisher)

## Step 4: Set Up Auto-Export

1. **Export Your Collection:**
   - Right-click "Website Bibliography" collection
   - Choose "Export Collection"
   - Format: "Better BibTeX JSON"
   - Check "Keep updated" ✅
   - Save as: `C:\Users\pasto\Desktop\zotero_export.json`

2. **Zotero will now automatically update this file** whenever you:
   - Add new sources to the collection
   - Edit existing source metadata
   - Remove sources from the collection

## Step 5: Set Up Automatic Conversion

1. **Use the conversion script:**
   ```bash
   python scripts/convert_zotero_simple.py C:\Users\pasto\Desktop\zotero_export.json data/bibliography.json
   ```

2. **Or use the batch file:**
   - Double-click `scripts/update_bibliography.bat`
   - It will automatically convert and update your site

## Your Current Bibliography Format

Your Hugo site now uses this simple JSON format:

```json
{
  "citation_key": {
    "author": "Author Name",
    "title": "Book Title",
    "year": "2023",
    "publisher": "Publisher Name",
    "series": "Series Name",
    "isbn": "978-1234567890"
  }
}
```

## Workflow Summary

1. **Add sources in Zotero** (to your "Website Bibliography" collection)
2. **Zotero auto-exports** to `zotero_export.json` (because "Keep updated" is checked)
3. **Run conversion script** to update `data/bibliography.json`
4. **Hugo rebuilds** your site with updated citations

## Citation Usage in Your Content

Use citations in your content exactly as before:

```markdown
Paul's understanding of partnership{{< note "fee1999:123-125" >}}{{< /note >}} shapes this greeting.

This concept is widely supported{{< note "fee1999:63-65,martin1983:45" >}}{{< /note >}} in scholarship.
```

## Pro Tips

1. **Consistent Citation Keys:**
   - Better BibTeX ensures consistent `author+year` format
   - No more manually creating citation keys

2. **Automatic Updates:**
   - When you update metadata in Zotero, it auto-exports
   - Run the conversion script to update your site

3. **Backup Your Bibliography:**
   - The JSON export serves as a backup of your sources
   - Keep both Zotero library and JSON files in version control

4. **Adding New Sources:**
   - Use Zotero's browser connector to add sources quickly
   - Drag them into your "Website Bibliography" collection
   - Run the conversion script

## Troubleshooting

**Missing Citation Keys:**
- Ensure Better BibTeX is generating keys automatically
- Check Preferences → Better BibTeX → Citation keys

**Export Not Updating:**
- Verify "Keep updated" is checked in export settings
- Try manually re-exporting the collection

**Conversion Errors:**
- Check that all sources have basic metadata (author, title)
- Empty or malformed entries may cause issues

This setup gives you the best of both worlds: Zotero's powerful source management with Hugo's flexible citation system!