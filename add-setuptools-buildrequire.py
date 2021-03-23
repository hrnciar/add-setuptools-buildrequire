import os
import shutil
import sys
import re
import tempfile

PYTHON3_DEVEL = [
    "BuildRequires:[ |\t]*python3-devel",
    "python%{python3_pkgversion}-devel",
    "%{libo_python}-devel", # libreoffice
    "pyproject-rpm-macros", # packages without python3-devel
]

def scan_file(spec_name):
    types_of_br = {
        "python3-(.*)": 0,
        "%{py3_dist (.*)}": 0,
        "python3dist\((.*)\)": 0,
        "python%{python3_pkgversion}-(.*)": 0,
        "%py3_dist (.*)": 0,
        "%{libo_python}-(.*)": 0, #libreoffice
    }
    inpath = f"{os.getcwd()}/rpm-specs-19-03-2021/{spec_name}.spec"
    with open(inpath, "r") as infile:
        for line in infile:
            for type_of_br in types_of_br:
                result = re.search("BuildRequires:(.*)" + type_of_br, line)
                if result:
                    types_of_br[type_of_br] += 1
    return max(types_of_br, key=types_of_br.get) + "\n"

def add_buildrequire(spec_name, type_of_br_regex):
    count = 0
    inpath = f"{os.getcwd()}/rpm-specs-19-03-2021/{spec_name}.spec"
    with tempfile.NamedTemporaryFile('w', delete=False) as outfile:
        with open(inpath, "r") as infile:
            for line in infile:
                outfile.write(line)
                for python_devel in PYTHON3_DEVEL:
                    result = re.search(python_devel, line)
                    if result:
                        count += 1
                        # get BuildRequires: and lenght of spaces between package name
                        br_substring = re.search("BuildRequires:[ |\t]*", line)
                        if br_substring:
                            # recreate new line by adding most used type of BuildRequires notation
                            updated_line = br_substring.group(0) + type_of_br_regex
                            # replace regex with setuptools
                            if type_of_br_regex == "python3dist\((.*)\)\n":
                                updated_line = updated_line.replace("\((.*)\)", "(setuptools)")
                            else:
                                updated_line = updated_line.replace("(.*)", "setuptools")
                            outfile.write(updated_line)
    if count == 1:
        shutil.move(outfile.name, inpath)
    else:
        print(f"ERROR: {spec_name}: {count}")

with open(sys.argv[1], "r") as packages:
    for package in packages:
        regex = scan_file(package.strip())
        add_buildrequire(package.strip(), regex)
