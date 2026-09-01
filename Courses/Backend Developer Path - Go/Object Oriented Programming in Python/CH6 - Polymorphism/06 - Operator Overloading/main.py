from dataclasses import dataclass
from typing import TypeVar, Literal, overload

Bronze = Literal["bronze"]; Iron = Literal["iron"]; Steel = Literal["steel"] 
SwordType = Literal[Bronze, Iron, Steel]
ST = TypeVar("ST", bound=SwordType)

@dataclass(frozen=True)
class Sword[S: SwordType]:
    sword_type: S

    @overload
    def __add__(self: "Sword[Bronze]", other: "Sword[Bronze]") -> "Sword[Iron]": ...

    @overload
    def __add__(self: "Sword[Iron]", other: "Sword[Iron]") -> "Sword[Steel]": ...

    @overload
    def __add__(self: "Sword[ST]", other: "Sword[ST]") -> "Sword[Iron] | Sword[Steel]": ...

    def __add__(self, other: "Sword[ST]") -> "Sword[Iron] | Sword[Steel]":
        if self == other:
            if self.sword_type == "bronze": return Sword("iron")
            if self.sword_type == "iron": return Sword("steel")
        raise Exception("cannot craft")
