from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CheckPermission_attributes_extension_data_permissions_details(AdditionalDataHolder, Parsable):
    """
    An object containing key value pairs, where the key represents the type of permission that was checked and the value is ``true`` if the user has permission.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The create property
    create: Optional[bool] = None
    # The download property
    download: Optional[bool] = None
    # The view property
    view: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckPermission_attributes_extension_data_permissions_details:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckPermission_attributes_extension_data_permissions_details
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckPermission_attributes_extension_data_permissions_details()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "create": lambda n : setattr(self, 'create', n.get_bool_value()),
            "download": lambda n : setattr(self, 'download', n.get_bool_value()),
            "view": lambda n : setattr(self, 'view', n.get_bool_value()),
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
        writer.write_bool_value("create", self.create)
        writer.write_bool_value("download", self.download)
        writer.write_bool_value("view", self.view)
        writer.write_additional_data_value(self.additional_data)
    

