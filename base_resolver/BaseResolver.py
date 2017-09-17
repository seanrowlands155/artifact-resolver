import re

BASE_REGEX = "\d+\.\d+\.\d+-"


class BaseResolver(object):
    def __init__(self):
        pass

    def resolve_artefact(self, artefact_versions, env):
        return self.resolve_highest_version(artefact_versions, env)

    def resolve_highest_version(self, tags, env, ignore_stage):
        highest_version = None

        for tag in tags:
            if re.match(BASE_REGEX + env, tag) or ignore_stage is True:
                version_dict = BaseResolver.create_dict(tag)
                highest_version = BaseResolver.get_highest_version(highest_version, version_dict)

        return highest_version["version"] if highest_version is not None else None

    @staticmethod
    def create_dict(version):
        values = re.split('\.|-', version)
        return {"mjr": int(values[0]),
                "mnr": int(values[1]),
                "build": int(values[2]),
                "version": version}

    @staticmethod
    def get_highest_version(highest_version, version2):
        result = None
        if highest_version is not None:
            if (version2["mjr"] > highest_version["mjr"]) \
                    or (version2["mjr"] == highest_version["mjr"] and version2["mnr"]
                        > version2["mnr"]) \
                    or (version2["mjr"] == highest_version["mjr"] and version2["mnr"]
                        == version2["mnr"] and version2["build"] > highest_version["build"]):
                result = version2
            else:
                result = highest_version
        elif version2 is not None:
            result = version2

        return result
