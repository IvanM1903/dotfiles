# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import hook

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal



mod = "mod4"
terminal = guess_terminal()
net_interface = "wlp1s0"
# GroupBox variables
color_bar = "#00000055"
bar_size = 26
font_default = "Ubuntu Mono Nerd Font"
active_color = "#CBFF4D"
inactive_color= "#6272a4"
dark_color = "#44475a"
light_color = "#006989"
#WindowName variables
window_name_color = "#FF5A5F"
#TextBox variables
color_g1 = "#EAEBED" #orange
color_g2 = "#006989" #dark pink
color_g3 = "#A3BAC3" #blue
color_g4 = "#007090" #red
color_g5 = "#E6AF2E" #green
color_updates = "#bc0000" #red

#Functions related to widgets
def fc_separator():
    return widget.Sep(
        linewidth=0,
        padding=4
    )

def fc_circle(vColor, type):
    if type == 0:
        icon = " "
    else:
        icon =" "
    return widget.TextBox(
        text = icon,
        fontsize = bar_size+5,
        foreground = vColor,
        background = color_bar,
        padding = -3
    )

def fc_icon(icon, color_group, type_fg):
    if type_fg == 0:
        fg_color = dark_color
    else:
        fg_color = "#ffffff"
    return widget.TextBox(
        text = icon,
        background = color_group,
        fontsize = 22,
        foreground = fg_color
    )

@hook.subscribe.client_new
def client_new(client):
    if client.name == 'Firefox':
        client.cmd_static(3)

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Change focus to the next monitor
    Key([mod], 'period', lazy.next_screen(), desc='Next monitor'),
    Key([mod], 'comma', lazy.prev_screen(), desc='Prev monitor'),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],"Return",lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack",),
    #Brightness settings
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-")),
    #Volume settings
    Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 5%+ unmute")),
    Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 5%- unmute")),
    Key([], "XF86AudioMute",lazy.spawn("amixer sset Master toggle")),
    #Launch new terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    #Launch files
    Key([mod], "e", lazy.spawn("nautilus"), desc="Launch files"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Open rofi menu
    Key([mod],"m", lazy.spawn("rofi -no-lazy-grab -show drun -modi drun -theme '~/.config/rofi/launchers/misc/launchpad'"), desc="Open rofi menu"),
    # Open brave browser
    Key([mod],"b",lazy.spawn("brave"),desc="Open brave browser"),
    #Take a screenshot
    Key([mod,"shift"],"s",lazy.spawn("scrot -s '/tmp/%F_%T_$wx$h.png' -e 'xclip -selection clipboard -target image/png -i $f'"),desc="Take an area screenshot"),
    #Lock screen with betterlockscreen
    Key([mod],"l",lazy.spawn("betterlockscreen --lock dimpixel"),desc="Lock the screen"),
    #Shutdown the system
    Key([mod,"control"],"p",lazy.spawn("shutdown now"),desc="Shutdown the system"),

]


groups = [Group(i) for i in [
" "," "," ﱮ "," "," "," "," ", " ﭮ"
]]


for i,group in enumerate(groups):
    numeroEscritorio = str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key([mod],
                numeroEscritorio,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"],
                numeroEscritorio,
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
    layout.Columns(
        border_normal="#000000ff",
        border_focus=active_color,
        border_width=2, 
        margin=12
        #margin = "[12 8 12 8]",
    ),
    layout.Max(),
    layout.Floating(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    #layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    layout.Zoomy(
        columnwidth = 300,
        margin=8
    ),
]

