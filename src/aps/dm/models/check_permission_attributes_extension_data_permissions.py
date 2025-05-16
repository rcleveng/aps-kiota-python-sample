from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .check_permission_attributes_extension_data_permissions_details import CheckPermission_attributes_extension_data_permissions_details
    from .type_entity import Type_entity

@dataclass
class CheckPermission_attributes_extension_data_permissions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An object containing key value pairs, where the key represents the type of permission that was checked and the value is ``true`` if the user has permission.
    details: Optional[CheckPermission_attributes_extension_data_permissions_details] = None
    # The URN of the resource.
    id: Optional[str] = None
    # ``true`` - The user is permitted to perform all the actions checked for.``false`` - The user is not permitted to perform at least one of the actions checked for.
    permission: Optional[bool] = None
    # The type of the resource. Possible values are ``folders``, ``items``, ``versions``.
    type: Optional[Type_entity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckPermission_attributes_extension_data_permissions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckPermission_attributes_extension_data_permissions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckPermission_attributes_extension_data_permissions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .check_permission_attributes_extension_data_permissions_details import CheckPermission_attributes_extension_data_permissions_details
        from .type_entity import Type_entity

        from .check_permission_attributes_extension_data_permissions_details import CheckPermission_attributes_extension_data_permissions_details
        from .type_entity import Type_entity

        fields: dict[str, Callable[[Any], None]] = {
            "details": lambda n : setattr(self, 'details', n.get_object_value(CheckPermission_attributes_extension_data_permissions_details)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "permission": lambda n : setattr(self, 'permission', n.get_bool_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_entity)),
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
        writer.write_object_value("details", self.details)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("permission", self.permission)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

