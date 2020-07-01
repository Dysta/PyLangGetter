import urllib.request as uriq
import os

url     = "http://dofusretro.cdn.ankama.com/lang/"
lang    = {"fr", "de", "en", "it", "es", "pt", "nl"}


def main():
    if not os.path.exists("lang/"):
        os.makedirs("lang/")
    for l in lang:
    v_fr = url + "versions_fr.txt"
    with uriq.urlopen(v_fr) as f:
        content = f.read().decode("utf-8")
        print(content)
    with uriq.urlopen("http://dofusretro.cdn.ankama.com/lang/swf/lang_fr_816.swf") as f:
        content = f.read()
        write_byte_to_file("lang_fr_816.swf", content)





def write_byte_to_file(filename, content):
    print("Creating filename : " + filename)
    with open("out/" + filename, "wb") as file:
        file.write(content)


if __name__ == "__main__":
    main()
