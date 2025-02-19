#!/usr/bin/env python

import sys, os, shutil



DOWNLOADS_PATH = os.path.join(os.path.expanduser("~"), "Downloads")



def main() -> None:
    filetypes: dict[str, list[str]] = {}
    files: list[str] = os.listdir(DOWNLOADS_PATH)
    files.remove(".DS_Store")
    files.remove(".localized")

    for file in files:
        filepath: str = os.path.join(DOWNLOADS_PATH, file)
        if os.path.isdir(filepath):
            if file[:10] == "downloads_":
                contents: list[str] = os.listdir(filepath)
                if ".DS_Store" in contents:
                    contents.remove(".DS_Store")
                if ".localized" in contents:
                    contents.remove(".localized")
                if len(contents) == 0 and file[-6:] != "_empty":
                    os.rename(filepath, os.path.join(DOWNLOADS_PATH, f"{file}_empty"))
                if len(contents) > 0 and file[-6:] == "_empty":
                    os.rename(filepath, os.path.join(DOWNLOADS_PATH, f"{file[:-6]}"))
                continue
            if "folder" not in filetypes:
                filetypes["folder"] = []
            filetypes["folder"].append(file)
        elif os.path.isfile(filepath):
            filetype: str = file.split('.')[1]
            if filetype not in filetypes:
                filetypes[filetype] = []
            filetypes[filetype].append(file)
        else:
            print(f"{filepath} is neither a file nor a folder")
            sys.exit(1)

    for key, value in filetypes.items():
        folderpath: str = os.path.join(DOWNLOADS_PATH, "downloads_" + key)
        if not os.path.exists(folderpath):
            os.mkdir(folderpath)

        for file in value:
            shutil.move(os.path.join(DOWNLOADS_PATH, file), folderpath)
            


if __name__ == "__main__":
    main()
