class Enhancer:
    def __init__(self, total):
        self.total = total
        self.piece = {
                "Flower of Life": lambda artifact: self.FoL(artifact),
                "Plume of Death": lambda artifact: self.PoD(artifact),
                  "Sands of Eon": lambda artifact: self.SoE(artifact),
            "Goblet of Eonothem": lambda artifact: self.GoE(artifact),
               "Circlet of Logo": lambda artifact: self.CoL(artifact)
                }

    def score(self, artifact):
        score = self.piece[artifact['piece']](artifact)
        if score == 2:
            self.total += 1
        return score

    def FoL(self, artifact):
        score, size = self.scorer(artifact)
        if 34 < score:
            return 1
        elif 21 < score and size == 3:
            return 1
        return 2

    def PoD(self, artifact):
        score, size = self.scorer(artifact)
        if 34 < score:
            return 1
        elif 21 < score and size == 3:
            return 1
        return 2

    def SoE(self, artifact):
        score, size = self.scorer(artifact)
        if artifact['mainStat'][0] == "ATK%":
            if 34 < score:
                return 1
            elif 31 < score and size == 3:
                return 1
        if 34 < score:
            return 1
        elif 21 < score and size == 3:
            return 1
        return 2

    def GoE(self, artifact):
        if "DMG Bonus" in artifact['mainStat'][0]:
            return 1
        score, size = self.scorer(artifact)
        if 34 < score:
            return 1
        elif 21 < score and size == 3:
            return 1
        return 2

    def CoL(self, artifact):
        if artifact['mainStat'][0] in ["CRIT Rate", "CRIT DMG"]:
            return 1
        score, size = self.scorer(artifact)
        if 34 < score:
            return 1
        elif 21 < score and size == 3:
            return 1
        return 2

    def scorer(self, artifact):
        points = {
               "CRIT Rate": 17,
                "CRIT DMG": 17,
       "Elemental Mastery": 7,
         "Energy Recharge": 7,
                    "ATK%": 7,
                    "DEF%": 2,
                     "HP%": 2,
                     "ATK": 2,
                     "DEF": 0,
                      "HP": 0,
                }
        score = 0
        subStats = [stat for stat in artifact['subStats']]
        for stat in subStats:
            score += points[stat]
        return score, len(subStats)