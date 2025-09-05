    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the pokemon type.

        Returns :
            float : the multiplier
        """
        elif self._type == "All rounder":
            multiplier = 1 + (self.sp_atk_current + self.sp_def_current) / 200
        return multiplier