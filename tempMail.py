import tempfile
import webbrowser
import folium
from PopulateConnection import Popolate


class Map:
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start
        self.my_map = folium.Map(location=self.center, zoom_start=self.zoom_start, max_bounds=True)

    def createHtml(self):
        # my_map.
        # Display the map
        temp_name = next(tempfile._get_candidate_names()) + ".html"
        print("Salvo " + temp_name)
        self.my_map.save(temp_name)


    def getFolium(self):
        return self.my_map


class Location:
    def __init__(self, name, lat, lon):
        self.name = name
        self.pointsConnected = []
        self.lat = lat
        self.lon = lon

    def addPoint(self, pointId, distanceCost):
        pointArray = [pointId, distanceCost]
        self.pointsConnected.append(pointArray)

    def getLocations(self):
        print("Collegamenti di " + self.name)
        for y in self.pointsConnected:
            print(y[0])
        print("-----------------------------")

    def getConnections(self):
        return self.pointsConnected

    def getLat(self):
        return self.lat

    def getLon(self):
        return self.lon


def calculatePath(length, startingPoints, reached, firstPoint):
    i = length
    if i > 0:

        pL2 = allPathLevel2(startingPoints)
        if pL2:
            if i <= 2:
                if startingPoints not in reached:
                    reached.append(startingPoints)

        for o in startingPoints.getConnections():
            i = length
            if i - o[1] >= 0:
                i -= o[1]

                newStartingPoint = getNewStartingPoint(o)
                # drawLine(startingPoints, newStartingPoint, o[1])
                calculatePath(i, newStartingPoint, reached, firstPoint)
        return
    else:
        if startingPoints not in reached:
            reached.append(startingPoints)


def drawLine(start, end, type, map):
    if type == 2:
        folium.PolyLine([[start.lat, start.lon], [end.lat, end.lon]], color='#FF0000', dash_array='10').add_to(
            map.getFolium())
    else:
        folium.PolyLine([[start.lat, start.lon], [end.lat, end.lon]], color='blue').add_to(
            map.getFolium())


def allPathLevel2(point1):
    for a in point1.getConnections():
        if a[1] == 2:
            continue
        else:
            return False
    return True


def getNewStartingPoint(point2):
    for b in locations:
        if getIndex(b.name) == point2[0]:
            return b


def getIndex(name):
    return next((i for i, item in enumerate(locations) if item.name == name), -1)


# MAIN

