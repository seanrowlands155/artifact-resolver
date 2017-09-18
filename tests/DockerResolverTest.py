#!/usr/bin/python
import unittest

from docker_resolver.DockerResolver import DockerResolver
from local_resolver.LocalResolver import LocalResolver


class DockerResolverTest(unittest.TestCase):
    def test_resolver_same_env(self):
        """Test for resolving version of the same env"""
        resolver = DockerResolver()
        test_versions = ["3.0.0-DEV", "1.0.10-DEV", "2.0.20-DEV", "2.1.2-DEV"]
        self.assertEqual(
            resolver.resolve_highest_version(test_versions, "DEV", False), "3.0.0-DEV")

    def test_resolver_mixed_env(self):
        resolver = DockerResolver()

        test_versions = ["3.0.0-FEATURE", "1.0.10-DEV", "2.0.20-UAT", "2.1.2-DEV"]
        self.assertEqual(
            resolver.resolve_highest_version(test_versions, "DEV", False), "2.1.2-DEV")

    def test_resolver_snapshot(self):
        resolver = DockerResolver()

        test_versions = ["3.0.0-FEATURE", "1.0.10-DEV", "2.0.20-UAT", "3.0.1-SNAPSHOT"]
        self.assertEqual(
            resolver.resolve_highest_version(test_versions, "SNAPSHOT", False), "3.0.1-SNAPSHOT")

    def test_resolver_snapshot_missing(self):
        resolver = DockerResolver()
        test_versions = ["3.0.0-FEATURE", "1.0.10-DEV", "2.0.20-UAT", "2.1.2-DEV"]
        self.assertEqual(
            resolver.resolve_highest_version(test_versions, "SNAPSHOT", False), None)

    def test_resolver_snapshot_missing_resolve_dev(self):
        resolver = DockerResolver()
        test_versions = ["3.0.0-FEATURE", "1.0.10-DEV", "2.0.20-UAT", "2.1.2-DEV"]
        self.assertEqual(
            resolver.resolve_highest_version(test_versions, "SNAPSHOT", False), None)

    def test_highest_version(self):
        resolver = DockerResolver()
        version1 = resolver.create_dict("3.0.0-FEATURE")
        version2 = resolver.create_dict("3.0.1-DEV")

        result = resolver.get_highest_version(version1, version2)

        self.assertEqual(version2, result)


    def test_local_resolve(self):
        testData = {}
        testData['catalogue-api'] = ["1.0.1-DEV", "1.0.2-SNAPSHOT"]
        testData['hadoop'] = ["2.1.0-DEV", "3.0.1-DEV"]

        resolver = LocalResolver()

        resolver.resolve_artefacts(testData)


if __name__ == '__main__':
    unittest.main()
