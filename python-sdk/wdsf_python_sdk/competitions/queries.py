from datetime import datetime
from dataclasses import dataclass

from wdsf_python_sdk.competitions.models import CompetitionStatus, CompetitionDivision
from wdsf_python_sdk.lib.datetime import serialize_date, serialize_datetime
from wdsf_python_sdk.lib.serialisation import Serializer


@dataclass(frozen=True, kw_only=True)
class CompetitionQuery:
    from_: datetime | None = None
    to: datetime | None = None
    modified_since: datetime | None = None
    world_ranking: bool | None = None
    division: CompetitionDivision | None = None
    status: CompetitionStatus | None = None
    location: str | None = None


class CompetitionQuerySerializer(Serializer[CompetitionQuery]):
    @classmethod
    def serialize(cls, obj: CompetitionQuery) -> dict[str, str]:
        serialised = {
            "from": serialize_date(obj.from_),
            "to": serialize_date(obj.to),
            "modifiedsince": serialize_datetime(obj.modified_since),
            "worldranking": obj.world_ranking,
            "division": obj.division,
            "status": obj.status,
            "location": obj.location,
        }
        return {k: v for k, v in serialised.items() if v is not None}
