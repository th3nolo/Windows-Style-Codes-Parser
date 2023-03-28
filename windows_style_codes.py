# windows_style_codes.py
#Ref: https://learn.microsoft.com/en-us/windows/win32/winmsg/window-styles
#Ref: https://learn.microsoft.com/en-us/windows/win32/controls/tooltip-controls

# Windows style codes list
windows_style_codes = [
    ('WS_BORDER', 0x00800000, 'The window has a thin-line border'),
    ('WS_CAPTION', 0x00C00000, 'The window has a title bar (includes the WS_BORDER style)'),
    ('WS_CHILD', 0x40000000, 'The window is a child window. A window with this style cannot have a menu bar. This style cannot be used with the WS_POPUP style'),
    ('WS_CHILDWINDOW', 0x40000000, 'Same as the WS_CHILD style'),
    ('WS_CLIPCHILDREN', 0x02000000, 'Excludes the area occupied by child windows when drawing occurs within the parent window. This style is used when creating the parent window'),
    ('WS_CLIPSIBLINGS', 0x04000000, 'Clips child windows relative to each other; that is, when a particular child window receives a WM_PAINT message, the WS_CLIPSIBLINGS style clips all other overlapping child windows out of the region of the child window to be updated. If WS_CLIPSIBLINGS is not specified and child windows overlap, it is possible, when drawing within the client area of a child window, to draw within the client area of a neighboring child window'),
    ('WS_DISABLED', 0x08000000, 'The window is initially disabled. A disabled window cannot receive input from the user. To change this after a window has been created, use the EnableWindow function'),
    ('WS_DLGFRAME', 0x00400000, 'The window has a border of a style typically used with dialog boxes. A window with this style cannot have a title bar'),
    ('WS_GROUP', 0x00020000, 'The window is the first control of a group of controls. The group consists of this first control and all controls defined after it, up to the next control with the WS_GROUP style. The first control in each group usually has the WS_TABSTOP style so that the user can move from group to group. The user can subsequently change the keyboard focus from one control in the group to the next control in the group by using the direction keys. You can turn this style on and off to change dialog box navigation. To change this style after a window has been created, use the SetWindowLong function'),
    ('WS_HSCROLL', 0x00100000, 'The window has a horizontal scroll bar'),
    ('WS_ICONIC', 0x20000000, 'The window is initially minimized. Same as the WS_MINIMIZE style'),
    ('WS_MAXIMIZE', 0x01000000, 'The window is initially maximized'),
    ('WS_MAXIMIZEBOX', 0x00010000, 'The window has a maximize button. Cannot be combined with the WS_EX_CONTEXTHELP style. The WS_SYSMENU style must also be specified'),
    ('WS_MINIMIZE', 0x20000000, 'The window is initially minimized. Same as the WS_ICONIC style'),
    ('WS_MINIMIZEBOX', 0x00020000, 'The window has a minimize button. Cannot be combined with the WS_EX_CONTEXTHELP style. The WS_SYSMENU style must also be specified'),
    ('WS_OVERLAPPED', 0x00000000, 'The window is an overlapped window. An overlapped window has a title bar and a border. Same as the WS_TILED style'),
    ('WS_OVERLAPPEDWINDOW', 0x00CF0000, 'The window is an overlapped window. Same as the WS_TILEDWINDOW style'),
    ('WS_VISIBLE', 0x10000000, 'The window is initially visible. This style can be turned on and off by using the ShowWindow or SetWindowPos function'),
    ('WS_VSCROLL', 0x00200000, 'The window has a vertical scroll bar'),
    ('WS_SYSMENU', 0x00080000, 'The window has a window menu on its title bar. The WS_CAPTION style must also be specified'),
    ('WS_SIZEBOX', 0x00040000, 'The window has a sizing border. Same as the WS_THICKFRAME style'),
    ('WS_POPUPWINDOW', 0x80880000, 'The window is a pop-up window. This style cannot be used with the WS_CHILD style'),
    ('WS_TABSTOP', 0x00010000, 'The window is a control that can receive the keyboard focus when the user presses the TAB key. Pressing the TAB key changes the keyboard focus to the next control with the WS_TABSTOP style'),
    ('WS_THICKFRAME', 0x00040000, 'The window has a sizing border. Same as the WS_SIZEBOX style'),
    ('WS_TILED', 0x00000000, 'The window is an overlapped window. An overlapped window has a title bar and a border. Same as the WS_OVERLAPPED style'),
    ('WS_TILEDWINDOW', 0x00CF0000, 'The window is an overlapped window. Same as the WS_OVERLAPPEDWINDOW style'),
    ('WS_VISIBLE', 0x10000000, 'The window is initially visible. This style can be turned on and off by using the ShowWindow or SetWindowPos function'),
    ('WS_POPUP', 0x80000000, 'The window is a pop-up window. This style cannot be used with the WS_CHILD style'),
    ('WS_VSCROLL', 0x00200000, 'The window has a vertical scroll bar'),
]


def get_descriptions(hex_value, table):
    """
    Returns a list of descriptions for the given hex_value based on the provided table of Windows style codes.

    :param hex_value: int
        The hexadecimal value of the Windows style codes.
    :param table: list of tuples
        A list of Windows style code tuples (name, value, description).
    :return: list of str
        A list of descriptions for the given hex_value.
    """
    descriptions = []

    for constant_name, constant_value, description in table:
        if hex_value & constant_value:
            descriptions.append(constant_name)

    return descriptions


