FISHES_TYPE = {
    "\N{BATTERY}": "garbage",
    "\N{SHOPPING TROLLEY}": "garbage",
    "\N{MANS SHOE}": "garbage",
    "\N{WRENCH}": "garbage",
    "\N{BABY BOTTLE}": "garbage",
    "\N{FISH}": "common",
    "\N{SHRIMP}": "common",
    "\N{CRAB}": "common",
    "\N{TROPICAL FISH}": "uncommon",
    "\N{BLOWFISH}": "uncommon",
    "\N{LOBSTER}": "uncommon",
    "\N{SQUID}": "rare",
    "\N{OCTOPUS}": "rare",
    "\N{DOLPHIN}": "rare",
    "\N{PACKAGE}\N{VARIATION SELECTOR-16}": "rare",
    "\N{SHARK}": "epic",
    "\N{SPOUTING WHALE}": "epic",
    "Locked \N{PACKAGE}\N{VARIATION SELECTOR-16}": "epic",
    "\N{DRAGON}": "legendary",
    "Legendary Locked \N{PACKAGE}\N{VARIATION SELECTOR-16}": "legendary",
    "\N{KEY}": "keys",
}

CHESTS = [
    "\N{PACKAGE}\N{VARIATION SELECTOR-16}",
    "Locked \N{PACKAGE}\N{VARIATION SELECTOR-16}",
    "Legendary Locked \N{PACKAGE}\N{VARIATION SELECTOR-16}",
]

