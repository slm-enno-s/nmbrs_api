"""Microservice responsible for bank account related actions on the company level."""

from zeep import Client

from src.nmbrs.service.microservices.micro_service import MicroService
from src.nmbrs.utils.nmbrs_exception_handler import nmbrs_exception_handler


class CompanyBankAccountService(MicroService):
    """Microservice responsible for bank account related actions on the company level."""

    def __init__(self, client: Client) -> None:
        super().__init__(client)

    def set_auth_header(self, auth_header: dict) -> None:
        self.auth_header = auth_header

    @nmbrs_exception_handler(resources=["CompanyService:BankAccount_GetCurrent"])
    def get_current(self):
        """
        Get the company's current bank account.

        For more information, refer to the official documentation:
            [BankAccount_GetCurrent](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=BankAccount_GetCurrent)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:BankAccount_Insert"])
    def insert(self):
        """
        Insert a company bank account.

        For more information, refer to the official documentation:
            [BankAccount_Insert](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=BankAccount_Insert)
        """
        raise NotImplementedError()  # pragma: no cover

    @nmbrs_exception_handler(resources=["CompanyService:BankAccount_Update"])
    def update(self):
        """
        Update the current company bank account.

        For more information, refer to the official documentation:
            [BankAccount_Update](https://api.nmbrs.nl/soap/v3/CompanyService.asmx?op=BankAccount_Update)
        """
        raise NotImplementedError()  # pragma: no cover
