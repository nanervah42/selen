1. В файле categories.txt вручную захардкожены ссылки на все категории (их всего 9).
2. list_run.py проходит по categories.txt и на основе пагинации формирует в categories_full.txt все страницы со списком товаров во всех категориях.
3. category_run.py собирает всю информацию по всем товарам из category_full.txt и складывает в result.csv (ошибки записываются в result_error.txt).