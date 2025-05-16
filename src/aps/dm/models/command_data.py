from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .check_permission import CheckPermission
    from .list_items import ListItems
    from .list_refs import ListRefs
    from .publish_model import PublishModel
    from .publish_model_job import PublishModelJob
    from .publish_without_links import PublishWithoutLinks

@dataclass
class Command_data(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes CheckPermission, ListItems, ListRefs, PublishModel, PublishModelJob, PublishWithoutLinks
    """
    # Composed type representation for type CheckPermission
    check_permission: Optional[CheckPermission] = None
    # Composed type representation for type ListItems
    list_items: Optional[ListItems] = None
    # Composed type representation for type ListRefs
    list_refs: Optional[ListRefs] = None
    # Composed type representation for type PublishModel
    publish_model: Optional[PublishModel] = None
    # Composed type representation for type PublishModelJob
    publish_model_job: Optional[PublishModelJob] = None
    # Composed type representation for type PublishWithoutLinks
    publish_without_links: Optional[PublishWithoutLinks] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Command_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Command_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = Command_data()
        if mapping_value and mapping_value.casefold() == "CheckPermission".casefold():
            from .check_permission import CheckPermission

            result.check_permission = CheckPermission()
        elif mapping_value and mapping_value.casefold() == "ListItems".casefold():
            from .list_items import ListItems

            result.list_items = ListItems()
        elif mapping_value and mapping_value.casefold() == "ListRefs".casefold():
            from .list_refs import ListRefs

            result.list_refs = ListRefs()
        elif mapping_value and mapping_value.casefold() == "PublishModel".casefold():
            from .publish_model import PublishModel

            result.publish_model = PublishModel()
        elif mapping_value and mapping_value.casefold() == "PublishModelJob".casefold():
            from .publish_model_job import PublishModelJob

            result.publish_model_job = PublishModelJob()
        elif mapping_value and mapping_value.casefold() == "PublishWithoutLinks".casefold():
            from .publish_without_links import PublishWithoutLinks

            result.publish_without_links = PublishWithoutLinks()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .check_permission import CheckPermission
        from .list_items import ListItems
        from .list_refs import ListRefs
        from .publish_model import PublishModel
        from .publish_model_job import PublishModelJob
        from .publish_without_links import PublishWithoutLinks

        if self.check_permission:
            return self.check_permission.get_field_deserializers()
        if self.list_items:
            return self.list_items.get_field_deserializers()
        if self.list_refs:
            return self.list_refs.get_field_deserializers()
        if self.publish_model:
            return self.publish_model.get_field_deserializers()
        if self.publish_model_job:
            return self.publish_model_job.get_field_deserializers()
        if self.publish_without_links:
            return self.publish_without_links.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.check_permission:
            writer.write_object_value(None, self.check_permission)
        elif self.list_items:
            writer.write_object_value(None, self.list_items)
        elif self.list_refs:
            writer.write_object_value(None, self.list_refs)
        elif self.publish_model:
            writer.write_object_value(None, self.publish_model)
        elif self.publish_model_job:
            writer.write_object_value(None, self.publish_model_job)
        elif self.publish_without_links:
            writer.write_object_value(None, self.publish_without_links)
    

