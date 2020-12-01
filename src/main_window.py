#!/usr/bin/env python3

'''
   Copyright 2020 Adi Hezral (hezral@gmail.com) (https://github.com/hezral)

   This file is part of quickview ("Application").

    The Application is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    The Application is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this Application.  If not, see <http://www.gnu.org/licenses/>.
'''


import sys, os
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gio, Gdk, Granite, GObject, Pango

# quickview imports
from settings_view import SettingsView
from viewer_view import ViewerView


#------------------CLASS-SEPARATOR------------------#


class QuickviewWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #-- variables --------#
        app = self.props.application

        # setup path
        self.modulepath = os.path.dirname(__file__)

        #-- view --------#
        viewer_view = ViewerView()
        settings_view = SettingsView()
        settings_view.connect("notify::visible", self.on_view_visible)
        
        #-- stack --------#
        stack = Gtk.Stack()
        stack.props.name = "main-stack"
        stack.props.transition_type = Gtk.StackTransitionType.CROSSFADE
        
        stack.add_named(viewer_view, viewer_view.get_name())
        stack.add_named(settings_view, settings_view.get_name())
        
        #-- header --------#
        headerbar = self.generate_headerbar(settings_view=settings_view)

        #-- construct--------#
        self.props.title = "quickview"
        self.set_keep_above(True)
        self.get_style_context().add_class("rounded")
        self.set_size_request(650, 550) #set width to -1 to expand and retract based on 
        self.set_titlebar(headerbar)
        self.add(stack)
        

    def generate_headerbar(self, settings_view):
        header_label = Gtk.Label()
        header_label.props.vexpand = True
        header_label.get_style_context().add_class("header-label")

        #------ view switch ----#
        icon_theme = Gtk.IconTheme.get_default()
        # icon_theme.prepend_search_path(os.path.join(self.modulepath, "data/icons"))
        icon_theme.prepend_search_path("data/icons")
        view_switch = Granite.ModeSwitch.from_icon_name("com.github.hezral.quickview-symbolic", "preferences-system-symbolic")
        view_switch.props.primary_icon_tooltip_text = "quickview"
        view_switch.props.secondary_icon_tooltip_text = "Settings"
        view_switch.props.valign = Gtk.Align.CENTER
        view_switch.props.name = "viewswitch"
        view_switch.bind_property("active", settings_view, "visible", GObject.BindingFlags.BIDIRECTIONAL)

        #-- header construct--------#
        headerbar = Gtk.HeaderBar()
        headerbar.pack_start(header_label)
        headerbar.pack_end(view_switch)
        headerbar.props.show_close_button = True
        headerbar.props.decoration_layout = "close:maximize"
        headerbar.get_style_context().add_class("default-decoration")
        headerbar.get_style_context().add_class(Gtk.STYLE_CLASS_FLAT)
        return headerbar

    def get_window_child_widgets(self):
        window = self
        window_children = window.get_children()
        headerbar = [child for child in window_children if isinstance(child, Gtk.HeaderBar)][0]
        stack = [child for child in window_children if isinstance(child, Gtk.Stack)][0]
        return headerbar, stack

    def get_widget_child(self, class_obj):
        widget = [child for child in self.get_children() if isinstance(child, class_obj)][0]
        return widget
            
    def on_view_visible(self, view, gparam=None, runlookup=None, word=None):
        headerbar, stack = self.get_window_child_widgets()
        #header_label = [child for child in headerbar.get_children() if isinstance(child, Gtk.Label)][0]
        #header_label = self.get_widget_child(Gtk.Label)
        
        if view.is_visible():
            #header_label.props.label = "Settings"
            self.current_view = "settings-view"
            print("on:settings")

        else:
            view.hide()
            #header_label.props.label = "Workspaces"
            self.current_view = "viewer-view"
            print("on:settings-view > viewer-view")

        # toggle css styling
        if self.current_view == "settings-view":
            stack.get_style_context().add_class("stack-settings")
            headerbar.get_style_context().add_class("headerbar-settings")
        else:
            stack.get_style_context().remove_class("stack-settings")
            headerbar.get_style_context().remove_class("headerbar-settings")

        stack.set_visible_child_name(self.current_view)

