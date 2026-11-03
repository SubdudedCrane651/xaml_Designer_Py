def generate_xaml(controls):

    lines = []

    lines.append(
        '<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"'
    )

    lines.append(
        '             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml">'
    )

    lines.append("")
    lines.append("<AbsoluteLayout>")
    lines.append("")

    for control in controls:

        lines.extend(
            generate_control(control)
        )

        lines.append("")

    lines.append("</AbsoluteLayout>")
    lines.append("")
    lines.append("</ContentPage>")

    return "\n".join(lines)


def generate_control(control):

    control_type = control.control_type

    if control_type == "Button":
        return generate_button(control)

    elif control_type == "Label":
        return generate_label(control)

    elif control_type == "Entry":
        return generate_entry(control)

    elif control_type == "Frame":
        return generate_frame(control)

    elif control_type == "Border":
        return generate_border(control)

    elif control_type == "CheckBox":
        return generate_checkbox(control)

    elif control_type == "Switch":
        return generate_switch(control)

    elif control_type == "Image":
        return generate_image(control)

    else:
        return generate_unknown(control)


def generate_bounds(control):

    return (
        f'{control.x},'
        f'{control.y},'
        f'{control.width},'
        f'{control.height}'
    )


def common_attributes(control):

    return [
        f'x:Name="{control.name}"',
        f'WidthRequest="{control.width}"',
        f'HeightRequest="{control.height}"'
    ]


# ---------------------------------------------------------
# BUTTON
# ---------------------------------------------------------

def generate_button(control):

    bounds = generate_bounds(control)

    return [
        "<Button",
        f'    x:Name="{control.name}"',
        f'    Text="{control.text}"',
        f'    TextColor="{control.foreground_color}"',
        f'    BackgroundColor="{control.background_color}"',
        f'    WidthRequest="{control.width}"',
        f'    HeightRequest="{control.height}"',
        f'    AbsoluteLayout.LayoutBounds="{bounds}"',
        "/>"
    ]


# ---------------------------------------------------------
# LABEL
# ---------------------------------------------------------

def generate_label(control):

    bounds = generate_bounds(control)

    return [
        "<Label",
        f'    x:Name="{control.name}"',
        f'    Text="{control.text}"',
        f'    TextColor="{control.foreground_color}"',
        f'    WidthRequest="{control.width}"',
        f'    HeightRequest="{control.height}"',
        f'    AbsoluteLayout.LayoutBounds="{bounds}"',
        "/>"
    ]


# ---------------------------------------------------------
# ENTRY
# ---------------------------------------------------------

def generate_entry(control):

    bounds = generate_bounds(control)

    return [
        "<Entry",
        f'    x:Name="{control.name}"',
        f'    Placeholder="{control.text}"',
        f'    TextColor="{control.foreground_color}"',
        f'    BackgroundColor="{control.background_color}"',
        f'    WidthRequest="{control.width}"',
        f'    HeightRequest="{control.height}"',
        f'    AbsoluteLayout.LayoutBounds="{bounds}"',
        "/>"
    ]


# ---------------------------------------------------------
# FRAME
# ---------------------------------------------------------

def generate_frame(control):

    bounds = generate_bounds(control)

    shadow = (
        "True"
        if control.shadow
        else "False"
    )

    return [
        "<Frame",
        f'    x:Name="{control.name}"',
        f'    BorderColor="{control.border_color}"',
        f'    BackgroundColor="{control.background_color}"',
        f'    CornerRadius="{control.border_radius}"',
        f'    HasShadow="{shadow}"',
        f'    WidthRequest="{control.width}"',
        f'    HeightRequest="{control.height}"',
        f'    AbsoluteLayout.LayoutBounds="{bounds}"',
        "/>"
    ]


# ---------------------------------------------------------
# BORDER
# ---------------------------------------------------------

def generate_border(control):

    bounds = generate_bounds(control)

    return [
        "<Border",
        f'    x:Name="{control.name}"',
        f'    Stroke="{control.border_color}"',
        f'    StrokeThickness="{control.border_width}"',
        f'    WidthRequest="{control.width}"',
        f'    HeightRequest="{control.height}"',
        f'    AbsoluteLayout.LayoutBounds="{bounds}"',
        ">",
        "</Border>"
    ]


# ---------------------------------------------------------
# CHECKBOX
# ---------------------------------------------------------

def generate_checkbox(control):

    bounds = generate_bounds(control)

    return [
        "<CheckBox",
        f'    x:Name="{control.name}"',
        f'    Color="{control.foreground_color}"',
        f'    WidthRequest="{control.width}"',
        f'    HeightRequest="{control.height}"',
        f'    AbsoluteLayout.LayoutBounds="{bounds}"',
        "/>"
    ]


# ---------------------------------------------------------
# SWITCH
# ---------------------------------------------------------

def generate_switch(control):

    bounds = generate_bounds(control)

    return [
        "<Switch",
        f'    x:Name="{control.name}"',
        f'    OnColor="{control.foreground_color}"',
        f'    WidthRequest="{control.width}"',
        f'    HeightRequest="{control.height}"',
        f'    AbsoluteLayout.LayoutBounds="{bounds}"',
        "/>"
    ]


# ---------------------------------------------------------
# IMAGE
# ---------------------------------------------------------

def generate_image(control):

    bounds = generate_bounds(control)

    return [
        "<Image",
        f'    x:Name="{control.name}"',
        f'    Source="{control.image_path}"',
        f'    WidthRequest="{control.width}"',
        f'    HeightRequest="{control.height}"',
        f'    AbsoluteLayout.LayoutBounds="{bounds}"',
        "/>"
    ]


# ---------------------------------------------------------
# FALLBACK
# ---------------------------------------------------------

def generate_unknown(control):

    bounds = generate_bounds(control)

    return [
        "<Label",
        f'    Text="{control.control_type}"',
        f'    AbsoluteLayout.LayoutBounds="{bounds}"',
        "/>"
    ]