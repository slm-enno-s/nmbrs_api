"""Unit tests for the DebtorFunctionService class."""

import unittest
from unittest.mock import Mock

from src.nmbrs.data_classes.debtor import Function
from src.nmbrs.service.microservices.debtor import DebtorFunctionService


class TestDebtorFunctionService(unittest.TestCase):
    """Unit tests for the DebtorFunctionService class."""

    def setUp(self):
        self.mock_client = Mock()
        self.debtor_function_service = DebtorFunctionService(self.mock_client)
        self.mock_auth_header = Mock()
        self.debtor_function_service.set_auth_header(self.mock_auth_header)

    def test_delete_function(self):
        """Test deleting a function of a debtor."""
        self.debtor_function_service.delete(1, 2)
        self.mock_client.service.Function_Delete.assert_called_once_with(DebtorId=1, id=2, _soapheaders=self.mock_auth_header)

    def test_get_all_functions(self):
        """Test retrieving all functions of a debtor."""
        mock_functions = [Mock() for _ in range(3)]
        self.mock_client.service.Function_GetList.return_value = mock_functions
        result = self.debtor_function_service.get_all(1, 2)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(func, Function) for func in result))
        self.mock_client.service.Function_GetList.assert_called_once_with(DebtorId=1, id=2, _soapheaders=self.mock_auth_header)

    def test_insert_function(self):
        """Test inserting a new function for a debtor."""
        self.mock_client.service.Function_Insert.return_value = 123
        result = self.debtor_function_service.insert(1, 2, 3, "test_description")
        self.assertEqual(result, 123)
        self.mock_client.service.Function_Insert.assert_called_once_with(
            DebtorId=1,
            function={"Id": 2, "Code": 3, "Description": "test_description"},
            _soapheaders=self.mock_auth_header,
        )

    def test_update_function(self):
        """Test updating a function for a debtor."""
        self.debtor_function_service.update(1, 2, 3, "test_description")
        self.mock_client.service.Function_Update.assert_called_once_with(
            DebtorId=1,
            function={"Id": 2, "Code": 3, "Description": "test_description"},
            _soapheaders=self.mock_auth_header,
        )
