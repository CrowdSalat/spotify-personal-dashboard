# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome_from_dict(json.loads(json_string))

from enum import Enum
from typing import Any, List, Optional, Union, TypeVar, Type, cast, Callable
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


class AlbumTypeEnum(Enum):
    ALBUM = "album"
    COMPILATION = "compilation"
    SINGLE = "single"


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


class ArtistType(Enum):
    ARTIST = "artist"


class Artist:
    external_urls: ExternalUrls
    href: str
    id: str
    name: str
    type: ArtistType
    uri: str

    def __init__(self, external_urls: ExternalUrls, href: str, id: str, name: str, type: ArtistType, uri: str) -> None:
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.name = name
        self.type = type
        self.uri = uri

    @staticmethod
    def from_dict(obj: Any) -> 'Artist':
        assert isinstance(obj, dict)
        external_urls = ExternalUrls.from_dict(obj.get("external_urls"))
        href = from_str(obj.get("href"))
        id = from_str(obj.get("id"))
        name = from_str(obj.get("name"))
        type = ArtistType(obj.get("type"))
        uri = from_str(obj.get("uri"))
        return Artist(external_urls, href, id, name, type, uri)

    def to_dict(self) -> dict:
        result: dict = {}
        result["external_urls"] = to_class(ExternalUrls, self.external_urls)
        result["href"] = from_str(self.href)
        result["id"] = from_str(self.id)
        result["name"] = from_str(self.name)
        result["type"] = to_enum(ArtistType, self.type)
        result["uri"] = from_str(self.uri)
        return result


class AvailableMarket(Enum):
    AD = "AD"
    AE = "AE"
    AR = "AR"
    AT = "AT"
    AU = "AU"
    BE = "BE"
    BG = "BG"
    BH = "BH"
    BO = "BO"
    BR = "BR"
    CA = "CA"
    CH = "CH"
    CL = "CL"
    CO = "CO"
    CR = "CR"
    CY = "CY"
    CZ = "CZ"
    DE = "DE"
    DK = "DK"
    DO = "DO"
    DZ = "DZ"
    EC = "EC"
    EE = "EE"
    EG = "EG"
    ES = "ES"
    FI = "FI"
    FR = "FR"
    GB = "GB"
    GR = "GR"
    GT = "GT"
    HK = "HK"
    HN = "HN"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IL = "IL"
    IN = "IN"
    IS = "IS"
    IT = "IT"
    JO = "JO"
    JP = "JP"
    KW = "KW"
    LB = "LB"
    LI = "LI"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    MA = "MA"
    MC = "MC"
    MT = "MT"
    MX = "MX"
    MY = "MY"
    NI = "NI"
    NL = "NL"
    NO = "NO"
    NZ = "NZ"
    OM = "OM"
    PA = "PA"
    PE = "PE"
    PH = "PH"
    PL = "PL"
    PS = "PS"
    PT = "PT"
    PY = "PY"
    QA = "QA"
    RO = "RO"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    SK = "SK"
    SV = "SV"
    TH = "TH"
    TN = "TN"
    TR = "TR"
    TW = "TW"
    US = "US"
    UY = "UY"
    VN = "VN"
    ZA = "ZA"


class CopyrightType(Enum):
    C = "C"
    P = "P"


