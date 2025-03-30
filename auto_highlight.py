# -*- coding: utf-8 -*-

from burp import IBurpExtender, IProxyListener
from burp import IHttpRequestResponse
import re  # For regex matching

class BurpExtender(IBurpExtender, IProxyListener):

    PRIMARY_COLOR = "orange"  # Customizable Primary Color
    SECONDARY_COLOR = "cyan"   # Customizable Secondary Color

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Auto Highlight Requests")
        callbacks.registerProxyListener(self)
        self._callbacks.printOutput("[+] Auto Highlight Requests Loaded Successfully!")

    def processProxyMessage(self, messageIsRequest, message):
        message_info = message.getMessageInfo()

        if messageIsRequest:
            self.checkAndHighlight(message_info, True)
        else:
            self.checkAndHighlight(message_info, False)

    def checkAndHighlight(self, message_info, is_request):
        request = message_info.getRequest()
        headers = self._helpers.analyzeRequest(request).getHeaders()

        for header in headers:
            if re.search(r"X-Custom-Header:\s*Primary", header):
                message_info.setHighlight(self.PRIMARY_COLOR)
                self._callbacks.printOutput("[INFO] Primary detected - Highlighted")
                break
            elif re.search(r"X-Custom-Header:\s*Secondary", header):
                message_info.setHighlight(self.SECONDARY_COLOR)
                self._callbacks.printOutput("[WARNING] Secondary detected - Highlighted")
                break
