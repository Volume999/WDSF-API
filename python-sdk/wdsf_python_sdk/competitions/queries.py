from datetime import datetime
from dataclasses import dataclass
from enum import StrEnum

from wdsf_python_sdk.query import Query


class CompetitionStatus(StrEnum):
    PRE_REGISTRATION = "PreRegistration"
    REGISTERING = "Registering"
    REGISTRATION_CLOSED = "RegistrationClosed"
    PROCESSING = "Processing"
    CLOSED = "Closed"
    CANCELED = "Canceled"


@dataclass(frozen=True, kw_only=True)
class CompetitionQuery(Query):
    _from: datetime | None = None
    to: datetime | None = None
    modified_since: datetime | None = None
    world_ranking: bool | None = None
    division: str | None = None
    status: CompetitionStatus | None = None
    location: str | None = None

    def serialize(self) -> dict[str, str]:
        serialised = {
            "from": self._from,
            "to": self.to,
            "modifiedsince": self.modified_since,
            "worldranking": self.world_ranking,
            "division": self.division,
            "status": self.status,
            "location": self.location,
        }
        return {k: v for k, v in serialised.items() if v is not None}
