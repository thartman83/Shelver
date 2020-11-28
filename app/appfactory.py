###############################################################################
## appfactory.py for Shelver app module                                         ##
## Copyright (c) 2020 Tom Hartman (thomas.lees.hartman@gmail.com)            ##
##                                                                           ##
## This program is free software; you can redistribute it and/or             ##
## modify it under the terms of the GNU General Public License               ##
## as published by the Free Software Foundation; either version 2            ##
## of the License, or the License, or (at your option) any later             ##
## version.                                                                  ##
##                                                                           ##
## This program is distributed in the hope that it will be useful,           ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of            ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             ##
## GNU General Public License for more details.                              ##
###############################################################################

### Commentary ## {{{
##
## Application Factory for Shelver
##
## }}}

### appfactory ## {{{
from flask import Flask

## Return an application object of Shelver using the application
## factory pattern
def create_app(cfg):
    app = Flask(__name__)
    app.config.from_object(cfg)

    return app

## }}}
