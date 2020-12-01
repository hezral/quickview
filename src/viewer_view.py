#!/usr/bin/env python3

'''
   Copyright 2020 Adi Hezral (hezral@gmail.com) (https://github.com/hezral)

   This file is part of Ghoster ("Application").

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

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite, GObject

#------------------CONSTANTS------------------#

WORKSPACE_WIDTH = 384
WORKSPACE_HEIGHT = 250
WORKSPACE_RADIUS = 4

DOCK_WIDTH = 120
DOCK_HEIGHT = 10
DOCK_RADIUS = 3

PANEL_HEIGHT = 8

OVERLAY_COLOR = Gdk.RGBA(red=252 / 255.0, green=245 / 255.0, blue=213 / 255.0, alpha=0.35)


#------------------CLASS-SEPARATOR------------------#


class ViewerView(Gtk.Grid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #-- construct --------#
        self.props.name = "viewer-view"
        self.props.expand = True
        self.props.margin = 10
        self.props.margin_top = 4
        self.props.row_spacing = 15
        self.props.column_spacing = 6
        
        label = Gtk.Label("TEST")

    
        frame = Gtk.Frame()
        frame.props.expand = True
        frame.props.shadow_type = Gtk.ShadowType.ETCHED_IN
        frame.get_style_context().add_class("contents-frame")
        frame.add(label)

        self.attach(frame, 0, 1, 1, 1)




