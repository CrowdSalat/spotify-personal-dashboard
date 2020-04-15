# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


class Cursors:
    after: str

    def __init__(self, after: str) -> None:
        self.after = after

    @staticmethod
    def from_dict(obj: Any) -> 'Cursors':
        assert isinstance(obj, dict)
        after = from_str(obj.get("after"))
        return Cursors(after)

    def to_dict(self) -> dict:
        result: dict = {}
        result["after"] = from_str(self.after)
        return result


class ExternalUrls:
    spotify: str

    def __init__(self, spotify: str) -> None:
        self.spotify = spotify

    @staticmethod
    def from_dict(obj: Any) -> 'ExternalUrls':
        assert isinstance(obj, dict)
        spotify = from_str(obj.get("spotify"))
        return ExternalUrls(spotify)

    def to_dict(self) -> dict:
        result: dict = {}
        result["spotify"] = from_str(self.spotify)
        return result


class Followers:
    href: None
    total: int

    def __init__(self, href: None, total: int) -> None:
        self.href = href
        self.total = total

    @staticmethod
    def from_dict(obj: Any) -> 'Followers':
        assert isinstance(obj, dict)
        href = from_none(obj.get("href"))
        total = from_int(obj.get("total"))
        return Followers(href, total)

    def to_dict(self) -> dict:
        result: dict = {}
        result["href"] = from_none(self.href)
        result["total"] = from_int(self.total)
        return result


class Image:
    height: int
    url: str
    width: int

    def __init__(self, height: int, url: str, width: int) -> None:
        self.height = height
        self.url = url
        self.width = width

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        height = from_int(obj.get("height"))
        url = from_str(obj.get("url"))
        width = from_int(obj.get("width"))
        return Image(height, url, width)

    def to_dict(self) -> dict:
        result: dict = {}
        result["height"] = from_int(self.height)
        result["url"] = from_str(self.url)
        result["width"] = from_int(self.width)
        return result


class TypeEnum(Enum):
    ARTIST = "artist"


class Item:
    external_urls: ExternalUrls
    followers: Followers
    genres: List[str]
    href: str
    id: str
    images: List[Image]
    name: str
    popularity: int
    type: TypeEnum
    uri: str

    def __init__(self, external_urls: ExternalUrls, followers: Followers, genres: List[str], href: str, id: str, images: List[Image], name: str, popularity: int, type: TypeEnum, uri: str) -> None:
        self.external_urls = external_urls
        self.followers = followers
        self.genres = genres
        self.href = href
        self.id = id
        self.images = images
        self.name = name
        self.popularity = popularity
        self.type = type
        self.uri = uri

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        external_urls = ExternalUrls.from_dict(obj.get("external_urls"))
        followers = Followers.from_dict(obj.get("followers"))
        genres = from_list(from_str, obj.get("genres"))
        href = from_str(obj.get("href"))
        id = from_str(obj.get("id"))
        images = from_list(Image.from_dict, obj.get("images"))
        name = from_str(obj.get("name"))
        popularity = from_int(obj.get("popularity"))
        type = TypeEnum(obj.get("type"))
        uri = from_str(obj.get("uri"))
        return Item(external_urls, followers, genres, href, id, images, name, popularity, type, uri)

    def to_dict(self) -> dict:
        result: dict = {}
        result["external_urls"] = to_class(ExternalUrls, self.external_urls)
        result["followers"] = to_class(Followers, self.followers)
        result["genres"] = from_list(from_str, self.genres)
        result["href"] = from_str(self.href)
        result["id"] = from_str(self.id)
        result["images"] = from_list(lambda x: to_class(Image, x), self.images)
        result["name"] = from_str(self.name)
        result["popularity"] = from_int(self.popularity)
        result["type"] = to_enum(TypeEnum, self.type)
        result["uri"] = from_str(self.uri)
        return result


class Artists:
    items: List[Item]
    next: str
    total: int
    cursors: Cursors
    limit: int
    href: str

    def __init__(self, items: List[Item], next: str, total: int, cursors: Cursors, limit: int, href: str) -> None:
        self.items = items
        self.next = next
        self.total = total
        self.cursors = cursors
        self.limit = limit
        self.href = href

    @staticmethod
    def from_dict(obj: Any) -> 'Artists':
        assert isinstance(obj, dict)
        items = from_list(Item.from_dict, obj.get("items"))
        next = from_str(obj.get("next"))
        total = from_int(obj.get("total"))
        cursors = Cursors.from_dict(obj.get("cursors"))
        limit = from_int(obj.get("limit"))
        href = from_str(obj.get("href"))
        return Artists(items, next, total, cursors, limit, href)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = from_list(lambda x: to_class(Item, x), self.items)
        result["next"] = from_str(self.next)
        result["total"] = from_int(self.total)
        result["cursors"] = to_class(Cursors, self.cursors)
        result["limit"] = from_int(self.limit)
        result["href"] = from_str(self.href)
        return result


class Welcome:
    artists: Artists

    def __init__(self, artists: Artists) -> None:
        self.artists = artists

    @staticmethod
    def from_dict(obj: Any) -> 'Welcome':
        assert isinstance(obj, dict)
        artists = Artists.from_dict(obj.get("artists"))
        return Welcome(artists)

    def to_dict(self) -> dict:
        result: dict = {}
        result["artists"] = to_class(Artists, self.artists)
        return result


def welcome_from_dict(s: Any) -> Welcome:
    return Welcome.from_dict(s)


def welcome_to_dict(x: Welcome) -> Any:
    return to_class(Welcome, x)