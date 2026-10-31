def generate_xaml(
    controls
):

    xaml = []

    xaml.append(
        "<AbsoluteLayout>"
    )

    for c in controls:

        if c.control_type == "Button":

            xaml.append(
                f'''
<Button
    Text="{c.text}"
    AbsoluteLayout.LayoutBounds=
    "{c.x},{c.y},{c.width},{c.height}" />
'''
            )

        elif c.control_type == "Label":

            xaml.append(
                f'''
<Label
    Text="{c.text}"
    AbsoluteLayout.LayoutBounds=
    "{c.x},{c.y},{c.width},{c.height}" />
'''
            )

        elif c.control_type == "Entry":

            xaml.append(
                f'''
<Entry
    Placeholder="{c.text}"
    AbsoluteLayout.LayoutBounds=
    "{c.x},{c.y},{c.width},{c.height}" />
'''
            )

    xaml.append(
        "</AbsoluteLayout>"
    )

    return "\n".join(
        xaml
    )