widget_defaults = dict(
    font=font_default,
    fontsize=18,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=active_color,
                    spacing=7,
                    highlight_method='block',
                    inactive=inactive_color,
                    other_current_screen_border=dark_color,
                    other_screen_border=dark_color,
                    this_current_screen_border=light_color,
                    this_screen_border=light_color,
                    urgent_alert_method='block'
                ),
                fc_separator(),
                widget.Prompt(),
                widget.WindowName(foreground=window_name_color),
                fc_separator(),
                #start G1
                fc_circle(color_g1,0),
                fc_icon("",color_g1,0),
                widget.ThermalSensor(
                    background = color_g1,
                    foreground = dark_color,
                    threshold = 50,
                    tag_sensor = "edge",
                    fmt = '{} '
                ),
                fc_icon("",color_g1,0),
                widget.Memory(
                    background = color_g1,
                    foreground = dark_color,
                    padding=0,
                    measure_mem="G"
                ),
                fc_circle(color_g1,1),
                #end G1
                fc_separator(),
                #start G2
                fc_circle(color_g2,0),
                fc_icon(" ", color_g2,1),
                widget.CheckUpdates(
                    background = color_g2,
                    color_have_updates=color_updates,
                    color_no_updates = "#ffffff",
                    no_update_string = "No updates",
                    display_format = "Pending: {updates}",
                    update_interval = 3600,
                ),
                fc_icon(" 龍 ",color_g2,1),
                widget.Net(
                    background = color_g2,
                    format ="{down}   {up}",
                    use_bits="true",
                    interface = net_interface
                ),
                fc_circle(color_g2,1),
                #end G2
                fc_separator(),
                #start G3
                fc_circle(color_g3,0),
                widget.Clock(
                    format="%d/%m/%Y %H:%M",
                    background = color_g3,
                    foreground= dark_color
                    ),
                fc_icon("  ",color_g3,0),
                widget.Volume(
                    background=color_g3,
                    foreground = dark_color
                ),
                fc_circle(color_g3,1),
                #end G3
                fc_separator(),
                #start G4
                fc_circle(color_g4,0),
                widget.CurrentLayoutIcon(
                    background = color_g4,
                    scale =0.70
                ),
                widget.CurrentLayout(
                    background=color_g4
                ),
                fc_circle(color_g4,1),
                #end G4
                fc_separator(),
                #start G5
                fc_circle(color_g5,0),
                fc_icon(" ", color_g5,0),
                widget.Backlight(
                    backlight_name="amdgpu_bl0", 
                    format='{percent:2.0%}',
                    background = color_g5,
                    foreground=dark_color
                    ),
                widget.Battery(
                    background = color_g5,
                    foreground = dark_color,
                    full_char=" ",
                    charge_char=" ",
                    discharge_char=" ﴅ",
                    format="{percent:2.0%} {char} ",
                    notify_below=15,
                    notification_timeout=10
                ),
                fc_circle(color_g5,1),
                #end G5
            ],
            bar_size,
            background=color_bar,
            #border_width=[4, 0, 2, 0],  # Draw top and bottom borders
            #border_color=["00000000"]  # Borders are magenta
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active=active_color,
                    spacing=7,
                    highlight_method='block',
                    inactive=inactive_color,
                    other_current_screen_border=dark_color,
                    other_screen_border=dark_color,
                    this_current_screen_border=light_color,
                    this_screen_border=light_color,
                    urgent_alert_method='block'
                ),
                fc_separator(),
                widget.Prompt(),
                widget.WindowName(foreground=window_name_color),
                fc_separator(),
                #start G1
                fc_circle(color_g1,0),
                fc_icon("",color_g1,0),
                widget.ThermalSensor(
                    background = color_g1,
                    foreground = dark_color,
                    threshold = 50,
                    tag_sensor = "edge",
                    fmt = '{} '
                ),
                fc_icon("",color_g1,0),
                widget.Memory(
                    background = color_g1,
                    foreground = dark_color,
                    padding=0,
                    measure_mem="G"
                ),
                fc_circle(color_g1,1),
                #end G1
                fc_separator(),
                #start G2
                fc_circle(color_g2,0),
                fc_icon(" ", color_g2,1),
                widget.CheckUpdates(
                    background = color_g2,
                    color_have_updates=color_updates,
                    color_no_updates = "#ffffff",
                    no_update_string = "No updates",
                    display_format = "Pending: {updates}",
                    update_interval = 3600,
                ),
                fc_icon(" 龍 ",color_g2,1),
                widget.Net(
                    background = color_g2,
                    format ="{down}   {up}",
                    use_bits="true",
                    interface = net_interface
                ),
                fc_circle(color_g2,1),
                #end G2
                fc_separator(),
                #start G3
                fc_circle(color_g3,0),
                widget.Clock(
                    format="%d/%m/%Y %H:%M",
                    background = color_g3,
                    foreground= dark_color
                    ),
                fc_icon("  ",color_g3,0),
                widget.Volume(
                    background=color_g3,
                    foreground = dark_color
                ),
                fc_circle(color_g3,1),
                #end G3
                fc_separator(),
                #start G4
                fc_circle(color_g4,0),
                widget.CurrentLayoutIcon(
                    background = color_g4,
                    scale =0.70
                ),
                widget.CurrentLayout(
                    background=color_g4
                ),
                fc_circle(color_g4,1),
                #end G4
                fc_separator(),
                #start G5
                fc_circle(color_g5,0),
                fc_icon(" ", color_g5,0),
                widget.Backlight(
                    backlight_name="amdgpu_bl0", 
                    format='{percent:2.0%}',
                    background = color_g5,
                    foreground=dark_color
                    ),
                widget.Battery(
                    background = color_g5,
                    foreground = dark_color,
                    full_char=" ",
                    charge_char=" ",
                    discharge_char=" ﴅ",
                    format="{percent:2.0%} {char} ",
                    notify_below=15,
                    notification_timeout=10
                ),
                fc_circle(color_g5,1),
                #end G5
            ],
            bar_size,
            background=color_bar,
            #border_width=[4, 0, 2, 0],  # Draw top and bottom borders
            #border_color=["00000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(["control"], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag(["control"], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click(["control"], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
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
        Match(wm_class="Org.gnome.Nautilus"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

#Execute programs on startup
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])


