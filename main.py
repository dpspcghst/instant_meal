from random import choice

class InstantMeal():

    def __init__(self):

        self.a_acid = ""
        self.choline = ""
        self.fatty_acid = ""
        self.mineral = ""
        self.vitamin = ""

    def a_acids(self):

        # lists of foods with high combinations of amino acids
        a_acids_high = ["dairy products"]
        a_acids_mid = ["fish", "meat (besides fish and poultry)"]
        a_acids_low = ["poultry"]
        a_acids_all = (a_acids_high * 3) + (a_acids_mid * 2) + a_acids_low
        self.a_acid = choice(a_acids_all)

    def cholines(self):

        # list of foods with high choline
        choline_all = [
            "bacon", "Brussels sprouts," "chicken (especially the dark meat)",
            "eggs (especially the yolk)", "liver (beef or chicken)", "pink shrimp",
            "salmon (wild-caught)"
        ]

        if self.a_acid != "dairy products":

            self.choline = "Brussels sprouts"
            
        else:

            self.choline = choice(choline_all)

    def fatty_acids(self):

        # list of foods with balanced combinations of omega 6s & omega 3s
        fatty_acids_high = ["walnuts"]
        fatty_acids_mid = [
            "chia seeds", "corn oil", "flax seeds", "mackerel", "pine nuts",
            "pumpkin seeds", "salmon", "sardines", "sunflower oil"
        ]

        if self.a_acid != "dairy products" or self.choline != "Brussels sprouts":

            fatty_acid_veggies = [
                "walnuts", "walnuts", "walnuts", "chia seeds", "chia seeds","corn oil",
                "corn oil", "flax seeds", "flax seeds", "pine nuts", "pine nuts",
                "pumpkin seeds", "pumpkin seeds", "sunflower oil", "sunflower oil"
            ]
            self.fatty_acid = choice(fatty_acid_veggies)

        else:

            fatty_acid_all = (fatty_acids_high * 3) + (fatty_acids_mid * 2)
            self.fatty_acid = choice(fatty_acid_all)


    def minerals(self):
        
        # lists of foods with high combinations of minerals
        minerals_high = ["legumes", "salmon (a fish)", "whole grains"]
        minerals_mid = ["fish", "red meat", "shellfish (a seafood)", "walnuts (a nut)"]
        minerals_low = [
            "broccoli (a green vegetable)", "nuts", "prunes (a fruit)",
            "spinach (a green leafy vegetable)"
        ]

        if self.a_acid != "dairy products" \
            or self.choline != "Brussels sprouts" \
            or self.fatty_acid in ["mackerel", "salmon", "sardines"]:

            minerals_veggies = [
                "legumes", "legumes", "legumes", "whole grains", "whole grains",
                "whole grains", "walnuts (a nut)", "walnut (a nut)",
                "broccoli (a green vegetable), nuts", "prunes (a fruit)",
                "spinach (a green leafy vegetable)"
            ]
            self.mineral = choice(minerals_veggies)

        else:

            minerals_all = (minerals_high * 3) + (minerals_mid * 2) + minerals_low
            self.mineral = choice(minerals_all)

    def vitamins(self):
        
        # lists of food with high combinations of vitamins
        vitamins_high = [
            "fish (especially fatty)",
            "whole grains and cereals (enriched or fortified with B2, B9, B12, & D)"
        ]
        vitamins_mid = [
            "broccoli (a leaf vegetable)", "chicken (a poultry)",
            "milk (especially fortified)", "spinach (a leaf vegetable)"
        ]
        vitamins_low = [
            "black-eyed peas (a legume)", "chickpeas (a legume)", "eggs", "meat",
            "poultry"
        ]

        if self.a_acid != "dairy products" \
            or self.choline != "Brussels sprouts" \
            or self.fatty_acid in ["mackerel", "salmon", "sardine"] \
            or self.mineral in [
                "salmon (a fish), fish", "red meat", "shelfish (a seafood)"
            ]:

            vitamins_veggies = [
                "whole grains and cereals (enriched or fortified with B2, B9, B12, D)",
                "whole grains and cereals (enriched or fortified with B2, B9, B12, D)",
                "whole grains and cereals (enriched or fortified with B2, B9, B12, D)",
                "broccoli (a leaf vegetable)", "broccoli (a leaf vegetable)",
                "milk (especially fortified)", "milk (especially fortified)",
                "spinach (a leaf vegetable)", "spinach (a leaf vegetable)",
                "black-eyed peas (a legume)", "chickpeas (a legume)"
            ]
            self.vitamin = choice(vitamins_veggies)
        
        else:
            
            vitamins_all = (vitamins_high * 3) + (vitamins_mid * 2) + vitamins_low
            self.vitamin = choice(vitamins_all)

    def soybeans(self):
        """
        When the lists were being put together, soy products were misgrouped, which
        significantly lowered their score. This function aims to correct that.
        """
    
        # drop rate
        options = [False, True]
        return choice(options)

    def prep(self):

        try:

            self.a_acids()
            self.cholines()
            self.fatty_acids()
            self.minerals()
            self.vitamins()

        except Exception as e:
            print(f"Error during preparation: {e}")
    
    def plan(self):

        try:

            if self.soybeans():

                print(f"Plan a meal with the following ingredients: {self.a_acid},")
                print(f"{self.choline}, {self.fatty_acid}, {self.mineral},")
                print(f"{self.vitamin}, and soybeans.")

            else:

                print(f"Plan a meal with the following ingredients: {self.a_acid},")
                print(f"{self.choline}, {self.fatty_acid}, {self.mineral},")
                print(f"and {self.vitamin}.")

        except ValueError as ve:

            print(f"ValueError during planning: {ve}")

        except Exception as e:

            print(f"Error during planning: {e}")

if __name__ == "__main__":
    instant_meal = InstantMeal()
    instant_meal.prep()
    instant_meal.plan()
