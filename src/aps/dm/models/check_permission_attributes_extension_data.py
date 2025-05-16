from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .check_permission_attributes_extension_data_permissions import CheckPermission_attributes_extension_data_permissions

@dataclass
class CheckPermission_attributes_extension_data(AdditionalDataHolder, Parsable):
    """
    A container of the results of the resourcesthat were checked for permission.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An array of objects, where each object represents a folder, item, or version that permission was checked for.
    permissions: Optional[list[CheckPermission_attributes_extension_data_permissions]] = None
    # An array of keywords where each keyword is an action that permission was checkedfor. Possible values:- ``read`` - Download and view specified resource.- ``view`` - View specified resource without downloading.- ``download`` - Download and view specified resource.- ``collaborate`` - Add comments for the specified resource.- ``write`` - Write to the specified resource.- ``upload`` - Upload to the specified resource.- ``updateMetaData`` - Update metadata of the specified resource.- ``create`` - Write and upload to the specified resource.- ``delete`` - Delete the specified resource.- ``admin`` - Perform administrative operations on specified resource.- ``share``- Share the specified resource.
    required_actions: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckPermission_attributes_extension_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckPermission_attributes_extension_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckPermission_attributes_extension_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .check_permission_attributes_extension_data_permissions import CheckPermission_attributes_extension_data_permissions

        from .check_permission_attributes_extension_data_permissions import CheckPermission_attributes_extension_data_permissions

        fields: dict[str, Callable[[Any], None]] = {
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_object_values(CheckPermission_attributes_extension_data_permissions)),
            "requiredActions": lambda n : setattr(self, 'required_actions', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("permissions", self.permissions)
        writer.write_collection_of_primitive_values("requiredActions", self.required_actions)
        writer.write_additional_data_value(self.additional_data)
    

