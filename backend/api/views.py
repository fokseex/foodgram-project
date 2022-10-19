from django.contrib.auth import password_validation
from django.shortcuts import render
from djoser.views import UserViewSet
from rest_framework import viewsets


class UsersViewSet(UserViewSet):
    """Отображение подписок/подписться/отписаться"""
    pass

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """Отображение тегов"""
    pass


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    """ Отображение ингредиентов. """
    pass


class RecipeViewSet(viewsets.ModelViewSet):
    """ Операции с рецептами: добавление/изменение/удаление/просмотр. """
    pass
