import os
import sys

from loguru import logger

from pylanggetter.utils import Utils

_BASE_URL: str = "http://dofusretro.cdn.ankama.com%s/lang/"
_BASE_DIR: str = "data%s/lang/"


def start():
    lang_list = Utils.parse_args_langs(sys.argv)
    builds = Utils.parse_args_build(sys.argv)

    logger.debug(f"Getting lang from this : {lang_list}")
    logger.debug(f"Getting build from this : {builds}")

    for count_build, build in enumerate(builds, start=1):
        os.makedirs(_BASE_DIR % build + "swf/", exist_ok=True)
        versions_uri = _BASE_URL % build + "versions.swf"
        versions_dir = _BASE_DIR % build + "versions.swf"

        try:
            content = Utils.get_content_from_uri(versions_uri, decode=False)
            Utils.write_content_to_file(versions_dir, content, is_byte=True)
        except Exception as e:
            logger.error(f"Error while getting versions file for build {build} at {versions_uri}: {e}")
            os.removedirs(_BASE_DIR % build + "swf/")
            continue

        for count_lang, lang in enumerate(lang_list, start=1):
            version_name = "versions_" + lang + ".txt"
            url_version = _BASE_URL % build + version_name
            dir_version = _BASE_DIR % build + version_name

            content = Utils.get_content_from_uri(url_version, decode=True)
            Utils.write_content_to_file(dir_version, content, is_byte=False)

            file_list = Utils.parse_version(dir_version)

            for count_file, file in enumerate(file_list, start=1):
                url_file = _BASE_URL % build + "swf/" + file
                dir_file = _BASE_DIR % build + "swf/" + file

                logger.info(
                    f"[{count_build}/{len(builds)}][{count_lang}/{len(lang_list)}][{count_file:02d}/{len(file_list)}] \t === {file} - {build[1:] or 'prod'}"
                )
                content = Utils.get_content_from_uri(url_file, decode=False)
                Utils.write_content_to_file(dir_file, content, is_byte=True)

    logger.success("Done. All files are in the data folder.")
