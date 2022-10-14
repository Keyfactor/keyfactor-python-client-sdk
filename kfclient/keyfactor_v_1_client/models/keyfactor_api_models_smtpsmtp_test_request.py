from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorAPIModelsSMTPSMTPTestRequest")


@attr.s(auto_attribs=True)
class KeyfactorAPIModelsSMTPSMTPTestRequest:
    """
    Attributes:
        host (Union[Unset, str]):
        id (Union[Unset, int]):
        port (Union[Unset, int]):
        relay_authentication_type (Union[Unset, int]):
        relay_password (Union[Unset, str]):
        relay_username (Union[Unset, str]):
        sender_account (Union[Unset, str]):
        sender_name (Union[Unset, str]):
        test_recipient (Union[Unset, str]):
        use_ssl (Union[Unset, bool]):
    """

    host: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    port: Union[Unset, int] = UNSET
    relay_authentication_type: Union[Unset, int] = UNSET
    relay_password: Union[Unset, str] = UNSET
    relay_username: Union[Unset, str] = UNSET
    sender_account: Union[Unset, str] = UNSET
    sender_name: Union[Unset, str] = UNSET
    test_recipient: Union[Unset, str] = UNSET
    use_ssl: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host
        id = self.id
        port = self.port
        relay_authentication_type = self.relay_authentication_type
        relay_password = self.relay_password
        relay_username = self.relay_username
        sender_account = self.sender_account
        sender_name = self.sender_name
        test_recipient = self.test_recipient
        use_ssl = self.use_ssl

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["Host"] = host
        if id is not UNSET:
            field_dict["Id"] = id
        if port is not UNSET:
            field_dict["Port"] = port
        if relay_authentication_type is not UNSET:
            field_dict["RelayAuthenticationType"] = relay_authentication_type
        if relay_password is not UNSET:
            field_dict["RelayPassword"] = relay_password
        if relay_username is not UNSET:
            field_dict["RelayUsername"] = relay_username
        if sender_account is not UNSET:
            field_dict["SenderAccount"] = sender_account
        if sender_name is not UNSET:
            field_dict["SenderName"] = sender_name
        if test_recipient is not UNSET:
            field_dict["TestRecipient"] = test_recipient
        if use_ssl is not UNSET:
            field_dict["UseSSL"] = use_ssl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("Host", UNSET)

        id = d.pop("Id", UNSET)

        port = d.pop("Port", UNSET)

        relay_authentication_type = d.pop("RelayAuthenticationType", UNSET)

        relay_password = d.pop("RelayPassword", UNSET)

        relay_username = d.pop("RelayUsername", UNSET)

        sender_account = d.pop("SenderAccount", UNSET)

        sender_name = d.pop("SenderName", UNSET)

        test_recipient = d.pop("TestRecipient", UNSET)

        use_ssl = d.pop("UseSSL", UNSET)

        keyfactor_api_models_smtpsmtp_test_request = cls(
            host=host,
            id=id,
            port=port,
            relay_authentication_type=relay_authentication_type,
            relay_password=relay_password,
            relay_username=relay_username,
            sender_account=sender_account,
            sender_name=sender_name,
            test_recipient=test_recipient,
            use_ssl=use_ssl,
        )

        keyfactor_api_models_smtpsmtp_test_request.additional_properties = d
        return keyfactor_api_models_smtpsmtp_test_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
