#!/usr/bin/python
import sys
import linecache

# return dependencies list for a given package
def getDeps(package):
    with open('/tmp/TMP/Packages') as PackagesFile:
        lDepPkgs = []
        for num, line in enumerate(PackagesFile, 1):
            line = line.rstrip()
            if "Package: " + package == line:
                lineDepends = linecache.getline(PackagesFile.name,num+2)
                if "Depends" in lineDepends:
                    tS = lineDepends.split(",")
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
            if len(depsNext) > 0:
                procDeps(depsNext)
            d = d + 1

# MAIN
if len(sys.argv) == 1:
    print "Pass package as parameter. Exit."
    sys.exit()

pkg = str(sys.argv[1])
deps = getDeps(pkg)
procDeps(deps)
print deps
