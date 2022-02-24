# coding=utf-8
from __future__ import absolute_import

__author__ = ""
__license__ = ""
__copyright__ = ""

import json
import logging
import os
import sys
import time

import flask
import octoprint.plugin
import requests
from octoprint.events import Events, eventManager
from octoprint.filemanager import storage
from octoprint.plugin.types import OctoPrintPlugin
from octoprint.server import admin_permission
from octoprint.server.util.flask import restricted_access


class Queueplanifier(
    octoprint.plugin.StartupPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.AssetPlugin,
    octoprint.plugin.SimpleApiPlugin,
    octoprint.plugin.SettingsPlugin,
    octoprint.plugin.BlueprintPlugin,
):
    def __init__(self):
        self.commandss = 0

    def on_after_startup(self):
        self._logger.info("Starting Ricky Queuplanifier Plugin")

    def get_api_commands(self):
        self._logger.info("Manually triggered get_api")
        self.RecupereListeFichiersJson()

    def get_assets(self):
        return dict(js=["js/queueplanifier.js"], css=["css/queueplanifier.css"])

    def get_update_information(self):
        return dict(
            Queuplanifier=dict(
                displayName="Queueplanifier",
                displayVersion=self._plugin_version,
                # version check: github repository
                type="github_release",
                user="",
                repo="Queuplanifier",
                current=self._plugin_version,
                # update method: pip w/ dependency links
                pip="",
            )
        )

    def RecupereListeFichiersJson(self):
        self._logger.info("Recupere la liste des fichiers")
        # api_link = "http://octopi.local/api/files"
        # APIKEY = "4471F125CD4E4A46910CDDB643E90418"
        # Trucheaders = {"X-Api-Key": APIKEY}
        # response = requests.get(api_link, headers=Trucheaders)
        self.Dossier = octoprint.settings.Settings.getBaseFolder(self, "data")
        self._logger.info(self.Dossier)
        response = octoprint.filemanager.storage.LocalFileStorage.list_files(
            self,
            Queueplanifier.Dossier,
            filter=None,
            recursive=True,
            level=0,
            force_refresh=False,
        )

        self._logger.info(response)


__plugin_name__ = "Queueplanifier"


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = Queueplanifier()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
