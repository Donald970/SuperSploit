#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  supersploit.py
#  
#  Copyright 2024 donaldford05091997 <donaldford05091997@penguin>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
import sys
from core.start import jsdm as jdbm
from core.start import database
from core.start.input import Input
database.exmgt.updateDb("")
import os
isRunning = True
Input.config_check()

while isRunning:
    try:
        data = Input()
    except KeyboardInterrupt:
        sys.exit()
