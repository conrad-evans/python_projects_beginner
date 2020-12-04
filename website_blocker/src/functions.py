import platform
import os


class WebsiteBlocker:
    IP_ADDR = "127.0.0.1"
    HOST_PATH = R"/etc/hosts"
    HOST_PATH_WIN = R"C:\Windows\System32\drivers\etc\hosts"

    def __init__(self, url):
        self.url = url
        print(self.readFile(self.HOST_PATH))

    @staticmethod
    def readFile(path):
        with open(path, "r") as f:
            contents = f.readlines()
        return contents

    @staticmethod
    def appendFile(path, content):
        with open(path, "a+") as f:
            f.write(content)

    @staticmethod
    def checkFileDirPath(path):
        if os.path.exists(path):
            return True
        return False

    @staticmethod
    def removeNewLine(line):
        try:
            if "\n" == line[-2:]:
                return line[:-2]
        except IndexError:
            return line
        return line

    def checkIfSiteBlocked(self):
        for content in self.contents:
            content = self.removeNewLine(content)
            self.blocked_url = self.IP_ADDR + " " + self.url
            if content == self.blocked_url:
                return False, "Already blocked {}".format(self.url)
        return True, None

    def _isWindows(self):
        if platform.system() == "Windows":
            return True
        return False

    def blockWebsite(self):
        if self._isWindows() and self.checkFileDirPath(self.HOST_PATH_WIN):
            self.contents = self.readFile(self.HOST_PATH_WIN)
            site_blocked, reason = self.checkIfSiteBlocked()

            if site_blocked:
                self.appendFile(self.HOST_PATH_WIN, self.blocked_url + "\n")
                return True
            return reason

        if not self._isWindows() and self.checkFileDirPath(self.HOST_PATH):
            self.contents = self.readFile(self.HOST_PATH)
            site_blocked, reason = self.checkIfSiteBlocked()

            if site_blocked:
                self.appendFile(self.HOST_PATH, self.blocked_url + "\n")
                return True
            return reason

        return "[Error] Failed to block site"
