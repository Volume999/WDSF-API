from enum import StrEnum


class CompetitionStatus(StrEnum):
    PRE_REGISTRATION = "PreRegistration"
    REGISTERING = "Registering"
    REGISTRATION_CLOSED = "RegistrationClosed"
    PROCESSING = "Processing"
    CLOSED = "Closed"
    CANCELED = "Canceled"


class CompetitionDivision(StrEnum):
    GENERAL = "General"
    PROFESSIONAL = "Professional"
