#!/usr/bin/env python3
""" Unittests and integration tests """


import unittest
from unittest.mock import patch, PropertyMock
from urllib.error import HTTPError
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient Class """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, test_org_name, mock_get_json):
        """ Test org method """
        mock_get_json.return_value = {"payload": True}
        test_class = GithubOrgClient(test_org_name)
        self.assertEqual(test_class.org, mock_get_json.return_value)
        mock_get_json.assert_called_once()

    @patch('client.get_json')
    def test_public_repos_url(self):
        """ Test _public_repos_url method """
        test_org_name = "test"
        test_class = GithubOrgClient(test_org_name)
        test_class.org = {"repos_url": "test_url"}
        self.assertEqual(test_class._public_repos_url,
                         test_class.org["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test public_repos method """
        mock_get_json.return_value = [{"name": "Test"}]
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "Test"
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class.public_repos(),
                             ["Test"])
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test has_license method """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ TestIntegrationGithubOrgClient Class """
    @classmethod
    def setUpClass(cls):
        """ setUpClass method """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ tearDownClass method """
        cls.get_patcher.stop()
