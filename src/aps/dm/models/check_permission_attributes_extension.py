from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .check_permission_attributes_extension_data import CheckPermission_attributes_extension_data
    from .check_permission_attributes_extension_schema import CheckPermission_attributes_extension_schema
    from .type_commandtype_check_permission import Type_commandtype_CheckPermission

@dataclass
class CheckPermission_attributes_extension(AdditionalDataHolder, Parsable):
    """
    An object that contains properties specific to the CheckPermissions command,  extending the default properties of a command.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A container of the results of the resourcesthat were checked for permission.
    data: Optional[CheckPermission_attributes_extension_data] = None
    # Contains the location of the schema.
    schema: Optional[CheckPermission_attributes_extension_schema] = None
    # The Type ID of the schema used for extending properties. Must be ``commands:autodesk.core:CheckPermission`` for the CheckPermission command.
    type: Optional[Type_commandtype_CheckPermission] = None
    # The version of the schema. Must be ``1.0.0`` for the CheckPermission command. 
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckPermission_attributes_extension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckPermission_attributes_extension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckPermission_attributes_extension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .check_permission_attributes_extension_data import CheckPermission_attributes_extension_data
        from .check_permission_attributes_extension_schema import CheckPermission_attributes_extension_schema
        from .type_commandtype_check_permission import Type_commandtype_CheckPermission

        from .check_permission_attributes_extension_data import CheckPermission_attributes_extension_data
        from .check_permission_attributes_extension_schema import CheckPermission_attributes_extension_schema
        from .type_commandtype_check_permission import Type_commandtype_CheckPermission

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(CheckPermission_attributes_extension_data)),
            "schema": lambda n : setattr(self, 'schema', n.get_object_value(CheckPermission_attributes_extension_schema)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Type_commandtype_CheckPermission)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_object_value("data", self.data)
        writer.write_object_value("schema", self.schema)
        writer.write_enum_value("type", self.type)
        writer.write_str_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    

