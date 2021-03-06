import os
import subprocess
from libqtile import hook

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()
color_bar = "#0e0f1a"
size_bar = 30
predetermined_font = 'Ubuntu Mono Nerd Font'
predetermined_font_size = 16

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    ##### CUSTOM KEY BINDINGS ####

    #OPEN DISCORD
    Key([mod, "control"], "d", lazy.spawn("discord"), desc="Abrir discord"),
    #OPEN BROWSER
    Key([mod], "b", lazy.spawn("firefox"), desc="Abrir firefox"),
    #OPEN ROFI
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Abrir menu Rofi"),
]

##ICON LIST NERD FONTS
#1- Arch Linux -> ???
#2- Firefox -> ???
#3- Terminal -> ??? 
#4- Vs Code -> ???
#5- Folders -> ???
#6- Discord -> ???
#7- Git -> ???
#8- Telegram -> ???
#9- Docker ->  ???
 


groups = [Group(i) for i in [
    " ???  "," ??? "," ???  "," ???  "," ???  "," ??? "," ??? "," ???  "," ???  ",
]]

for i, group in enumerate(groups):
    DeskNumber = str(i +1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                DeskNumber,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                DeskNumber,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

## TOOL BAR
widget_defaults = dict(
    font= predetermined_font,
    fontsize= predetermined_font_size,
    padding= 2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active='ffffff',
                    border_width=1,
                    disable_drag = True,
                    fontsize= 21,
                    highlight_method = 'block',
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("default config", name="default"),
                widget.Net(interface='enp4s0'),
                widget.Systray(),
                widget.Clock(format='%d/%m/%Y - %H:%M '),
                widget.QuickExit(),
                widget.CurrentLayout(),
            ],
            size_bar,
            background = color_bar,
            border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            #border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active='ffffff',
                    border_width=1,
                    disable_drag = True,
                    fontsize= 21,
                    highlight_method = 'block',
                    padding_x = 1,
                    padding_y = 5,
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("default config", name="default"),
                widget.Net(interface='enp4s0'),
                widget.Systray(),
                widget.Clock(format='%d/%m/%Y - %H:%M '),
                widget.QuickExit(),
                widget.CurrentLayout(),
            ],
            size_bar,
            #border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            background = color_bar,
            #border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

##### BAR COLORS #####

""" def init__colors():
    return [["#a151d3","#a151d3"],
            ["#F07178","#F07178"],
            ["#fb9f7f","#fb9f7f"],
            ["#ffd47e","#ffd47e"],

            ]

def init_grups_names():
    return[
        ("WWW",{'layout':'monadtall'}),
        ("DEV",{'layout':'monadtall'}),
        ("TERM",{'layout':'monadtall'}),
        ("DISCORD",{'layout':'monadtall'}),
        ("DOC",{'layout':'monadtall'}),
        ("AUX1",{'layout':'monadtall'}),
        ("AUX2",{'layout':'monadtall'}),
        ("AUX3",{'layout':'monadtall'}),
        ("AUX4",{'layout':'monadtall'}),
    ] """