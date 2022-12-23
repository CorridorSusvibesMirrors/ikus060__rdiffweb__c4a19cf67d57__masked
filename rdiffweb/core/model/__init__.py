# -*- coding: utf-8 -*-
# rdiffweb, A web interface to rdiff-backup repositories
# Copyright (C) 2012-2021 rdiffweb contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
import sys

import cherrypy
from sqlalchemy import event
from sqlalchemy.exc import IntegrityError

from ._repo import RepoObject  # noqa
from ._session import DbSession, SessionObject  # noqa
from ._token import Token  # noqa
from ._user import UserObject, user_username_index  # noqa

Base = cherrypy.tools.db.get_base()

logger = logging.getLogger(__name__)






