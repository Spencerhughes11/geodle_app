import json
import numpy as np
import pandas as pd
import string
import random

class Comparisons():
    def __init__(self, secret_country):
        self.df = pd.read_json('data.json')

        # self.secret_country = random.choice(self.df.keys())
        self.secret_country = secret_country

    @property
    def get_secret_country(self):
        return self.secret_country

    def get_data(self, guess):
        return {
            # 'name': guess,
            'letter': guess[0].upper(),
            'hemisphere': self.df[guess].hemisphere,
            'continent': self.df[guess].continent,
            'area': str(self.df[guess].area),
            'population': str(self.df[guess].population),
        }

    # ------------------------------------------------ LETTER COMPARISONS ----------------------------------------------
    def compare_letter(self, guess_letter):
        """ Returns feedback telling the user if the first letter of the guess is near the first letter of the answer """
       
        secret_letter = self.secret_country[0].upper()     ## Saves first letter

        alphabet = list(string.ascii_uppercase)   #creates a list of every letter
        letter_index = 0
        if guess_letter == secret_letter:
            return 'green'                   # if the guess and correct country start with the same letter
        elif guess_letter in alphabet:
            for char in alphabet:
                if guess_letter == char:
                    letter_index = alphabet.index(char)        # stores index of the guess letter

            if letter_index < 5:
                # if letter is one of the first 5 of the alphabet
                for letter in alphabet[0:letter_index + 5:1]:         
                    if secret_letter == letter:
                        return 'yellow'               #if guess and correct letter are one of first 5 letters in alphabet, return close feedback
                return 'grey'
            elif letter_index > 20:
                # if letter is one of the last 5 of the alphabet
                for letter in alphabet[(letter_index - 5):25:1]:
                    if secret_letter == letter:       #if guess and correct letter are one of last 5 letters in alphabet, return close
                        return 'yellow'
                return 'grey'
            elif 5 <= letter_index <= 20:
                for letter in alphabet[(letter_index - 5):(letter_index + 5):1]:
                    if secret_letter == letter:     #if correct letter is within 5 indices of the guess letter
                        return 'yellow'
                return 'grey'

    # ------------------------------------------------ HEMISPHERE COMPARISONS ----------------------------------------------

    def compare_hemi(self, guess):
        """ Returns feedback telling user if guess in in same hemisphere or not """

        if self.df[guess].hemisphere == self.df[self.secret_country].hemisphere:
            return "green"
        elif self.df[self.secret_country].hemisphere == "B":
            return "yellow"
        else:
            return "grey"
        
    # ------------------------------------------------ CONTINENT COMPARISONS ----------------------------------------------

    def compare_continent(self, guess):
        """ Returns feedback lettin user know if country guess is in same, bordering, or wrong continent """
        test = self.secret_country
        if self.df[guess].continent == self.df[self.secret_country].continent:
            return 'green'
        elif self.bordering_continent(guess):
            return 'yellow'    ## if country is in a bordering continent, return yellow, meaning 'close'
        else:
            return 'grey'
        
    def bordering_continent(self, guess):
        """ Creates relationships for bordering continent """
        
        if self.df[guess].continent == "North America":
            if self.df[self.secret_country].continent == "South America":
                return True
        elif self.df[guess].continent == "South America":
            if self.df[self.secret_country].continent == "North America":
                return True
        elif self.df[guess].continent == "Oceania":
            if self.df[self.secret_country].continent == "Asia":
                return True
        elif self.df[guess].continent == "Asia":
            if self.df[self.secret_country].continent == "Oceania":
                return True
            elif self.df[self.secret_country].continent == "Europe":
                return True
            elif self.df[self.secret_country].continent == "Africa":
                return True
        elif self.df[guess].continent == "Europe":
            if self.df[self.secret_country].continent == "Africa":
                return True
            elif self.df[self.secret_country].continent == "Asia":
                return True
        elif self.df[guess].continent == "Africa":
            if self.df[self.secret_country].continent == "Europe":
                return True
            elif self.df[self.secret_country].continent == "Asia":
                return True
        return False

    # ------------------------------------------------ AREA COMPARISONS ----------------------------------------------

    def compare_area_range(self, guess):
        """ Returns feedback telling user info about area of guess vs. answer """
        guess_no_comma = self.df[guess].area.replace(',', '')
        secret_country_no_comma = self.df[self.secret_country].area.replace(',', '')

        if int(guess_no_comma) == int(secret_country_no_comma):
            return "green"
        elif abs(int(guess_no_comma) - int(secret_country_no_comma)) <= 250000:
            return "yellow"      ## if guess country area is within 250,000 sq. km of answer area, tell user they are "close"
        else:
            return "grey"
    
    def area_higher_lower(self, guess):
        guess_no_comma = self.df[guess].population.replace(',', '')
        secret_country_no_comma = self.df[self.secret_country].population.replace(',', '')

        if int(guess_no_comma) < int(secret_country_no_comma):
            return 'higher'
        elif int(guess_no_comma) > int(secret_country_no_comma):
            return 'lower'

    # ------------------------------------------------ POPULATION COMPARISONS ----------------------------------------------
 
    def compare_pop_range(self, guess):
        """ Returns feedback telling info about population of guess vs. answer """
        guess_no_comma = self.df[guess].population.replace(',', '')
        secret_country_no_comma = self.df[self.secret_country].population.replace(',', '')

        if int(guess_no_comma) == int(secret_country_no_comma):
            return "green"
        elif abs(int(guess_no_comma) - int(secret_country_no_comma)) <= 10000000:
            return "yellow"  ## if guess population is within 10 mil. of answer, tell user they are "close"
        else:
            return "grey"

    def pop_higher_lower(self, guess):
        guess_no_comma = self.df[guess].population.replace(',', '')
        secret_country_no_comma = self.df[self.secret_country].population.replace(',', '')
        if int(guess_no_comma) < int(secret_country_no_comma):
            return 'higher'
        elif int(guess_no_comma) > int(secret_country_no_comma):
            return 'lower'
        
    # def __str__(self):
    #     return f"Secret Country: {self.df[self.secret_country]}"
    
    # def __repr__(self):
    #     return f"Secret Country: {self.df[self.secret_country]}"

def main():

    test = Comparisons()
    # print(test.get_secret_country)
    secret = test.get_secret_country

    # test.pop_higher_lower('China')
    x = test.compare_area_range('Libya')

    y = 1
    print(x)

if __name__ == '__main__': 
    main()