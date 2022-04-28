from typing import Literal
from assert_never import assert_never
from dataclasses import dataclass
from maybe import Just

# For now just an entrypoint for running experiments...


# Exercising the Maybe
mightBe = Just[str]('something')
doit = (mightBe
        .map(lambda a: a + ' else')
        .map(lambda b: b + " more")
        .getOrElseValue('no mas'))
print(doit)


# Working out a Result


@dataclass(frozen=True)
class OK:
    result: int


@dataclass(frozen=True)
class Failure:
    msg: str


Result = OK | Failure


# Exhaustive switch experiments


def showResult(r: Result) -> str:
    match r:
        case OK():
            print('its ok')
            return str(r.result)
        case Failure():
            print('fail')
            return f"""Failure: {r.msg}"""
        case _:
            assert_never(r)


@dataclass
class Doohickey:
    name: str


@dataclass
class Whatchamacallit:
    name: str


Thingy = Doohickey | Whatchamacallit

print(Thingy)


d: Doohickey = Doohickey('Bob')


def makesomething(thingy: Thingy):
    print(thingy.name)
    match thingy:
        case Doohickey():
            print('it is a doohockey')
        case Whatchamacallit():
            print('it is a whatchamacallit')
        case _:
            assert_never(thingy)


print(makesomething(Doohickey('D')))

# Experimenting with union of types
StuffKind = Literal["stuff", "things"]


class Stuff:
    def __init__(self, kind: StuffKind, name: str):
        self.kind = kind
        self.name = name

    def __str__(self):
        return f'Stuff({self.kind} {self.name})'


oneOrOther = Stuff(kind='stuff', name="socks")

match oneOrOther.kind:
    case 'stuff':
        print('stuff')
    case 'things':
        print('things')
    case _:
        assert_never(oneOrOther)
