def parse_version(raw_version):
    return int("".join(map(str, raw_version)))


def parse_version_tag(version_tag):
    version_tag = version_tag.replace("v", "")
    version_tag = version_tag.replace(".", "")
    return int(version_tag)


def parse_version_arr(version_arr):
    return 'v' + ".".join(map(str, version_arr))
