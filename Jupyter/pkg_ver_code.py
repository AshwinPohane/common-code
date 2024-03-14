from importlib.metadata import distributions

installed = distributions()

with open('req.txt', 'w') as f:
    for i in installed:
        pkg_name = i.metadata['Name']
        pkg_ver = i.version
        f.write(f"{pkg_name}=={pkg_ver}\n")