import os
import sys
import urllib.request as urireq


class Utils:
    DEFAULT_LANG: list = ["fr", "de", "en", "it", "es", "pt", "nl"]
    DEFAULT_BUILD: dict = {
        "prod": "",
        # "beta": "/beta",
        "betaenv": "/betaenv",
        "temporis": "/temporis",
        "ephemeris2releasebucket": "/ephemeris2releasebucket",
    }

    @staticmethod
    def write_content_to_file(filename: str, content: str, isByte: bool) -> None:
        """Write content to the file filename

        Args:
            filename (str): the filename destination
            content (str): the content to write
            isByte (bool): true if the content is raw bytes, false otherwise
        """
        mode = "wb" if isByte else "w"
        with open(filename, mode) as file:
            file.write(content)

    @staticmethod
    def get_content_from_uri(uri: str, decode: bool) -> str:
        """Get the content of a file from the uri

        Args:
            uri (str): the url of the file
            decode (bool): true if decode the content in utf-8, false otherwise

        Returns:
            str: the content of the file
        """
        with urireq.urlopen(uri) as file:
            if decode:
                return file.read().decode("utf-8")
            return file.read()

    @staticmethod
    def parse_version(version_file: str) -> list:
        """Parse the given version file and return a list of the swf files

        Args:
            version_file (str): the version_*.txt to parse

        Returns:
            list: a list of swf file name
        """
        with open(version_file, "r") as file:
            content = file.read()
        file_list = content.replace("&f=", "").replace(",", "_").split("|")[:-1]
        return [f"{name}.swf" for name in file_list]

    @staticmethod
    def parse_args_langs(args: list) -> list:
        """Parse the CLI args to determine the swf lang to get

        Args:
            args (list): the list of args to parse

        Raises:
            ValueError: When a lang arg is not available

        Returns:
            list: the list of the language lang to get
        """
        args = args[1:]  # ? remove the program name
        args = [arg for arg in args if not arg.startswith("--")]

        if len(args) < 1:
            return Utils.DEFAULT_LANG

        for arg in args:
            if arg not in Utils.DEFAULT_LANG:
                raise ValueError(f"Unknow lang {arg}, available lang : {Utils.DEFAULT_LANG}")
        return args

    @staticmethod
    def parse_args_build(args: list) -> list:
        """Parse the CLI args to determine swf the build to get

        Args:
            args (list): the list of args to parse

        Raises:
            ValueError: When a build arg is not available

        Returns:
            list: the build to get
        """
        args = args[1:]  # ? remove the program name
        args = [arg for arg in args if arg.startswith("--")]
        args = [arg.replace("--", "") for arg in args]

        if len(args) < 1:
            return list(Utils.DEFAULT_BUILD.values())

        res: list = []
        for arg in args:
            if arg not in Utils.DEFAULT_BUILD:
                raise ValueError(
                    f"Unknow build {arg}, available build : {list(Utils.DEFAULT_BUILD.keys())}"
                )
            res.append(Utils.DEFAULT_BUILD[arg])

        return res
