""" Cheat for Guessing """

# By @Krishna_Singhal

from re import match
from userge import userge, Message

# List of All Pokemon's
POKE_LIST_ = [

    "bulbasaur", "chikorita", "treecko", "turtwig", "victini", "chespin", "rowlet",
    "grookey", "ivysaur", "bayleef", "grovyle", "grotle", "snivy", "quilladin",
    "dartrix", "thwackey", "venusaur", "meganium", "sceptile", "torterra", "servine",
    "chesnaught", "decidueye", "rillaboom", "charmander", "cyndaquil", "torchic",
    "chimchar", "serperior", "fennekin", "litten", "scorbunny", "charmeleon", "quilava",
    "combusken", "monferno", "tepig", "braixen", "torracat", "raboot", "charizard",
    "typhlosion", "blaziken", "infernape", "pignite", "delphox", "incineroar", "cinderace",
    "squirtle", "totodile", "mudkip", "piplup", "emboar", "froakie", "popplio",
    "sobble", "wartortle", "croconaw", "marshtomp", "prinplup", "oshawott", "frogadier",
    "brionne", "drizzile", "blastoise", "feraligatr", "swampert", "empoleon", "dewott",
    "greninja", "primarina", "inteleon", "caterpie", "sentret", "poochyena", "starly",
    "samurott", "bunnelby", "pikipek", "skwovet", "metapod", "furret", "mightyena",
    "staravia", "patrat", "diggersby", "trumbeak", "greedent", "butterfree", "hoothoot",
    "zigzagoon", "staraptor", "watchog", "fletchling", "toucannon", "rookidee",
    "weedle", "noctowl", "linoone", "bidoof", "lillipup", "fletchinder", "yungoos",
    "corvisquire", "kakuna", "ledyba", "wurmple", "bibarel", "herdier", "talonflame",
    "gumshoos", "corviknight", "beedrill", "ledian", "silcoon", "kricketot",
    "stoutland", "scatterbug", "grubbin", "blipbug", "pidgey", "spinarak", "beautifly",
    "kricketune", "purrloin", "spewpa", "charjabug", "dottler", "pidgeotto", "ariados",
    "cascoon", "shinx", "liepard", "vivillon", "vikavolt", "orbeetle", "pidgeot",
    "crobat", "dustox", "luxio", "pansage", "litleo", "crabrawler", "nickit",
    "chinchou", "lotad", "luxray", "simisage", "pyroar", "crabominable", "thievul",
    "raticate", "lanturn", "lombre", "budew", "pansear", "oricorio", "gossifleur",
    "spearow", "pichu", "ludicolo", "roserade", "simisear", "floette", "cutiefly",
    "eldegoss", "fearow", "cleffa", "seedot", "cranidos", "panpour", "florges",
    "ribombee", "wooloo", "ekans", "igglybuff", "nuzleaf", "rampardos", "simipour",
    "skiddo", "rockruff", "dubwool", "arbok", "togepi", "shiftry", "shieldon",
    "munna", "gogoat", "lycanroc", "chewtle", "pikachu", "togetic", "taillow",
    "bastiodon", "musharna", "pancham", "wishiwashi", "drednaw", "raichu", "natu",
    "swellow", "burmy", "pidove", "pangoro", "mareanie", "yamper", "sandshrew",
    "xatu", "wingull", "wormadam", "tranquill", "furfrou", "toxapex", "boltund",
    "sandslash", "mareep", "pelipper", "mothim", "unfezant", "espurr", "mudbray",
    "rolycoly", "flaaffy", "ralts", "combee", "blitzle", "meowstic", "mudsdale",
    "carkol", "nidorina", "ampharos", "kirlia", "vespiquen", "zebstrika", "honedge",
    "dewpider", "coalossal", "nidoqueen", "bellossom", "gardevoir", "pachirisu", "roggenrola",
    "doublade", "araquanid", "applin", "marill", "surskit", "buizel", "boldore",
    "aegislash", "fomantis", "flapple", "nidorino", "azumarill", "masquerain", "floatzel",
    "mantyke", "gigalith", "spritzee", "lurantis", "appletun", "nidoking", "sudowoodo",
    "shroomish", "cherubi", "woobat", "aromatisse", "morelull", "silicobra", "clefairy",
    "politoed", "breloom", "cherrim", "swoobat", "swirlix", "shiinotic", "sandaconda",
    "clefable", "hoppip", "slakoth", "shellos", "drilbur", "slurpuff", "salandit",
    "cramorant", "vulpix", "skiploom", "vigoroth", "gastrodon", "excadrill", "inkay",
    "salazzle", "arrokuda", "ninetales", "jumpluff", "slaking", "ambipom", "audino",
    "malamar", "stufful", "barraskewda", "jigglypuff", "aipom", "nincada", "drifloon",
    "timburr", "binacle", "bewear", "toxel", "wigglytuff", "sunkern", "ninjask",
    "drifblim", "gurdurr", "barbaracle", "bounsweet", "toxtricity", "zubat", "sunflora",
    "shedinja", "buneary", "conkeldurr", "skrelp", "steenee", "sizzlipede", "golbat",
    "yanma", "whismur", "lopunny", "tympole", "dragalge", "tsareena", "centiskorch",
    "oddish", "wooper", "loudred", "mismagius", "palpitoad", "clauncher", "comfey",
    "clobbopus", "gloom", "quagsire", "exploud", "honchkrow", "seismitoad", "clawitzer",
    "oranguru", "grapploct", "vileplume", "espeon", "makuhita", "glameow", "throh",
    "helioptile", "passimian", "sinistea", "paras", "umbreon", "hariyama", "purugly",
    "sawk", "heliolisk", "wimpod", "polteageist", "parasect", "murkrow", "azurill",
    "chingling", "sewaddle", "tyrunt", "golisopod", "hatenna", "venonat", "slowking",
    "nosepass", "stunky", "swadloon", "tyrantrum", "sandygast", "hattrem", "venomoth",
    "misdreavus", "skitty", "skuntank", "leavanny", "amaura", "palossand", "hatterene",
    "diglett", "unown", "delcatty", "bronzor", "venipede", "aurorus", "pyukumuku",
    "impidimp", "dugtrio", "wobbuffet", "sableye", "bronzong", "whirlipede", "sylveon",
    "morgrem", "meowth", "girafarig", "mawile", "bonsly", "scolipede", "hawlucha",
    "silvally", "grimmsnarl", "persian", "pineco", "aron", "mime jr.", "cottonee",
    "dedenne", "minior", "obstagoon", "psyduck", "forretress", "lairon", "happiny",
    "whimsicott", "carbink", "komala", "perrserker", "golduck", "dunsparce", "aggron",
    "chatot", "petilil", "goomy", "turtonator", "cursola", "mankey", "gligar",
    "meditite", "spiritomb", "lilligant", "sliggoo", "togedemaru", "sirfetch'd", "primeape",
    "steelix", "medicham", "gible", "basculin", "goodra", "snom", "kadabra",
    "mimikyu", "mr. rime", "growlithe", "snubbull", "electrike", "gabite", "sandile",
    "klefki", "bruxish", "runerigus", "arcanine", "granbull", "manectric", "garchomp",
    "krokorok", "phantump", "drampa", "milcery", "poliwag", "qwilfish", "plusle",
    "munchlax", "krookodile", "trevenant", "dhelmise", "alcremie", "poliwhirl", "scizor",
    "minun", "riolu", "darumaka", "pumpkaboo", "jangmo-o", "falinks", "poliwrath",
    "shuckle", "volbeat", "lucario", "darmanitan", "gourgeist", "hakamo-o", "pincurchin",
    "abra", "heracross", "illumise", "hippopotas", "maractus", "bergmite", "kommo-o",
    "sneasel", "roselia", "hippowdon", "dwebble", "avalugg", "tapu", "koko",
    "frosmoth", "alakazam", "teddiursa", "gulpin", "skorupi", "crustle", "noibat",
    "tapu", "lele", "stonjourner", "machop", "ursaring", "swalot", "drapion",
    "scraggy", "noivern", "tapu", "bulu", "eiscue", "machoke", "slugma",
    "carvanha", "croagunk", "scrafty", "xerneas", "tapu", "fini", "indeedee",
    "machamp", "magcargo", "sharpedo", "toxicroak", "sigilyph", "yveltal", "cosmog",
    "bellsprout", "swinub", "wailmer", "carnivine", "yamask", "zygarde","cosmoem",
    "cufant", "weepinbell", "piloswine", "wailord", "finneon", "cofagrigus", "diancie",
    "morpeko", "solgaleo", "copperajah", "victreebel", "corsola", "numel", "lumineon",
    "tirtouga", "hoopa", "lunala", "dracozolt", "tentacool", "remoraid", "camerupt",
    "carracosta", "volcanion", "nihilego", "arctozolt", "tentacruel", "octillery", "torkoal",
    "snover", "archen", "buzzwole", "dracovish", "geodude", "delibird", "spoink",
    "abomasnow", "archeops", "pheromosa", "arctovish", "graveler", "mantine", "grumpig",
    "weavile", "trubbish", "xurkitree", "duraludon", "golem", "skarmory", "spinda",
    "magnezone", "garbodor", "celesteela", "dreepy", "ponyta", "houndour", "trapinch",
    "lickilicky", "zorua", "kartana", "drakloak", "rapidash", "houndoom", "vibrava",
    "rhyperior", "zoroark", "guzzlord", "dragapult", "slowpoke", "kingdra", "flygon",
    "tangrowth", "minccino", "necrozma", "zacian", "slowbro", "phanpy", "cacnea",
    "electivire", "cinccino", "magearna", "zamazenta", "magnemite", "donphan", "cacturne",
    "magmortar", "gothita", "marshadow", "eternatus", "magneton", "porygon", "swablu",
    "togekiss", "gothorita", "poipole", "kubfu", "farfetch'd", "stantler", "altaria",
    "yanmega", "gothitelle", "naganadel", "urshifu", "doduo", "smeargle", "zangoose",
    "leafeon", "solosis", "stakataka", "zarude", "dodrio", "tyrogue", "seviper",
    "glaceon", "duosion", "blacephalon", "regieleki", "seel", "hitmontop", "lunatone",
    "gliscor", "reuniclus", "zeraora", "regidrago", "dewgong", "smoochum", "solrock",
    "mamoswine", "ducklett", "meltan", "calyrex", "grimer", "elekid", "barboach",
    "porygon-z", "swanna", "melmetal", "muk", "magby", "whiscash", "gallade",
    "vanillite", "shellder", "miltank", "corphish", "probopass", "vanillish", "cloyster",
    "blissey", "crawdaunt", "dusknoir", "anorith", "azelf", "vanilluxe", "gastly",
    "raikou", "baltoy", "froslass", "deerling", "haunter", "entei", "claydol",
    "rotom", "sawsbuck", "gengar", "suicune", "lileep", "uxie", "emolga", "rattata",
    "onix", "larvitar", "cradily", "mesprit", "karrablast", "drowzee", "pupitar",
    "escavalier", "hypno", "tyranitar", "armaldo", "dialga", "foongus", "krabby",
    "lugia", "feebas", "palkia", "amoonguss", "kingler", "ho-oh", "milotic",
    "heatran", "frillish", "voltorb", "celebi", "castform", "regigigas", "jellicent",
    "electrode", "kecleon", "giratina", "alomomola", "exeggcute", "shuppet", "cresselia",
    "joltik", "exeggutor", "banette", "phione", "galvantula", "cubone", "duskull",
    "marowak",  "metagross",  "latios",  "omastar",  "snorlax", "manaphy", "ferroseed",
    "dusclops", "darkrai", "ferrothorn", "hitmonlee", "tropius", "shaymin", "klink",
    "hitmonchan", "chimecho", "arceus", "klang", "lickitung", "absol", "klinklang",
    "koffing", "wynaut", "tynamo", "weezing", "snorunt", "eelektrik", "rhyhorn",
    "glalie", "eelektross", "rhydon", "spheal", "elgyem", "chansey", "sealeo",
    "beheeyem", "tangela", "walrein", "litwick", "kangaskhan", "clamperl", "lampent",
    "horsea", "huntail", "chandelure", "seadra", "gorebyss", "axew", "goldeen",
    "relicanth", "fraxure", "seaking", "luvdisc", "haxorus", "staryu", "bagon",
    "cubchoo", "starmie", "shelgon", "beartic", "mr. mime", "salamence", "cryogonal",
    "scyther", "beldum", "shelmet", "jynx", "metang", "accelgor", "electabuzz",
    "stunfisk", "magmar", "regirock", "mienfoo", "pinsir", "regice", "mienshao",
    "tauros", "registeel", "druddigon", "magikarp", "latias", "golett", "gyarados",
    "golurk", "lapras", "kyogre", "pawniard", "ditto", "groudon", "bisharp", "eevee",
    "rayquaza", "bouffalant", "vaporeon", "jirachi", "rufflet", "jolteon", "deoxys",
    "braviary", "flareon", "vullaby", "porygon", "mandibuzz", "omanyte", "heatmor",
    "durant", "kabuto", "deino", "kabutops", "zweilous", "aerodactyl", "hydreigon",
    "larvesta", "articuno", "volcarona", "zapdos", "cobalion", "moltres", "terrakion",
    "dratini", "virizion", "dragonair", "tornadus", "dragonite", "thundurus", "mewtwo",
    "reshiram", "mew", "zekrom", "landorus", "kyurem", "keldeo", "meloetta", "genesect"
]


@userge.on_cmd("guess", about={
    'header': "For cheating tod find PokÃ©mon",
    'usage': "{tr}guess [Text | reply to text msg]"})
async def guess(msg: Message):
    """ Mainly for Guessing """

    global POKE_LIST_
    replied = msg.reply_to_message
    args = msg.input_str
    if args:
        text = args
    elif replied:
        text = args or replied.text
    else:
        await msg.edit("`Use Common Sense...`")
        await msg.reply_sticker("CAADAgADNAEAAiI3jgQ-ge2MLm43MxYE")
        return
    
    to_find = text.lower()

    pattern = to_find.replace('hint:   ', '').replace('_', '.').replace(' ', '')
    guessed = None

    for word in POKE_LIST_:
        if match(pattern, word):
            guessed = word
            await msg.delete()
            await msg.client.send_message(msg.chat.id, guessed.title(),
                                          reply_to_message_id=replied.message_id or None)
    if not guessed:
        await msg.edit("`This Pokemon is not in my Pokedex...`")
        await msg.reply_sticker("CAADAgADNAEAAiI3jgQ-ge2MLm43MxYE")