# Creo tutti i collegamenti tra città
locations = [Location('Honolulu', 21.315603, -157.858093),
             Location('Vancouver', 45.633331, -122.599998),
             Location('Portland', 45.523064, -122.676483),
             Location('San Francisco', 37.809326, -122.409981),
             Location('Los Angeles', 34.052235, -118.243683),
             Location('Calgary', 51.121502, -114.007812),
             Location('Salt Lake City', 40.758701, -111.876183),
             Location('Edmonton', 53.522778, -113.623055),
             Location('El Paso', 31.813677450607354, -106.49889984805216),
             Location('Santa Fe', 35.691544, -105.944183),
             Location('Denver', 39.742043, -104.991531),
             Location('Winnipeg', 49.895077, -97.138451),
             Location('Mexico City', 19.432608, -99.133209),
             Location('Houston', 29.740700, -95.463600),
             Location('Minneapolis', 44.986656, -93.258133),
             Location('Duluth', 46.786671, -92.100487),
             Location('St. Louis', 38.627003, -90.199402),
             Location('New Orleans', 29.951065, -90.071533),
             Location('Guatemala', 14.628434, -90.522713),
             Location('Chicago', 41.881832, -87.623177),
             Location('Managua', 12.136389, -86.251389),
             Location('Jacksonville', 34.753956, -77.428955),
             Location('Havana', 23.113592, -82.366592),
             Location('Miami', 25.774948, -80.185989),
             Location('Washington', 38.889248, -77.050636),
             Location('Panama City', 8.983333, -79.516670),
             Location('Quito', -0.180653, -78.467834),
             Location('Kingston', 18.014650, -76.814048),
             Location('Lima', -12.046936089030828, -77.04812460581493),
             Location('New York', 40.73060402889025, -73.99117854715581),
             Location('Montreal', 45.51460707068689, -73.60624465771463),
             Location('Halifax', 44.65402913737653, -63.60534121150779),
             Location('Caracas', 10.478476565400083, -66.90200672095293),
             Location('Bogotà', 4.645289140241357, -74.10835238426442),
             Location('Manaus', -3.0571114785001248, -59.99621065974163),
             Location('Belém', -1.377816482485504, -48.4654892396583),
             Location('Recife', -8.057990855370921, -34.8989162578658),
             Location('Cuzco', -13.525447716155558, -71.96307734600705),
             Location('La Paz', -16.49815292920903, -68.13031886764102),
             Location('Brasilia', -15.793285875135243, -47.87820295105947),
             Location('Rio de Janeiro', -22.89048043792374, -43.24514989295282),
             Location('Asunción', -25.284446164143002, -57.583582614921916),
             Location('Porto Alegre', -30.053867459475192, -51.21680926590053),
             Location('Santiago', -33.46323079696967, -70.65186355648771),
             Location('Buenos Aires', -34.600231356571214, -58.42103386635462),
             Location('Punta Arenas', -53.15601625502625, -70.91051444262882),
             Location('Godthaab', 64.19095547810416, -51.68173649044631),
             Location('Tunis', 36.799751043477734, 10.165224542096324),
             Location('Alger', 36.73395150795658, 3.087339562805945),
             Location('Rabat', 33.98537733815859, -6.854343990505182),
             Location('Tripoli', 32.88867135232733, 13.191454863584362),
             Location('Bengasi', 32.112651726490284, 20.087220187761776),
             Location('Cairo', 30.04239784424635, 31.23790480509589),
             Location('Las Palmas', 28.12292918636908, -15.437491733882903),
             Location('Aswàn', 24.08792969613979, 32.899959556070584),
             Location('Tamanrasset', 22.78946509834804, 5.52344329011419),
             Location('Timbuktu', 16.778790659783176, -3.00816644491352),
             Location('Khartoum', 15.528927920295875, 32.54232804302991),
             Location('Dakar', 14.726323081129438, -17.46970721479075),
             Location('Bamako', 12.639830374197361, -7.999778280617688),
             Location('Niamey', 13.527523084099329, 2.111749674053536),
             Location('Ndjamena', 12.121767940498822, 15.054637169691675),
             Location('Addis Abeba', 9.006019927714206, 38.749968418867915),
             Location('Abidjan', 5.365553055537514, -3.995578821699679),
             Location('Accra', 5.596344276525243, -0.17590332592796612),
             Location('Lagos', 6.517898776447551, 3.377478296127528),
             Location('Yaoundé', 3.865638826521986, 11.518057080855737),
             Location('Mogadishu', 2.044495238919581, 45.33624182690682),
             Location('Nairobi', -1.2939624262859812, 36.81841638302538),
             Location('Kinshasa', -4.374751648167065, 15.296956929129635),
             Location('Dar-es-Salaam', -6.789325308727341, 39.24694995560166),
             Location('Lobito', -12.361588329179988, 13.556587325809938),
             Location('Lusaka', -15.399967538553973, 28.29904862738445),
             Location('Salisbury', -17.83562969489522, 31.041625435213174),
             Location('Tananarive', -18.90503624993189, 47.51748458146181),
             Location('Windhoek', -22.56393881594583, 17.06655022379289),
             Location('Johannesburg', -26.205507272733655, 28.012602124012304),
             Location('Cape-Town', -33.96633488482901, 18.543031467066765),
             Location('Murmansk', 68.94978040277131, 33.07816086837604),
             Location('Narvik', 68.43953342436699, 17.425608263586515),
             Location('Luleå', 65.58396351204507, 22.155933816187744),
             Location('Reykjavik', 64.1251450264626, -21.891823198138553),
             Location('Trondheim', 63.43024302250075, 10.393595156245901),
             Location('Arkhangelsk', 64.54448370427512, 40.52808790919851),
             Location('Bergen', 60.39308159333795, 5.322812589009132),
             Location('Oslo', 59.9135401986181, 10.750259258234045),
             Location('Stockholm', 59.329794145826774, 18.06732817173352),
             Location('Helsinki', 60.16877411088869, 24.937501633309207),
             Location('Leningrad', 59.9298777924397, 30.35929626489591),
             Location('Riga', 56.957830138089925, 24.123982868002038),
             Location('Perm', 58.01035136865527, 56.233196560324515),
             Location('Kopenhagen', 55.67736815940724, 12.572330566310702),
             Location('Edinburgh', 55.95345961660875, -3.2052393605812246),
             Location('Gdansk', 54.36474990365211, 18.61775711146291),
             Location('Hamburg', 53.552986110624325, 9.974632863815023),
             Location('Moskva', 55.75075855212244, 37.614293138575505),
             Location('Dublin', 53.34009190342795, -6.261558032498459),
             Location('London', 51.50548706241523, -0.13083696682427773),
             Location('Amsterdam', 52.3647987985942, 4.878143120351435),
             Location('Berlin', 52.506618705674164, 13.374563873161186),
             Location('Warsazawa', 52.24471791436062, 21.015033297155163),
             Location('Kiyev', 50.450658979907374, 30.51934254113208),
             Location('Praha', 50.08104484896988, 14.436524533428521),
             Location('Frankfurt', 50.11944664765741, 8.66279729899169),
             Location('Brest', 48.39217055455015, -4.486696895906255),
             Location('Paris', 48.86048162552169, 2.3423909196499206),
             Location('Wien', 48.19689220581868, 16.34004226535315),
             Location('Budapest', 47.493110610503464, 19.05459207060534),
             Location('Odessa', 46.46944547984643, 30.721003375438947),
             Location('Bucuresti', 44.441214153551286, 26.08558461962845),
             Location('Beograd', 44.813464332810426, 20.45428113081859),
             Location('Milan', 45.46784695870503, 9.182538329238133),
             Location('Bern', 46.95066261924856, 7.438646911683183),
             Location('Bordeaux', 44.84629438096004, -0.5896463211239207),
             Location('Marseille', 43.30342932788407, 5.371037632623498),
             Location('Madrid', 40.41663415351959, -3.700675786163321),
             Location('Lisboa', 38.719811072534405, -9.1386717574807),
             Location('Roma', 41.894718728321145, 12.480304454978478),
             Location('Palermo', 38.10272768678544, 13.381459816376115),
             Location('Sofiva', 42.69572412500409, 23.320705223365884),
             Location('Istanbul', 40.99824010567749, 28.915970133874588),
             Location('Ankara', 39.92120917120731, 32.80497111747703),
             Location('Athinai', 37.98012565680233, 23.712666856680613),
             Location('Tifils', 41.728393342260865, 44.79350116937954),
             Location('Tehran', 35.70978828971715, 51.34205412722407),
             Location('Beirut', 33.89095170272479, 35.48588892776915),
             Location('Jerusalem', 31.775130717227754, 35.22079015517044),
             Location('Mecca', 21.398406021315985, 39.82209625343083),
             Location('Aden', 12.780821186548831, 45.01756152642958),
             Location('Riyadh', 24.676183865775005, 46.70479071668007),
             Location('Kuwait', 29.374583462206793, 47.9751634438874),
             Location('Dubayy', 25.197821559726215, 55.25711652019728),
             Location('Baghdad', 33.323797454318424, 44.36928561682272),
             Location('Volgograd', 48.714588941915885, 44.49872298400437),
             Location('Sverdiovsk', 58.62622243062065, 61.541914663601474),
             Location('Omsk', 54.97732037271333, 73.36101905652717),
             Location('Novosibirsk', 55.00814759476994, 82.9212950714278),
             Location('Samarkand', 39.65827284348242, 66.94717574503495),
             Location('Kabul', 34.55601467392823, 69.1881820689787),
             Location('Karachi', 24.870125556453576, 66.99671808043995),
             Location('Delhi', 28.639246204160948, 77.18740192219532),
             Location('Alma-Ata', 43.2344972036743, 76.86067786645384),
             Location('Krasnoyarsk', 56.01627141358328, 92.87152846103274),
             Location('Urumchi', 43.86578955783496, 87.56129777160592),
             Location('Lhasa', 29.654487232904774, 91.11073366788948),
             Location('Calcutta', 22.538231944997612, 88.34612389724309),
             Location('Bombay', 19.076909647234636, 72.86635943083171),
             Location('Madras', 12.998239448359325, 80.22718394147712),
             Location('Colombo', 6.924391503365095, 79.86581930077317),
             Location('Irkutsk', 52.28157770570359, 104.2794511434263),
             Location('Ulan Bator', 47.914257164446056, 106.8959357176943),
             Location('Rangoon', 16.794553976724483, 96.1516604259627),
             Location('Bangkok', 13.776783182229947, 100.52523003926139),
             Location('Singapore', 1.2903244739963025, 103.85024563807505),
             Location('Peking', 39.90867513761209, 116.36608713189868),
             Location('Chungking', 29.535014240218437, 106.51051879246236),
             Location('Hanoi', 21.0203317373777, 105.82950831843708),
             Location('Ho Chi Minh City', 10.789268692434193, 106.64030085670346),
             Location('Shanghai', 31.214892986630534, 121.47520592140386),
             Location('Seoul', 37.54877948872791, 126.9656767221929),
             Location('Djakarta', -6.19490188699772, 106.8288775341265),
             Location('Surabaja', -7.257826620454726, 112.7555466893734),
             Location('Manila', 14.599724505115425, 120.97709923719034),
             Location('Hong Kong', 22.31448792843254, 114.16992631765187),
             Location('Taipei', 25.049869220685707, 121.47336105667424),
             Location('Tokyo', 35.69840035261359, 139.74517073385275),
             Location('Sapporo', 43.103180841432426, 141.3294984835052),
             Location('Vladivostok', 43.13086240767487, 131.89974834828095),
             Location('Khabarovsk', 48.46939590417491, 135.09856978316947),
             Location('Norilsk', 69.34918610187714, 88.19274499294565),
             Location('Yakutsk', 62.029546960189656, 129.69134820908192),
             Location('Oymyakon', 63.46460776508575, 142.77630167071337),
             Location('Magadan', 59.55562316227126, 150.80562611660503),
             Location('Petropavlovsk Kamchatskiy', 53.04806961752562, 158.6396097010467),
             Location('Port Darwin', -12.449761890838769, 130.87778536926172),
             Location('Perth', -31.9564593802894, 115.84598477252484),
             Location('Alice Springs', -23.695529795239743, 133.86295649244016),
             Location('Adelaide', -34.92897931653579, 138.59430763639205),
             Location('Melbourne', -37.81955775484325, 144.9863354041322),
             Location('Canberra', -35.279882346882026, 149.12947823379804),
             Location('Brisbane', -27.44924685684797, 153.0294493121029),
             Location('Wellington', -41.291676170186015, 174.77852700308242)
             ]