class Copyright:
    text: str
    type: CopyrightType

    def __init__(self, text: str, type: CopyrightType) -> None:
        self.text = text
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Copyright':
        assert isinstance(obj, dict)
        text = from_str(obj.get("text"))
        type = CopyrightType(obj.get("type"))
        return Copyright(text, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_str(self.text)
        result["type"] = to_enum(CopyrightType, self.type)
        return result


class ExternalIDS:
    upc: str

    def __init__(self, upc: str) -> None:
        self.upc = upc

    @staticmethod
    def from_dict(obj: Any) -> 'ExternalIDS':
        assert isinstance(obj, dict)
        upc = from_str(obj.get("upc"))
        return ExternalIDS(upc)

    def to_dict(self) -> dict:
        result: dict = {}
        result["upc"] = from_str(self.upc)
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


class ReleaseDatePrecision(Enum):
    DAY = "day"
    YEAR = "year"


class ItemType(Enum):
    TRACK = "track"


class TracksItem:
    artists: List[Artist]
    available_markets: List[AvailableMarket]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_urls: ExternalUrls
    href: str
    id: str
    is_local: bool
    name: str
    preview_url: Optional[str]
    track_number: int
    type: ItemType
    uri: str

    def __init__(self, artists: List[Artist], available_markets: List[AvailableMarket], disc_number: int, duration_ms: int, explicit: bool, external_urls: ExternalUrls, href: str, id: str, is_local: bool, name: str, preview_url: Optional[str], track_number: int, type: ItemType, uri: str) -> None:
        self.artists = artists
        self.available_markets = available_markets
        self.disc_number = disc_number
        self.duration_ms = duration_ms
        self.explicit = explicit
        self.external_urls = external_urls
        self.href = href
        self.id = id
        self.is_local = is_local
        self.name = name
        self.preview_url = preview_url
        self.track_number = track_number
        self.type = type
        self.uri = uri

    @staticmethod
    def from_dict(obj: Any) -> 'TracksItem':
        assert isinstance(obj, dict)
        artists = from_list(Artist.from_dict, obj.get("artists"))
        available_markets = from_list(AvailableMarket, obj.get("available_markets"))
        disc_number = from_int(obj.get("disc_number"))
        duration_ms = from_int(obj.get("duration_ms"))
        explicit = from_bool(obj.get("explicit"))
        external_urls = ExternalUrls.from_dict(obj.get("external_urls"))
        href = from_str(obj.get("href"))
        id = from_str(obj.get("id"))
        is_local = from_bool(obj.get("is_local"))
        name = from_str(obj.get("name"))
        preview_url = from_union([from_none, from_str], obj.get("preview_url"))
        track_number = from_int(obj.get("track_number"))
        type = ItemType(obj.get("type"))
        uri = from_str(obj.get("uri"))
        return TracksItem(artists, available_markets, disc_number, duration_ms, explicit, external_urls, href, id, is_local, name, preview_url, track_number, type, uri)

    def to_dict(self) -> dict:
        result: dict = {}
        result["artists"] = from_list(lambda x: to_class(Artist, x), self.artists)
        result["available_markets"] = from_list(lambda x: to_enum(AvailableMarket, x), self.available_markets)
        result["disc_number"] = from_int(self.disc_number)
        result["duration_ms"] = from_int(self.duration_ms)
        result["explicit"] = from_bool(self.explicit)
        result["external_urls"] = to_class(ExternalUrls, self.external_urls)
        result["href"] = from_str(self.href)
        result["id"] = from_str(self.id)
        result["is_local"] = from_bool(self.is_local)
        result["name"] = from_str(self.name)
        result["preview_url"] = from_union([from_none, from_str], self.preview_url)
        result["track_number"] = from_int(self.track_number)
        result["type"] = to_enum(ItemType, self.type)
        result["uri"] = from_str(self.uri)
        return result


class Tracks:
    href: str
    items: List[TracksItem]
    limit: int
    next: None
    offset: int
    previous: None
    total: int

    def __init__(self, href: str, items: List[TracksItem], limit: int, next: None, offset: int, previous: None, total: int) -> None:
        self.href = href
        self.items = items
        self.limit = limit
        self.next = next
        self.offset = offset
        self.previous = previous
        self.total = total

    @staticmethod
    def from_dict(obj: Any) -> 'Tracks':
        assert isinstance(obj, dict)
        href = from_str(obj.get("href"))
        items = from_list(TracksItem.from_dict, obj.get("items"))
        limit = from_int(obj.get("limit"))
        next = from_none(obj.get("next"))
        offset = from_int(obj.get("offset"))
        previous = from_none(obj.get("previous"))
        total = from_int(obj.get("total"))
        return Tracks(href, items, limit, next, offset, previous, total)

    def to_dict(self) -> dict:
        result: dict = {}
        result["href"] = from_str(self.href)
        result["items"] = from_list(lambda x: to_class(TracksItem, x), self.items)
        result["limit"] = from_int(self.limit)
        result["next"] = from_none(self.next)
        result["offset"] = from_int(self.offset)
        result["previous"] = from_none(self.previous)
        result["total"] = from_int(self.total)
        return result


class Album:
    album_type: AlbumTypeEnum
    artists: List[Artist]
    available_markets: List[AvailableMarket]
    copyrights: List[Copyright]
    external_ids: ExternalIDS
    external_urls: ExternalUrls
    genres: List[Any]
    href: str
    id: str
    images: List[Image]
    label: str
    name: str
    popularity: int
    release_date: Union[datetime, int]
    release_date_precision: ReleaseDatePrecision
    total_tracks: int
    tracks: Tracks
    type: AlbumTypeEnum
    uri: str

    def __init__(self, album_type: AlbumTypeEnum, artists: List[Artist], available_markets: List[AvailableMarket], copyrights: List[Copyright], external_ids: ExternalIDS, external_urls: ExternalUrls, genres: List[Any], href: str, id: str, images: List[Image], label: str, name: str, popularity: int, release_date: Union[datetime, int], release_date_precision: ReleaseDatePrecision, total_tracks: int, tracks: Tracks, type: AlbumTypeEnum, uri: str) -> None:
        self.album_type = album_type
        self.artists = artists
        self.available_markets = available_markets
        self.copyrights = copyrights
        self.external_ids = external_ids
        self.external_urls = external_urls
        self.genres = genres
        self.href = href
        self.id = id
        self.images = images
        self.label = label
        self.name = name
        self.popularity = popularity
        self.release_date = release_date
        self.release_date_precision = release_date_precision
        self.total_tracks = total_tracks
        self.tracks = tracks
        self.type = type
        self.uri = uri

    @staticmethod
    def from_dict(obj: Any) -> 'Album':
        assert isinstance(obj, dict)
        album_type = AlbumTypeEnum(obj.get("album_type"))
        artists = from_list(Artist.from_dict, obj.get("artists"))
        available_markets = from_list(AvailableMarket, obj.get("available_markets"))
        copyrights = from_list(Copyright.from_dict, obj.get("copyrights"))
        external_ids = ExternalIDS.from_dict(obj.get("external_ids"))
        external_urls = ExternalUrls.from_dict(obj.get("external_urls"))
        genres = from_list(lambda x: x, obj.get("genres"))
        href = from_str(obj.get("href"))
        id = from_str(obj.get("id"))
        images = from_list(Image.from_dict, obj.get("images"))
        label = from_str(obj.get("label"))
        name = from_str(obj.get("name"))
        popularity = from_int(obj.get("popularity"))
        release_date = from_union([lambda x: from_union([from_datetime, lambda x: int(x)], from_str(x))], obj.get("release_date"))
        release_date_precision = ReleaseDatePrecision(obj.get("release_date_precision"))
        total_tracks = from_int(obj.get("total_tracks"))
        tracks = Tracks.from_dict(obj.get("tracks"))
        type = AlbumTypeEnum(obj.get("type"))
        uri = from_str(obj.get("uri"))
        return Album(album_type, artists, available_markets, copyrights, external_ids, external_urls, genres, href, id, images, label, name, popularity, release_date, release_date_precision, total_tracks, tracks, type, uri)

    def to_dict(self) -> dict:
        result: dict = {}
        result["album_type"] = to_enum(AlbumTypeEnum, self.album_type)
        result["artists"] = from_list(lambda x: to_class(Artist, x), self.artists)
        result["available_markets"] = from_list(lambda x: to_enum(AvailableMarket, x), self.available_markets)
        result["copyrights"] = from_list(lambda x: to_class(Copyright, x), self.copyrights)
        result["external_ids"] = to_class(ExternalIDS, self.external_ids)
        result["external_urls"] = to_class(ExternalUrls, self.external_urls)
        result["genres"] = from_list(lambda x: x, self.genres)
        result["href"] = from_str(self.href)
        result["id"] = from_str(self.id)
        result["images"] = from_list(lambda x: to_class(Image, x), self.images)
        result["label"] = from_str(self.label)
        result["name"] = from_str(self.name)
        result["popularity"] = from_int(self.popularity)
        result["release_date"] = from_union([lambda x: from_str((lambda x: (lambda x: is_type(datetime, x))(x).isoformat())(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.release_date)
        result["release_date_precision"] = to_enum(ReleaseDatePrecision, self.release_date_precision)
        result["total_tracks"] = from_int(self.total_tracks)
        result["tracks"] = to_class(Tracks, self.tracks)
        result["type"] = to_enum(AlbumTypeEnum, self.type)
        result["uri"] = from_str(self.uri)
        return result


class WelcomeItem:
    added_at: datetime
    album: Album

    def __init__(self, added_at: datetime, album: Album) -> None:
        self.added_at = added_at
        self.album = album

    @staticmethod
    def from_dict(obj: Any) -> 'WelcomeItem':
        assert isinstance(obj, dict)
        added_at = from_datetime(obj.get("added_at"))
        album = Album.from_dict(obj.get("album"))
        return WelcomeItem(added_at, album)

    def to_dict(self) -> dict:
        result: dict = {}
        result["added_at"] = self.added_at.isoformat()
        result["album"] = to_class(Album, self.album)
        return result


class Welcome:
    href: str
    items: List[WelcomeItem]
    limit: int
    next: str
    offset: int
    previous: None
    total: int

    def __init__(self, href: str, items: List[WelcomeItem], limit: int, next: str, offset: int, previous: None, total: int) -> None:
        self.href = href
        self.items = items
        self.limit = limit
        self.next = next
        self.offset = offset
        self.previous = previous
        self.total = total

    @staticmethod
    def from_dict(obj: Any) -> 'Welcome':
        assert isinstance(obj, dict)
        href = from_str(obj.get("href"))
        items = from_list(WelcomeItem.from_dict, obj.get("items"))
        limit = from_int(obj.get("limit"))
        next = from_str(obj.get("next"))
        offset = from_int(obj.get("offset"))
        previous = from_none(obj.get("previous"))
        total = from_int(obj.get("total"))
        return Welcome(href, items, limit, next, offset, previous, total)

    def to_dict(self) -> dict:
        result: dict = {}
        result["href"] = from_str(self.href)
        result["items"] = from_list(lambda x: to_class(WelcomeItem, x), self.items)
        result["limit"] = from_int(self.limit)
        result["next"] = from_str(self.next)
        result["offset"] = from_int(self.offset)
        result["previous"] = from_none(self.previous)
        result["total"] = from_int(self.total)
        return result


def welcome_from_dict(s: Any) -> Welcome:
    return Welcome.from_dict(s)


def welcome_to_dict(x: Welcome) -> Any:
    return to_class(Welcome, x)
