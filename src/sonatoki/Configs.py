# STL
from copy import deepcopy
from typing import List, Type, TypedDict

# LOCAL
from sonatoki.Filters import (
    Filter,
    Numeric,
    Syllabic,
    NimiUCSUR,
    Alphabetic,
    ProperName,
    Punctuation,
    LongSyllabic,
    Miscellaneous,
    NimiLinkuCore,
    LongAlphabetic,
    LongProperName,
    OrMemberFilter,
    NimiLinkuCommon,
    NimiLinkuObscure,
    NimiLinkuSandbox,
    EnglishIgnorables,
    NimiLinkuUncommon,
)
from sonatoki.Scorers import Number, Scorer, PassFail, SoftScaling, SoftPassFail
from sonatoki.Cleaners import Cleaner, ConsecutiveDuplicates
from sonatoki.Tokenizers import Tokenizer, WordTokenizer
from sonatoki.Preprocessors import (
    URLs,
    Backticks,
    Reference,
    Preprocessor,
    AngleBracketObject,
)


class IloConfig(TypedDict):
    preprocessors: List[Type[Preprocessor]]
    word_tokenizer: Type[Tokenizer]
    cleaners: List[Type[Cleaner]]
    ignoring_filters: List[Type[Filter]]
    scoring_filters: List[Type[Filter]]
    scorer: Type[Scorer]
    passing_score: Number


# TODO: branching configs?

BaseConfig: IloConfig = {
    "preprocessors": [URLs],
    "cleaners": [ConsecutiveDuplicates],
    "ignoring_filters": [Numeric, Punctuation],
    "scoring_filters": [],
    "scorer": PassFail,
    "passing_score": 0.8,
    "word_tokenizer": WordTokenizer,
}


PrefConfig: IloConfig = {
    "preprocessors": [Backticks, URLs, Reference],
    "cleaners": [ConsecutiveDuplicates],
    "ignoring_filters": [Numeric, Punctuation],
    "scoring_filters": [
        OrMemberFilter(NimiLinkuCore, NimiLinkuCommon, NimiUCSUR, Miscellaneous),
        LongSyllabic,
        LongProperName,
        LongAlphabetic,
    ],
    "scorer": SoftScaling,
    "passing_score": 0.8,
    "word_tokenizer": WordTokenizer,
}

CorpusConfig: IloConfig = {
    "preprocessors": [Backticks, URLs, AngleBracketObject, Reference],
    "cleaners": [ConsecutiveDuplicates],
    "ignoring_filters": [Numeric, Punctuation],
    "scoring_filters": [
        OrMemberFilter(
            NimiLinkuCore,
            NimiLinkuCommon,
            NimiLinkuUncommon,
            NimiLinkuObscure,
            NimiLinkuSandbox,
            NimiUCSUR,
            Miscellaneous,
        ),
        LongSyllabic,
        LongProperName,
        LongAlphabetic,
    ],
    "scorer": SoftScaling,
    "passing_score": 0.8,
    "word_tokenizer": WordTokenizer,
}


"""
Mimics the previous implementation of ilo pi toki pona taso
"""
LazyConfig: IloConfig = {
    "preprocessors": [Backticks, URLs, AngleBracketObject, Reference],
    "cleaners": [ConsecutiveDuplicates],
    "ignoring_filters": [Numeric, Punctuation],
    "scoring_filters": [Alphabetic, NimiUCSUR, ProperName, Miscellaneous],
    "scorer": SoftPassFail,
    "passing_score": 0.8,
    "word_tokenizer": WordTokenizer,
}

DiscordConfig: IloConfig = {
    "preprocessors": [Backticks, URLs, AngleBracketObject, Reference],
    "cleaners": [ConsecutiveDuplicates],
    "ignoring_filters": [Numeric, Punctuation, EnglishIgnorables],
    "scoring_filters": [
        OrMemberFilter(NimiLinkuCore, NimiLinkuCommon, NimiUCSUR),
        LongSyllabic,
        LongProperName,
        LongAlphabetic,
    ],
    "scorer": SoftScaling,
    "passing_score": 0.8,
    "word_tokenizer": WordTokenizer,
}

TelegramConfig: IloConfig = deepcopy(PrefConfig)
ForumConfig: IloConfig = deepcopy(PrefConfig)

__all__ = [
    "BaseConfig",
    "CorpusConfig",
    "DiscordConfig",
    "ForumConfig",
    "IloConfig",
    "LazyConfig",
    "PrefConfig",
    "TelegramConfig",
]
