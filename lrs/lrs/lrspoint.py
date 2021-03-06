# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LrsPlugin
                                 A QGIS plugin
 Linear reference system builder and editor
                              -------------------
        begin                : 2013-10-02
        copyright            : (C) 2013 by Radim Blažek
        email                : radim.blazek@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
# from PyQt4.QtGui import *

from .utils import *


class LrsPoint(object):
    def __init__(self, fid, routeId, measure, geo):
        self.fid = fid  # point feature id
        self.routeId = routeId
        self.measure = measure
        if self.measure is not None:
            self.measure = float(self.measure)
        # debug ( "routeId = %s %s measure = %s %s" % (routeId, type(routeId), measure, type(measure) ) )
        # original feature geo, may be multipart
        self.geo = QgsGeometry(geo)  # store copy of QgsGeometry

    def getNumParts(self):
        if not self.geo: return 0

        if self.geo.isMultipart():
            return len(self.geo.asMultiPoint())

        return 1
