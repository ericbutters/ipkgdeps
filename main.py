#!/usr/bin/python
import sys

# return dependencies list for a given package
def getDeps(package):
    with open('/tmp/TMP/Packages') as PackagesFile:
        for num, line in enumerate(PackagesFile, 1):
            line = line.rstrip()
            if "Package: " + package == line:
                for numDepends, lineDepends in enumerate(PackagesFile,num):
                    if "Depends" in lineDepends:
                        tS = lineDepends.split(",")
                        lDepPkgs = []
                        for e in range(0,len(tS)):
                            lDepPkgs.append(tS[e].split(" ")[1])
                        return lDepPkgs
# scan manifest file for a given package
def findPkgInManifest(pkg):
    with open('/tmp/TMP/manifest') as ManifestFile:
        for num, line in enumerate(ManifestFile, 1):
            p = line.split(" ")[0]
            if pkg == p:
                return 1
# process dependencies list.
def procDeps(deps):
    d = 0
    while d < len(deps):
        found = findPkgInManifest(deps[d])
        if found == 1:
            deps.pop(d)
        else:
            pkg = ''.join(deps[d])
            depsNext = getDeps(pkg)
            procDeps(depsNext)
            if len(depsNext):
                deps.append(depsNext)
            d = d + 1

# MAIN
if len(sys.argv) == 1:
    print "Pass package as parameter. Exit."
    sys.exit()

pkg = str(sys.argv[1])
deps = getDeps(pkg)
procDeps(deps)
print deps
