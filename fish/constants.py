FISHES_TYPE = {
    "\N{BATTERY}": "garbage",
    "\N{SHOPPING TROLLEY}": "garbage",
    "\N{MANS SHOE}": "garbage",
    "\N{WRENCH}": "garbage",
    "\N{BONE}": "garbage",
    "\N{BILLED CAP}": "garbage",
    "\N{BRIEFS}": "garbage",
    "\N{SOCKS}": "garbage",
    "\N{ICE HOCKEY STICK AND PUCK}": "garbage",
    "\N{TRUMPET}": "garbage",
    "\N{KITE}": "garbage",
    "\N{BICYCLE}": "garbage",
    "\N{MONEY BAG}": "garbage",
    "\N{TEDDY BEAR}": "garbage",
    "\N{SPONGE}": "garbage",
    "\N{OIL DRUM}\N{VARIATION SELECTOR-16}": "garbage",
    "\N{BRIEFCASE}": "garbage",
    "\N{BABY BOTTLE}": "garbage",
    "\N{FISH}": "common",
    "\N{SHRIMP}": "common",
    "\N{CRAB}": "common",
    "\N{DIVING MASK}": "common",
    "\N{HANDBAG}": "common",
    "\N{SPIRAL SHELL}": "common",
    "\N{SNAIL}": "common",
    "\N{BUG}": "common",
    "\N{FROG FACE}": "common",
    "\N{BIKINI}": "common",
    "\N{TROPICAL FISH}": "uncommon",
    "\N{BLOWFISH}": "uncommon",
    "\N{OTTER}": "uncommon",
    "\N{DUCK}": "uncommon",
    "\N{LIZARD}": "uncommon",
    "\N{LOBSTER}": "uncommon",
    "\N{SQUID}": "rare",
    "\N{OCTOPUS}": "rare",
    "\N{FLAMINGO}": "rare",
    "\N{SWAN}": "rare",
    "\N{DOLPHIN}": "rare",
    "\N{SHARK}": "epic",
    "\N{SPOUTING WHALE}": "epic",
    "\N{CROCODILE}": "epic",
    "\N{RING}": "epic",
    "\N{HIPPOPOTAMUS}": "epic",
    "\N{OYSTER}": "epic",
    "\N{CROWN}": "legendary",
    "\N{DRAGON}": "legendary",
}

WEEKEND_BONUS = {
    "legendary": 1.4,
    "epic": 1.5,
    "rare": 1.6,
    "uncommon": 2,
    "common": 3,
    "garbage": 1.5,
}

