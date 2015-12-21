# -*- coding: utf-8 -*-

import os
import re
import io
import plistlib
import logging
import zipfile


class IpaFile():
    def __init__(self, application_file):
        with zipfile.ZipFile(application_file, "r") as zip_file:
            name_lists = zip_file.namelist()
            payload, app_name, blank = name_lists[1].split("/")

            code_signature_path = os.path.join("Payload", app_name, "_CodeSignature", "CodeResources")
            if not code_signature_path in name_lists:
                raise InvalidApplicationError('Ipa file is invalid.')

            plist_path = os.path.join("Payload", app_name, "Info.plist")
            if not plist_path in name_lists:
                raise NotFoundInfoPlistError('Info.plist is not found.')

            embedded_mobile_provision_path = os.path.join("Payload", app_name, "embedded.mobileprovision")
            if not embedded_mobile_provision_path in name_lists:
                raise NotFoundMobileProvisionError('embedded.mobileprovision is not found.')

            plist_content = zip_file.read(plist_path) 
            plist_stream = io.BytesIO(plist_content)
            self.info_plist = plistlib.load(plist_stream)

            provision_xml_regex = re.compile(b'<\?xml.+</plist>', re.DOTALL)
            mobile_provision_file = zip_file.read(embedded_mobile_provision_path)
            mobile_provision_content = provision_xml_regex.search(mobile_provision_file)
            mobile_provision_stream = io.BytesIO(mobile_provision_content.group())
            self.embedded_mobile_provision = plistlib.load(mobile_provision_stream)


class NotFoundInfoPlistError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class NotFoundMobileProvisionError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class InvalidApplicationError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
