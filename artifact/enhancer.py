class Enhancer:
    def __init__(self, total):
        self.total = total
        self.piece = {
                "Flower of Life": lambda artifact: self.FoL(artifact),
                "Plume of Death": lambda artifact: self.PoD(artifact),
                  "Sands of Eon": lambda artifact: self.SoE(artifact),
            "Goblet of Eonothem": lambda artifact: self.GoE(artifact),
              "Circlet of Logos": lambda artifact: self.CoL(artifact)
                }

    def score(self, artifact):
        score = self.piece[artifact['piece']](artifact)
        if score == 2:
            self.total += 1
        return score

    def FoL(self, artifact):
        score, size = self.scorer(artifact)
        if 33 < score:
            return 0
        elif score < 7:
            return 2
        return 1

    def PoD(self, artifact):
        score, size = self.scorer(artifact)
        if 33 < score:
            return 0
        elif score < 7:
            return 2
        return 1

    def SoE(self, artifact):
        score, size = self.scorer(artifact)
        if 33 < score:
            return 0
        elif score < 7:
            return 2
        return 1

    def GoE(self, artifact):
        score, size = self.scorer(artifact)
        if "DMG Bonus" in artifact['mainStat'][0]:
            if 33 < score:
                return 0
            return 1
        if 33 < score:
            return 0
        elif score < 7:
            return 2
        return 1

    def CoL(self, artifact):
        score, size = self.scorer(artifact)
        if artifact['mainStat'][0] in ["CRIT Rate", "CRIT DMG"]:
            if 33 < score:
                return 0
            return 1
        if 33 < score:
            return 0
        elif score < 7:
            return 2
        return 1

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
