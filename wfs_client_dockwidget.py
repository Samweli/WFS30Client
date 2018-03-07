# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WFSClientDockWidget
                                 A QGIS plugin
 Client for Web Feature Service 3.0
                             -------------------
        begin                : 2018-03-07
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Samweli Mwakisambwe
        email                : smwltwesa6@gmail.com
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

import os

from PyQt4 import QtGui, uic
from PyQt4.QtCore import *

from PyQt4.QtGui import *
from PyQt4.QtGui import (
    QDialog,)

import requests

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'wfs_client_dockwidget_base.ui'))


class WFSClientDockWidget(QtGui.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(WFSClientDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def accept(self):
        """Create an isochrone map and display it in QGIS."""
        error_dialog_title = self.tr("Error")
        try:
            self.save_state()
            self.require_input()

            server_url= self.server.text()

            QApplication.instance().setOverrideCursor(Qt.BusyCursor)

            result = ""
            clientServer = "http://localhost:5000"

            # WFS 3.0  Requirement 5
            # WFS 3.0  Requirement 6

            result = requests.get(clientServer +'/?server=' + str(server_url))

            result = result + "\n" + requests.get(clientServer + '/api?server=' + str(server_url))

            result = result + "\n" + requests.get(clientServer +'/api/conformance?server=' + str(server_url))

            result = result + "\n" + requests.get(clientServer +'/link?server=' + str(server_url))

            result = result + "\n" + requests.get(clientServer +'/http1.1?server=' + str(server_url))

            result = result + "\n" + requests.get(clientServer +'/etag?server=' + str(server_url))

            self.textBrowser.setText(result);

            # WFS 3.0 Requirement 7

            # WFS 3.0 Requirement 30

            # WFS 3.0 Requirement 2
            # WFS 3.0 Requirement 3

            QApplication.instance().setOverrideCursor(Qt.ArrowCursor)

            self.done(QDialog.Accepted)

        except Exception as exception:  # pylint: disable=broad-except
            # noinspection PyCallByClass,PyTypeChecker,PyArgumentList
            self.display_warning_message_box(
                self, error_dialog_title, exception.message)
            pass
        finally:
            dialog_title = self.tr("Success")


    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def display_warning_message_box(parent=None, title=None, message=None):
        """
        Display a warning message box.

        :param title: The title of the message box.
        :type title: str

        :param message: The message inside the message box.
        :type message: str
        """
        QMessageBox.warning(parent, title, message)

