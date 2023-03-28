# Windows-Style-Codes-Parser
This repository provides a Python function to parse and display the descriptions of Windows style codes based on a given hexadecimal value. It can be helpful for developers working with Windows APIs who need to quickly understand the styles applied to a window.

## Usage

1. Clone the repository or copy the `windows_style_codes.py` file to your project.
2. Import the `get_descriptions` function and the `windows_style_codes` list into your script.
3. Call the `get_descriptions` function with a hexadecimal value and the `windows_style_codes` list as arguments.

Example:

```python
from windows_style_codes import get_descriptions, windows_style_codes

hex_value = 0x97080000
descriptions = get_descriptions(hex_value, windows_style_codes)

for description in descriptions:
    print("- {}".format(description))
