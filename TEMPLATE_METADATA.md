# Template Metadata System

## Overview

Each template file should include a metadata header that describes its configuration. This ensures consistency and makes it easy to understand how to configure each template in PyCharm.

## Metadata Format

The metadata should be placed at the top of each template file as a comment block. Use the appropriate comment syntax for the file type (e.g., `#` for Python, `//` for JavaScript, `<!-- -->` for HTML).

### Standard Metadata Fields

```
Template Name: [Name of the template as it appears in PyCharm]
Template Tab: [Files | Includes]
Extension: [File extension, e.g., .py, .js, .html]
Output Filename: [Default filename pattern, e.g., ${NAME}.py]
Reformat: [Yes | No]
Live Templates: [Enabled | Disabled]
Description: [Brief description of what this template is for]
```

## Field Descriptions

### Template Name
- **Purpose**: The display name that appears in PyCharm's "New File" menu
- **Example**: `Python Script`, `React Component`, `Django Model`
- **Guidelines**: Use clear, descriptive names that indicate the template's purpose

### Template Tab
- **Purpose**: Indicates whether this template goes in the main "Files" tab or the "Includes" tab
- **Values**:
  - `Files` - Main template tab (appears in the New File menu)
  - `Includes` - Include template tab (used by other templates via #parse directive)
- **Example**: `Files` for complete file templates, `Includes` for reusable snippets

### Extension
- **Purpose**: The file extension for files created from this template
- **Example**: `.py`, `.js`, `.tsx`, `.html`, `.css`
- **Guidelines**: Include the dot prefix

### Output Filename
- **Purpose**: The default pattern for naming files created from this template
- **Example**: `${NAME}.py`, `${NAME}.component.tsx`, `test_${NAME}.py`
- **Guidelines**: Use `${NAME}` variable for the user-provided filename

### Reformat
- **Purpose**: Indicates whether PyCharm should automatically reformat the file according to code style settings after creation
- **Values**: `Yes` or `No`
- **Guidelines**: 
  - Use `Yes` for code files where consistent formatting is important
  - Use `No` for templates where exact formatting must be preserved

### Live Templates
- **Purpose**: Indicates whether PyCharm Live Templates should be enabled/processed in the generated file
- **Values**: `Enabled` or `Disabled`
- **Guidelines**:
  - Use `Enabled` if the template uses Live Template syntax (e.g., `$VAR$`)
  - Use `Disabled` for standard file templates

### Description
- **Purpose**: A brief explanation of what the template is for and when to use it
- **Example**: `"Basic Python script with shebang and main guard"`
- **Guidelines**: Keep it concise but informative

## Example Templates

### Example 1: Python Script Template (Main Template)

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
#!/usr/bin/env python3
"""
${NAME}.py

${USER} - ${DATE}
"""


def main():
    """Main function."""
    pass


if __name__ == "__main__":
    main()
```

### Example 2: Python File Header (Include Template)

```python
#[[
Template Name: Python File Header
Template Tab: Includes
Extension: N/A
Output Filename: N/A
Reformat: No
Live Templates: Disabled
Description: Standard header with copyright and license information
]]#
# -*- coding: utf-8 -*-
"""
File: ${NAME}
Author: ${USER}
Date: ${DATE}
Project: ${PROJECT_NAME}

Description:
    TODO: Add file description

Copyright (c) ${YEAR}
"""
```

### Example 3: React Component (Main Template)

```javascript
//[[
// Template Name: React Functional Component
// Template Tab: Files
// Extension: .tsx
// Output Filename: ${NAME}.tsx
// Reformat: Yes
// Live Templates: Disabled
// Description: TypeScript React functional component with props interface
//]]
import React from 'react';

interface ${NAME}Props {
  // TODO: Define props
}

const ${NAME}: React.FC<${NAME}Props> = (props) => {
  return (
    <div>
      {/* TODO: Implement component */}
    </div>
  );
};

export default ${NAME};
```

## Using Metadata

When adding a new template to this repository:

1. **Copy the metadata format** from the examples above
2. **Fill in all required fields** according to your template's configuration
3. **Use the appropriate comment syntax** for your file type
4. **Place the metadata at the top** of the template file
5. **Follow the guidelines** for each field to ensure consistency

When importing templates into PyCharm:

1. **Read the metadata** at the top of the template file
2. **Configure PyCharm settings** according to the metadata fields
3. **Verify** that the template name, extension, and options match the metadata

## Comment Syntax by Language

| Language | Comment Syntax | Example |
|----------|----------------|---------|
| Python | `#[[ ... ]]#` | See Python examples above |
| JavaScript/TypeScript | `//[[ ... ]]` or `/*[[ ... ]]*/ ` | See React example above |
| HTML/XML | `<!--[[ ... ]]-->` | `<!--[[ metadata ]]-->` |
| CSS | `/*[[ ... ]]*/` | `/*[[ metadata ]]*/` |
| Shell Script | `#[[ ... ]]#` | Same as Python |
| Java/C/C++ | `/*[[ ... ]]*/` | `/*[[ metadata ]]*/` |

## Notes

- The `#[[ ]]#` syntax is used to prevent PyCharm from processing the metadata as template code
- Metadata is for human reference and documentation purposes
- The metadata helps maintain consistency across template files
- When submitting new templates, always include complete metadata
