from docker_registry_client import *
import re
from base_resolver.BaseResolver import *


class DockerResolver(BaseResolver):
    def __init__(self):
        BaseResolver.__init__(self)

    def get_all_in_docker(self):
        docker_client = DockerRegistryClient(host="http://localhost:5000", verify_ssl=False)
        repos = docker_client.repositories()

        results = {}

        for repo in repos:
            rep = repos[repo]
            tags = rep.tags()
            results[repo] = tags
            print tags
            self.resolve_highest_version(tags, "env")

        return len(results)
