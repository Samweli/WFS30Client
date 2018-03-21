# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WFSClient
                                 A QGIS plugin
 Client for Web Feature Service 3.0
                             -------------------
        begin                : 2018-03-07
        copyright            : (C) 2018 by Samweli Mwakisambwe
        email                : smwltwesa6@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load WFSClient class from file WFSClient.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #

    from .wfs_client import WFSClient
    import sys
    sys.path.append('/home/samweli/Setups/pycharm-5.0.1/debug-eggs/pycharm-debug.egg')
    import pydevd
    pydevd.settrace('localhost', port=54321, stdoutToServer=True, stderrToServer=True)
    return WFSClient(iface)
