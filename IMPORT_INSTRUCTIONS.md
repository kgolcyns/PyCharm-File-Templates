# PyCharm File Templates - Import Instructions

## How to Import File Templates into PyCharm

### Method 1: Manual Import via Settings

1. **Open PyCharm Settings**
   - Windows/Linux: `File` → `Settings`
   - macOS: `PyCharm` → `Preferences`
   - Keyboard shortcut: `Ctrl+Alt+S` (Windows/Linux) or `Cmd+,` (macOS)

2. **Navigate to File Templates**
   - Go to: `Editor` → `File and Code Templates`

3. **Import Templates**
   
   **For Main Templates:**
   - Select the `Files` tab
   - Click the `+` (plus) button to create a new template
   - Give it a name and extension (as specified in the template metadata)
   - Copy the content from the template file in the `templates/` directory
   - Paste it into the template editor
   - Configure the settings:
     - Check/uncheck "Reformat according to style" based on metadata
     - Check/uncheck "Enable Live Templates" based on metadata
   
   **For Include Templates:**
   - Select the `Includes` tab
   - Click the `+` (plus) button to create a new include
   - Give it a name (as specified in the include metadata)
   - Copy the content from the include file in the `includes/` directory
   - Paste it into the template editor

4. **Apply and Save**
   - Click `Apply` to save your changes
   - Click `OK` to close the settings

### Method 2: Direct File System Copy (Advanced)

1. **Locate PyCharm Configuration Directory**
   
   - Windows: `%USERPROFILE%\.PyCharmXXXX.X\config\fileTemplates`
   - Linux: `~/.PyCharmXXXX.X/config/fileTemplates`
   - macOS: `~/Library/Application Support/JetBrains/PyCharmXXXX.X/fileTemplates`
   
   (Replace `XXXX.X` with your PyCharm version, e.g., `2023.3`)

2. **Copy Template Files**
   
   - Copy files from `templates/` to the `fileTemplates/` directory
   - Copy files from `includes/` to the `fileTemplates/includes/` directory

3. **Restart PyCharm**
   
   - Close and reopen PyCharm for the templates to be recognized

### Verification

1. Create a new file: `File` → `New` or `Right-click in Project View` → `New`
2. Your custom templates should appear in the list
3. Select a template to create a file based on it

## Template Variables

PyCharm supports several predefined variables that can be used in templates:

- `${NAME}` - Name of the new file
- `${DATE}` - Current system date
- `${TIME}` - Current system time
- `${YEAR}` - Current year
- `${MONTH}` - Current month
- `${DAY}` - Current day
- `${HOUR}` - Current hour
- `${MINUTE}` - Current minute
- `${USER}` - Current user name
- `${PRODUCT_NAME}` - Name of the IDE (PyCharm)
- `${PROJECT_NAME}` - Name of the current project
- `${PACKAGE_NAME}` - Name of the package in which the file is created

## Additional Resources

- [JetBrains Documentation - File Templates](https://www.jetbrains.com/help/pycharm/using-file-and-code-templates.html)
- [JetBrains Documentation - Template Variables](https://www.jetbrains.com/help/pycharm/file-template-variables.html)
