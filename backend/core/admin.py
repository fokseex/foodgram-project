from django.contrib import admin

from .models import Tag, Ingredient, Recipe, ShoppingCart, Favorite


class IngredientsRecipeLine(admin.TabularInline):
    """ Связь  ингридиентов в рецепте """
    model = Recipe.ingredients.through


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """ Админ панель управление ингридиентами """
    list_display = ('name', 'measurement_unit')
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = '-пусто-'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """ Админ панель управление тегами """
    list_display = ('name', 'color', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name', )
    empty_value_display = '-пусто-'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """ Админ панель управление рецептами """
    list_display = ('name', 'author', 'favorites')
    search_fields = ('author', 'name')
    list_filter = ('tags', )
    filter_horizontal = ('tags', )
    empty_value_display = '-пусто-'
    inlines = (IngredientsRecipeLine,)

    def favorites(self, obj):
        if Favorite.objects.filter(recipe=obj).exists():
            return Favorite.objects.filter(recipe=obj).count()
        return 0

    favorites.short_description = 'Количество добавлений рецепта в избранное'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """ Админ панель управление подписками """
    list_display = ('user', 'recipe')
    list_filter = ('user', 'recipe')
    search_fields = ('user', 'recipe')
    empty_value_display = '-пусто-'


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """ Админ панель списка покупок """
    list_display = ('recipe', 'user')
    list_filter = ('recipe', 'user')
    search_fields = ('user', )
    empty_value_display = '-пусто-'
