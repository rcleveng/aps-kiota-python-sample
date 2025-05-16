from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .allow_access import AllowAccess

@dataclass
class Create_buckets_payload_allow(AdditionalDataHolder, Parsable):
    """
    An object that represents the permissions allowed for a bucket.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies the level of permission the application has. Required when ``allow`` is specified. Possible values are: - ``full`` - Unrestricted access to objects within the bucket.- ``read_only`` - Read only access to the objects within the bucket. Modification or deletion of objects is not allowed.
    access: Optional[AllowAccess] = None
    # The Client ID of the application.
    auth_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Create_buckets_payload_allow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Create_buckets_payload_allow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Create_buckets_payload_allow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .allow_access import AllowAccess

        from .allow_access import AllowAccess

        fields: dict[str, Callable[[Any], None]] = {
            "access": lambda n : setattr(self, 'access', n.get_enum_value(AllowAccess)),
            "authId": lambda n : setattr(self, 'auth_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("access", self.access)
        writer.write_str_value("authId", self.auth_id)
        writer.write_additional_data_value(self.additional_data)
    

