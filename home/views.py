from django.shortcuts import render
from django.views import View
from django.views.decorators.http import require_http_methods

from django.http import HttpResponse, JsonResponse, HttpRequest
import json
import numpy as np
import pandas as pd
from helpers.compare import Comparisons

# Create your views here.
# request handlers

class Main(View):
    def __init__(self):
        pass

    # @require_http_methods(['GET'])
    def get(self, request: HttpRequest, **kwargs):
        try:
            guess = (request.GET.get('guess'))
            capitalized = []
            # Handle multi-word country names
            if ' ' in guess:
                temp = guess.strip().split(' ')
                for word in temp:
                    if word != 'and':
                        word = word.capitalize()
                    capitalized.append(word)

                guess = ' '.join(capitalized)
            else:
                guess = guess.capitalize()
            secret_country = request.GET.get('secret_country')
            self.compare = Comparisons(secret_country)
            if not (guess and secret_country):
                return JsonResponse({'error': 'Bad Request: Missing required parameters.'}, status=400)

                # return {'guess is None'}


            # all_data = self.process_guess(guess)
            # json_data = json.dumps(all_data)
            # print(self.compare.get_data(guess))

            # Call feedback functions, passing in info from request
            if self.compare.valid_guess(guess):
                letter_feedback = self.compare.compare_letter(guess[0].upper())
                hemisphere_feedback = self.compare.compare_hemi(guess)
                continent_feedback = self.compare.compare_continent(guess)   
                area_range = self.compare.compare_area_range(guess)       # color feedback if area is within specified range
                area_higher_lower = self.compare.area_higher_lower(guess)
                population_range_color = self.compare.compare_pop_range(guess)      # color feedback if population is within specific range    
                pop_higher_lower = self.compare.pop_higher_lower(guess)      # color feedback if population is within specific range    
            else:
                return JsonResponse({'Error': 'Country not found in database'})


            # letter_feedback = self.compare.get_letter_feedback('S')
            # hemisphere_feedback = self.compare.get_hemisphere_feedback('N')
            # continent_feedback = self.compare.get_continent_feedback('South America')   
            # area_feedback = self.compare.get_area_feedback('95000')       
            # population_feedback = self.compare.get_population_feedback('10000000')


            feedback = {
                'letter': letter_feedback,
                'hemisphere': hemisphere_feedback,
                'continent': continent_feedback,
                'area': area_range,
                'area_higher_lower': area_higher_lower,
                'population': population_range_color,
                'pop_higher_lower': pop_higher_lower,

            }
            # print(f'Guess: {guess}: {feedback}') # test

            all_data = {
                'feedback': feedback,
                'guess_data': self.compare.get_data(guess)
            }
        except AttributeError:
            pass
        # return all_data
    
        return JsonResponse(all_data)
    
    def get_secret_country(self):
        print(f'Secret: {self.compare.get_secret_country}')




# if __name__ == '__main__':
#     guesses = ['China', 'Canada', 'France', 'Germany', 'Italy', 'Syria', 'Australia',
#                'Brazil', 'Congo', 'Algeria']
#     x = Main()
#     for country in guesses:
#         # x.get_guess(country)
#         # x.get_secret_country()
#         print(x.process_guess(country))