WEATHER = {
    "\N{BLACK SUN WITH RAYS}\N{VARIATION SELECTOR-16}": {
        "legendary": 0.0,
        "epic": 0.0,
        "rare": 0.0,
        "uncommon": 0.2,
        "common": 0.0,
        "garbage": 0.0,
    },
    "\N{WHITE SUN WITH SMALL CLOUD}\N{VARIATION SELECTOR-16}": {
        "legendary": 0.0,
        "epic": 0.0,
        "rare": 0.0,
        "uncommon": 0.0,
        "common": 0.2,
        "garbage": 0.0,
    },
    "\N{SUN BEHIND CLOUD}": {
        "legendary": 0.0,
        "epic": 0.0,
        "rare": 0.0,
        "uncommon": 0.0,
        "common": 0.2,
        "garbage": 0.0,
    },
    "\N{WHITE SUN BEHIND CLOUD}": {
        "legendary": 0.0,
        "epic": 0.0,
        "rare": 0.0,
        "uncommon": 0.0,
        "common": 0.2,
        "garbage": 0.0,
    },
    "\N{CLOUD}\N{VARIATION SELECTOR-16}": {
        "legendary": 0.0,
        "epic": 0.0,
        "rare": 0.2,
        "uncommon": 0.0,
        "common": 0.0,
        "garbage": 0.0,
    },
    "\N{WHITE SUN BEHIND CLOUD WITH RAIN}\N{VARIATION SELECTOR-16}": {
        "legendary": 0.0,
        "epic": 0.1,
        "rare": 0.2,
        "uncommon": 0.0,
        "common": 0.0,
        "garbage": 0.0,
    },
    "\N{CLOUD WITH RAIN}\N{VARIATION SELECTOR-16}": {
        "legendary": 0.1,
        "epic": 0.2,
        "rare": 0.0,
        "uncommon": 0.0,
        "common": 0.0,
        "garbage": 0.0,
    },
    "\N{THUNDER CLOUD AND RAIN}\N{VARIATION SELECTOR-16}": {
        "legendary": 0.3,
        "epic": 0.3,
        "rare": 0.0,
        "uncommon": 0.0,
        "common": 0.0,
        "garbage": 0.0,
    },
    "\N{CLOUD WITH LIGHTNING}\N{VARIATION SELECTOR-16}": {
        "legendary": 0.2,
        "epic": 0.1,
        "rare": 0.0,
        "uncommon": 0.0,
        "common": 0.0,
        "garbage": 0.0,
    },
    "\N{CLOUD WITH SNOW}\N{VARIATION SELECTOR-16}": {
        "legendary": 0.0,
        "epic": 0.0,
        "rare": 0.1,
        "uncommon": 0.0,
        "common": 0.0,
        "garbage": 0.2,
    },
    "\N{SNOWFLAKE}\N{VARIATION SELECTOR-16}": {
        "legendary": -0.1,
        "epic": -0.1,
        "rare": -0.1,
        "uncommon": -0.1,
        "common": -0.1,
        "garbage": 0.2,
    },
    "\N{FOG}\N{VARIATION SELECTOR-16}": {
        "legendary": 0.05,
        "epic": 0.0,
        "rare": 0.0,
        "uncommon": 0.0,
        "common": 0.0,
        "garbage": 0.0,
    },
    "\N{DASH SYMBOL}": {
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
        "legendary": 0.001,
        "epic": 0.001,
        "rare": 0.002,
        "uncommon": 0.06,
        "common": 0.2,
        "garbage": 0.35,
    },
    "magnet rod": {
        "legendary": 0.0005,
        "epic": 0.001,
        "rare": 0.04,
        "uncommon": 0.15,
        "common": 0.35,
        "garbage": 0.65,
    },
    "fly-fishing rod": {
        "legendary": 0.0005,
        "epic": 0.001,
        "rare": 0.002,
        "uncommon": 0.06,
        "common": 0.25,
        "garbage": 0.35,
    },
    "spinning rod": {
        "legendary": 0.0005,
        "epic": 0.001,
        "rare": 0.002,
        "uncommon": 0.1,
        "common": 0.25,
        "garbage": 0.35,
    },
    "harpoon": {
        "legendary": 0.001,
        "epic": 0.002,
        "rare": 0.004,
        "uncommon": 0.1,
        "common": 0.2,
        "garbage": 0.35,
    },
    "telescopic rod": {
        "legendary": 0.0005,
        "epic": 0.002,
        "rare": 0.007,
        "uncommon": 0.23,
        "common": 0.4,
        "garbage": 0.35,
    },
    "carbon-fibre rod": {
        "legendary": 0.0005,
        "epic": 0.001,
        "rare": 0.002,
        "uncommon": 0.12,
        "common": 0.3,
        "garbage": 0.35,
    },
    "metal rod": {
        "legendary": 0.001,
        "epic": 0.002,
        "rare": 0.004,
        "uncommon": 0.1,
        "common": 0.25,
        "garbage": 0.35,
    },
    "trusty rod": {
        "legendary": 0.0015,
        "epic": 0.003,
        "rare": 0.006,
        "uncommon": 0.2,
        "common": 0.3,
        "garbage": 0.35,
    },
    "pikachu rod": {
        "legendary": 0.01,
        "epic": 0.02,
        "rare": 0.04,
        "uncommon": 0.1,
        "common": 0.2,
        "garbage": 0.25,
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
RODS_WEIGHT = [0.80, 0.07, 0.07, 0.031, 0.01, 0.01, 0.005, 0.0003, 0.003, 0.001]
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

STORMY_WEATHER = ["\N{THUNDER CLOUD AND RAIN}\N{VARIATION SELECTOR-16}", "\N{CLOUD WITH LIGHTNING}\N{VARIATION SELECTOR-16}"]

EVENTS = [
    "Oops. You spill all your bait into the water. You spend {amount} {currency} to buy a bucket from the shop.",
    "Your line snaps while you cast out and pay {amount} {currency} for a new spool.",
    "Your hook is blunt and you pay {amount} {currency} for a new set from the shop.",
]
STORM_EVENTS = [
    "A bolt of \N{HIGH VOLTAGE SIGN} comes out of nowhere and nearly zaps you. You spend {amount} {currency} to buy new pants.",
]

LEGENDARY_PRICE = 150000
EPIC_PRICE = 6500
RARE_PRICE = 3000
UNCOMMON_PRICE = 650
COMMON_PRICE = 140
GARBAGE_PRICE = 7
