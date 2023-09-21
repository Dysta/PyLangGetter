import os
import sys

from loguru import logger

from pylanggetter.utils import Utils

_BASE_URL: str = "http://dofusretro.cdn.ankama.com%s/lang/"
_BASE_DIR: str = "data%s/lang/"


def start():
    lang_list = Utils.parse_args_langs(sys.argv)
    builds = Utils.parse_args_build(sys.argv)

    logger.info(f"Getting lang from this : {lang_list}")
    logger.info(f"Getting build from this : {builds}")

    for count_build, build in enumerate(builds, start=1):
        os.makedirs(_BASE_DIR % build + "swf/", exist_ok=True)
        versions_uri = _BASE_URL % build + "versions.swf"
        versions_dir = _BASE_DIR % build + "versions.swf"

        content = Utils.get_content_from_uri(versions_uri, False)
        Utils.write_content_to_file(versions_dir, content, True)

        for count_lang, lang in enumerate(lang_list, start=1):
            version_name = "versions_" + lang + ".txt"
            url_version = _BASE_URL % build + version_name
            dir_version = _BASE_DIR % build + version_name

            content = Utils.get_content_from_uri(url_version, True)
            Utils.write_content_to_file(dir_version, content, False)

            file_list = Utils.parse_version(dir_version)

            for count_file, file in enumerate(file_list, start=1):
                url_file = _BASE_URL % build + "swf/" + file
                dir_file = _BASE_DIR % build + "swf/" + file

                logger.info(
                    f"[{count_build}/{len(builds)}][{count_lang}/{len(lang_list)}][{count_file}/{len(file_list)}] \t === {file} - {build[1:] or 'default'}"
                )
                content = Utils.get_content_from_uri(url_file, False)
                Utils.write_content_to_file(dir_file, content, True)

    logger.success("Done. All files are in the data folder.")
