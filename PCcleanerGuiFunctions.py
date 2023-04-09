import ctypes as ct


def dark_title_bar(window):
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value),
                         ct.sizeof(value))


def change_on_hover(button, color_on_hover, color_on_leave):
    button.bind("<Enter>", func=lambda e: button.config(
        background=color_on_hover))

    button.bind("<Leave>", func=lambda e: button.config(
        background=color_on_leave, foreground="#000000"))
