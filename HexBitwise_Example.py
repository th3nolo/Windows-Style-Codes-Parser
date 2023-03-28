from windows_style_codes import get_descriptions, windows_style_codes

hex_value = 0x97080000
descriptions = get_descriptions(hex_value, windows_style_codes)

for description in descriptions:
    print("- {}".format(description))
