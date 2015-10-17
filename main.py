
# return depends list for a package
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

# scan manifest file for given package
def findPkgInManifest(pkg):
    with open('/tmp/TMP/manifest') as ManifestFile:
        for num, line in enumerate(ManifestFile, 1):
            p = line.split(" ")[0]
            if pkg == p:
                return 1

# MAIN
depsParted = getDeps("parted")
print depsParted
d = 0
while d < len(depsParted):
        found = findPkgInManifest(depsParted[d])
        if found == 1:
            depsParted.pop(d)
        else:
            # TODO: getDeps
            d = d + 1

print depsParted

