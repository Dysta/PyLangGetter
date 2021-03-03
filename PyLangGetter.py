import os
import sys
from utils import Utils

BASE_URL: str = "http://dofusretro.cdn.ankama.com/lang/"
BASE_DIR: str = "lang/"

if __name__ == "__main__":
    lang_list = Utils.parse_args(sys.argv)
    print(f"Getting lang from this : {lang_list}")

    if not os.path.exists(BASE_DIR + "swf/"):
        os.makedirs(BASE_DIR + "swf/")
    
    versions_uri = BASE_URL + "versions.swf"
    versions_dir = BASE_DIR + "versions.swf"

    content = Utils.get_content_from_uri(versions_uri, False)
    Utils.write_content_to_file(versions_dir, content, True)
    
    countLang = 1
    countFile = 1
    
    for lang in lang_list:
        version_name = "versions_" + lang + ".txt"
        url_version  = BASE_URL + version_name
        dir_version  = BASE_DIR + version_name

        content = Utils.get_content_from_uri(url_version, True)
        Utils.write_content_to_file(dir_version, content, False)
        
        file_list = Utils.parse_version(dir_version)

        for file in file_list:
            url_file = BASE_URL + "swf/" + file
            dir_file = BASE_DIR + "swf/" + file

            print(f"[{countLang}/{len(lang_list)}][{countFile}/{len(file_list)}] \t Get lang {file}")
            content = Utils.get_content_from_uri(url_file, False)
            Utils.write_content_to_file(dir_file, content, True)
            countFile+=1
        
        countFile = 1
        countLang+=1


