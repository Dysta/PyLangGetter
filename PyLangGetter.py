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
        else:
            return file.read()

def parse_version(version_file):
    with open(version_file, "r") as file:
        content = file.read()
    file_list = content.replace("&f=", "").replace(",", "_").split("|")
    del file_list[-1]
    return [name + ".swf" for name in file_list]

def parse_args(args):
    default_lang = {"fr", "de", "en", "it", "es", "pt", "nl"}
    if len(args) > 1 :
        del args[0]
        for arg in args:
            if arg not in default_lang:
                print("Unknow lang {}, available lang : {}".format(arg, default_lang))
                exit(0)
        return args
    else:
        return default_lang

base_url    = "http://dofusretro.cdn.ankama.com/lang/"
base_dir    = "lang/"

if __name__ == "__main__":
    lang_list = parse_args(sys.argv)
    print(f"Getting lang from this : {lang_list}")

    if not os.path.exists(base_dir + "swf/"):
        os.makedirs(base_dir + "swf/")
    
    versions_uri = base_url + "versions.swf"
    versions_dir = base_dir + "versions.swf"

    print(f"Getting file : versions.swf ({versions_uri})") 
    content = get_content_from_uri(versions_uri, False)
    write_content_to_file(versions_dir, content, True)
    countLang = 1
    countFile = 1
    
    for lang in lang_list:
        version_name = "versions_" + lang + ".txt"
        url_version  = base_url + version_name
        dir_version  = base_dir + version_name

        content = get_content_from_uri(url_version, True)
        write_content_to_file(dir_version, content, False)
        
        file_list = parse_version(dir_version)

        for file in file_list:
            url_file = base_url + "swf/" + file
            dir_file = base_dir + "swf/" + file

            print(f"[{countLang}/{len(lang_list)}][{countFile}/{len(file_list)}] Getting file {file} [{url_file}]")
            content = get_content_from_uri(url_file, False)
            write_content_to_file(dir_file, content, True)
            countFile+=1
        
        countFile = 1
        countLang+=1


