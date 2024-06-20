import unittest
import HtmlTestRunner


from tests.test_get_status import TestGetStatus
from tests.test_get_book import TestGetBook
from tests.test_get_books import TestGetBooks
from tests.test_get_order import TestGetOrder
from tests.test_get_orders import TestGetOrders
from tests.test_submit_order import TestSubmitOrder
from tests.test_update_order import TestUpdateOrder
from tests.test_delete_order import TestDeleteOrder


class TestSuite(unittest.TestCase):

    def test_suite(self):
        tests_to_run = unittest.TestSuite()

        tests_to_run.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetStatus),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetBook),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetBooks),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetOrders),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSubmitOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestUpdateOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestDeleteOrder)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="TestReport",
            report_name="SimpleBooks Test Result"
        )
        runner.run(tests_to_run)