WEEKEND_BONUS = {
    "keys": 0.0,
    "legendary": 1.4,
    "epic": 1.5,
    "rare": 1.6,
    "uncommon": 2,
    "common": 3,
    "garbage": 1.5,
}
WEATHER = {
    "\N{BLACK SUN WITH RAYS}\N{VARIATION SELECTOR-16}": {
        "keys": 0.0,
        "legendary": -0.2,
        "epic": -0.005,
        "rare": 0.0,
        "uncommon": 0.0,
        "common": 0.0,
        "garbage": 0.2,
    },
    "\N{WHITE SUN WITH SMALL CLOUD}\N{VARIATION SELECTOR-16}": {
        "keys": 0.0,
        "legendary": -0.0005,
        "epic": 0.0,
        "rare": 0.0,
        "uncommon": 0.0,
        "common": 0.2,
        "garbage": 0.0,
    },
    "\N{SUN BEHIND CLOUD}": {
        "keys": 0.0,
        "legendary": 0.0,
        "epic": 0.0,
        "rare": 0.0,
        "uncommon": 0.0,
        "common": 0.2,
        "garbage": 0.0,
    },
    "\N{WHITE SUN BEHIND CLOUD}": {
        "keys": 0.0,
        "legendary": 0.0,
        "epic": 0.0,
        "rare": 0.0,
        "uncommon": 0.0,
        "common": 0.2,
        "garbage": 0.0,
    },
    "\N{CLOUD}\N{VARIATION SELECTOR-16}": {
        "keys": 0.0,
        "legendary": 0.005,
        "epic": 0.0,
        "rare": 0.2,
        "uncommon": 0.0,
        "common": 0.0,
        "garbage": 0.0,
    },
    "\N{WHITE SUN BEHIND CLOUD WITH RAIN}\N{VARIATION SELECTOR-16}": {
        "keys": 0.0,
        "legendary": 0.0,
        "epic": 0.05,
        "rare": 0.08,
        "uncommon": 0.1,
        "common": 0.1,
        "garbage": 0.0,
    },
    "\N{CLOUD WITH RAIN}\N{VARIATION SELECTOR-16}": {
        "keys": 0.0,
        "legendary": 0.007,
        "epic": 0.01,
        "rare": 0.0,
        "uncommon": 0.0,
        "common": 0.0,
        "garbage": 0.0,
    },
    "\N{THUNDER CLOUD AND RAIN}\N{VARIATION SELECTOR-16}": {
        "keys": 0.0,
        "legendary": 0.005,
        "epic": 0.02,
        "rare": 0.0,
        "uncommon": 0.0,
        "common": 0.0,
        "garbage": 0.0,
    },
    "\N{CLOUD WITH LIGHTNING}\N{VARIATION SELECTOR-16}": {
        "keys": 0.0,
        "legendary": 0.009,
        "epic": 0.02,
        "rare": 0.0,
        "uncommon": 0.0,
        "common": 0.0,
        "garbage": 0.0,
    },
    "\N{CLOUD WITH SNOW}\N{VARIATION SELECTOR-16}": {
        "keys": 0.0,
        "legendary": 0.0,
        "epic": 0.0,
        "rare": 0.1,
        "uncommon": 0.0,
        "common": 0.0,
        "garbage": 0.2,
    },
    "\N{SNOWFLAKE}\N{VARIATION SELECTOR-16}": {
        "keys": 0.0,
        "legendary": -0.1,
        "epic": -0.1,
        "rare": -0.1,
        "uncommon": -0.1,
        "common": -0.1,
        "garbage": 0.2,
    },
    "\N{FOG}\N{VARIATION SELECTOR-16}": {
        "keys": 0.0,
        "legendary": 0.009,
        "epic": 0.0,
        "rare": 0.0,
        "uncommon": 0.0,
        "common": 0.0,
        "garbage": 0.0,
    },
    "\N{DASH SYMBOL}": {
        "keys": 0.0,
        "legendary": 0.0,
        "epic": 0.0,
        "rare": 0.0,
        "uncommon": 0.3,
        "common": 0.0,
        "garbage": 0.1,
    },
}
WEIGHT_RATES = {
    "wooden rod": {
        "keys": 0.008077544426494344,
        "legendary": 0.0016155088852988688,
        "epic": 0.0016155088852988688,
        "rare": 0.0032310177705977376,
        "uncommon": 0.09693053311793212,
        "common": 0.3231017770597738,
        "garbage": 0.5654281098546041,
    },
    "magnet rod": {
        "keys": 0.040273862263391066,
        "legendary": 0.00040273862263391066,
        "epic": 0.0008054772452678213,
        "rare": 0.03221908981071285,
        "uncommon": 0.12082158679017319,
        "common": 0.28191703584373745,
        "garbage": 0.5235602094240839,
    },
    "fly-fishing rod": {
        "keys": 0.007479431563201197,
        "legendary": 0.0007479431563201197,
        "epic": 0.0014958863126402393,
        "rare": 0.0029917726252804786,
        "uncommon": 0.08975317875841436,
        "common": 0.3739715781600598,
        "garbage": 0.5235602094240838,
    },
    "spinning rod": {
        "keys": 0.007057163020465773,
        "legendary": 0.0007057163020465773,
        "epic": 0.0014114326040931546,
        "rare": 0.0028228652081863093,
        "uncommon": 0.14114326040931546,
        "common": 0.3528581510232886,
        "garbage": 0.49400141143260407,
    },
    "harpoon": {
        "keys": 0.007552870090634442,
        "legendary": 0.0015105740181268884,
        "epic": 0.003021148036253777,
        "rare": 0.006042296072507554,
        "uncommon": 0.15105740181268884,
        "common": 0.3021148036253777,
        "garbage": 0.5287009063444109,
    },
    "telescopic rod": {
        "keys": 0.005027652086475615,
        "legendary": 0.0005027652086475615,
        "epic": 0.002011060834590246,
        "rare": 0.007038712921065862,
        "uncommon": 0.23127199597787834,
        "common": 0.4022121669180493,
        "garbage": 0.3519356460532931,
    },
    "carbon-fibre rod": {
        "keys": 0.0064226075786769435,
        "legendary": 0.0006422607578676943,
        "epic": 0.0012845215157353887,
        "rare": 0.0025690430314707774,
        "uncommon": 0.15414258188824662,
        "common": 0.3853564547206166,
        "garbage": 0.449582530507386,
    },
    "metal rod": {
        "keys": 0.00702247191011236,
        "legendary": 0.001404494382022472,
        "epic": 0.002808988764044944,
        "rare": 0.005617977528089888,
        "uncommon": 0.1404494382022472,
        "common": 0.351123595505618,
        "garbage": 0.49157303370786515,
    },
    "trusty rod": {
        "keys": 0.02244668911335578,
        "legendary": 0.005611672278338945,
        "epic": 0.006734006734006734,
        "rare": 0.01122334455667789,
        "uncommon": 0.2244668911335578,
        "common": 0.33670033670033667,
        "garbage": 0.39281705948372614,
    },
    "pikachu rod": {
        "keys": 0.08823529411764705,
        "legendary": 0.014705882352941176,
        "epic": 0.029411764705882353,
        "rare": 0.058823529411764705,
        "uncommon": 0.14705882352941177,
        "common": 0.29411764705882354,
        "garbage": 0.3676470588235294,
    },
}

