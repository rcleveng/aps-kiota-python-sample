from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .check_permission_payload import CheckPermissionPayload
    from .list_items_payload import ListItemsPayload
    from .list_refs_payload import ListRefsPayload
    from .publish_model_job_payload import PublishModelJobPayload
    from .publish_model_payload import PublishModelPayload
    from .publish_without_links_payload import PublishWithoutLinksPayload

@dataclass
class CommandPayload_data(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes CheckPermissionPayload, ListItemsPayload, ListRefsPayload, PublishModelJobPayload, PublishModelPayload, PublishWithoutLinksPayload
    """
    # Composed type representation for type CheckPermissionPayload
    check_permission_payload: Optional[CheckPermissionPayload] = None
    # Composed type representation for type ListItemsPayload
    list_items_payload: Optional[ListItemsPayload] = None
    # Composed type representation for type ListRefsPayload
    list_refs_payload: Optional[ListRefsPayload] = None
    # Composed type representation for type PublishModelJobPayload
    publish_model_job_payload: Optional[PublishModelJobPayload] = None
    # Composed type representation for type PublishModelPayload
    publish_model_payload: Optional[PublishModelPayload] = None
    # Composed type representation for type PublishWithoutLinksPayload
    publish_without_links_payload: Optional[PublishWithoutLinksPayload] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CommandPayload_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CommandPayload_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = CommandPayload_data()
        if mapping_value and mapping_value.casefold() == "CheckPermissionPayload".casefold():
            from .check_permission_payload import CheckPermissionPayload

            result.check_permission_payload = CheckPermissionPayload()
        elif mapping_value and mapping_value.casefold() == "ListItemsPayload".casefold():
            from .list_items_payload import ListItemsPayload

            result.list_items_payload = ListItemsPayload()
        elif mapping_value and mapping_value.casefold() == "ListRefsPayload".casefold():
            from .list_refs_payload import ListRefsPayload

            result.list_refs_payload = ListRefsPayload()
        elif mapping_value and mapping_value.casefold() == "PublishModelJobPayload".casefold():
            from .publish_model_job_payload import PublishModelJobPayload

            result.publish_model_job_payload = PublishModelJobPayload()
        elif mapping_value and mapping_value.casefold() == "PublishModelPayload".casefold():
            from .publish_model_payload import PublishModelPayload

            result.publish_model_payload = PublishModelPayload()
        elif mapping_value and mapping_value.casefold() == "PublishWithoutLinksPayload".casefold():
            from .publish_without_links_payload import PublishWithoutLinksPayload

            result.publish_without_links_payload = PublishWithoutLinksPayload()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .check_permission_payload import CheckPermissionPayload
        from .list_items_payload import ListItemsPayload
        from .list_refs_payload import ListRefsPayload
        from .publish_model_job_payload import PublishModelJobPayload
        from .publish_model_payload import PublishModelPayload
        from .publish_without_links_payload import PublishWithoutLinksPayload

        if self.check_permission_payload:
            return self.check_permission_payload.get_field_deserializers()
        if self.list_items_payload:
            return self.list_items_payload.get_field_deserializers()
        if self.list_refs_payload:
            return self.list_refs_payload.get_field_deserializers()
        if self.publish_model_job_payload:
            return self.publish_model_job_payload.get_field_deserializers()
        if self.publish_model_payload:
            return self.publish_model_payload.get_field_deserializers()
        if self.publish_without_links_payload:
            return self.publish_without_links_payload.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.check_permission_payload:
            writer.write_object_value(None, self.check_permission_payload)
        elif self.list_items_payload:
            writer.write_object_value(None, self.list_items_payload)
        elif self.list_refs_payload:
            writer.write_object_value(None, self.list_refs_payload)
        elif self.publish_model_job_payload:
            writer.write_object_value(None, self.publish_model_job_payload)
        elif self.publish_model_payload:
            writer.write_object_value(None, self.publish_model_payload)
        elif self.publish_without_links_payload:
            writer.write_object_value(None, self.publish_without_links_payload)
    

