from base_api_test import BaseAPITest
import unittest
import requests

class TestDeleteIssue(BaseAPITest):

    def test_delete_issue(self):
        issue_id = self.create_issue()
        url = self.base_url + '/issue/' + issue_id

        r = requests.delete(url, cookies=self.cookies)
        self.assertEquals(r.status_code, 200)

        r = requests.delete(url, cookies=self.cookies)
        self.assertEquals(r.status_code, 404)

    def test_delete_unexisted_issue(self):
        issue_id = 'NOTEXISTED'
        url = self.base_url + '/issue/' + issue_id

        r = requests.delete(url, cookies=self.cookies)
        self.assertEquals(r.status_code, 404)

if __name__ == '__main__':
    unittest.main()