"""
Возможность WebDriver - умение взаимодействовать с элементами веб-страницы.
HTML - язык разметки, с помощью который описывается структура веб-страницы.
Сайты используют JS - который позволяет сделать веб-страницу интерактивной, реагировать на действия пользователей, зап-
рашивать у пользователя данные и возвращать их.
CSS - каскадная таблица стилей, который используется для вёрстки страницы. "Благодаря WebDriver можно поймать неожиданную ошибку,
когда кнопку перекрывает другой элемент"

Необходимый навык - умение описывать путь к элементу, для выполнения с ним каких-либо действий.

Способы поиска элемента:
1. С помощью CSS селекторов. Селектор - это описание пути к элементу на странице.
2. Поиск с помощью указания значений тегов или атрибутов элементов: ID, CLASS и т.д.
3. Поиск с помощью XPATH

Три особенности языка HTML:
1. Страница HTML состоит из элементов, начало и конец элемента задаётся с помощью тегов;
2. У тегов есть атрибуты, которые определяют свойства элементов;
3. Страница на язык HTML имеет иерархическую систему.

Для общего ознакомления:
Задача тега - обозначить, какой именно тип информации на странице они (элементы) представляют (картинка, текст, блок,
ссылка и т.д.)
Основные атрибуты, которые необходимо знать:
- class (классы чаще всего используют для задания правил вёрстки с помощью CSS)
- name (например, используется для задания якоря (закладки) в html-странице)
- id (уникальный указатель на элемент, не должно повторяться в пределах страницы)

Иерархия HTML документа

HTML-документ часто сравнивают с моделью семейного древа, в котором есть родители, дети, братья, предки и потомки.
- потомок элемента X – элемент любой степени вложенности внутри элемента X;
- ребёнок или дочерний элемент — прямой потомок (т.е. элемент на первом уровне вложенности);
- предок элемента Y – любой элемент X, который включает в себя элемент Y;
- родитель — это прямой предок (т.е. элемент, который расположен выше строго на 1 уровень);
- братский или соседний элемент – элемент X, который расположен на одном уровне иерархии с элементом Y. Элементы X и Y имеют одного родителя.

Курс по "Веб-разработка для начинающих: HTML и CSS" - https://stepik.org/course/38218/promo

"""