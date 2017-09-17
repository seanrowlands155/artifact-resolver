from base_resolver.BaseResolver import *


class LocalResolver(BaseResolver):
    def __init__(self):
        BaseResolver.__init__(self)

    def resolve_artefacts(self, artefacts):
        resultsDict = {}
        for artefact in artefacts:
            # Resolve both SNAPSHOT and DEV versions incase local ws has not been updated.
            local_version = self.resolve_artefact(artefacts[artefact], "SNAPSHOT", False)
            dev_version = self.resolve_artefact(artefacts[artefact], "DEV", False)

            #If there is a local version, ensure it is higher than the highest DEV
            if local_version is not None and dev_version is not None:
                print "Resolving Snapshot vs Dev dependencies"
                dev_version = self.create_dict(dev_version)
                local_version = self.create_dict(local_version)

                if BaseResolver.get_highest_version(dev_version,local_version) == dev_version:
                    print "Uh oh someone needs to update"



