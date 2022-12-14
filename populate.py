from scrape import scrape
from chemical import Chemical

for id in range(1,201):
    chemical_properties = scrape(id)
    if chemical_properties:
        chemical = Chemical(chemical_properties["name"], 
                            chemical_properties["cas_number"])
        if chemical.is_chemical_already_present():
            chemical.update()
        else:
            chemical.save()