def requirement_pkg(name=''):

    from importlib.metadata import distributions
    installed = distributions()

    with open(f'requirement_{name}.txt', 'w') as f:
        for i in installed:
            pkg_name = i.metadata['Name']
            pkg_ver = i.version
            f.write(f"{pkg_name}=={pkg_ver}\n")