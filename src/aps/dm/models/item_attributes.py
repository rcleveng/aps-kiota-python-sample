from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_extension_with_schema_link import Item_extension_with_schema_link

@dataclass
class ItemAttributes(AdditionalDataHolder, Parsable):
    """
    Properties of an item.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The time that the resource was created at.
    create_time: Optional[datetime.datetime] = None
    # The ID of the user that created the version.
    create_user_id: Optional[str] = None
    # The user name of the user that created the version.
    create_user_name: Optional[str] = None
    # A human friendly name to identify the item. Note that for BIM 360 projects, this attribute is reserved for future releases and should not be used. Use a version's ``attributes.name`` for the file name.
    display_name: Optional[str] = None
    # A container of additional properties that extends the default properties of this resource.
    extension: Optional[Item_extension_with_schema_link] = None
    # ``true``: The file has been deleted. ``false``: The file has not been deleted.
    hidden: Optional[bool] = None
    # The time that the version was last modified.
    last_modified_time: Optional[datetime.datetime] = None
    # The ID of the user that last modified the version.
    last_modified_user_id: Optional[str] = None
    # The user name of the user that last modified the version.
    last_modified_user_name: Optional[str] = None
    # ``true``: The file is locked.``false`` The file is not locked. **Note:** You can lock BIM 360 Project Files folder files and A360 files, but you cannot lock BIM 360 Plans Folder files.
    reserved: Optional[bool] = None
    # The time the item was reserved in the following format: ``YYYY-MM-DDThh:mm:ss.sz``.
    reserved_time: Optional[datetime.datetime] = None
    # The unique identifier of the user who reserved the item.
    reserved_user_id: Optional[str] = None
    # The name of the user who reserved the item.
    reserved_user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemAttributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemAttributes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemAttributes()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_extension_with_schema_link import Item_extension_with_schema_link

        from .item_extension_with_schema_link import Item_extension_with_schema_link

        fields: dict[str, Callable[[Any], None]] = {
            "createTime": lambda n : setattr(self, 'create_time', n.get_datetime_value()),
            "createUserId": lambda n : setattr(self, 'create_user_id', n.get_str_value()),
            "createUserName": lambda n : setattr(self, 'create_user_name', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extension": lambda n : setattr(self, 'extension', n.get_object_value(Item_extension_with_schema_link)),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "lastModifiedTime": lambda n : setattr(self, 'last_modified_time', n.get_datetime_value()),
            "lastModifiedUserId": lambda n : setattr(self, 'last_modified_user_id', n.get_str_value()),
            "lastModifiedUserName": lambda n : setattr(self, 'last_modified_user_name', n.get_str_value()),
            "reserved": lambda n : setattr(self, 'reserved', n.get_bool_value()),
            "reservedTime": lambda n : setattr(self, 'reserved_time', n.get_datetime_value()),
            "reservedUserId": lambda n : setattr(self, 'reserved_user_id', n.get_str_value()),
            "reservedUserName": lambda n : setattr(self, 'reserved_user_name', n.get_str_value()),
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
        writer.write_datetime_value("createTime", self.create_time)
        writer.write_str_value("createUserId", self.create_user_id)
        writer.write_str_value("createUserName", self.create_user_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("extension", self.extension)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_datetime_value("lastModifiedTime", self.last_modified_time)
        writer.write_str_value("lastModifiedUserId", self.last_modified_user_id)
        writer.write_str_value("lastModifiedUserName", self.last_modified_user_name)
        writer.write_bool_value("reserved", self.reserved)
        writer.write_datetime_value("reservedTime", self.reserved_time)
        writer.write_str_value("reservedUserId", self.reserved_user_id)
        writer.write_str_value("reservedUserName", self.reserved_user_name)
        writer.write_additional_data_value(self.additional_data)
    

