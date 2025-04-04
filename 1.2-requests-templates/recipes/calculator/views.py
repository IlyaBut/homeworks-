from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template.defaultfilters import lower

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

#__________________________________________________________________________

def dish(requests, name):
    servings = int(requests.GET.get("servings", 0))
    eat = lower(name)

    context = {
      'recipe': {

      }
    }

    try:
        if eat in DATA:
            context["recipe"] = DATA.get(eat)

            if servings != 0:

                for key in context["recipe"]:
                    context['recipe'][key] *= servings

        return render(requests, "calculator/index.html", context)

    except KeyError:
        raise Http404 ("Такого нет!")



