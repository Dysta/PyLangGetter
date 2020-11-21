import urllib.request as urireq
import os
import sys

def write_content_to_file(filename, content, isByte):
    mode = "wb" if isByte else "w"
    with open(filename, mode) as file:
        file.write(content)

def get_content_from_uri(uri, decode):
    with urireq.urlopen(uri) as file:
        if decode:
            return file.read().decode("utf-8")
        return file.read()

def parse_version(version_file):
    with open(version_file, "r") as file:
        content = file.read()
    file_list = content.replace("&f=", "").replace(",", "_").split("|")[:-1]
    return [f"{name}.swf" for name in file_list]

def parse_args(args):
    args = args[1:]
    default_lang = ["fr", "de", "en", "it", "es", "pt", "nl"]
    if len(args) < 1:
        return default_lang
        
    for arg in args:
        if arg not in default_lang:
            print(f"Unknow lang {arg}, available lang : {default_lang}")
            exit(0)
    return args

BASE_URL = "http://dofusretro.cdn.ankama.com/lang/"
BASE_DIR = "lang/"

if __name__ == "__main__":
    lang_list = parse_args(sys.argv)
    print(f"Getting lang from this : {lang_list}")

    if not os.path.exists(BASE_DIR + "swf/"):
        os.makedirs(BASE_DIR + "swf/")
    
    versions_uri = BASE_URL + "versions.swf"
    versions_dir = BASE_DIR + "versions.swf"

    content = get_content_from_uri(versions_uri, False)
    write_content_to_file(versions_dir, content, True)
    
    countLang = 1
    countFile = 1
    
    for lang in lang_list:
        version_name = "versions_" + lang + ".txt"
        url_version  = BASE_URL + version_name
        dir_version  = BASE_DIR + version_name

        content = get_content_from_uri(url_version, True)
        write_content_to_file(dir_version, content, False)
        
        file_list = parse_version(dir_version)

        for file in file_list:
            url_file = BASE_URL + "swf/" + file
            dir_file = BASE_DIR + "swf/" + file

            print(f"[{countLang}/{len(lang_list)}][{countFile}/{len(file_list)}] \t Get lang {file}")
            content = get_content_from_uri(url_file, False)
            write_content_to_file(dir_file, content, True)
            countFile+=1
        
        countFile = 1
        countLang+=1


