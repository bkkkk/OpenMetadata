# generated by datamodel-codegen:
#   filename:  schema/api/services/updateMessagingService.json
#   timestamp: 2021-08-22T00:32:25+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from ...type import schedule


class UpdateMessagingServiceEntityRequest(BaseModel):
    description: Optional[str] = Field(
        None, description='Description of Messaging service entity.'
    )
    ingestionSchedule: Optional[schedule.Schedule] = Field(
        None, description='Schedule for running metadata ingestion jobs'
    )
