import os
import sys

from loguru import logger

from pylanggetter.utils import Utils

_BASE_URL: str = "http://dofusretro.cdn.ankama.com/lang/"
_BASE_DIR: str = "lang/"


def start():
    lang_list = Utils.parse_args(sys.argv)

    logger.info(f"Getting lang from this : {lang_list}")

    os.makedirs(_BASE_DIR + "swf/", exist_ok=True)

    versions_uri = _BASE_URL + "versions.swf"
    versions_dir = _BASE_DIR + "versions.swf"

    content = Utils.get_content_from_uri(versions_uri, False)
    Utils.write_content_to_file(versions_dir, content, True)

    for count_lang, lang in enumerate(lang_list, start=1):
        version_name = "versions_" + lang + ".txt"
        url_version = _BASE_URL + version_name
        dir_version = _BASE_DIR + version_name

        content = Utils.get_content_from_uri(url_version, True)
        Utils.write_content_to_file(dir_version, content, False)

        file_list = Utils.parse_version(dir_version)

        for count_file, file in enumerate(file_list, start=1):
            url_file = _BASE_URL + "swf/" + file
            dir_file = _BASE_DIR + "swf/" + file

            logger.info(
                f"[{count_lang}/{len(lang_list)}][{count_file}/{len(file_list)}] \t Get lang {file}"
            )
            content = Utils.get_content_from_uri(url_file, False)
            Utils.write_content_to_file(dir_file, content, True)
