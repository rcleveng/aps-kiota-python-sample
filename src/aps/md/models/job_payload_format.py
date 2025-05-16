from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, ParseNodeHelper, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_payload_format_d_w_g import JobPayloadFormatDWG
    from .job_payload_format_i_f_c import JobPayloadFormatIFC
    from .job_payload_format_i_g_e_s import JobPayloadFormatIGES
    from .job_payload_format_o_b_j import JobPayloadFormatOBJ
    from .job_payload_format_s_t_e_p import JobPayloadFormatSTEP
    from .job_payload_format_s_t_l import JobPayloadFormatSTL
    from .job_payload_format_s_v_f import JobPayloadFormatSVF
    from .job_payload_format_s_v_f2 import JobPayloadFormatSVF2
    from .job_payload_format_thumbnail import JobPayloadFormatThumbnail

@dataclass
class JobPayloadFormat(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes JobPayloadFormatDWG, JobPayloadFormatIFC, JobPayloadFormatIGES, JobPayloadFormatOBJ, JobPayloadFormatSTEP, JobPayloadFormatSTL, JobPayloadFormatSVF, JobPayloadFormatSVF2, JobPayloadFormatThumbnail
    """
    # Composed type representation for type JobPayloadFormatDWG
    job_payload_format_d_w_g: Optional[JobPayloadFormatDWG] = None
    # Composed type representation for type JobPayloadFormatIFC
    job_payload_format_i_f_c: Optional[JobPayloadFormatIFC] = None
    # Composed type representation for type JobPayloadFormatIGES
    job_payload_format_i_g_e_s: Optional[JobPayloadFormatIGES] = None
    # Composed type representation for type JobPayloadFormatOBJ
    job_payload_format_o_b_j: Optional[JobPayloadFormatOBJ] = None
    # Composed type representation for type JobPayloadFormatSTEP
    job_payload_format_s_t_e_p: Optional[JobPayloadFormatSTEP] = None
    # Composed type representation for type JobPayloadFormatSTL
    job_payload_format_s_t_l: Optional[JobPayloadFormatSTL] = None
    # Composed type representation for type JobPayloadFormatSVF
    job_payload_format_s_v_f: Optional[JobPayloadFormatSVF] = None
    # Composed type representation for type JobPayloadFormatSVF2
    job_payload_format_s_v_f2: Optional[JobPayloadFormatSVF2] = None
    # Composed type representation for type JobPayloadFormatThumbnail
    job_payload_format_thumbnail: Optional[JobPayloadFormatThumbnail] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPayloadFormat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPayloadFormat
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        result = JobPayloadFormat()
        from .job_payload_format_d_w_g import JobPayloadFormatDWG

        result.job_payload_format_d_w_g = JobPayloadFormatDWG()
        from .job_payload_format_i_f_c import JobPayloadFormatIFC

        result.job_payload_format_i_f_c = JobPayloadFormatIFC()
        from .job_payload_format_i_g_e_s import JobPayloadFormatIGES

        result.job_payload_format_i_g_e_s = JobPayloadFormatIGES()
        from .job_payload_format_o_b_j import JobPayloadFormatOBJ

        result.job_payload_format_o_b_j = JobPayloadFormatOBJ()
        from .job_payload_format_s_t_e_p import JobPayloadFormatSTEP

        result.job_payload_format_s_t_e_p = JobPayloadFormatSTEP()
        from .job_payload_format_s_t_l import JobPayloadFormatSTL

        result.job_payload_format_s_t_l = JobPayloadFormatSTL()
        from .job_payload_format_s_v_f import JobPayloadFormatSVF

        result.job_payload_format_s_v_f = JobPayloadFormatSVF()
        from .job_payload_format_s_v_f2 import JobPayloadFormatSVF2

        result.job_payload_format_s_v_f2 = JobPayloadFormatSVF2()
        from .job_payload_format_thumbnail import JobPayloadFormatThumbnail

        result.job_payload_format_thumbnail = JobPayloadFormatThumbnail()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_payload_format_d_w_g import JobPayloadFormatDWG
        from .job_payload_format_i_f_c import JobPayloadFormatIFC
        from .job_payload_format_i_g_e_s import JobPayloadFormatIGES
        from .job_payload_format_o_b_j import JobPayloadFormatOBJ
        from .job_payload_format_s_t_e_p import JobPayloadFormatSTEP
        from .job_payload_format_s_t_l import JobPayloadFormatSTL
        from .job_payload_format_s_v_f import JobPayloadFormatSVF
        from .job_payload_format_s_v_f2 import JobPayloadFormatSVF2
        from .job_payload_format_thumbnail import JobPayloadFormatThumbnail

        if self.job_payload_format_d_w_g or self.job_payload_format_i_f_c or self.job_payload_format_i_g_e_s or self.job_payload_format_o_b_j or self.job_payload_format_s_t_e_p or self.job_payload_format_s_t_l or self.job_payload_format_s_v_f or self.job_payload_format_s_v_f2 or self.job_payload_format_thumbnail:
            return ParseNodeHelper.merge_deserializers_for_intersection_wrapper(self.job_payload_format_d_w_g, self.job_payload_format_i_f_c, self.job_payload_format_i_g_e_s, self.job_payload_format_o_b_j, self.job_payload_format_s_t_e_p, self.job_payload_format_s_t_l, self.job_payload_format_s_v_f, self.job_payload_format_s_v_f2, self.job_payload_format_thumbnail)
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value(None, self.job_payload_format_d_w_g, self.job_payload_format_i_f_c, self.job_payload_format_i_g_e_s, self.job_payload_format_o_b_j, self.job_payload_format_s_t_e_p, self.job_payload_format_s_t_l, self.job_payload_format_s_v_f, self.job_payload_format_s_v_f2, self.job_payload_format_thumbnail)
    

