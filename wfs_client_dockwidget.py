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

def get_ui_class(ui_file):
    """Get UI Python class from .ui file.

    :param ui_file: The file of the ui in isochrones.gui.ui
    :type ui_file: str
    """
    ui_file_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            os.pardir,
            'WFSClient',
            ui_file
        )
    )
    return uic.loadUiType(ui_file_path)[0]

FORM_CLASS = get_ui_class('wfs_client_dialog_base.ui')


class WFSClientDockWidget(QtGui.QDialog, FORM_CLASS):

    def __init__(self, parent=None, iface=None):
        """Constructor."""
        QDialog.__init__(self, parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.parent = parent
        self.iface = iface

        self.setupUi(self)

        # Setting up progress window

        self.progress_dialog = QProgressDialog(self)
        self.progress_dialog.setAutoClose(False)
        title = self.tr('Progress')
        self.progress_dialog.setWindowTitle(title)

        self.restore_state()

        if iface:
            self.canvas = iface.mapCanvas()

    def accept(self):
        error_dialog_title = self.tr("Error")
        try:
            self.save_state()
            server_url= self.server.text()

            QApplication.instance().setOverrideCursor(Qt.BusyCursor)

            result = ""
            clientServer = "http://127.0.0.1:5000"

            # WFS 3.0  Requirement 5
            # WFS 3.0  Requirement 6

            ans = requests.get(clientServer +'/?server=' + str(server_url))

            result = result + "\n" + "Testing WFS 3.0  Requirement 2 and 3 " + str(ans.text)

            ans = requests.get(clientServer +'/links?server=' + str(server_url))

            result = result + "\n" + "Testing WFS 3.0  Requirement 7  " + str(ans.text)

            ans = requests.get(clientServer +'/http1.1?server=' + str(server_url))

            result = result + "\n" +  "Testing WFS 3.0  Requirement 4  " + str(ans.text)

            ans = requests.get(clientServer +'/etag?server=' + str(server_url))

            result = result + "\n" + "Testing WFS 3.0  Recommendation 2  " + str(ans.text)

            result = result + "Testing WFS 3.0  Requirement 5 and 6 " + ans.text

           

            result = result + "Testing WFS 3.0  Requirement 30  " + str(ans.text)

            ans = requests.get(clientServer +'/api/conformance?server=' + str(server_url))

            self.textBrowser.setText(result);

            # WFS 3.0 Requirement 7

            # WFS 3.0 Requirement 30

            # WFS 3.0 Requirement 2
            # WFS 3.0 Requirement 3

            QApplication.instance().setOverrideCursor(Qt.ArrowCursor)

            self.done(QDialog.Accepted)

        except Exception as exception:  # pylint: disable=broad-except
            sti = exception
            # noinspection PyCallByClass,PyTypeChecker,PyArgumentList
            pass
        finally:
            dialog_title = self.tr("Success")

    def restore_state(self):
        """ Read last state of GUI from configuration file."""
        settings = QSettings()
        try:
            database_name = settings.value('database', type=str)

        except TypeError:
            database_name = ''

        self.server.setText("")

    def save_state(self):
        """ Store current state of GUI to configuration file """
        settings = QSettings()


    def reject(self):
        """Redefinition of the reject() method
        """
        super (WFSClientDockWidget, self).reject()

    def display_warning_message_box(parent=None, title=None, message=None):
        """
        Display a warning message box.

        :param title: The title of the message box.
        :type title: str

        :param message: The message inside the message box.
        :type message: str
        """
        QMessageBox.warning(parent, title, message)

