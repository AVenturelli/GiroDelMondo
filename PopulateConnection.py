class Popolate:
    def __init__(self,locations):
        self.locations = locations
        
    def doPopulate(self):
        # Collegamenti Honolulu
        self.locations[self.getIndex('Honolulu')].addPoint(self.getIndex('San Francisco'), 2)  # San Francisco
        self.locations[self.getIndex('Honolulu')].addPoint(self.getIndex('Tokyo'), 2)  # Tokyo
        self.locations[self.getIndex('Honolulu')].addPoint(self.getIndex('Wellington'), 2)  # Wellington

        # Collegamenti Vancouver
        self.locations[self.getIndex('Vancouver')].addPoint(self.getIndex('Edmonton'), 1)  # Edmonton
        self.locations[self.getIndex('Vancouver')].addPoint(self.getIndex('Portland'), 1)  # Portland
        self.locations[self.getIndex('Vancouver')].addPoint(self.getIndex('Calgary'), 1)  # Calgary

        # Collegamenti Portland
        self.locations[self.getIndex('Portland')].addPoint(self.getIndex('Vancouver'), 1)  # Vancouver
        self.locations[self.getIndex('Portland')].addPoint(self.getIndex('San Francisco'), 1)  # San Francisco

        # Collegamenti San Francisco
        self.locations[self.getIndex('San Francisco')].addPoint(self.getIndex('Portland'), 1)  # Portland
        self.locations[self.getIndex('San Francisco')].addPoint(self.getIndex('Los Angeles'), 1)  # Los Angels
        self.locations[self.getIndex('San Francisco')].addPoint(self.getIndex('Salt Lake City'), 1)  # Salt Lake City
        self.locations[self.getIndex('San Francisco')].addPoint(self.getIndex('New York'), 2)  # New York
        self.locations[self.getIndex('San Francisco')].addPoint(self.getIndex('Honolulu'), 2)  # Honolulu

        # Collegamenti Los Angeles
        self.locations[self.getIndex('Los Angeles')].addPoint(self.getIndex('San Francisco'), 1)  # San Francisco
        self.locations[self.getIndex('Los Angeles')].addPoint(self.getIndex('Santa Fe'), 1)  # Santa Fe
        self.locations[self.getIndex('Los Angeles')].addPoint(self.getIndex('El Paso'), 1)  # El Paso
        self.locations[self.getIndex('Los Angeles')].addPoint(self.getIndex('Mexico City'), 1)  # Mexico City
        self.locations[self.getIndex('Los Angeles')].addPoint(self.getIndex('Lima'), 2)  # Lima

        # Collegamenti Calgary
        self.locations[self.getIndex('Calgary')].addPoint(self.getIndex('Edmonton'), 1)  # Edmonton
        self.locations[self.getIndex('Calgary')].addPoint(self.getIndex('Winnipeg'), 1)  # Winnipeg
        self.locations[self.getIndex('Calgary')].addPoint(self.getIndex('Minneapolis'), 1)  # Minneapolis
        self.locations[self.getIndex('Calgary')].addPoint(self.getIndex('Vancouver'), 1)  # Vancouver

        # Collegamenti Salt Lake City
        self.locations[self.getIndex('Salt Lake City')].addPoint(self.getIndex('San Francisco'), 1)  # San Francisco
        self.locations[self.getIndex('Salt Lake City')].addPoint(self.getIndex('Denver'), 1)  # Denver

        # Collegamenti Edmonton
        self.locations[self.getIndex('Edmonton')].addPoint(self.getIndex('Calgary'), 1)  # Calgary
        self.locations[self.getIndex('Edmonton')].addPoint(self.getIndex('Vancouver'), 1)  # Vancouver
        self.locations[self.getIndex('Edmonton')].addPoint(self.getIndex('Winnipeg'), 1)  # Winnipeg

        # Collegamenti El Paso
        self.locations[self.getIndex('El Paso')].addPoint(self.getIndex('Santa Fe'), 1)  # Santa Fe
        self.locations[self.getIndex('El Paso')].addPoint(self.getIndex('Los Angeles'), 1)  # Los Angeles
        self.locations[self.getIndex('El Paso')].addPoint(self.getIndex('Houston'), 1)  # Houston

        # Collegamenti Santa Fe
        self.locations[self.getIndex('Santa Fe')].addPoint(self.getIndex('El Paso'), 1)  # El Paso
        self.locations[self.getIndex('Santa Fe')].addPoint(self.getIndex('Houston'), 1)  # Houston
        self.locations[self.getIndex('Santa Fe')].addPoint(self.getIndex('Los Angeles'), 1)  # Los Angeles

        # Collegamenti Denver
        self.locations[self.getIndex('Denver')].addPoint(self.getIndex('Houston'), 1)  # Houston
        self.locations[self.getIndex('Denver')].addPoint(self.getIndex('Minneapolis'), 1)  # Minneapolis
        self.locations[self.getIndex('Denver')].addPoint(self.getIndex('Salt Lake City'), 1)  # Salt Lake City
        self.locations[self.getIndex('Denver')].addPoint(self.getIndex('St. Louis'), 1)  # St. Louis
        self.locations[self.getIndex('Denver')].addPoint(self.getIndex('Santa Fe'), 1)  # Santa Fe

        # Collegamenti Winnipeg
        self.locations[self.getIndex('Winnipeg')].addPoint(self.getIndex('Edmonton'), 1)  # Edmonton
        self.locations[self.getIndex('Winnipeg')].addPoint(self.getIndex('Calgary'), 1)  # Calgary
        self.locations[self.getIndex('Winnipeg')].addPoint(self.getIndex('Minneapolis'), 1)  # Minneapolis
        self.locations[self.getIndex('Winnipeg')].addPoint(self.getIndex('Duluth'), 1)  # Duluth
        self.locations[self.getIndex('Winnipeg')].addPoint(self.getIndex('Montreal'), 1)  # Montreal

        # Collegamenti Mexico City
        self.locations[self.getIndex('Mexico City')].addPoint(self.getIndex('Guatemala'), 1)  # Guatemala
        self.locations[self.getIndex('Mexico City')].addPoint(self.getIndex('Houston'), 1)  # Houston
        self.locations[self.getIndex('Mexico City')].addPoint(self.getIndex('Los Angeles'), 1)  # Los Angeles

        # Collegamenti Houston
        self.locations[self.getIndex('Houston')].addPoint(self.getIndex('El Paso'), 1)  # El Paso
        self.locations[self.getIndex('Houston')].addPoint(self.getIndex('Denver'), 1)  # Denver
        self.locations[self.getIndex('Houston')].addPoint(self.getIndex('New Orleans'), 1)  # New Orleans
        self.locations[self.getIndex('Houston')].addPoint(self.getIndex('Mexico City'), 1)  # Mexico City

        # Collegamenti Minneapolis
        self.locations[self.getIndex('Minneapolis')].addPoint(self.getIndex('Calgary'), 1)  # Calgary
        self.locations[self.getIndex('Minneapolis')].addPoint(self.getIndex('Winnipeg'), 1)  # Winnipeg
        self.locations[self.getIndex('Minneapolis')].addPoint(self.getIndex('Chicago'), 1)  # Chicago
        self.locations[self.getIndex('Minneapolis')].addPoint(self.getIndex('St. Louis'), 1)  # St. Louis
        self.locations[self.getIndex('Minneapolis')].addPoint(self.getIndex('Denver'), 1)  # Denver

        # Collegamenti Duluth
        self.locations[self.getIndex('Duluth')].addPoint(self.getIndex('Winnipeg'), 1)  # Winnipeg
        self.locations[self.getIndex('Duluth')].addPoint(self.getIndex('Chicago'), 1)  # Chicago

        # St. Louis
        self.locations[self.getIndex('St. Louis')].addPoint(self.getIndex('Minneapolis'), 1)  # Minneapolis
        self.locations[self.getIndex('St. Louis')].addPoint(self.getIndex('Chicago'), 1)  # Chicago
        self.locations[self.getIndex('St. Louis')].addPoint(self.getIndex('New Orleans'), 1)  # New Orleans
        self.locations[self.getIndex('St. Louis')].addPoint(self.getIndex('Denver'), 1)  # Denver
        self.locations[self.getIndex('St. Louis')].addPoint(self.getIndex('Washington'), 1)  # Washington

        # Collegamenti New Orleans
        self.locations[self.getIndex('New Orleans')].addPoint(self.getIndex('Houston'), 1)  # Houston
        self.locations[self.getIndex('New Orleans')].addPoint(self.getIndex('St. Louis'), 1)  #
        self.locations[self.getIndex('New Orleans')].addPoint(self.getIndex('Jacksonville'), 1)  #

        # Colleagamenti Guatemala
        self.locations[self.getIndex('Guatemala')].addPoint(self.getIndex('Mexico City'), 1)  #
        self.locations[self.getIndex('Guatemala')].addPoint(self.getIndex('Managua'), 1)  #

        # Collegamenti Chicago
        self.locations[self.getIndex('Chicago')].addPoint(self.getIndex('Duluth'), 1)  #
        self.locations[self.getIndex('Chicago')].addPoint(self.getIndex('Minneapolis'), 1)  #
        self.locations[self.getIndex('Chicago')].addPoint(self.getIndex('St. Louis'), 1)  #
        self.locations[self.getIndex('Chicago')].addPoint(self.getIndex('New York'), 1)  #

        # Collegamenti Managua
        self.locations[self.getIndex('Managua')].addPoint(self.getIndex('Panama City'), 1)  #
        self.locations[self.getIndex('Managua')].addPoint(self.getIndex('Guatemala'), 1)  #

        # Collegamenti Jacksonville
        self.locations[self.getIndex('Jacksonville')].addPoint(self.getIndex('Miami'), 1)  #
        self.locations[self.getIndex('Jacksonville')].addPoint(self.getIndex('New Orleans'), 1)  #
        self.locations[self.getIndex('Jacksonville')].addPoint(self.getIndex('Washington'), 1)  #

        # Collegamenti Havana
        self.locations[self.getIndex('Havana')].addPoint(self.getIndex('Kingston'), 2)  #

        # Collegamenti Miami
        self.locations[self.getIndex('Miami')].addPoint(self.getIndex('New York'), 1)  #
        self.locations[self.getIndex('Miami')].addPoint(self.getIndex('Jacksonville'), 2)  #

        # Collegamenti Washington
        self.locations[self.getIndex('Washington')].addPoint(self.getIndex('New York'), 1)  #
        self.locations[self.getIndex('Washington')].addPoint(self.getIndex('Jacksonville'), 1)  #
        self.locations[self.getIndex('Washington')].addPoint(self.getIndex('St. Louis'), 1)  #

        # Collegamenti Panama City
        self.locations[self.getIndex('Panama City')].addPoint(self.getIndex('Bogotà'), 1)  #
        self.locations[self.getIndex('Panama City')].addPoint(self.getIndex('Managua'), 1)  #

        # Collegamenti Quito
        self.locations[self.getIndex('Quito')].addPoint(self.getIndex('Bogotà'), 1)  #
        self.locations[self.getIndex('Quito')].addPoint(self.getIndex('Lima'), 1)  #

        # Collegamenti Kingston
        self.locations[self.getIndex('Kingston')].addPoint(self.getIndex('Havana'), 2)  #
        self.locations[self.getIndex('Kingston')].addPoint(self.getIndex('Caracas'), 2)  #

        # Collegamenti Lima
        self.locations[self.getIndex('Lima')].addPoint(self.getIndex('Los Angeles'), 2)  #
        self.locations[self.getIndex('Lima')].addPoint(self.getIndex('Santiago'), 2)  #
        self.locations[self.getIndex('Lima')].addPoint(self.getIndex('Quito'), 1)  #
        self.locations[self.getIndex('Lima')].addPoint(self.getIndex('Manaus'), 1)  #
        self.locations[self.getIndex('Lima')].addPoint(self.getIndex('Cuzco'), 1)  #

        # Collegamenti New York
        self.locations[self.getIndex('New York')].addPoint(self.getIndex('San Francisco'), 2)  #
        self.locations[self.getIndex('New York')].addPoint(self.getIndex('Miami'), 2)  #
        self.locations[self.getIndex('New York')].addPoint(self.getIndex('Paris'), 2)  #
        self.locations[self.getIndex('New York')].addPoint(self.getIndex('London'), 2)  #
        self.locations[self.getIndex('New York')].addPoint(self.getIndex('Washington'), 1)  #
        self.locations[self.getIndex('New York')].addPoint(self.getIndex('Chicago'), 1)  #
        self.locations[self.getIndex('New York')].addPoint(self.getIndex('Montreal'), 1)  #
        self.locations[self.getIndex('New York')].addPoint(self.getIndex('Halifax'), 1)  #

        # Collegamenti Montreal
        self.locations[self.getIndex('Montreal')].addPoint(self.getIndex('Godthaab'), 2)  #
        self.locations[self.getIndex('Montreal')].addPoint(self.getIndex('Halifax'), 1)  #
        self.locations[self.getIndex('Montreal')].addPoint(self.getIndex('Winnipeg'), 1)  #
        self.locations[self.getIndex('Montreal')].addPoint(self.getIndex('New York'), 1)  #

        # Collegamenti Halifax
        self.locations[self.getIndex('Halifax')].addPoint(self.getIndex('Montreal'), 1)  #
        self.locations[self.getIndex('Halifax')].addPoint(self.getIndex('New York'), 1)  #

        # Collegamenti Caracas
        self.locations[self.getIndex('Caracas')].addPoint(self.getIndex('Brasilia'), 2)  #
        self.locations[self.getIndex('Caracas')].addPoint(self.getIndex('Buenos Aires'), 2)  #
        self.locations[self.getIndex('Caracas')].addPoint(self.getIndex('Kingston'), 2)  #
        self.locations[self.getIndex('Caracas')].addPoint(self.getIndex('Paris'), 2)  #
        self.locations[self.getIndex('Caracas')].addPoint(self.getIndex('Bogotà'), 1)  #

        # Collegamenti Bogotà
        self.locations[self.getIndex('Bogotà')].addPoint(self.getIndex('Caracas'), 1)  #
        self.locations[self.getIndex('Bogotà')].addPoint(self.getIndex('Panama City'), 1)  #
        self.locations[self.getIndex('Bogotà')].addPoint(self.getIndex('Quito'), 1)  #

        # Collegamenti Manaus
        self.locations[self.getIndex('Manaus')].addPoint(self.getIndex('Lima'), 1)  #
        self.locations[self.getIndex('Manaus')].addPoint(self.getIndex('Belém'), 1)  #

        # Collegamenti Belém
        self.locations[self.getIndex('Belém')].addPoint(self.getIndex('Recife'), 1)  #
        self.locations[self.getIndex('Belém')].addPoint(self.getIndex('Manaus'), 1)  #

        # Collegamenti Recife
        self.locations[self.getIndex('Recife')].addPoint(self.getIndex('Belém'), 1)  #
        self.locations[self.getIndex('Recife')].addPoint(self.getIndex('Rio de Janeiro'), 1)  #

        # Collegamenti Cuzco
        self.locations[self.getIndex('Cuzco')].addPoint(self.getIndex('Lima'), 1)  #
        self.locations[self.getIndex('Cuzco')].addPoint(self.getIndex('La Paz'), 1)  #

        # Collegamenti La Paz
        self.locations[self.getIndex('La Paz')].addPoint(self.getIndex('Cuzco'), 1)  #
        self.locations[self.getIndex('La Paz')].addPoint(self.getIndex('Asunción'), 1)  #
        self.locations[self.getIndex('La Paz')].addPoint(self.getIndex('Santiago'), 1)  #

        # Collegamenti Asunción
        self.locations[self.getIndex('Asunción')].addPoint(self.getIndex('La Paz'), 1)  #
        self.locations[self.getIndex('Asunción')].addPoint(self.getIndex('Buenos Aires'), 1)  #
        self.locations[self.getIndex('Asunción')].addPoint(self.getIndex('Porto Alegre'), 1)  #

        # Collegamenti Porto Alegre
        self.locations[self.getIndex('Porto Alegre')].addPoint(self.getIndex('Asunción'), 1)  #
        self.locations[self.getIndex('Porto Alegre')].addPoint(self.getIndex('Rio de Janeiro'), 1)  #
        self.locations[self.getIndex('Porto Alegre')].addPoint(self.getIndex('Buenos Aires'), 1)  #
        self.locations[self.getIndex('Porto Alegre')].addPoint(self.getIndex('Brasilia'), 1)  #

        # Collegamenti Brasilia
        self.locations[self.getIndex('Brasilia')].addPoint(self.getIndex('Caracas'), 2)  #
        self.locations[self.getIndex('Brasilia')].addPoint(self.getIndex('Rio de Janeiro'), 1)  #
        self.locations[self.getIndex('Brasilia')].addPoint(self.getIndex('Porto Alegre'), 1)  #

        # Collegamenti Rio de Janeiro
        self.locations[self.getIndex('Rio de Janeiro')].addPoint(self.getIndex('Recife'), 1)  #
        self.locations[self.getIndex('Rio de Janeiro')].addPoint(self.getIndex('Dakar'), 2)  #
        self.locations[self.getIndex('Rio de Janeiro')].addPoint(self.getIndex('Brasilia'), 1)  #
        self.locations[self.getIndex('Rio de Janeiro')].addPoint(self.getIndex('Porto Alegre'), 1)  #

        # Collegamenti Santiago
        self.locations[self.getIndex('Santiago')].addPoint(self.getIndex('Punta Arenas'), 1)  #
        self.locations[self.getIndex('Santiago')].addPoint(self.getIndex('Lima'), 2)  #
        self.locations[self.getIndex('Santiago')].addPoint(self.getIndex('Buenos Aires'), 1)  #
        self.locations[self.getIndex('Santiago')].addPoint(self.getIndex('La Paz'), 1)  #

        # Collegamenti Buenos Aires
        self.locations[self.getIndex('Buenos Aires')].addPoint(self.getIndex('Asunción'), 1)  #
        self.locations[self.getIndex('Buenos Aires')].addPoint(self.getIndex('Caracas'), 2)  #
        self.locations[self.getIndex('Buenos Aires')].addPoint(self.getIndex('Porto Alegre'), 1)  #
        self.locations[self.getIndex('Buenos Aires')].addPoint(self.getIndex('Santiago'), 1)  #

        # Collegamenti Punta Arenas
        self.locations[self.getIndex('Punta Arenas')].addPoint(self.getIndex('Santiago'), 1)  #

        # Collegamenti Godthaab
        self.locations[self.getIndex('Godthaab')].addPoint(self.getIndex('Reykjavik'), 2)  #
        self.locations[self.getIndex('Godthaab')].addPoint(self.getIndex('Montreal'), 2)  #

        # Collegamenti Tunis
        self.locations[self.getIndex('Tunis')].addPoint(self.getIndex('Tripoli'), 2)  #
        self.locations[self.getIndex('Tunis')].addPoint(self.getIndex('Roma'), 2)  #
        self.locations[self.getIndex('Tunis')].addPoint(self.getIndex('Alger'), 1)  #

        # Collegamenti Alger
        self.locations[self.getIndex('Alger')].addPoint(self.getIndex('Rabat'), 1)  #
        self.locations[self.getIndex('Alger')].addPoint(self.getIndex('Marseille'), 2)  #
        self.locations[self.getIndex('Alger')].addPoint(self.getIndex('Tunis'), 1)  #
        self.locations[self.getIndex('Alger')].addPoint(self.getIndex('Tamanrasset'), 1)  #

        # Collegamenti Rabat
        self.locations[self.getIndex('Rabat')].addPoint(self.getIndex('Alger'), 1)  #
        self.locations[self.getIndex('Rabat')].addPoint(self.getIndex('Dakar'), 1)  #

        # Collegamenti Tripoli
        self.locations[self.getIndex('Tripoli')].addPoint(self.getIndex('Tunis'), 1)  #
        self.locations[self.getIndex('Tripoli')].addPoint(self.getIndex('Bengasi'), 1)  #

        # Collegamenti Bengasi
        self.locations[self.getIndex('Bengasi')].addPoint(self.getIndex('Tripoli'), 1)  #
        self.locations[self.getIndex('Bengasi')].addPoint(self.getIndex('Cairo'), 1)  #

        # Collegamenti Cairo
        self.locations[self.getIndex('Cairo')].addPoint(self.getIndex('Bengasi'), 1)  #
        self.locations[self.getIndex('Cairo')].addPoint(self.getIndex('Aswàn'), 1)  #
        self.locations[self.getIndex('Cairo')].addPoint(self.getIndex('Jerusalem'), 1)  #
        self.locations[self.getIndex('Cairo')].addPoint(self.getIndex('Athinai'), 2)  #
        self.locations[self.getIndex('Cairo')].addPoint(self.getIndex('Nairobi'), 2)  #
        self.locations[self.getIndex('Cairo')].addPoint(self.getIndex('Aden'), 2)  #

        # Collegamenti Las Palmas
        self.locations[self.getIndex('Las Palmas')].addPoint(self.getIndex('Frankfurt'), 2)  #
        self.locations[self.getIndex('Las Palmas')].addPoint(self.getIndex('Lisboa'), 2)  #

        # Collegamenti Aswàn
        self.locations[self.getIndex('Aswàn')].addPoint(self.getIndex('Cairo'), 1)  #
        self.locations[self.getIndex('Aswàn')].addPoint(self.getIndex('Khartoum'), 1)  #

        # Collegamenti Tamanrasset
        self.locations[self.getIndex('Tamanrasset')].addPoint(self.getIndex('Timbuktu'), 1)  #
        self.locations[self.getIndex('Tamanrasset')].addPoint(self.getIndex('Alger'), 1)  #
        self.locations[self.getIndex('Tamanrasset')].addPoint(self.getIndex('Niamey'), 1)  #

        # Collegamenti Timbuktu
        self.locations[self.getIndex('Timbuktu')].addPoint(self.getIndex('Tamanrasset'), 1)  #
        self.locations[self.getIndex('Timbuktu')].addPoint(self.getIndex('Bamako'), 1)  #

        # Collegamenti Khartoum
        self.locations[self.getIndex('Khartoum')].addPoint(self.getIndex('Aswàn'), 1)  #
        self.locations[self.getIndex('Khartoum')].addPoint(self.getIndex('Addis Abeba'), 1)  #
        self.locations[self.getIndex('Khartoum')].addPoint(self.getIndex('Ndjamena'), 1)  #

        # Collegamenti Dakar
        self.locations[self.getIndex('Dakar')].addPoint(self.getIndex('Abidjan'), 2)  #
        self.locations[self.getIndex('Dakar')].addPoint(self.getIndex('Rabat'), 1)  #
        self.locations[self.getIndex('Dakar')].addPoint(self.getIndex('Bamako'), 1)  #

        # Collegamenti Bamako
        self.locations[self.getIndex('Bamako')].addPoint(self.getIndex('Timbuktu'), 1)  #
        self.locations[self.getIndex('Bamako')].addPoint(self.getIndex('Dakar'), 1)  #
        self.locations[self.getIndex('Bamako')].addPoint(self.getIndex('Niamey'), 1)  #

        # Collegamenti Niamey
        self.locations[self.getIndex('Niamey')].addPoint(self.getIndex('Tamanrasset'), 1)  #
        self.locations[self.getIndex('Niamey')].addPoint(self.getIndex('Bamako'), 1)  #
        self.locations[self.getIndex('Niamey')].addPoint(self.getIndex('Lagos'), 1)  #
        self.locations[self.getIndex('Niamey')].addPoint(self.getIndex('Ndjamena'), 1)  #

        # Collegamenti Ndjamena
        self.locations[self.getIndex('Ndjamena')].addPoint(self.getIndex('Niamey'), 1)  #
        self.locations[self.getIndex('Ndjamena')].addPoint(self.getIndex('Yaoundé'), 1)  #
        self.locations[self.getIndex('Ndjamena')].addPoint(self.getIndex('Khartoum'), 1)  #

        # Collegamenti Addis Abeba
        self.locations[self.getIndex('Addis Abeba')].addPoint(self.getIndex('Aden'), 2)  #
        self.locations[self.getIndex('Addis Abeba')].addPoint(self.getIndex('Mogadishu'), 1)  #
        self.locations[self.getIndex('Addis Abeba')].addPoint(self.getIndex('Khartoum'), 1)  #

        # Collegamenti Abidjan
        self.locations[self.getIndex('Abidjan')].addPoint(self.getIndex('Accra'), 2)  #
        self.locations[self.getIndex('Abidjan')].addPoint(self.getIndex('Dakar'), 2)  #

        # Collegamenti Accra
        self.locations[self.getIndex('Accra')].addPoint(self.getIndex('Abidjan'), 2)  #
        self.locations[self.getIndex('Accra')].addPoint(self.getIndex('Lagos'), 2)  #

        # Collegamenti Lagos
        self.locations[self.getIndex('Lagos')].addPoint(self.getIndex('Accra'), 2)  #
        self.locations[self.getIndex('Lagos')].addPoint(self.getIndex('Yaoundé'), 1)  #
        self.locations[self.getIndex('Lagos')].addPoint(self.getIndex('Niamey'), 1)  #

        # Collegamenti Yaoundé
        self.locations[self.getIndex('Yaoundé')].addPoint(self.getIndex('Kinshasa'), 2)  #
        self.locations[self.getIndex('Yaoundé')].addPoint(self.getIndex('Lagos'), 1)  #
        self.locations[self.getIndex('Yaoundé')].addPoint(self.getIndex('Ndjamena'), 1)  #

        # Collegamenti Mogadishu
        self.locations[self.getIndex('Mogadishu')].addPoint(self.getIndex('Nairobi'), 2)  #
        self.locations[self.getIndex('Mogadishu')].addPoint(self.getIndex('Tananarive'), 2)  #
        self.locations[self.getIndex('Mogadishu')].addPoint(self.getIndex('Addis Abeba'), 1)  #

        # Collegamenti Nairobi
        self.locations[self.getIndex('Nairobi')].addPoint(self.getIndex('Kinshasa'), 2)  #
        self.locations[self.getIndex('Nairobi')].addPoint(self.getIndex('Lusaka'), 2)  #
        self.locations[self.getIndex('Nairobi')].addPoint(self.getIndex('Cape-Town'), 2)  #
        self.locations[self.getIndex('Nairobi')].addPoint(self.getIndex('Mogadishu'), 2)  #
        self.locations[self.getIndex('Nairobi')].addPoint(self.getIndex('Cairo'), 2)  #
        self.locations[self.getIndex('Nairobi')].addPoint(self.getIndex('Paris'), 2)  #
        self.locations[self.getIndex('Nairobi')].addPoint(self.getIndex('Bangkok'), 2)  #

        # Collegamenti Kinshasa
        self.locations[self.getIndex('Kinshasa')].addPoint(self.getIndex('Yaoundé'), 2)  #
        self.locations[self.getIndex('Kinshasa')].addPoint(self.getIndex('Nairobi'), 2)  #
        self.locations[self.getIndex('Kinshasa')].addPoint(self.getIndex('Lobito'), 1)  #

        # Collegamenti Dar-es-Salaam
        self.locations[self.getIndex('Dar-es-Salaam')].addPoint(self.getIndex('Tananarive'), 2)  #
        self.locations[self.getIndex('Dar-es-Salaam')].addPoint(self.getIndex('Nairobi'), 1)  #
        self.locations[self.getIndex('Dar-es-Salaam')].addPoint(self.getIndex('Salisbury'), 1)  #

        # Collegamenti Lobito
        self.locations[self.getIndex('Lobito')].addPoint(self.getIndex('Kinshasa'), 1)  #
        self.locations[self.getIndex('Lobito')].addPoint(self.getIndex('Lusaka'), 1)  #
        self.locations[self.getIndex('Lobito')].addPoint(self.getIndex('Windhoek'), 1)  #

        # Collegamenti Lusaka
        self.locations[self.getIndex('Lusaka')].addPoint(self.getIndex('Nairobi'), 2)  #
        self.locations[self.getIndex('Lusaka')].addPoint(self.getIndex('Salisbury'), 1)  #
        self.locations[self.getIndex('Lusaka')].addPoint(self.getIndex('Lobito'), 1)  #

        # Collegamenti Salisbury
        self.locations[self.getIndex('Salisbury')].addPoint(self.getIndex('Lusaka'), 1)  #
        self.locations[self.getIndex('Salisbury')].addPoint(self.getIndex('Dar-es-Salaam'), 1)  #
        self.locations[self.getIndex('Salisbury')].addPoint(self.getIndex('Johannesburg'), 1)  #
        self.locations[self.getIndex('Salisbury')].addPoint(self.getIndex('Windhoek'), 1)  #

        # Collegamenti Tananarive
        self.locations[self.getIndex('Tananarive')].addPoint(self.getIndex('Mogadishu'), 2)  #
        self.locations[self.getIndex('Tananarive')].addPoint(self.getIndex('Dar-es-Salaam'), 2)  #

        # Collegamenti Windhoek
        self.locations[self.getIndex('Windhoek')].addPoint(self.getIndex('Lobito'), 1)  #
        self.locations[self.getIndex('Windhoek')].addPoint(self.getIndex('Salisbury'), 1)  #
        self.locations[self.getIndex('Windhoek')].addPoint(self.getIndex('Cape-Town'), 1)  #

        # Collegamenti Johannesburg
        self.locations[self.getIndex('Johannesburg')].addPoint(self.getIndex('Salisbury'), 1)  #
        self.locations[self.getIndex('Johannesburg')].addPoint(self.getIndex('Cape-Town'), 1)  #

        # Collegamenti Cape-Town
        self.locations[self.getIndex('Cape-Town')].addPoint(self.getIndex('Nairobi'), 2)  #
        self.locations[self.getIndex('Cape-Town')].addPoint(self.getIndex('Johannesburg'), 1)  #
        self.locations[self.getIndex('Cape-Town')].addPoint(self.getIndex('Windhoek'), 1)  #

        # Collegamenti Murmansk
        self.locations[self.getIndex('Murmansk')].addPoint(self.getIndex('Moskva'), 2)  #
        self.locations[self.getIndex('Murmansk')].addPoint(self.getIndex('Leningrad'), 1)  #

        # Collegamenti Narvik
        self.locations[self.getIndex('Narvik')].addPoint(self.getIndex('Luleå'), 1)  #
        self.locations[self.getIndex('Narvik')].addPoint(self.getIndex('Trondheim'), 1)  #

        # Collegamenti Luleå
        self.locations[self.getIndex('Luleå')].addPoint(self.getIndex('Narvik'), 1)  #
        self.locations[self.getIndex('Luleå')].addPoint(self.getIndex('Stockholm'), 1)  #
        self.locations[self.getIndex('Luleå')].addPoint(self.getIndex('Helsinki'), 1)  #

        # Collegamenti Reykjavik
        self.locations[self.getIndex('Reykjavik')].addPoint(self.getIndex('Edinburgh'), 2)  #

        # Collegamenti Trondheim
        self.locations[self.getIndex('Trondheim')].addPoint(self.getIndex('Narvik'), 1)  #
        self.locations[self.getIndex('Trondheim')].addPoint(self.getIndex('Bergen'), 1)  #

        # Collegamenti Arkhangelsk
        self.locations[self.getIndex('Arkhangelsk')].addPoint(self.getIndex('Moskva'), 1)  #

        # Collegamenti Bergen
        self.locations[self.getIndex('Bergen')].addPoint(self.getIndex('Frankfurt'), 2)  #
        self.locations[self.getIndex('Bergen')].addPoint(self.getIndex('Oslo'), 1)  #
        self.locations[self.getIndex('Bergen')].addPoint(self.getIndex('Trondheim'), 1)  #

        # Collegamenti Oslo
        self.locations[self.getIndex('Oslo')].addPoint(self.getIndex('Stockholm'), 1)  #
        self.locations[self.getIndex('Oslo')].addPoint(self.getIndex('Bergen'), 1)  #

        # Collegamenti Stockholm
        self.locations[self.getIndex('Stockholm')].addPoint(self.getIndex('Luleå'), 1)  #
        self.locations[self.getIndex('Stockholm')].addPoint(self.getIndex('Oslo'), 1)  #
        self.locations[self.getIndex('Stockholm')].addPoint(self.getIndex('Helsinki'), 1)  #
        self.locations[self.getIndex('Stockholm')].addPoint(self.getIndex('Kopenhagen'), 1)  #

        # Collegamenti Helsinki
        self.locations[self.getIndex('Helsinki')].addPoint(self.getIndex('Frankfurt'), 2)  #
        self.locations[self.getIndex('Helsinki')].addPoint(self.getIndex('Stockholm'), 1)  #
        self.locations[self.getIndex('Helsinki')].addPoint(self.getIndex('Luleå'), 1)  #
        self.locations[self.getIndex('Helsinki')].addPoint(self.getIndex('Leningrad'), 1)  #

        # Collegamenti Leningrad
        self.locations[self.getIndex('Leningrad')].addPoint(self.getIndex('Murmansk'), 1)  #
        self.locations[self.getIndex('Leningrad')].addPoint(self.getIndex('Riga'), 1)  #
        self.locations[self.getIndex('Leningrad')].addPoint(self.getIndex('Moskva'), 1)  #
        self.locations[self.getIndex('Leningrad')].addPoint(self.getIndex('Helsinki'), 1)  #

        # Collegamenti Riga
        self.locations[self.getIndex('Riga')].addPoint(self.getIndex('Leningrad'), 1)  #
        self.locations[self.getIndex('Riga')].addPoint(self.getIndex('Gdansk'), 1)  #

        # Collegamenti Perm
        self.locations[self.getIndex('Perm')].addPoint(self.getIndex('Moskva'), 1)  #
        self.locations[self.getIndex('Perm')].addPoint(self.getIndex('Sverdiovsk'), 1)  #

        # Collegamenti Kopenhagen
        self.locations[self.getIndex('Kopenhagen')].addPoint(self.getIndex('Stockholm'), 1)  #
        self.locations[self.getIndex('Kopenhagen')].addPoint(self.getIndex('Hamburg'), 1)  #

        # Collegamenti Edinburgh
        self.locations[self.getIndex('Edinburgh')].addPoint(self.getIndex('Reykjavik'), 1)  #
        self.locations[self.getIndex('Edinburgh')].addPoint(self.getIndex('Dublin'), 2)  #
        self.locations[self.getIndex('Edinburgh')].addPoint(self.getIndex('London'), 1)  #

        # Collegamenti Gdansk
        self.locations[self.getIndex('Gdansk')].addPoint(self.getIndex('Berlin'), 1)  #
        self.locations[self.getIndex('Gdansk')].addPoint(self.getIndex('Warsazawa'), 1)  #
        self.locations[self.getIndex('Gdansk')].addPoint(self.getIndex('Riga'), 1)  #

        # Collegamenti Hamburg
        self.locations[self.getIndex('Hamburg')].addPoint(self.getIndex('Amsterdam'), 1)  #
        self.locations[self.getIndex('Hamburg')].addPoint(self.getIndex('Kopenhagen'), 1)  #
        self.locations[self.getIndex('Hamburg')].addPoint(self.getIndex('Berlin'), 1)  #
        self.locations[self.getIndex('Hamburg')].addPoint(self.getIndex('Frankfurt'), 1)  #

        # Collegamenti Moskva
        self.locations[self.getIndex('Moskva')].addPoint(self.getIndex('Frankfurt'), 2)  #
        self.locations[self.getIndex('Moskva')].addPoint(self.getIndex('Murmansk'), 2)  #
        self.locations[self.getIndex('Moskva')].addPoint(self.getIndex('Norilsk'), 2)  #
        self.locations[self.getIndex('Moskva')].addPoint(self.getIndex('Tifils'), 2)  #
        self.locations[self.getIndex('Moskva')].addPoint(self.getIndex('Irkutsk'), 2)  #
        self.locations[self.getIndex('Moskva')].addPoint(self.getIndex('Kiyev'), 1)  #
        self.locations[self.getIndex('Moskva')].addPoint(self.getIndex('Warsazawa'), 1)  #
        self.locations[self.getIndex('Moskva')].addPoint(self.getIndex('Leningrad'), 1)  #
        self.locations[self.getIndex('Moskva')].addPoint(self.getIndex('Arkhangelsk'), 1)  #
        self.locations[self.getIndex('Moskva')].addPoint(self.getIndex('Perm'), 1)  #
        self.locations[self.getIndex('Moskva')].addPoint(self.getIndex('Volgograd'), 1)  #

        # Collegamenti Dublin
        self.locations[self.getIndex('Dublin')].addPoint(self.getIndex('Edinburgh'), 2)  #
        self.locations[self.getIndex('Dublin')].addPoint(self.getIndex('London'), 1)  #

        # Collegamenti London
        self.locations[self.getIndex('London')].addPoint(self.getIndex('Lisboa'), 2)  #
        self.locations[self.getIndex('London')].addPoint(self.getIndex('New York'), 2)  #
        self.locations[self.getIndex('London')].addPoint(self.getIndex('Edinburgh'), 1)  #
        self.locations[self.getIndex('London')].addPoint(self.getIndex('Dublin'), 1)  #
        self.locations[self.getIndex('London')].addPoint(self.getIndex('Amsterdam'), 1)  #

        # Collegamenti Amsterdam
        self.locations[self.getIndex('Amsterdam')].addPoint(self.getIndex('London'), 1)  #
        self.locations[self.getIndex('Amsterdam')].addPoint(self.getIndex('Hamburg'), 1)  #
        self.locations[self.getIndex('Amsterdam')].addPoint(self.getIndex('Paris'), 1)  #
        self.locations[self.getIndex('Amsterdam')].addPoint(self.getIndex('Frankfurt'), 1)  #

        # Collegamenti Warsazawa
        self.locations[self.getIndex('Warsazawa')].addPoint(self.getIndex('Gdansk'), 1)  #
        self.locations[self.getIndex('Warsazawa')].addPoint(self.getIndex('Berlin'), 1)  #
        self.locations[self.getIndex('Warsazawa')].addPoint(self.getIndex('Praha'), 1)  #
        self.locations[self.getIndex('Warsazawa')].addPoint(self.getIndex('Moskva'), 1)  #

        # Collegamenti Kiyev
        self.locations[self.getIndex('Kiyev')].addPoint(self.getIndex('Odessa'), 1)  #
        self.locations[self.getIndex('Kiyev')].addPoint(self.getIndex('Moskva'), 1)  #

        # Collegamenti Praha
        self.locations[self.getIndex('Praha')].addPoint(self.getIndex('Warsazawa'), 1)  #
        self.locations[self.getIndex('Praha')].addPoint(self.getIndex('Wien'), 1)  #
        self.locations[self.getIndex('Praha')].addPoint(self.getIndex('Berlin'), 1)  #

        # Collegamenti Frankfurt
        self.locations[self.getIndex('Frankfurt')].addPoint(self.getIndex('Amsterdam'), 1)  #
        self.locations[self.getIndex('Frankfurt')].addPoint(self.getIndex('Bergen'), 2)  #
        self.locations[self.getIndex('Frankfurt')].addPoint(self.getIndex('Hamburg'), 1)  #
        self.locations[self.getIndex('Frankfurt')].addPoint(self.getIndex('Helsinki'), 2)  #
        self.locations[self.getIndex('Frankfurt')].addPoint(self.getIndex('Berlin'), 1)  #
        self.locations[self.getIndex('Frankfurt')].addPoint(self.getIndex('Moskva'), 2)  #
        self.locations[self.getIndex('Frankfurt')].addPoint(self.getIndex('Wien'), 1)  #
        self.locations[self.getIndex('Frankfurt')].addPoint(self.getIndex('Istanbul'), 2)  #
        self.locations[self.getIndex('Frankfurt')].addPoint(self.getIndex('Milan'), 1)  #
        self.locations[self.getIndex('Frankfurt')].addPoint(self.getIndex('Bern'), 1)  #
        self.locations[self.getIndex('Frankfurt')].addPoint(self.getIndex('Roma'), 2)  #
        self.locations[self.getIndex('Frankfurt')].addPoint(self.getIndex('Las Palmas'), 2)  #
        self.locations[self.getIndex('Frankfurt')].addPoint(self.getIndex('Paris'), 2)  #

        # Collegamenti Brest
        self.locations[self.getIndex('Brest')].addPoint(self.getIndex('Paris'), 1)  #
        self.locations[self.getIndex('Brest')].addPoint(self.getIndex('Bordeaux'), 1)  #

        # Collegamenti Paris
        self.locations[self.getIndex('Paris')].addPoint(self.getIndex('New York'), 2)  #
        self.locations[self.getIndex('Paris')].addPoint(self.getIndex('Caracas'), 2)  #
        self.locations[self.getIndex('Paris')].addPoint(self.getIndex('Nairobi'), 2)  #
        self.locations[self.getIndex('Paris')].addPoint(self.getIndex('Paris'), 1)  #
        self.locations[self.getIndex('Paris')].addPoint(self.getIndex('Brest'), 1)  #
        self.locations[self.getIndex('Paris')].addPoint(self.getIndex('Amsterdam'), 1)  #
        self.locations[self.getIndex('Paris')].addPoint(self.getIndex('Frankfurt'), 1)  #
        self.locations[self.getIndex('Paris')].addPoint(self.getIndex('Bern'), 1)  #
        self.locations[self.getIndex('Paris')].addPoint(self.getIndex('Marseille'), 1)  #

        # Collegamenti Wien
        self.locations[self.getIndex('Wien')].addPoint(self.getIndex('Milan'), 1)  #
        self.locations[self.getIndex('Wien')].addPoint(self.getIndex('Frankfurt'), 1)  #
        self.locations[self.getIndex('Wien')].addPoint(self.getIndex('Praha'), 1)  #
        self.locations[self.getIndex('Wien')].addPoint(self.getIndex('Budapest'), 1)  #

        # Collegamenti Budapest
        self.locations[self.getIndex('Budapest')].addPoint(self.getIndex('Wien'), 1)  #
        self.locations[self.getIndex('Budapest')].addPoint(self.getIndex('Beograd'), 1)  #

        # Collegamenti Odessa
        self.locations[self.getIndex('Odessa')].addPoint(self.getIndex('Bucuresti'), 1)  #
        self.locations[self.getIndex('Odessa')].addPoint(self.getIndex('Kiyev'), 1)  #

        # Collegamenti Bucuresti
        self.locations[self.getIndex('Bucuresti')].addPoint(self.getIndex('Odessa'), 1)  #
        self.locations[self.getIndex('Bucuresti')].addPoint(self.getIndex('Beograd'), 1)  #

        # Collegamenti Beograd
        self.locations[self.getIndex('Beograd')].addPoint(self.getIndex('Bucuresti'), 1)  #
        self.locations[self.getIndex('Beograd')].addPoint(self.getIndex('Budapest'), 1)  #
        self.locations[self.getIndex('Beograd')].addPoint(self.getIndex('Sofiva'), 1)  #
        self.locations[self.getIndex('Beograd')].addPoint(self.getIndex('Athinai'), 1)  #

        # Collegamenti Milan
        self.locations[self.getIndex('Milan')].addPoint(self.getIndex('Roma'), 1)  #
        self.locations[self.getIndex('Milan')].addPoint(self.getIndex('Marseille'), 1)  #
        self.locations[self.getIndex('Milan')].addPoint(self.getIndex('Bern'), 1)  #
        self.locations[self.getIndex('Milan')].addPoint(self.getIndex('Frankfurt'), 1)  #
        self.locations[self.getIndex('Milan')].addPoint(self.getIndex('Wien'), 1)  #

        # Collegamenti Bern
        self.locations[self.getIndex('Bern')].addPoint(self.getIndex('Milan'), 1)  #
        self.locations[self.getIndex('Bern')].addPoint(self.getIndex('Frankfurt'), 1)  #
        self.locations[self.getIndex('Bern')].addPoint(self.getIndex('Paris'), 1)  #

        # Collegamenti Bordeaux
        self.locations[self.getIndex('Bordeaux')].addPoint(self.getIndex('Madrid'), 1)  #
        self.locations[self.getIndex('Bordeaux')].addPoint(self.getIndex('Brest'), 1)  #
        self.locations[self.getIndex('Bordeaux')].addPoint(self.getIndex('Paris'), 1)  #

        # Collegamenti Marseille
        self.locations[self.getIndex('Marseille')].addPoint(self.getIndex('Marseille'), 2)  #
        self.locations[self.getIndex('Marseille')].addPoint(self.getIndex('Paris'), 1)  #
        self.locations[self.getIndex('Marseille')].addPoint(self.getIndex('Madrid'), 1)  #
        self.locations[self.getIndex('Marseille')].addPoint(self.getIndex('Milan'), 1)  #

        # Collegamenti Madrid
        self.locations[self.getIndex('Madrid')].addPoint(self.getIndex('Marseille'), 1)  #
        self.locations[self.getIndex('Madrid')].addPoint(self.getIndex('Lisboa'), 1)  #
        self.locations[self.getIndex('Madrid')].addPoint(self.getIndex('Bordeaux'), 1)  #

        # Collegamenti Lisboa
        self.locations[self.getIndex('Lisboa')].addPoint(self.getIndex('London'), 2)  #
        self.locations[self.getIndex('Lisboa')].addPoint(self.getIndex('Las Palmas'), 2)  #
        self.locations[self.getIndex('Lisboa')].addPoint(self.getIndex('Dakar'), 2)  #

        # Collegamenti Roma
        self.locations[self.getIndex('Roma')].addPoint(self.getIndex('Frankfurt'), 2)  #
        self.locations[self.getIndex('Roma')].addPoint(self.getIndex('Palermo'), 2)  #
        self.locations[self.getIndex('Roma')].addPoint(self.getIndex('Jerusalem'), 2)  #
        self.locations[self.getIndex('Roma')].addPoint(self.getIndex('Tunis'), 2)  #
        self.locations[self.getIndex('Roma')].addPoint(self.getIndex('Milan'), 1)  #

        # Collegamenti Palermo
        self.locations[self.getIndex('Palermo')].addPoint(self.getIndex('Roma'), 2)  #

        # Collegamenti Sofiva
        self.locations[self.getIndex('Sofiva')].addPoint(self.getIndex('Beograd'), 1)  #
        self.locations[self.getIndex('Sofiva')].addPoint(self.getIndex('Istanbul'), 1)  #

        # Collegamenti Istanbul
        self.locations[self.getIndex('Istanbul')].addPoint(self.getIndex('Sofiva'), 1)  #
        self.locations[self.getIndex('Istanbul')].addPoint(self.getIndex('Ankara'), 1)  #

        # Collegamenti Ankara
        self.locations[self.getIndex('Ankara')].addPoint(self.getIndex('Baghdad'), 2)  #
        self.locations[self.getIndex('Ankara')].addPoint(self.getIndex('Beirut'), 1)  #
        self.locations[self.getIndex('Ankara')].addPoint(self.getIndex('Istanbul'), 1)  #

        # Collegamenti Athinai
        self.locations[self.getIndex('Athinai')].addPoint(self.getIndex('Beograd'), 1)  #
        self.locations[self.getIndex('Athinai')].addPoint(self.getIndex('Cairo'), 2)  #

        # Collegamenti Tifils
        self.locations[self.getIndex('Tifils')].addPoint(self.getIndex('Volgograd'), 1)  #
        self.locations[self.getIndex('Tifils')].addPoint(self.getIndex('Moskva'), 2)  #

        # Collegamenti Tehran
        self.locations[self.getIndex('Tehran')].addPoint(self.getIndex('Baghdad'), 2)  #
        self.locations[self.getIndex('Tehran')].addPoint(self.getIndex('Kabul'), 1)  #

        # Collegamenti Jerusalem
        self.locations[self.getIndex('Jerusalem')].addPoint(self.getIndex('Roma'), 2)  #
        self.locations[self.getIndex('Jerusalem')].addPoint(self.getIndex('Beirut'), 1)  #
        self.locations[self.getIndex('Jerusalem')].addPoint(self.getIndex('Kuwait'), 2)  #
        self.locations[self.getIndex('Jerusalem')].addPoint(self.getIndex('Mecca'), 1)  #
        self.locations[self.getIndex('Jerusalem')].addPoint(self.getIndex('Cairo'), 1)  #

        # Collegamenti Mecca
        self.locations[self.getIndex('Mecca')].addPoint(self.getIndex('Aden'), 2)  #
        self.locations[self.getIndex('Mecca')].addPoint(self.getIndex('Cairo'), 2)  #
        self.locations[self.getIndex('Mecca')].addPoint(self.getIndex('Riyadh'), 1)  #
        self.locations[self.getIndex('Mecca')].addPoint(self.getIndex('Jerusalem'), 1)  #

        # Collegamenti Aden
        self.locations[self.getIndex('Aden')].addPoint(self.getIndex('Mecca'), 2)  #
        self.locations[self.getIndex('Aden')].addPoint(self.getIndex('Addis Abeba'), 2)  #

        # Collegamenti Riyadh
        self.locations[self.getIndex('Riyadh')].addPoint(self.getIndex('Mecca'), 1)  #
        self.locations[self.getIndex('Riyadh')].addPoint(self.getIndex('Kuwait'), 2)  #

        # Collegamenti Kuwait
        self.locations[self.getIndex('Kuwait')].addPoint(self.getIndex('Baghdad'), 1)  #
        self.locations[self.getIndex('Kuwait')].addPoint(self.getIndex('Jerusalem'), 2)  #
        self.locations[self.getIndex('Kuwait')].addPoint(self.getIndex('Dubayy'), 2)  #
        self.locations[self.getIndex('Kuwait')].addPoint(self.getIndex('Riyadh'), 2)  #

        # Collegamenti Dubayy
        self.locations[self.getIndex('Dubayy')].addPoint(self.getIndex('Kuwait'), 2)  #
        self.locations[self.getIndex('Dubayy')].addPoint(self.getIndex('Bombay'), 2)  #

        # Collegamenti Baghdad
        self.locations[self.getIndex('Baghdad')].addPoint(self.getIndex('Tehran'), 2)  #
        self.locations[self.getIndex('Baghdad')].addPoint(self.getIndex('Ankara'), 2)  #
        self.locations[self.getIndex('Baghdad')].addPoint(self.getIndex('Beirut'), 1)  #
        self.locations[self.getIndex('Baghdad')].addPoint(self.getIndex('Kuwait'), 1)  #

        # Collegamenti Volgograd
        self.locations[self.getIndex('Volgograd')].addPoint(self.getIndex('Tifils'), 1)  #
        self.locations[self.getIndex('Volgograd')].addPoint(self.getIndex('Moskva'), 1)  #
        self.locations[self.getIndex('Volgograd')].addPoint(self.getIndex('Samarkand'), 1)  #

        # Collegameni Sverdiovsk
        self.locations[self.getIndex('Sverdiovsk')].addPoint(self.getIndex('Omsk'), 1)  #
        self.locations[self.getIndex('Sverdiovsk')].addPoint(self.getIndex('Perm'), 1)  #

        # Collegamenti Omsk
        self.locations[self.getIndex('Omsk')].addPoint(self.getIndex('Sverdiovsk'), 1)  #
        self.locations[self.getIndex('Omsk')].addPoint(self.getIndex('Novosibirsk'), 1)  #

        # Collegamenti Novosibirsk
        self.locations[self.getIndex('Novosibirsk')].addPoint(self.getIndex('Omsk'), 1)  #
        self.locations[self.getIndex('Novosibirsk')].addPoint(self.getIndex('Krasnoyarsk'), 1)  #

        # Collegamenti Samarkand
        self.locations[self.getIndex('Samarkand')].addPoint(self.getIndex('Alma-Ata'), 1)  #
        self.locations[self.getIndex('Samarkand')].addPoint(self.getIndex('Volgograd'), 1)  #
        self.locations[self.getIndex('Samarkand')].addPoint(self.getIndex('Kabul'), 1)  #

        # Collegamenti Kabul
        self.locations[self.getIndex('Kabul')].addPoint(self.getIndex('Samarkand'), 1)  #
        self.locations[self.getIndex('Kabul')].addPoint(self.getIndex('Karachi'), 1)  #
        self.locations[self.getIndex('Kabul')].addPoint(self.getIndex('Tehran'), 1)  #

        # Collegamenti Karachi
        self.locations[self.getIndex('Karachi')].addPoint(self.getIndex('Delhi'), 1)  #
        self.locations[self.getIndex('Karachi')].addPoint(self.getIndex('Kabul'), 1)  #

        # Collegamenti Alma-Ata
        self.locations[self.getIndex('Alma-Ata')].addPoint(self.getIndex('Samarkand'), 1)  #
        self.locations[self.getIndex('Alma-Ata')].addPoint(self.getIndex('Urumchi'), 1)  #

        # Collegamenti Krasnoyarsk
        self.locations[self.getIndex('Krasnoyarsk')].addPoint(self.getIndex('Irkutsk'), 1)  #
        self.locations[self.getIndex('Krasnoyarsk')].addPoint(self.getIndex('Novosibirsk'), 1)  #

        # Collegamenti Lhasa
        self.locations[self.getIndex('Lhasa')].addPoint(self.getIndex('Calcutta'), 1)  #
        self.locations[self.getIndex('Lhasa')].addPoint(self.getIndex('Chungking'), 1)  #

        # Collegamenti Calcutta
        self.locations[self.getIndex('Calcutta')].addPoint(self.getIndex('Delhi'), 1)  #
        self.locations[self.getIndex('Calcutta')].addPoint(self.getIndex('Madras'), 1)  #
        self.locations[self.getIndex('Calcutta')].addPoint(self.getIndex('Lhasa'), 1)  #
        self.locations[self.getIndex('Calcutta')].addPoint(self.getIndex('Rangoon'), 2)  #

        # Collegamenti Bombay
        self.locations[self.getIndex('Bombay')].addPoint(self.getIndex('Dubayy'), 2)  #
        self.locations[self.getIndex('Bombay')].addPoint(self.getIndex('Madras'), 1)  #
        self.locations[self.getIndex('Bombay')].addPoint(self.getIndex('Colombo'), 2)  #
        self.locations[self.getIndex('Bombay')].addPoint(self.getIndex('Singapore'), 2)  #
        self.locations[self.getIndex('Bombay')].addPoint(self.getIndex('Delhi'), 1)  #

        # Collegamenti Madras
        self.locations[self.getIndex('Madras')].addPoint(self.getIndex('Calcutta'), 1)  #
        self.locations[self.getIndex('Madras')].addPoint(self.getIndex('Bombay'), 1)  #

        # Collegamenti Colombo
        self.locations[self.getIndex('Colombo')].addPoint(self.getIndex('Bombay'), 2)  #
        self.locations[self.getIndex('Colombo')].addPoint(self.getIndex('Perth'), 2)  #

        # Collegamenti Irkutsk
        self.locations[self.getIndex('Irkutsk')].addPoint(self.getIndex('Norilsk'), 2)  #
        self.locations[self.getIndex('Irkutsk')].addPoint(self.getIndex('Moskva'), 2)  #
        self.locations[self.getIndex('Irkutsk')].addPoint(self.getIndex('Petropavlovsk Kamchatskiy'), 2)  #
        self.locations[self.getIndex('Irkutsk')].addPoint(self.getIndex('Krasnoyarsk'), 1)  #
        self.locations[self.getIndex('Irkutsk')].addPoint(self.getIndex('Ulan Bator'), 1)  #
        self.locations[self.getIndex('Irkutsk')].addPoint(self.getIndex('Yakutsk'), 1)  #
        self.locations[self.getIndex('Irkutsk')].addPoint(self.getIndex('Khabarovsk'), 1)  #
        self.locations[self.getIndex('Irkutsk')].addPoint(self.getIndex('Vladivostok'), 1)  #

        # Collegamenti Ulan Bator
        self.locations[self.getIndex('Ulan Bator')].addPoint(self.getIndex('Peking'), 1)  #
        self.locations[self.getIndex('Ulan Bator')].addPoint(self.getIndex('Irkutsk'), 1)  #

        # Collegamenti Rangoon
        self.locations[self.getIndex('Rangoon')].addPoint(self.getIndex('Calcutta'), 2)  #
        self.locations[self.getIndex('Rangoon')].addPoint(self.getIndex('Singapore'), 2)  #

        # Collegamenti Bangkok
        self.locations[self.getIndex('Bangkok')].addPoint(self.getIndex('Manila'), 2)  #
        self.locations[self.getIndex('Bangkok')].addPoint(self.getIndex('Nairobi'), 2)  #
        self.locations[self.getIndex('Bangkok')].addPoint(self.getIndex('Ho Chi Minh City'), 1)  #
        self.locations[self.getIndex('Bangkok')].addPoint(self.getIndex('Singapore'), 1)  #

        # Collegamenti Singapore
        self.locations[self.getIndex('Singapore')].addPoint(self.getIndex('Melbourne'), 2)  #
        self.locations[self.getIndex('Singapore')].addPoint(self.getIndex('Bombay'), 2)  #
        self.locations[self.getIndex('Singapore')].addPoint(self.getIndex('Rangoon'), 2)  #
        self.locations[self.getIndex('Singapore')].addPoint(self.getIndex('Djakarta'), 2)  #
        self.locations[self.getIndex('Singapore')].addPoint(self.getIndex('Hong Kong'), 2)  #
        self.locations[self.getIndex('Singapore')].addPoint(self.getIndex('Bangkok'), 1)  #

        # Collegamenti Peking
        self.locations[self.getIndex('Peking')].addPoint(self.getIndex('Hong Kong'), 2)  #
        self.locations[self.getIndex('Peking')].addPoint(self.getIndex('Seoul'), 1)  #
        self.locations[self.getIndex('Peking')].addPoint(self.getIndex('Ulan Bator'), 1)  #
        self.locations[self.getIndex('Peking')].addPoint(self.getIndex('Shanghai'), 1)  #

        # Collegamenti Chungking
        self.locations[self.getIndex('Chungking')].addPoint(self.getIndex('Lhasa'), 1)  #
        self.locations[self.getIndex('Chungking')].addPoint(self.getIndex('Urumchi'), 1)  #
        self.locations[self.getIndex('Chungking')].addPoint(self.getIndex('Hong Kong'), 1)  #

        # Collegamenti Hanoi
        self.locations[self.getIndex('Hanoi')].addPoint(self.getIndex('Hong Kong'), 1)  #
        self.locations[self.getIndex('Hanoi')].addPoint(self.getIndex('Ho Chi Minh City'), 1)  #

        # Collegamenti Ho Chi Minh City
        self.locations[self.getIndex('Ho Chi Minh City')].addPoint(self.getIndex('Hanoi'), 1)  #
        self.locations[self.getIndex('Ho Chi Minh City')].addPoint(self.getIndex('Bangkok'), 1)  #

        # Collegamenti Shanghai
        self.locations[self.getIndex('Shanghai')].addPoint(self.getIndex('Hong Kong'), 1)  #
        self.locations[self.getIndex('Shanghai')].addPoint(self.getIndex('Peking'), 1)  #

        # Collegamenti Seoul
        self.locations[self.getIndex('Seoul')].addPoint(self.getIndex('Taipei'), 2)  #
        self.locations[self.getIndex('Seoul')].addPoint(self.getIndex('Tokyo'), 2)  #
        self.locations[self.getIndex('Seoul')].addPoint(self.getIndex('Peking'), 1)  #
        self.locations[self.getIndex('Seoul')].addPoint(self.getIndex('Vladivostok'), 1)  #

        # Collegamenti Djakarta
        self.locations[self.getIndex('Djakarta')].addPoint(self.getIndex('Singapore'), 2)  #
        self.locations[self.getIndex('Djakarta')].addPoint(self.getIndex('Surabaja'), 2)  #

        # Collegamenti Surabaja
        self.locations[self.getIndex('Surabaja')].addPoint(self.getIndex('Djakarta'), 2)  #

        # Collegamenti Manila
        self.locations[self.getIndex('Manila')].addPoint(self.getIndex('Hong Kong'), 2)  #
        self.locations[self.getIndex('Manila')].addPoint(self.getIndex('Bangkok'), 2)  #

        # Collegamenti Hong Kong
        self.locations[self.getIndex('Hong Kong')].addPoint(self.getIndex('Singapore'), 2)  #
        self.locations[self.getIndex('Hong Kong')].addPoint(self.getIndex('Manila'), 2)  #
        self.locations[self.getIndex('Hong Kong')].addPoint(self.getIndex('Taipei'), 2)  #
        self.locations[self.getIndex('Hong Kong')].addPoint(self.getIndex('Tokyo'), 2)  #
        self.locations[self.getIndex('Hong Kong')].addPoint(self.getIndex('Peking'), 2)  #
        self.locations[self.getIndex('Hong Kong')].addPoint(self.getIndex('Hanoi'), 1)  #
        self.locations[self.getIndex('Hong Kong')].addPoint(self.getIndex('Shanghai'), 1)  #
        self.locations[self.getIndex('Hong Kong')].addPoint(self.getIndex('Chungking'), 1)  #

        # Collegamenti Taipei
        self.locations[self.getIndex('Taipei')].addPoint(self.getIndex('Hong Kong'), 2)  #
        self.locations[self.getIndex('Taipei')].addPoint(self.getIndex('Seoul'), 2)  #

        # Collegamenti Tokyo
        self.locations[self.getIndex('Tokyo')].addPoint(self.getIndex('Hong Kong'), 2)  #
        self.locations[self.getIndex('Tokyo')].addPoint(self.getIndex('Seoul'), 2)  #
        self.locations[self.getIndex('Tokyo')].addPoint(self.getIndex('Honolulu'), 2)  #

        # Collegamentei Sapporo
        self.locations[self.getIndex('Sapporo')].addPoint(self.getIndex('Tokyo'), 1)  #

        # Collegamenti Vladivostok
        self.locations[self.getIndex('Vladivostok')].addPoint(self.getIndex('Seoul'), 1)  #
        self.locations[self.getIndex('Vladivostok')].addPoint(self.getIndex('Khabarovsk'), 1)  #
        self.locations[self.getIndex('Vladivostok')].addPoint(self.getIndex('Irkutsk'), 1)  #

        # Collegamenti Khabarovsk
        self.locations[self.getIndex('Khabarovsk')].addPoint(self.getIndex('Vladivostok'), 1)  #
        self.locations[self.getIndex('Khabarovsk')].addPoint(self.getIndex('Irkutsk'), 1)  #

        # Collegamenti Norilsk
        self.locations[self.getIndex('Norilsk')].addPoint(self.getIndex('Moskva'), 2)  #
        self.locations[self.getIndex('Norilsk')].addPoint(self.getIndex('Irkutsk'), 2)  #

        # Collegamenti Yakutsk
        self.locations[self.getIndex('Yakutsk')].addPoint(self.getIndex('Oymyakon'), 1)  #
        self.locations[self.getIndex('Yakutsk')].addPoint(self.getIndex('Irkutsk'), 1)  #

        # Collegamenti Oymyakon
        self.locations[self.getIndex('Oymyakon')].addPoint(self.getIndex('Yakutsk'), 1)  #
        self.locations[self.getIndex('Oymyakon')].addPoint(self.getIndex('Magadan'), 1)  #

        # Collegamenti Magadan
        self.locations[self.getIndex('Magadan')].addPoint(self.getIndex('Oymyakon'), 1)  #
        self.locations[self.getIndex('Magadan')].addPoint(self.getIndex('Petropavlovsk Kamchatskiy'), 2)  #

        # Collegamenti Petropavlovsk Kamchatskiy
        self.locations[self.getIndex('Petropavlovsk Kamchatskiy')].addPoint(self.getIndex('Magadan'), 2)  #
        self.locations[self.getIndex('Petropavlovsk Kamchatskiy')].addPoint(self.getIndex('Irkutsk'), 2)  #

        # Collegamenti Port Darwin
        self.locations[self.getIndex('Port Darwin')].addPoint(self.getIndex('Brisbane'), 2)  #
        self.locations[self.getIndex('Port Darwin')].addPoint(self.getIndex('Perth'), 2)  #

        # Collegamenti Perth
        self.locations[self.getIndex('Perth')].addPoint(self.getIndex('Port Darwin'), 2)  #
        self.locations[self.getIndex('Perth')].addPoint(self.getIndex('Colombo'), 2)  #
        self.locations[self.getIndex('Perth')].addPoint(self.getIndex('Adelaide'), 1)  #

        # Collegamenti Alice Springs
        self.locations[self.getIndex('Alice Springs')].addPoint(self.getIndex('Adelaide'), 1)  #

        # Collegamenti Adelaide
        self.locations[self.getIndex('Adelaide')].addPoint(self.getIndex('Alice Springs'), 1)  #
        self.locations[self.getIndex('Adelaide')].addPoint(self.getIndex('Melbourne'), 1)  #
        self.locations[self.getIndex('Adelaide')].addPoint(self.getIndex('Perth'), 1)  #

        # Collegamenti Melbourne
        self.locations[self.getIndex('Melbourne')].addPoint(self.getIndex('Singapore'), 2)  #
        self.locations[self.getIndex('Melbourne')].addPoint(self.getIndex('Wellington'), 2)  #
        self.locations[self.getIndex('Melbourne')].addPoint(self.getIndex('Adelaide'), 1)  #
        self.locations[self.getIndex('Melbourne')].addPoint(self.getIndex('Canberra'), 1)  #

        # Collegamenti Canberra
        self.locations[self.getIndex('Canberra')].addPoint(self.getIndex('Brisbane'), 1)  #
        self.locations[self.getIndex('Canberra')].addPoint(self.getIndex('Melbourne'), 1)  #

        # Collegamenti Brisbane
        self.locations[self.getIndex('Brisbane')].addPoint(self.getIndex('Canberra'), 1)  #
        self.locations[self.getIndex('Brisbane')].addPoint(self.getIndex('Port Darwin'), 2)  #

        # Collegamenti Wellington
        self.locations[self.getIndex('Wellington')].addPoint(self.getIndex('Melbourne'), 2)  #
        self.locations[self.getIndex('Wellington')].addPoint(self.getIndex('Honolulu'), 2)  #

        return self.locations
    
    def getIndex(self,name):
        return next((i for i, item in enumerate(self.locations) if item.name == name), -1)