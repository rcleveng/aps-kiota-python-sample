from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .begins_with import BeginsWith
    from .between import Between
    from .contains import Contains
    from .equals_to import EqualsTo
    from .greater_than import GreaterThan
    from .less_than import LessThan
    from .match_id import MatchId

@dataclass
class SpecificPropertiesPayload_query(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes BeginsWith, Between, Contains, EqualsTo, GreaterThan, LessThan, MatchId
    """
    # Composed type representation for type BeginsWith
    begins_with: Optional[BeginsWith] = None
    # Composed type representation for type Between
    between: Optional[Between] = None
    # Composed type representation for type Contains
    contains: Optional[Contains] = None
    # Composed type representation for type EqualsTo
    equals_to: Optional[EqualsTo] = None
    # Composed type representation for type GreaterThan
    greater_than: Optional[GreaterThan] = None
    # Composed type representation for type LessThan
    less_than: Optional[LessThan] = None
    # Composed type representation for type MatchId
    match_id: Optional[MatchId] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpecificPropertiesPayload_query:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpecificPropertiesPayload_query
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = SpecificPropertiesPayload_query()
        if mapping_value and mapping_value.casefold() == "BeginsWith".casefold():
            from .begins_with import BeginsWith

            result.begins_with = BeginsWith()
        elif mapping_value and mapping_value.casefold() == "Between".casefold():
            from .between import Between

            result.between = Between()
        elif mapping_value and mapping_value.casefold() == "Contains".casefold():
            from .contains import Contains

            result.contains = Contains()
        elif mapping_value and mapping_value.casefold() == "EqualsTo".casefold():
            from .equals_to import EqualsTo

            result.equals_to = EqualsTo()
        elif mapping_value and mapping_value.casefold() == "GreaterThan".casefold():
            from .greater_than import GreaterThan

            result.greater_than = GreaterThan()
        elif mapping_value and mapping_value.casefold() == "LessThan".casefold():
            from .less_than import LessThan

            result.less_than = LessThan()
        elif mapping_value and mapping_value.casefold() == "MatchId".casefold():
            from .match_id import MatchId

            result.match_id = MatchId()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .begins_with import BeginsWith
        from .between import Between
        from .contains import Contains
        from .equals_to import EqualsTo
        from .greater_than import GreaterThan
        from .less_than import LessThan
        from .match_id import MatchId

        if self.begins_with:
            return self.begins_with.get_field_deserializers()
        if self.between:
            return self.between.get_field_deserializers()
        if self.contains:
            return self.contains.get_field_deserializers()
        if self.equals_to:
            return self.equals_to.get_field_deserializers()
        if self.greater_than:
            return self.greater_than.get_field_deserializers()
        if self.less_than:
            return self.less_than.get_field_deserializers()
        if self.match_id:
            return self.match_id.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.begins_with:
            writer.write_object_value(None, self.begins_with)
        elif self.between:
            writer.write_object_value(None, self.between)
        elif self.contains:
            writer.write_object_value(None, self.contains)
        elif self.equals_to:
            writer.write_object_value(None, self.equals_to)
        elif self.greater_than:
            writer.write_object_value(None, self.greater_than)
        elif self.less_than:
            writer.write_object_value(None, self.less_than)
        elif self.match_id:
            writer.write_object_value(None, self.match_id)
    

