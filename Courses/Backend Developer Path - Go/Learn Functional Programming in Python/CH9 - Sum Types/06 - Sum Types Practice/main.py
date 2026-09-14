from enum import Enum
from typing import Any

class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


RawCSVData = list[list[object]]
PreparedCSVData = list[list[str]]
CSVStatusResult = tuple[str, PreparedCSVData | str]

# Don't touch above this line

# pyright: reportUnusedImport = hint
# pyright: reportUnreachable = hint
# pyright: reportUnnecessaryComparison = hint

from typing import cast, overload, Literal

@overload
def get_csv_status(
    status: Literal[CSVExportStatus.PENDING],
    csv: RawCSVData
) -> tuple[Literal["Pending..."], PreparedCSVData]: ...

@overload
def get_csv_status(
    status: CSVExportStatus,
    csv: PreparedCSVData
) -> tuple[str, str]: ...

def get_csv_status(
    status: CSVExportStatus,
    csv: RawCSVData | PreparedCSVData
) -> CSVStatusResult:
    match status:
        case CSVExportStatus.PENDING: # returns tuple[str, PreparedCSVData]
            return "Pending...", [ [*map(str, row)] for row in csv ]

        case CSVExportStatus.PROCESSING: # returns tuple[str, str]
            prepared = cast(PreparedCSVData, csv)
            return "Processing...", '\n'.join(','.join(row) for row in prepared)

        case CSVExportStatus.SUCCESS: # returns tuple[str, str]
            return "Success!", cast(PreparedCSVData, csv)

        case CSVExportStatus.FAILURE: # returns tuple[str, str]
            return "Unknown error, retrying...", get_csv_status(
                CSVExportStatus.PROCESSING,
                get_csv_status(
                    CSVExportStatus.PENDING,
                    cast(RawCSVData, csv)
                )[1]
            )[1]

        case _: raise Exception("unknown export status")