RODS = [
    "wooden rod",
    "magnet rod",
    "fly-fishing rod",
    "spinning rod",
    "harpoon",
    "telescopic rod",
    "carbon-fibre rod",
    "metal rod",
    "trusty rod",
    "pikachu rod",
]
RODS_WEIGHT = [
    0.7988017973040439,
    0.06989515726410385,
    0.06989515726410385,
    0.0309535696455317,
    0.009985022466300548,
    0.009985022466300548,
    0.004992511233150274,
    0.0029955067398901645,
    0.0019970044932601095,
    0.0004992511233150274,
]
RODS_PRICES = {
    "fly-fishing rod": 85000,
    "magnet rod": 100000,
    "spinning rod": 200000,
    "harpoon": 350000,
    "telescopic rod": 420000,
    "carbon-fibre rod": 800000,
    "metal rod": 1000000,
    "trusty rod": 5000000,
    "pikachu rod": 15000000,
}

CHEST_REWARDS = {
    "\N{PACKAGE}\N{VARIATION SELECTOR-16}": {
        "wooden rod": 0.4513004504542621,
        "magnet rod": 0.06208765947124511,
        "fly-fishing rod": 0.06208765947124511,
        "spinning rod": 0.03443704499747553,
        "harpoon": 0.022590408173051156,
        "telescopic rod": 0.022590408173051156,
        "carbon-fibre rod": 0.002820627815339138,
        "metal rod": 0.0016923766892034827,
        "trusty rod": 0.0011282511261356551,
        "pikachu rod": 0.0002820627815339138,
        "cash": 0.3389830508474576,
    },
    "Locked \N{PACKAGE}\N{VARIATION SELECTOR-16}": {
        "wooden rod": 0.2518313287146192,
        "magnet rod": 0.10597030048863999,
        "fly-fishing rod": 0.10597030048863999,
        "spinning rod": 0.07044774102937536,
        "harpoon": 0.055460361582501914,
        "telescopic rod": 0.055460361582501914,
        "carbon-fibre rod": 0.03277890615823507,
        "metal rod": 0.015123490864655344,
        "trusty rod": 0.0030277228711039997,
        "pikachu rod": 0.0010059642006806577,
        "cash": 0.30292352201904654,
    },
    "Legendary Locked \N{PACKAGE}\N{VARIATION SELECTOR-16}": {
        "wooden rod": 0.04227252050883879,
        "magnet rod": 0.05707396300780143,
        "fly-fishing rod": 0.06659460826323564,
        "spinning rod": 0.12354736485365633,
        "harpoon": 0.133217735683502,
        "telescopic rod": 0.1141764451726336,
        "carbon-fibre rod": 0.08326999703876087,
        "metal rod": 0.057102482164832186,
        "trusty rod": 0.026656380757364245,
        "pikachu rod": 0.010469144886348784,
        "cash": 0.28561935766302626,
    },
}

CASH_REWARDS = {
    "\N{PACKAGE}\N{VARIATION SELECTOR-16}": [1, 254],
    "Locked \N{PACKAGE}\N{VARIATION SELECTOR-16}": [300, 1640],
    "Legendary Locked \N{PACKAGE}\N{VARIATION SELECTOR-16}": [5000, 13540],
}

RODS_SELL_PRICES = {
    "wooden rod": 350,
    "fly-fishing rod": 1500,
    "magnet rod": 1500,
    "spinning rod": 3000,
    "harpoon": 8000,
    "telescopic rod": 8000,
    "carbon-fibre rod": 15000,
    "metal rod": 25000,
    "trusty rod": 75000,
    "pikachu rod": 1000000,
}

WEIGHTS = lambda x: {
    k: [v[j] + WEATHER[x][j] for i, j in FISHES_TYPE.items()]
    for k, v in WEIGHT_RATES.items()
}
WEIGHTS_WEEKEND = lambda x: {
    k: [v[j] + WEATHER[x][j] * WEEKEND_BONUS[j] for i, j in FISHES_TYPE.items()]
    for k, v in WEIGHT_RATES.items()
}

FISHES = list(FISHES_TYPE.keys())
WEATHER_EFFECTS = list(WEATHER.keys())
ROD = "\N{FISHING POLE AND FISH}"


EVENTS = [
    "Oops. You spill all your bait into the water. You spend {amount} {currency} to buy a bucket from the shop.",
    "Your line snaps while you cast out and pay {amount} {currency} for a new spool.",
    "Your hook is blunt and you pay {amount} {currency} for a new set from the shop.",
]

LEGENDARY_PRICE = 150000
EPIC_PRICE = 6500
RARE_PRICE = 3000
UNCOMMON_PRICE = 650
COMMON_PRICE = 140
GARBAGE_PRICE = 7
