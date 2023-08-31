# kanji-data
This repository provides a JSON file with kanji readings. ~13600 covered characters.
The reading data is derived from Wiktionary, accessing its {{ja-readings}} template to gather each reading and put it in its respective categories.
By this token, the data are available under the licenses specified by the Wiktionary project, namely the [Creative Commons Attribution-ShareAlike 3.0 Unported License](https://en.wiktionary.org/wiki/Wiktionary:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License) and the [GNU Free Documentation License](https://en.wiktionary.org/wiki/Wiktionary:GNU_Free_Documentation_License). You can choose which license to use contents under. I wouldn't be saying this principally, but we can't abuse the work of Wiktionarians by flouting these terms. However, the licenses are both very permissive, and loosely you can do anything with the data as long as you attribute the source, Wiktionary, and don't further restrict access to the original data in your own project. On my end, I impose no restrictions, and so the only license to worry about is whatever it says in the Wiktionary one.

## Data layout
The contents of the JSON are arranges as follows:
- The JSON is arranged as kanji-readings pairs, where each kanji is a key in the JSON object / dictionary.
- The readings are the values that correspond to the kanji key.
- The readings are a dictionary, with these possible keys:
  - goon
  - kanon
  - toon
  - soon
  - kanyoon
  - kun
  - nanori
- Each of these keys corresponds to an array of readings of that type. If there are none of that type, the value is an empty array.

Actual example data item in the JSON:
```
"生": {
    "goon": [
      "しょう"
    ],
    "kanon": [
      "せい"
    ],
    "toon": [
      "さん"
    ],
    "soon": [],
    "kanyoon": [],
    "on": [],
    "kun": [
      "は-やす",
      "うま-れる",
      "なま-",
      "う-まれる",
      "む-す",
      "き-",
      "い-きる",
      "うま-れ",
      "うぶ-",
      "い-かす",
      "は-える",
      "な-す",
      "お-う",
      "う-む",
      "い-ける",
      "な-る"
    ],
    "nanori": [
      "ふ",
      "いけ",
      "ちる",
      "そ",
      "すぎ",
      "え",
      "くるみ",
      "そう",
      "なば",
      "い",
      "み",
      "おい",
      "にう",
      "あさ",
      "うぶ",
      "さ",
      "にゅう",
      "ぎゅう",
      "もう",
      "うまい",
      "ごせ",
      "りゅう",
      "いく",
      "よい",
      "じょ",
      "いき"
    ]
```

The full data consists of many such key-value pairs.

## Notes on reading types
"Kun'yomi" is the name given to any reading of a kanji whose value is unrelated to the character's pronunciation in Chinese. These readings are effectively translations of the concepts that the kanji represent into native Japanese words (yamato kotoba). For example, the kun'yomi かたな for 刀 has nothing to do with the Middle Chinese pronunciation of that word (taw), but rather is the native Japanese word for a sword, which is what the character represents. かたな means sword, which is then applied to the 刀 character which means the same thing. However, the "effectively" in the above description is meant: 甅 can be read as センチグラム, meaning "centigram", showing that kun'yomi's actual value is in representing the _meaning_ of whatever kanji is being read, which just happens to usually take the form of a native-Japanese translation. In cases like these, where the word used as the "meaning" is not from any on'yomi pronunciation layer, it is still called kun'yomi. These days, these kinds of readings are very rare, since non-Japanese words are typically just written in katakana instead of kanji, making this reading type very scarce. センチグラム is one example of such a reading.
"Nanori" is a type of kun reading of a kanji which is used in people's names. However, just because a kanji is used in a name does not make it nanori: many names are also spelled with on'yomi or non-nanori kun'yomi. There are some readings of kanji, however, such as くるみ for 生 above, which can only be used in someone's name. These are nanori.
"On'yomi" is the name for readings whose pronunciation values are derived from (Middle) Chinese. The groups are as seen above (the ones ending in "on"): go-on (Wu sound), kan-on (Han sound), sō-on (Song sound), tō-on (Tang sound); and there's also kan'yō-on (customary sound), which deviate from any one of their actual etymological origins (one of the other on'yomi categories), often due to sound change or confusion with a similar reading.
"Go-on" was the first reading type to be borrowed from China, from the then-extant South Dynasty, starting in the 5th century AD and proceeding through the 6th. These days it is known for appearing in old, literary or scriptural terms, and is the overwhelmingly most common in old Buddhist terms.
It was closely followed by kan-on, which came about from the Tang dynasty, i.e. from the 7th century to the 9th. Both go-on and kan-on are essentially sound-borrowings from Middle Chinese, albeit different variants of it; this explains various substantial differences between them, but also why there can often be many patterns linking them, e.g. 平 can be read in go-on as びょう, but in kan-on as へい: a common observation is that go-on readings lose both their initial voicing and palatalization (yōon) in the transition to kan-on.
It should further be noted that many go-on readings have become lost to time, partly because kan-on was at times seen as more prestigious than go-on: it is theorized that go-on readings may have come to Japan via the Korean peninsula, and were thus viewed as being made impure through an additional layer of "corruption" in passing through a separate language. Thus, kan-on sounds—which were the direct result of Japanese-ordained missionaries—could have come to be seen as more upright and proper.
Indeed, however, some kan-on have also been lost, and both go-on and kan-on readings in the modern day may not be fully reliable for some characters: many readings that you will find in this dataset will have their roots in scholarly reconstruction of what the reading _probably_ was, but these are ultimately just speculation.
Wiktionary does not specify which characters are reconstructed, and indeed most dictionaries that do the reconstructions, and are thus the source of these potentially erroneous data, also don't anyway, so it should be taken with some degree of doubt whether the readings you see here are necessarily the ones used exactly back in those ages. However, it doesn't really matter, because it may be possible that new words are formed in more recent times, basing off of these selfsame reconstructions, so just because they are reconstructed does not necessarily mean they are not valuable.
Tō-on was a pronunciation layer borrowed from China during the Japanese Heian and Edo periods, which therefore spans from roughly 800 AD (Tang dynasty from 618–907) to 1800 AD (actual end of the Edo period: 1867 AD). Terms based on this form of Chinese are often based on Zen Buddhism, because they were partly relayed by Zen monks from China at this time.
Meanwhile, sō-on was borrowed from China during the Song dynasty, thus from 960 to 1279. The above two, sō-on and tō-on, are exceedingly rare, and can be found in quite rare terms, e.g. 布団 (where 布団's 団 is read as its tō-on とん); sō-on is really only a reading by name, because in reality it is ridiculously rare, even more so than tō-on: I could only find a one-digit number of terms with this reading type on Wiktionary, such as 東京 (とんきん, the northern part of Vietnam), 東 (とん, a mahjong term), 青 (しい, archaic word for an obscure mythological creature). Those are literally it. Like 3 terms. I don't know why this is even studied at this point... Tō-on, in comparison, has a lot more readings, but I would still be surprised if they added up to more than 200: I would put the figure at maybe 100-ish.

## What to use it for?
These data may be used in categorizing uncategorized readings (by way of machine-learning predictions, statistics, etc.), for statistical analyses, for learning (e.g. I will be using it for Kanken level 1), or whatever else you want, really. This is not intended to be a substitute for the much-more-comprehensive-in-other-areas [KANJIDIC](http://www.edrdg.org/wiki/index.php/KANJIDIC_Project) project, which, besides readings is a much more complete data source. It might do to fully mine Wiktionary's coverage of kanji, but altogether the Wiktionary data is often varyingly formatted, so for this rendition I opted not to go for it. Thus, whilst it was very easy to extract just the readings, profiled by type—which KANJIDIC does not distinguish, besides just kun and on—further data would be harder to garner.