populate = Popolate(locations)
locations = populate.doPopulate()

# Scelgo il punto di partenza e inizio a creare la mappa
pointReached = []
startingPoint = locations[getIndex('Samarkand')]
coords = [0, 0]
miaMappa = Map(center=coords, zoom_start=2.5)
allLines = []

# Ciclo per ogni città collegandola alle altre, eliminando i doppioni
for point in locations:
    for h in point.getConnections():
        if [point, locations[h[0]]] not in allLines:
            allLines.append([point, locations[h[0]]])
            allLines.append([locations[h[0]], point])
            drawLine(point, locations[h[0]], h[1], miaMappa)

# Calcolo i punti raggiungibili dal punto di partenza con un certo numero di passi
#calculatePath(5, startingPoint, pointReached, startingPoint)

# Creo i marker a seconda del fatto che siano stati raggiunti o no
for coord in locations:
    if coord == startingPoint:
        if coord in pointReached:
            folium.Marker(
                location=[coord.getLat(), coord.getLon()],
                popup=coord.name,
                icon=folium.Icon(color='green')
            ).add_to(miaMappa.getFolium())
        else:
            folium.Marker(
                location=[coord.getLat(), coord.getLon()],
                popup=coord.name,
                icon=folium.Icon(color='orange')
            ).add_to(miaMappa.getFolium())
    else:
        if coord in pointReached:
            folium.Marker(
                location=[coord.getLat(), coord.getLon()],
                popup=coord.name,
                icon=folium.Icon(color='red')
            ).add_to(miaMappa.getFolium())
        else:
            folium.Marker(
                location=[coord.getLat(), coord.getLon()],
                popup=coord.name,
            ).add_to(miaMappa.getFolium())

# Siumm
miaMappa.createHtml()
window = webbrowser.open("GiroDelMonto.html")



