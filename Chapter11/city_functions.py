def get_city_country(city,country,population=0):
	if population==0:
		full_name=city+" "+country
	else:
		full_name=city+" "+country+" "+str(population)
	return full_name.title()