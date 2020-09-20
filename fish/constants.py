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
    "\N{SHARK}": "legendary",
    "\N{SPOUTING WHALE}": "legendary",
}

RODS = ["wooden rod", "fly-fishing rod", "harpoon", "metal rod", "pikachu rod"]
RODS_WEIGHT = [0.85, 0.12, 0.02, 0.0090, 0.001]
RODS_PRICES = {
    "fly-fishing rod": 85000,
    "harpoon": 200000,
    "metal rod": 1000000,
    "pikachu rod": 15000000,
}

WEIGHTS = {
    "wooden rod": [
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.2,
        0.2,
        0.2,
        0.06,
        0.06,
        0.06,
        0.002,
        0.002,
    ],
    "fly-fishing rod": [
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.22,
        0.22,
        0.22,
        0.08,
        0.08,
        0.08,
        0.003,
        0.003,
    ],
    "harpoon": [
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.25,
        0.25,
        0.25,
        0.11,
        0.11,
        0.11,
        0.005,
        0.005,
    ],
    "metal rod": [
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.28,
        0.28,
        0.28,
        0.13,
        0.13,
        0.13,
        0.007,
        0.007,
    ],
    "pikachu rod": [
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.3,
        0.3,
        0.3,
        0.15,
        0.15,
        0.15,
        0.015,
        0.015,
    ],
}

FISHES = list(FISHES_TYPE.keys())
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