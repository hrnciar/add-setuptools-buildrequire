import os
import shutil
import sys
import re
import tempfile

PYTHON3_DEVEL = [
    "python3-devel",
    "python%{python3_other_pkgversion}-devel",
    "python%{python3_pkgversion}-devel",
]

def add_buildrequire(spec_name):
    count = 0
    inpath = f"{os.getcwd()}/rpm-specs-19-03-2021/{spec_name}.spec"
    with tempfile.NamedTemporaryFile('w', delete=False) as outfile:
        with open(inpath, "r") as infile:
            for line in infile:
                outfile.write(line)
                for python_devel in PYTHON3_DEVEL:
                    regex = re.compile(python_devel)
                    result = regex.search(line)
                    if result:
                        count += 1
                        updated_line = line.replace("devel", "setuptools")
                        outfile.write(updated_line)
    if count == 1:
        shutil.move(outfile.name, inpath)
    else:
        print(f"ERROR: {spec_name}: {count}")

with open(sys.argv[1], "r") as packages:
    for package in packages:
        add_buildrequire(package.strip())
