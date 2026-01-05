# Quick Reference Guide

## Template Metadata Fields

Every template file in this repository includes a standardized metadata header:

```
Template Name:     [Display name in PyCharm menu]
Template Tab:      [Files | Includes]
Extension:         [.py, .js, .html, etc. or N/A for includes]
Output Filename:   [Pattern like ${NAME}.py or N/A for includes]
Reformat:          [Yes | No]
Live Templates:    [Enabled | Disabled]
Description:       [Brief description of template purpose]
```

## Directory Structure

```
templates/    → Main templates (appear in New File menu)
includes/     → Include templates (reusable snippets via #parse)
```

## PyCharm Variables

Common variables you can use in templates:

- `${NAME}` - Filename
- `${USER}` - Username  
- `${DATE}` - Current date
- `${TIME}` - Current time
- `${YEAR}` - Current year
- `${PROJECT_NAME}` - Project name
- `${PACKAGE_NAME}` - Package name

## Import Quick Steps

1. Open PyCharm Settings (`Ctrl+Alt+S` / `Cmd+,`)
2. Navigate to: `Editor` → `File and Code Templates`
3. Select tab: `Files` (for templates/) or `Includes` (for includes/)
4. Click `+` to create new template
5. Copy metadata fields to configure settings
6. Copy template content to editor
7. Apply and Save

## Files in This Repository

### Documentation
- `README.md` - Main overview and guide
- `IMPORT_INSTRUCTIONS.md` - Detailed import instructions
- `TEMPLATE_METADATA.md` - Complete metadata system documentation
- `QUICK_REFERENCE.md` - This file

### Templates (templates/)
- `Python_Script_with_Main.py` - Python script with main guard
- `Python_Class.py` - Python class definition
- `Python_Unit_Test.py` - unittest test class

### Includes (includes/)
- `Python_File_Header.py` - Standard file header
- `Python_TODO_Block.py` - Formatted TODO comments

## Adding New Templates

1. Create file in `templates/` or `includes/`
2. Add metadata header (copy from existing template)
3. Fill in all metadata fields
4. Write template content using PyCharm variables
5. Test by importing into PyCharm
6. Submit pull request

## Metadata Comment Syntax

| Language | Syntax |
|----------|--------|
| Python | `#[[ ... ]]#` |
| JavaScript/TypeScript | `//[[ ... ]]` or `/*[[ ... ]]*/ ` |
| HTML/XML | `<!--[[ ... ]]-->` |
| CSS | `/*[[ ... ]]*/` |
| Java/C/C++ | `/*[[ ... ]]*/` |

## Need Help?

- Read [IMPORT_INSTRUCTIONS.md](IMPORT_INSTRUCTIONS.md) for import help
- Read [TEMPLATE_METADATA.md](TEMPLATE_METADATA.md) for metadata details
- Check [PyCharm Documentation](https://www.jetbrains.com/help/pycharm/using-file-and-code-templates.html)
