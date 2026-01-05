# PyCharm File Templates

A collection of file templates for PyCharm IDE with a comprehensive metadata labeling system.

## Overview

This repository provides:
- **Organized template structure** - Separate directories for main templates and includes
- **Metadata labeling system** - Standardized format for documenting template configuration
- **Import instructions** - Step-by-step guide for adding templates to PyCharm
- **Example templates** - Ready-to-use Python templates demonstrating the labeling system

## Repository Structure

```
PyCharm-File-Templates/
├── templates/              # Main file templates (appear in New File menu)
│   ├── Python_Script_with_Main.py
│   ├── Python_Class.py
│   └── Python_Unit_Test.py
├── includes/               # Include templates (reusable snippets)
│   ├── Python_File_Header.py
│   └── Python_TODO_Block.py
├── IMPORT_INSTRUCTIONS.md  # How to import templates into PyCharm
├── TEMPLATE_METADATA.md    # Documentation for the metadata labeling system
└── README.md              # This file
```

## Quick Start

1. **Browse Templates**: Explore the `templates/` and `includes/` directories
2. **Read Metadata**: Each template file contains metadata describing its configuration
3. **Import to PyCharm**: Follow the instructions in [IMPORT_INSTRUCTIONS.md](IMPORT_INSTRUCTIONS.md)
4. **Start Using**: Create new files using your imported templates

## Template Metadata System

Each template includes a metadata header with the following fields:

- **Template Name**: Display name in PyCharm's menu
- **Template Tab**: `Files` (main templates) or `Includes` (reusable snippets)
- **Extension**: File extension (e.g., `.py`, `.js`)
- **Output Filename**: Default filename pattern (e.g., `${NAME}.py`)
- **Reformat**: Whether to auto-format the file (`Yes`/`No`)
- **Live Templates**: Whether Live Templates are enabled (`Enabled`/`Disabled`)
- **Description**: Brief explanation of the template's purpose

### Example Metadata

```python
#[[
Template Name: Python Script with Main
Template Tab: Files
Extension: .py
Output Filename: ${NAME}.py
Reformat: Yes
Live Templates: Disabled
Description: Python script with shebang, docstring, and main guard
]]#
```

## Documentation

- **[IMPORT_INSTRUCTIONS.md](IMPORT_INSTRUCTIONS.md)** - Detailed instructions for importing templates into PyCharm
- **[TEMPLATE_METADATA.md](TEMPLATE_METADATA.md)** - Complete guide to the metadata labeling system

## Available Templates

### Main Templates (templates/)

1. **Python Script with Main** - Complete Python script with shebang and main guard
2. **Python Class** - Class definition with docstrings and basic methods
3. **Python Unit Test** - unittest-based test class with setUp and tearDown

### Include Templates (includes/)

1. **Python File Header** - Standard file header with copyright and metadata
2. **Python TODO Block** - Formatted TODO comment with priority and status fields

## Contributing

To add a new template:

1. Create the template file in the appropriate directory (`templates/` or `includes/`)
2. Add complete metadata at the top of the file (see [TEMPLATE_METADATA.md](TEMPLATE_METADATA.md))
3. Follow the naming convention: Use underscores for spaces (e.g., `Python_Script.py`)
4. Test the template by importing it into PyCharm
5. Submit a pull request with your template

## PyCharm Variables

Templates support PyCharm's predefined variables:

- `${NAME}` - Name of the new file
- `${USER}` - Current user name
- `${DATE}` - Current date
- `${TIME}` - Current time
- `${YEAR}` - Current year
- `${PROJECT_NAME}` - Current project name
- `${PACKAGE_NAME}` - Package name where file is created

See [PyCharm documentation](https://www.jetbrains.com/help/pycharm/file-template-variables.html) for all available variables.

## License

This repository is provided as-is for use with PyCharm IDE.

## Resources

- [PyCharm File Templates Documentation](https://www.jetbrains.com/help/pycharm/using-file-and-code-templates.html)
- [PyCharm Template Variables](https://www.jetbrains.com/help/pycharm/file-template-variables.html)
