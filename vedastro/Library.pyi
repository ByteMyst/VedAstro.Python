# AUTO GENERATED ON 00:57 03/02/2025 +08:00
# DO NOT EDIT DIRECTLY, USE STATIC TABLE GENERATOR IN MAIN REPO

from typing import Any

class Tarabala:
    pass
class Karana:
    pass
class NithyaYoga:
    pass
class House:
    pass
class DayOfWeek:
    pass
class LunarMonth:
    pass
class Object:
    pass
class Type:
    pass
class DateTimeOffset:
    pass
class DateTime:
    pass
class Boolean:
    pass
class Int32:
    pass
class TimeSpan:
    pass
class Double:
    pass
class String:
    pass
class Time:
    pass
class Angle:
    pass
class ZodiacSign:
    pass
class ZodiacName:
    pass
class ConstellationName:
    pass
class ConstellationAnimal:
    pass
class PlanetToSignRelationship:
    pass
class PlanetToPlanetRelationship:
    pass
class HouseSubStrength:
    pass
class PlanetName:
    pass
class PlanetConstellation:
    pass
class HouseName:
    pass
class GeoLocation:
    pass
class Person:
    pass
class PanchakaName:
    pass
class EventNature:
    pass
class Varna:
    pass
class PlanetMotion:
    pass
class Shashtiamsa:
    pass
class Dasas:
    pass
class Tools:
    pass
class LunarDay:
    pass


class Calculate:
    def FindBirthTimeByAnimal(possibleBirthTime: Time, precisionHours: Double) -> JObject:
        """
        Empty sample text
        :return: JObject
         """
        ...
    def FindBirthTimeByRisingSign(possibleBirthTime: Time, precisionHours: Double) -> JObject:
        """
        Empty sample text
        :return: JObject
         """
        ...
    def FindBirthTimeHouseStrengthPerson(possibleBirthTime: Time, precisionHours: Double) -> JObject:
        """
        Empty sample text
        :return: JObject
         """
        ...
    def BouncBackInputPlanet(planetName: PlanetName, time: Time) -> String:
        """
         Special debug function 
        :return: String
         """
        ...
    def BouncBackInputGeoLocation(time: Time) -> GeoLocation:
        """
         Basic bounce back data to confirm validity or ML table needs 
        :return: GeoLocation
         """
        ...
    def BouncBackInputTime(time: Time) -> String:
        """
         Basic bounce back data to confirm validity or ML table needs 
        :return: String
         """
        ...
    def ListAPICalls(cls) -> JArray:
        """
         Returns list of all API calls for fun why not 
        :return: JArray
         """
        ...
    def AddressToGeoLocation(address: String) -> GeoLocation:
        """
         Given an address will convert to its geo location equivelant httplocalhost7071apiCalculateAddressToGeoLocationAddressGaithersburg 
        :return: GeoLocation
         """
        ...
    def SearchLocation(address: String) -> Any:
        """
        Empty sample text
        :return: Task`1
         """
        ...
    def CoordinatesToGeoLocation(latitude: String, longitude: String) -> Any:
        """
         Given coordinates will convert to its geo location equivalent httplocalhost7071apiCalculateCoordinatesToGeoLocationLatitude35.6764Longitude139.6500 
        :return: Task`1
         """
        ...
    def GeoLocationToTimezone(geoLocation: GeoLocation, timeAtLocation: DateTimeOffset) -> Any:
        """
         Gets all timezone given a location accounts for Daylight savings historical changes Note location name is not mandatory it is there because location names can change but coordinates are essential .....apiCalculateGeoLocationToTimezoneLocationTokyo JapanCoordinates35.65139.83Time1402091119770000 
        :return: Task`1
         """
        ...
    def IpAddressToGeoLocation(ipAddress: String) -> Any:
        """
         .....apiCalculateIpAddressToGeoLocationIpAddress180.89.33.89 
        :return: Task`1
         """
        ...
    def EventsAtTime(birthTime: Time, checkTime: Time, eventTagList: Any) -> Any:
        """
         Gets all events occuring at given time. Basically a slice from Events Chart Can be used by LLM to interprate final prediction. Also known as Muhurtha 
        :return: List`1
         """
        ...
    def EventsAtRange(birthTime: Time, startTime: Time, endTime: Time, eventTagList: Any, precisionHours: Int32) -> Any:
        """
        Empty sample text
        :return: List`1
         """
        ...
    def EventStartEndTime(birthTime: Time, checkTime: Time, nameOfEvent: EventName) -> Event:
        """
         Given a birth time current time and event name gets the event data occuring at current time Easy way to check if Gochara is occuring at given time with start and end time calculated Precision hard set to 1 hour TODO 
        :return: Event
         """
        ...
    def EventStartTime(birthTime: Time, checkTime: Time, eventData: EventData, precisionInHours: Int32) -> Time:
        """
        Empty sample text
        :return: Time
         """
        ...
    def EventEndTime(birthTime: Time, checkTime: Time, eventData: EventData, precisionInHours: Int32) -> Time:
        """
        Empty sample text
        :return: Time
         """
        ...
    def MatchReport(maleBirthTime: Time, femaleBirthTime: Time) -> MatchReport:
        """
         Get full kuta match data for 2 horoscopes 
        :return: MatchReport
         """
        ...
    def BirthTimeLocationAutoAIFill(personFullName: String) -> Any:
        """
        Empty sample text
        :return: Task`1
         """
        ...
    def BirthTimeAutoAIFill(personFullName: String) -> Any:
        """
         Given a famous person name will auto find birth time using LLM AI 
        :return: Task`1
         """
        ...
    def MarriageTagsAutoAIFill(personA: String, personB: String) -> Any:
        """
        Empty sample text
        :return: Task`1
         """
        ...
    def BirthLocationAutoAIFill(personFullName: String) -> Any:
        """
         Given a famous person name will auto find birth location using LLM AI 
        :return: Task`1
         """
        ...
    def MarriagePartnerNameAutoAIFill(personFullName: String) -> Any:
        """
         Given a famous person name will auto find marriage partner using LLM AI 
        :return: Task`1
         """
        ...
    def HoroscopeChat(birthTime: Time, userQuestion: String, userId: String, sessionId: String) -> Any:
        """
         Ask questions to AI astrologer about life horoscope predictions 
        :return: Task`1
         """
        ...
    def HoroscopeChat2(birthTime: Time, userQuestion: String, userId: String, sessionId: String) -> Task:
        """
        Empty sample text
        :return: Task
         """
        ...
    def HoroscopeChatFeedback(answerHash: String, feedbackScore: Int32) -> Any:
        """
        Empty sample text
        :return: Task`1
         """
        ...
    def HoroscopeFollowUpChat(birthTime: Time, followUpQuestion: String, primaryAnswerHash: String, userId: String, sessionId: String) -> Any:
        """
        Empty sample text
        :return: Task`1
         """
        ...
    def MatchChat(maleBirthTime: Time, femaleBirthTime: Time, userQuestion: String, chatSession: String) -> Any:
        """
         Ask questions to AI astrologer about life horoscope predictions 
        :return: Task`1
         """
        ...
    def HoroscopeLLMSearch(birthTime: Time, textInput: String) -> Any:
        """
         Searches all horoscopes predictions with LLM 
        :return: Task`1
         """
        ...
    def GenerateTimeListCSV(startTime: Time, endTime: Time, hoursBetween: Double) -> String:
        """
         Given a start time end time and space in hours between. Will generate massive CSV tables for ML Data Science Will contain 3 columns NameTimeLocation this can then be fed into ML Table Generator to make datasets worthy of HuggingFace 
        :return: String
         """
        ...
    def IsHouseSignName(house: HouseName, sign: ZodiacName, time: Time) -> Boolean:
        """
         Checks if the inputed sign was the sign of the house during the inputed time 
        :return: Boolean
         """
        ...
    def HouseSignName(houseNumber: HouseName, time: Time) -> ZodiacName:
        """
         Gets only the the zodiac sign name at middle longitude of the house. 
        :return: ZodiacName
         """
        ...
    def HouseZodiacSign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets the zodiac sign at middle longitude of the house with degrees data Bhava Chalit 
        :return: ZodiacSign
         """
        ...
    def HouseRasiSign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets zodiac sign for a given house counted from lagna 
        :return: ZodiacSign
         """
        ...
    def AllHouseZodiacSigns(time: Time) -> Any:
        """
         Gets the zodiac sign at middle longitude of the house. 
        :return: Dictionary`2
         """
        ...
    def AllHouseRasiSigns(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllHouseHoraSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllHouseDrekkanaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllHouseChaturthamsaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllHouseSaptamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllHouseNavamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllHouseDashamamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllHouseDwadashamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllHouseShodashamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllHouseVimshamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllHouseChaturvimshamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllHouseBhamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllHouseTrimshamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllHouseKhavedamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllHouseAkshavedamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllHouseShashtyamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def PlanetDivisionalLongitude(planetName: PlanetName, inputTime: Time, divisionalNo: Int32) -> Angle:
        """
         Calculates the divisional longitude of a planet in a Dchart divisional chart in Vedic Astrology. written by AI Human 
        :return: Angle
         """
        ...
    def DivisionalLongitude(totalDegrees: Double, divisionalNo: Int32) -> Angle:
        """
        Empty sample text
        :return: Angle
         """
        ...
    def PlanetZodiacSignBasedOnHouseLongitudes(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         Get zodiac sign planet is in based on house longitudes basically the sign of the house the planet is in based on longitudes D0 Bhava chart 
        :return: ZodiacSign
         """
        ...
    def PlanetRasiD1Sign(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         Get zodiac sign planet is in. D1 
        :return: ZodiacSign
         """
        ...
    def PlanetHoraD2Signs(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         Gets Hora D2 zodiac sign of a planet 
        :return: ZodiacSign
         """
        ...
    def HoraSignName(zodiacSign: ZodiacSign) -> ZodiacSign:
        """
         D2 chart 
        :return: ZodiacSign
         """
        ...
    def HoraSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Given a longitude will return Hora D2 sign at that longitude 
        :return: ZodiacSign
         """
        ...
    def HouseHoraD2Sign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets the zodiac sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        ...
    def PlanetDrekkanaD3Sign(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         Gets the Drekkana sign the planet is in D3 
        :return: ZodiacSign
         """
        ...
    def DrekkanaSignName(zodiacSign: ZodiacSign) -> ZodiacSign:
        """
         Given a zodiac sign will convert to drekkana D3 
        :return: ZodiacSign
         """
        ...
    def DrekkanaSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Given a longitude will return Drekkana D3 sign at that longitude 
        :return: ZodiacSign
         """
        ...
    def HouseDrekkanaD3Sign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets the Drekkana sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        ...
    def PlanetChaturthamshaD4Sign(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         D4 chart 
        :return: ZodiacSign
         """
        ...
    def ChaturthamshaSignName(zodiacSign: ZodiacSign) -> ZodiacSign:
        """
         D4 chart 
        :return: ZodiacSign
         """
        ...
    def ChaturthamshaSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Given a longitude will return Hora D4 sign at that longitude 
        :return: ZodiacSign
         """
        ...
    def HouseChaturthamshaD4Sign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets the Chaturthamsha D4 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        ...
    def PlanetSaptamshaD7Sign(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         D7 chart 
        :return: ZodiacSign
         """
        ...
    def SaptamshaSignName(zodiacSign: ZodiacSign) -> ZodiacSign:
        """
         D7 chart 
        :return: ZodiacSign
         """
        ...
    def SaptamshaSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Given a longitude will return Saptamsha D7 sign at that longitude 
        :return: ZodiacSign
         """
        ...
    def HouseSaptamshaD7Sign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets the Saptamsha D7 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        ...
    def PlanetSaptamshaSignOLD(planetName: PlanetName, time: Time) -> ZodiacName:
        """
         Saptamsa D7 and measures 4.28 degrees TODO BV RAMAN method OLD MARKED FOR OBLIVION NEEDS TESTING AGAINST NEW METHOD 
        :return: ZodiacName
         """
        ...
    def PlanetNavamshaD9Sign(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         D9 chart 
        :return: ZodiacSign
         """
        ...
    def NavamshaSignName(zodiacSign: ZodiacSign) -> ZodiacSign:
        """
         D9 chart 
        :return: ZodiacSign
         """
        ...
    def NavamshaSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Gets Navamsa D9 sign given a longitude 
        :return: ZodiacSign
         """
        ...
    def HouseNavamshaD9Sign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Get Navamsa D9 sign of house mid point 
        :return: ZodiacSign
         """
        ...
    def NavamshaSignAtLongitudeOLD(longitude: Angle) -> ZodiacSign:
        """
         Gets Navamsa D9 sign given a longitude TODO BV RAMAN method OLD MARKED FOR OBLIVION NEEDS TESTING AGAINST NEW METHOD 
        :return: ZodiacSign
         """
        ...
    def PlanetDashamamshaD10Sign(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         D10 chart 
        :return: ZodiacSign
         """
        ...
    def DashamamshaSignName(zodiacSign: ZodiacSign) -> ZodiacSign:
        """
         D10 chart 
        :return: ZodiacSign
         """
        ...
    def DashamamshaSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Given a longitude will return Dashamamsha D10 sign at that longitude 
        :return: ZodiacSign
         """
        ...
    def HouseDashamamshaD10Sign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets the Dashamamsha D10 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        ...
    def PlanetDwadashamshaD12Sign(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         D12 chart 
        :return: ZodiacSign
         """
        ...
    def DwadashamshaSignName(zodiacSign: ZodiacSign) -> ZodiacSign:
        """
         D12 chart 
        :return: ZodiacSign
         """
        ...
    def DwadashamshaSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Given a longitude will return Dwadashamsha D12 sign at that longitude 
        :return: ZodiacSign
         """
        ...
    def HouseDwadashamshaD12Sign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets the Dwadashamsha D12 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        ...
    def PlanetDwadashamshaSignOLD(planetName: PlanetName, time: Time) -> ZodiacName:
        """
         When a sign is divided into 12 equal parts each is called a Dwadasamsa D12 and measures 2.5 degrees. The Bhachakra can thus he said to contain 12x12144 Dwadasamsas. The lords of the 12 Dwadasamsas in a sign are the lords of the 12 signs from it i.e. the lord of the first Dwadasamsa in Mesha is Kuja that of the second Sukra and so on. TODO BV RAMAN method OLD MARKED FOR OBLIVION NEEDS TESTING AGAINST NEW METHOD 
        :return: ZodiacName
         """
        ...
    def PlanetShodashamshaD16Sign(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         D16 chart 
        :return: ZodiacSign
         """
        ...
    def ShodashamshaSignName(zodiacSign: ZodiacSign) -> ZodiacSign:
        """
         D16 chart 
        :return: ZodiacSign
         """
        ...
    def ShodashamshaSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Given a longitude will return Shodashamsha D16 sign at that longitude 
        :return: ZodiacSign
         """
        ...
    def HouseShodashamshaD16Sign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets the Shodashamsha D16 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        ...
    def PlanetVimshamshaD20Sign(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         D20 chart 
        :return: ZodiacSign
         """
        ...
    def VimshamshaSignName(zodiacSign: ZodiacSign) -> ZodiacSign:
        """
         D20 chart 
        :return: ZodiacSign
         """
        ...
    def VimshamshaSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Given a longitude will return Vimshamsha D20 sign at that longitude 
        :return: ZodiacSign
         """
        ...
    def HouseVimshamshaD20Sign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets the Vimshamsha D20 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        ...
    def PlanetChaturvimshamshaD24Sign(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         D24 chart 
        :return: ZodiacSign
         """
        ...
    def ChaturvimshamshaSignName(zodiacSign: ZodiacSign) -> ZodiacSign:
        """
         D24 chart 
        :return: ZodiacSign
         """
        ...
    def ChaturvimshamshaSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Given a longitude will return Chaturvimshamsha D24 sign at that longitude 
        :return: ZodiacSign
         """
        ...
    def HouseChaturvimshamshaD24Sign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets the Chaturvimshamsha D24 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        ...
    def PlanetBhamshaD27Sign(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         D27 chart 
        :return: ZodiacSign
         """
        ...
    def BhamshaSignName(zodiacSign: ZodiacSign) -> ZodiacSign:
        """
         D27 chart 
        :return: ZodiacSign
         """
        ...
    def BhamshaSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Given a longitude will return Bhamsha D27 sign at that longitude 
        :return: ZodiacSign
         """
        ...
    def HouseBhamshaD27Sign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets the Bhamsha D27 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        ...
    def PlanetTrimshamshaD30Sign(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         Get Thrimsamsa D30 sign of planet Trimshamsha or onethirtieth of a sign Reference Elements of Astrology Trimshamsha Table X12 Literally speaking it is considered as one thirtieth division of a sign. Actually however each sign is divided into five unequal parts each part belonging to one of the five planets from Mars to Saturn. In odd signs the first five degrees belong to Mars the next five degrees to Saturn the next eight degrees to Jupiter the subsequent seven degrees to Mercury and the last five degrees to Venus. This order gets reversed in case of even signs where the planets Venus Mercury Jupiter Saturn and Mars respectively own five degrees seven degrees eight degrees five degrees and five degrees in a sign. 
        :return: ZodiacSign
         """
        ...
    def TrimshamshaSignName(zodiacSign: ZodiacSign) -> ZodiacSign:
        """
         D30 chart 
        :return: ZodiacSign
         """
        ...
    def TrimshamshaSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Given a longitude will return Trimshamsha D30 sign at that longitude 
        :return: ZodiacSign
         """
        ...
    def HouseTrimshamshaD30Sign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets the Trimshamsha D30 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        ...
    def PlanetKhavedamshaD40Sign(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         D40 chart 
        :return: ZodiacSign
         """
        ...
    def KhavedamshaSignName(zodiacSign: ZodiacSign) -> ZodiacSign:
        """
         D40 chart 
        :return: ZodiacSign
         """
        ...
    def KhavedamshaSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Given a longitude will return Khavedamsha D40 sign at that longitude 
        :return: ZodiacSign
         """
        ...
    def HouseKhavedamshaD40Sign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets the Khavedamsha D40 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        ...
    def PlanetAkshavedamshaD45Sign(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         D45 chart 
        :return: ZodiacSign
         """
        ...
    def AkshavedamshaSignName(zodiacSign: ZodiacSign) -> ZodiacSign:
        """
         D45 chart 
        :return: ZodiacSign
         """
        ...
    def AkshavedamshaSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Given a longitude will return Akshavedamsha D45 sign at that longitude 
        :return: ZodiacSign
         """
        ...
    def HouseAkshavedamshaD45Sign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets the Akshavedamsha D45 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        ...
    def PlanetShashtyamshaD60Sign(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         D60 chart 
        :return: ZodiacSign
         """
        ...
    def ShashtyamshaSignName(zodiacSign: ZodiacSign) -> ZodiacSign:
        """
         D60 chart 
        :return: ZodiacSign
         """
        ...
    def ShashtyamshaSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Given a longitude will return Shashtyamsha D60 sign at that longitude 
        :return: ZodiacSign
         """
        ...
    def HouseShashtyamshaD60Sign(houseNumber: HouseName, time: Time) -> ZodiacSign:
        """
         Gets the Shashtyamsha D60 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        ...
    def AllPlanetSignsBasedOnHouseLongitudes(time: Time) -> Any:
        """
         Gets list of all planets and the zodiac signs they are in based on house longitudes 
        :return: Dictionary`2
         """
        ...
    def AllPlanetRasiSigns(time: Time) -> Any:
        """
         Gets list of all planets and the zodiac signs they are in 
        :return: Dictionary`2
         """
        ...
    def AllPlanetHoraSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllPlanetDrekkanaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllPlanetChaturthamsaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllPlanetSaptamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllPlanetNavamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllPlanetDashamamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllPlanetDwadashamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllPlanetShodashamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllPlanetVimshamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllPlanetChaturvimshamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllPlanetBhamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllPlanetTrimshamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllPlanetKhavedamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllPlanetAkshavedamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def AllPlanetShashtyamshaSign(time: Time) -> Any:
        """
        Empty sample text
        :return: Dictionary`2
         """
        ...
    def PlanetTajikaLongitude(planetName: PlanetName, birthTime: Time, scanYear: Int32) -> Angle:
        """
         Gets a given planets Tajika Longitude 
        :return: Angle
         """
        ...
    def PlanetTajikaConstellation(planetName: PlanetName, birthTime: Time, scanYear: Int32) -> Constellation:
        """
         Gets a given planets Tajika constellation 
        :return: Constellation
         """
        ...
    def PlanetTajikaZodiacSign(planetName: PlanetName, birthTime: Time, scanYear: Int32) -> ZodiacSign:
        """
         Gets a given planets Tajika zodiac sign 
        :return: ZodiacSign
         """
        ...
    def TajikaDateForYear2(birthTime: Time, scanYear: Int32) -> Time:
        """
         Annual or Progressed Horoscope The annual or progressed horoscope sidereal solar return according to Western astrology is cast the same way as the birth horoscope. The time of the commencement of the anniversary known as Varsharambha is said to begin at the exact moment when the Sun comes to the same position he was in at the time of birth. In other words the individuals New Year begins when the Sun comes back to the same point he heJd at the time of birth. Given a birth time and scan year will return exact time for tajika chart The tjika system attempts to predict in detail the likely happenings in one year of an individuals life. The system goes to such details as to predict events even on a daybyday basis or even halfaday. On account of this this system is also called the varaphala system. 
        :return: Time
         """
        ...
    def TajikaDateForYear(birthTime: Time, scanYear: Int32) -> Time:
        """
         Annual or Progressed Horoscope The annual or progressed horoscope sidereal solar return according to Western astrology is cast the same way as the birth horoscope. The time of the commencement of the anniversary known as Varsharambha is said to begin at the exact moment when the Sun comes to the same position he was in at the time of birth. In other words the individuals New Year begins when the Sun comes back to the same point he heJd at the time of birth. Calculated based on method in BV Raman book Varshaphala 
        :return: Time
         """
        ...
    def TransitHouseFromLagna(transitPlanet: PlanetName, checkTime: Time, birthTime: Time) -> HouseName:
        """
        Empty sample text
        :return: HouseName
         """
        ...
    def TransitHouseFromNavamsaLagna(transitPlanet: PlanetName, checkTime: Time, birthTime: Time) -> HouseName:
        """
        Empty sample text
        :return: HouseName
         """
        ...
    def TransitHouseFromMoon(transitPlanet: PlanetName, checkTime: Time, birthTime: Time) -> HouseName:
        """
        Empty sample text
        :return: HouseName
         """
        ...
    def TransitHouseFromNavamsaMoon(transitPlanet: PlanetName, checkTime: Time, birthTime: Time) -> HouseName:
        """
        Empty sample text
        :return: HouseName
         """
        ...
    def Murthi(transitPlanet: PlanetName, checkTime: Time, birthTime: Time) -> String:
        """
        Empty sample text
        :return: String
         """
        ...
    def AbstractActivity(checkTime: Time) -> BirdActivity:
        """
         In each of the main activities the other four activities also occur as abstract subactivity for short duration of time gaps covering the complete duration of the main activity the period being 2 hrs. 24 min for Pancha Pakshi 
        :return: BirdActivity
         """
        ...
    def MainActivity(birthTime: Time, checkTime: Time) -> BirdActivity:
        """
         Each bird performs these five activities during each day and in night over the week days and during waxing and waning Moon cycles during the 5 YAMAS in day and 5 YAMAS in night in a stipulated order for Pancha Pakshi 
        :return: BirdActivity
         """
        ...
    def BirthYama(inputTime: Time) -> BirthYama:
        """
         These 5 elemental vibrations act in 5 gradations offaculties for stipulated time intervals called YAMAS consisting of 2 hrs. 24 mits. each 6 Ghatikas each over the 5 YAMAS in the day and 5 YAMAS in the night thus spread over evenly in 24 hours. 
        :return: BirthYama
         """
        ...
    def VedicDayStartTime(inputTime: Time) -> Time:
        """
         Given a time it will find out the start time of for that vedic day If time is before sunrise the previous day 
        :return: Time
         """
        ...
    def AbstractActivityStrength(birthTime: Time, checkTime: Time) -> Double:
        """
         yama works out to 2 hrs. 24 mts. of our modern time. It is to be noted that the beginning of the day is reckoned from Sun rise to Sun set in Hindu system. Similarly night is reckoned from Sun set to Sun rise on the following day thus consisting of 24 hours for one day. The timings of the five Yamas are the same during day and night for Pancha Pakshi 
        :return: Double
         """
        ...
    def PanchaPakshiBirthBird(birthTime: Time) -> BirdName:
        """
         Gets birth bird for a birth time. Sidhas have personified the elements as birds identifying each element under which an individual is born when these elements are all functioning differentially during each time gap. These 5 elemental vibrations are personified as PAKSHIS or BIRDS and the gradations of their faculities are named as 5 activities. This bird is called his birth Stellar Lunar bird. 
        :return: BirdName
         """
        ...
    def PanchaPakshiBirthBirdFromName(name: String) -> BirdName:
        """
         Ancients have evolved a method of identifying the birth bird of other individuals by recognising the first vowel sound that shoots out while uttering the name of such individual. Here we have to be very careful in identifying the first vowel sound and not the first vowel letter ofthe other mans name. In this system the vowels referred to are ofthe Dravidian Origin TAMIL and do not indicate the English vowel sounds. This should always be borne in mind. It should be remembered that the eleven vowels of Dravidian Tamil language are distributed among the 5 birds. These vowels and consonants which contain them are to be identified from the first sound of the name. Virtually these eleven vowel sounds are to be equated and sounded by the five English vowels A E I O and U. In this language U is uttered as V U VU to project the Dravidian sound. Except the sound I all other sounds have short and long vowels. From what has been explained so far it can be understood that for the same name the birds are different during bright half and dark halfperiods of Moon where we do not know the birth data of the other person and for such persons only we should use this system 
        :return: BirdName
         """
        ...
    def IsWaxingMoon(birthTime: Time) -> Boolean:
        """
         Given a time will return true if it is on Waxing moon or Shukla Paksha or Bright half 
        :return: Boolean
         """
        ...
    def IsWaningMoon(birthTime: Time) -> Boolean:
        """
         Given a time will return true if it is on Waning moon or Krishna Paksha or Dark half 
        :return: Boolean
         """
        ...
    def FirstVowelSound(word: String) -> String:
        """
         Given a name will extract out the 1st vowel sound. Used to get Pancha Pakshi bird when birth date not known 
        :return: String
         """
        ...
    def PanchangaTable(inputTime: Time) -> PanchangaTable:
        """
         Its used to determine auspicious times and rituals. It includes multiple attributes such as Tithi lunar day Lunar Month Vara weekday Nakshatra constellation Yoga lunisolar day and Karana half of a Tithi. Disha Shool 
        :return: PanchangaTable
         """
        ...
    def DishaShool(inputTime: Time) -> String:
        """
         Here are the following Disha shool days and the directions that are considered as inauspicious or Disha shool. Check the Disha Shool chart to find the inauspicious direction to travel 
        :return: String
         """
        ...
    def LunarMonth(inputTime: Time, ignoreLeapMonth: Boolean) -> LunarMonth:
        """
         Also know as Chandramana or Hindu Month. Each Hindu month begins with the New Moon. These lunar months go by special names. The name of a lunar month is decided by the rasi in which SunMoon conjunction takes place. These names come from the constellation that Moon is most likely to occupy on the full Moon day. Names are Chaitra Vaisaakha Jyeshtha Aashaadha Sraavana etc... 
        :return: LunarMonth
         """
        ...
    def NextNewMoon(inputTime: Time) -> Time:
        """
         Gets next future New Moon date when tithi will be 1. Uses conjunctions angle to calculate with accuracy of 30min Includes start time in scan 
        :return: Time
         """
        ...
    def PreviousNewMoon(inputTime: Time) -> Time:
        """
         Gets last occured New Moon date when tithi will be 1. Uses conjunctions angle to calculate with accuracy of 30min Includes start time in scan 
        :return: Time
         """
        ...
    def SunMoonConjunctionAngle(ccc: Time) -> Angle:
        """
         Gets the distance in degrees between Sun Moon at a given time Used to calculate lunar months. 
        :return: Angle
         """
        ...
    def PlanetAvasta(planetName: PlanetName, time: Time) -> Any:
        """
         Gets all the Avastas for a planet Lajjita Garvita Kshudita etc... 
        :return: List`1
         """
        ...
    def IsPlanetInLajjitaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
         Lajjita humiliated Planet in the 5th house in conjunction with rahu or ketu Saturn or mars. 
        :return: Boolean
         """
        ...
    def IsPlanetInGarvitaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
         Garvita proud Planet in exaltation sign or moolatrikona zone happiness and gains 
        :return: Boolean
         """
        ...
    def IsPlanetInKshuditaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
         Kshudita hungry Planet in enemys sign or conjoined with enemy or aspected by enemy Grief 
        :return: Boolean
         """
        ...
    def IsPlanetInTrashitaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
         Trashita thirsty Planet in a watery sign aspected by a enemy and is without the aspect of benefic Planets The Planet who being conjoined or aspected by a Malefic or his enemy Planet is situated without the aspect of a benefic Planet in the 4th House is Trashita. Another version If the Planet is situated in a watery sign is aspected by an enemy Planet and is without the aspect of benefic Planets he is called Trashita. A planet in a Water Sign and aspected by an enemy planet with no auspiscious Graha aspecting is said to be Trishita AvasthaThirsty State. This state is in effect whenever a planet is in a Water Sign and it gets aspected by an enemy planet. But if a Gentle Planet MercuryVenusMoon aspects here it strengthens the planet in Water Sign. This Avastha is only for the aspecting enemy planet that will cause TrishitaThirst. This state shows that a planet in a watery Rasi can still be productive even when aspected by enemies though it will not be happy. As the name Thirsty State implies it indicates the lack of emotional fulfillment that a planet experiences. 
        :return: Boolean
         """
        ...
    def IsPlanetInMuditaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
         The Planet who is in his friends sign is in conjunction with Jupiter and is together with or is aspected by a friendly Planet is called Mudita Mudita sated happy Planet in a friends sign or aspected by a friend and conjoined with Jupiter Gains If a planet is in a friends sign or joined with a friend or aspected by a friend or that joined with Jupiter is called Mudita AvasthaDelighted State It is clear from explanation itself that a planet will feel delighted when it is in friendly sign or friendly planet conjunctsaspects or it is joined by the biggest benefic planet Jupiter. We can understand planets delight in such cases. Planet in friendly sign A planet in a friendly sign is productive and the stronger that friend planet the more productive it will be. 
        :return: Boolean
         """
        ...
    def IsPlanetInKshobhitaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
         If a planet is conjunct by Sun or it is aspected by Enemy Malefic Planets then it should always be known as Kshobhita AvasthaAgitated State Kshobhita guilty repentant Planet in conjunction with sun and aspected by malefics and an enemy. Penury 
        :return: Boolean
         """
        ...
    def PlanetSignTransit(startTime: Time, endTime: Time, planetName: PlanetName) -> Any:
        """
        Empty sample text
        :return: List`1
         """
        ...
    def GetConstellationTransitStartTime(startTime: Time, endTime: Time, planetName: PlanetName) -> Any:
        """
         Gets all the constellation start time for a given planet Set to an accuracy of 1 minute 
        :return: List`1
         """
        ...
    def AllPlanetConstellation(time: Time) -> Any:
        """
         Niryana Constellation of all 9 planets 
        :return: Dictionary`2
         """
        ...
    def AllTimeData(time: Time) -> Any:
        """
         Gets all possible calculations for a given Time 
        :return: List`1
         """
        ...
    def AllPlanetData(planetName: PlanetName, time: Time) -> Any:
        """
         Gets all possible calculations for a Planet at a given Time 
        :return: List`1
         """
        ...
    def AllHouseData(houseName: HouseName, time: Time) -> Any:
        """
         All possible calculations for a House at a given Time 
        :return: List`1
         """
        ...
    def AllPlanetHouseData(planetName: PlanetName, houseName: HouseName, time: Time) -> Any:
        """
         All possible calculations for a Planet and House at a given Time 
        :return: List`1
         """
        ...
    def AllZodiacSignData(zodiacName: ZodiacName, time: Time) -> Any:
        """
         All possible calculations for a Zodiac Sign at a given Time 
        :return: List`1
         """
        ...
    def TimeOffsetToLongitude(time: TimeSpan) -> Angle:
        """
         Converts time back to longitude it is the reverse of LongitudeToLMTOffset Exp 5h. 10m. 20s. E. Long. to 77 35 E. Long 
        :return: Angle
         """
        ...
    def TimeToJulianEphemerisTime(time: Time) -> Double:
        """
         Gets the ephemris time that is consumed by Swiss Ephemeris Converts normal time to Ephemeris time shown as a number 
        :return: Double
         """
        ...
    def TimeToJulianUniversalTime(time: Time) -> Double:
        """
        Empty sample text
        :return: Double
         """
        ...
    def LmtToStd(lmtDateTime: LocalMeanTime, stdOffset: TimeSpan) -> DateTimeOffset:
        """
         Convert Local Mean Time LMT to Standard Time STD API URL ..LmtToStdTime054503051932Longitude75STDOffset0530 
        :return: DateTimeOffset
         """
        ...
    def LongitudeToLMTOffset(longitudeDeg: Double) -> TimeSpan:
        """
         Convert longitude to LMT offset input longitude range 180 to 180 
        :return: TimeSpan
         """
        ...
    def LocalMeanTime(time: Time) -> String:
        """
         Given a standard time LMT and location will get Local mean time 
        :return: String
         """
        ...
    def LocalStandardTime(time: Time) -> String:
        """
         Given a standard time STD and location will get local standard time based on location Offset auto set by Google Offset API 
        :return: String
         """
        ...
    def AutoCalculateTimeRange(inputBirthTime: Time, timePreset: String, outputTimezone: TimeSpan) -> TimeRange:
        """
         supports dynamic 3 types of preset age1to10 3weeks 3months 3years fulllife 19902000 given a nice human time range will generate start and end times input users current timezone could be different from birth 
        :return: TimeRange
         """
        ...
    def DaysBetweenTimeRangePreset(inputBirthTime: Time, timePreset: String, outputTimezone: TimeSpan) -> Double:
        """
         Give a time preset 3 types will return days between them NOTE used by web UI via API for chart precision calculation 
        :return: Double
         """
        ...
    def ParseJHDFiles(personName: String, rawTextData: String) -> Person:
        """
         Easyly import Jaganath Hora .jhd files into VedAstro. Yeah Competition drives growth 
        :return: Person
         """
        ...
    def HoroscopePredictionAlpacaTemplateLoRA(birthTime: Time) -> Any:
        """
         All horoscope predictions as Alpaca Template ready for LoRA training in JSON 
        :return: Task`1
         """
        ...
    def HoroscopePredictions(birthTime: Time, filterTag: EventTag) -> Any:
        """
         Given a birth time will calculate all predictions that match for given birth time. Default includes all predictions ie Yoga Planets in Sign AshtakavargaYoga Can be filtered. 
        :return: List`1
         """
        ...
    def HoroscopePredictionNames(birthTime: Time) -> Any:
        """
         Given a birth time will calculate all prediction names that match for given birth time example Moon House 8 10th Lord in 8th House note used by AI Chat when talking to Astro tuned LLM server 
        :return: List`1
         """
        ...
    def FortunaPoint(ascZodiacSignName: ZodiacName, time: Time) -> Int32:
        """
         Calculate Fortuna Point for a given birth time place. Returns Sign Number from Lagna for KP system a fastmoving point which can differentiate between two early births as twins. 
        :return: Int32
         """
        ...
    def DestinyPoint(time: Time, ascZodiacSignName: ZodiacName) -> Int32:
        """
         Calculate Destiny Point for a given birth time place. Returns Sign Number from Lagna 
        :return: Int32
         """
        ...
    def YoniKutaAnimal(birthTime: Time) -> String:
        """
         Given a person will give yoni kuta animal with sex 
        :return: String
         """
        ...
    def YoniKutaAnimalFromConstellation(sign: ConstellationName) -> ConstellationAnimal:
        """
         Given a constellation will give animal with sex used for yoni kuta calculations and body appearance prediction 
        :return: ConstellationAnimal
         """
        ...
    def SkyChartGIF(time: Time) -> Any:
        """
         Get sky chart as animated GIF. URL can be used like a image source link 
        :return: Task`1
         """
        ...
    def SkyChart(time: Time) -> Any:
        """
         Get sky chart at a given time. SVG image file. URL can be used like a image source link 
        :return: Task`1
         """
        ...
    def SouthIndianChart(time: Time, chartType: ChartType) -> String:
        """
         Creates a kundali chart from D1 to D20. In south indian style. URL can be used like a SVG image source link 
        :return: String
         """
        ...
    def NorthIndianChart(time: Time, chartType: ChartType) -> String:
        """
         Creates a kundali chart from D1 to D20. In north indian style. URL can be used like a SVG image source link 
        :return: String
         """
        ...
    def TimeToJulianDay(time: Time) -> Double:
        """
         special function localized to allow caching note there is another version that does caching 
        :return: Double
         """
        ...
    def ConvertLmtToJulian(time: Time) -> Double:
        """
         Convert LMT to Julian Days used in Swiss Ephemeris 
        :return: Double
         """
        ...
    def DistanceBetweenPlanets(planet1: PlanetName, planet2: PlanetName, time: Time) -> Angle:
        """
         Gets longitudinal space between 2 planets Note Longitude of planet after 360 is 0 degrees when calculating difference this needs to be accounted for. Calculation in Nirayana longitudes Calculates longitudes for you 
        :return: Angle
         """
        ...
    def DistanceBetweenPlanets(planet1: Angle, planet2: Angle) -> Angle:
        """
         Gets longitudinal space between 2 planets Note Longitude of planet after 360 is 0 degrees when calculating difference this needs to be accounted for Expects you to calculate longitude 
        :return: Angle
         """
        ...
    def GreenwichApparentInJulianDays(time: Time) -> Double:
        """
         Greenwich Apparent In Julian Days 
        :return: Double
         """
        ...
    def LocalApparentTime(time: Time) -> DateTime:
        """
         Shows local apparent time from Swiss Eph 
        :return: DateTime
         """
        ...
    def PlanetDasaNature(birthTime: Time, planet: PlanetName) -> EventNature:
        """
         WARNING MARKED FOR DELETION ERONEOUS RESULTS NOT SUITED FOR INTENDED PURPOSE METHOD NOT VERIFIED This methods perpose is to define the final good or bad nature of planet in antaram. For now only data from chapter Keyplanets for Each Sign If this proves to be inacurate add more checks in this method. bindu points Similar to method GetDasaInfoForAscendant Data from pg 80 of Keyplanets for Each Sign in Hindu Predictive Astrology TODO meant to determine nature of antram 
        :return: EventNature
         """
        ...
    def SwissEphemeris(planetName: PlanetName, time: Time) -> Object:
        """
         Get planets Longitude Latitude DistanceAU SpeedLongitude SpeedLatitude... Swiss Ephemeris swe_calc wrapper for open API 
        :return: Object
         """
        ...
    def SwissEphemerisAll(time: Time) -> Any:
        """
         For all planets including Pluto Neptune Uranus Get planets Longitude Latitude DistanceAU SpeedLongitude SpeedLatitude... Uses Swiss Ephemeris directly to get values 
        :return: List`1
         """
        ...
    def IsPlanetSameHouseWithHouseLord(houseNumber: Int32, planet: PlanetName, birthTime: Time) -> Boolean:
        """
         Checks if a planet is same house not nessarly conjunct with the lord of a certain house Example Is Sun joined with lord of 9th 
        :return: Boolean
         """
        ...
    def HouseNatureScore(birthTime: Time, inputHouse: HouseName) -> Double:
        """
         Based on Shadvarga get nature of house for a person nature in number form to for easy calculation into summary good 1 bad 1 neutral 0 specially made method for life chart summary Experimental Code 
        :return: Double
         """
        ...
    def PlanetNatureScore(personBirthTime: Time, inputPlanet: PlanetName) -> Int32:
        """
         Based on Shadvarga get nature of planet for a person nature in number form to for easy calculation into summary good 1 bad 1 neutral 0 specially made method for life chart summary 
        :return: Int32
         """
        ...
    def PlanetIshtaKashtaScoreDegree(planet: PlanetName, birthTime: Time) -> Double:
        """
         Used for judging dasa good or bad Bala book pg 110 output range 5 to 5 
        :return: Double
         """
        ...
    def PlanetKashtaScore(planet: PlanetName, birthTime: Time) -> Double:
        """
         Kashta Phala Bad Strength of a Planet 
        :return: Double
         """
        ...
    def PlanetIshtaScore(planet: PlanetName, birthTime: Time) -> Double:
        """
         Ishta Phala Good Strength of a Planet 
        :return: Double
         """
        ...
    def DhumaLongitude(time: Time) -> Angle:
        """
         Dhuma Sun s longitude 13320 
        :return: Angle
         """
        ...
    def VyatipaataLongitude(time: Time) -> Angle:
        """
         360Dhumas longitude 
        :return: Angle
         """
        ...
    def PariveshaLongitude(time: Time) -> Angle:
        """
         Vyatipaatas longitude 180 
        :return: Angle
         """
        ...
    def IndrachaapaLongitude(time: Time) -> Angle:
        """
         360 Pariveshas longitude 
        :return: Angle
         """
        ...
    def UpaketuLongitude(time: Time) -> Angle:
        """
         Indrachaapas longitude 1640 
        :return: Angle
         """
        ...
    def KaalaLongitude(time: Time) -> Angle:
        """
         Kaala rises at the middle of Suns part. In other words we find the time at the middle of Suns part and find lagna rising then. That gives Kaalas longitude. 
        :return: Angle
         """
        ...
    def MrityuLongitude(time: Time) -> Angle:
        """
         Mrityu rises at the middle of Marss part. 
        :return: Angle
         """
        ...
    def ArthaprahaaraLongitude(time: Time) -> Angle:
        """
         Artha Praharaka rises at the middle of Mercurys part. 
        :return: Angle
         """
        ...
    def YamaghantakaLongitude(time: Time) -> Angle:
        """
         Yama ghantaka rises at the middle of Jupiters part 
        :return: Angle
         """
        ...
    def GulikaLongitude(time: Time) -> Angle:
        """
         Gulika rises at the middle of Saturns part. 
        :return: Angle
         """
        ...
    def MaandiLongitude(time: Time) -> Angle:
        """
         Maandi rises at the beginning of Saturns part. 
        :return: Angle
         """
        ...
    def UpagrahaLongitude(time: Time, relatedPlanet: PlanetNameEnum, upagrahaPart: String) -> Angle:
        """
         Calculates longitudes for the non sun based Upagrahas subplanets 
        :return: Angle
         """
        ...
    def UpagrahaPartNumber(inputTime: Time, inputPlanet: PlanetNameEnum) -> Int32:
        """
         Depending on whether one is born during the day or the night we divide the length of the daynight into 8 equal parts. Each part is assigned a planet. Given a planet and time the part number will be returned. Each part is 128 1.5 hours. 
        :return: Int32
         """
        ...
    def IsUpagraha(planet: PlanetName) -> Boolean:
        """
         Given a planet name will tell if it is an Upagraha planet 
        :return: Boolean
         """
        ...
    def Nutation(time: Time) -> Double:
        """
         Gets nutation from Swiss Ephemeris
        :return: Double
         """
        ...
    def AscendantDegreesToARMC(ascendant: Double, obliquityOfEcliptic: Double, geographicLatitude: Double, time: Time) -> Double:
        """
         This method is used to convert the tropical ascendant to the ARMC Ascendant Right Meridian Circle. It first calculates the right ascension and declination using the provided tropical ascendant and obliquity of the ecliptic. Then it calculates the oblique ascension by subtracting a value derived from the declination and geographic latitude from the right ascension. Finally it calculates the ARMC based on the value of the tropical ascendant and the oblique ascension. 
        :return: Double
         """
        ...
    def AyanamsaDegree(time: Time) -> Angle:
        """
         The distance between the Hindu First Point and the Vernal Equinox measured at an epoch is known as the Ayanamsa in Varahamihiras time the summer solistice coincided with the first degree of Cancer and the winter solistice with the first degree of Capricorn whereas at one time the summer solistice coincided with the middle of the Aslesha 
        :return: Angle
         """
        ...
    def PlanetSayanaLongitude(planetName: PlanetName, time: Time) -> Angle:
        """
         Get fixed longitude used in western systems connects SwissEph Library with VedAstro NOTE This method connects SwissEph Library with VedAstro Library 
        :return: Angle
         """
        ...
    def PlanetNirayanaLongitude(planetName: PlanetName, time: Time) -> Angle:
        """
         Planet longitude that has been corrected with Ayanamsa Gets planet longitude used vedic astrology Nirayana Longitude Sayana Longitude corrected to Ayanamsa Number from 0 to 360 represent the degrees in the zodiac as viewed from earth Note Since Nirayana is corrected in actuality 0 degrees will start at Taurus not Aries 
        :return: Angle
         """
        ...
    def NextLunarEclipse(time: Time) -> DateTime:
        """
         find time of next lunar eclipse UTC time 
        :return: DateTime
         """
        ...
    def NextSolarEclipse(time: Time) -> DateTime:
        """
         finds the next solar eclipse globally UTC time 
        :return: DateTime
         """
        ...
    def PlanetEphemerisLongitude(planetName: PlanetName, time: Time) -> Angle:
        """
         Get fixed longitude used in western systems aka Sayana longitude NOTE This method connects SwissEph Library with VedAstro Library 
        :return: Angle
         """
        ...
    def PlanetSayanaLatitude(planetName: PlanetName, time: Time) -> Angle:
        """
         Gets Swiss Ephemeris longitude for a planet 
        :return: Angle
         """
        ...
    def PlanetSpeed(planetName: PlanetName, time: Time) -> Double:
        """
         Speed of planet from Swiss eph 
        :return: Double
         """
        ...
    def ConstellationAtLongitude(planetLongitude: Angle) -> Constellation:
        """
         Converts Planet Longitude to Constellation equivelant Gets info about the constellation at a given longitude ie. Constellation Name Quarter Degrees in constellation etc. 
        :return: Constellation
         """
        ...
    def ZodiacSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Converts Planet Longitude to Zodiac Sign equivalent 
        :return: ZodiacSign
         """
        ...
    def LongitudeAtZodiacSign(zodiacSign: ZodiacSign) -> Angle:
        """
         Converts Zodiac Sign to Planet Longitude equivalent 
        :return: Angle
         """
        ...
    def DayOfWeek(time: Time) -> DayOfWeek:
        """
         Get Vedic Day Of Week The Hindu day begins with sunrise and continues till next sunrise.The first hora on any day will be the first hour after sunrise and the last hora the hour before sunrise the next day. 
        :return: DayOfWeek
         """
        ...
    def LordOfHoraFromWeekday(hora: Int32, day: DayOfWeek) -> PlanetName:
        """
         Gets hora lord based on hora number week day 
        :return: PlanetName
         """
        ...
    def LordOfHoraFromTime(time: Time) -> PlanetName:
        """
         Each day starts at sunrise and ends at next days sunrise. This period is divided into 24 equal parts and they are called horas. A hora is almost equal to an hour. These horas are ruled by different planets. The lords of hora come in the order of decreasing speed with respect to earth Saturn Jupiter Mars Sun Venus Mercury and Moon. After Moon we go back to Saturn and repeat the 7 planets. 
        :return: PlanetName
         """
        ...
    def HouseJunctionPoint(previousHouse: Angle, nextHouse: Angle) -> Angle:
        """
         Gets the junction point sandhi between 2 consecutive houses where one house begins and the other ends. 
        :return: Angle
         """
        ...
    def LordOfZodiacSign(signName: ZodiacName) -> PlanetName:
        """
         Gets planet which is the lord of a given sign 
        :return: PlanetName
         """
        ...
    def ZodiacSignsOwnedByPlanet(planetName: PlanetName) -> Any:
        """
         Given a planet name will return list of signs that the planet rules 
        :return: List`1
         """
        ...
    def NextZodiacSign(inputSign: ZodiacName) -> ZodiacName:
        """
         Gets next zodiac sign after input sign 
        :return: ZodiacName
         """
        ...
    def NextHouseNumber(inputHouseNumber: Int32) -> Int32:
        """
         Gets next house number after input house number goes to 1 after 12 
        :return: Int32
         """
        ...
    def PlanetExaltationPoint(planetName: PlanetName) -> ZodiacSign:
        """
         Gets the exact longitude where planet is ExaltedExaltation Exaltation Each planet is held to be exalted when it is in a particular sign. The power to do good when in exaltation is greater than when in its own sign. Throughout the sign ascribed the planet is exalted but in a particular degree its exaltation is at the maximum level. NOTE For Upagrahas no exact degree for exaltation the whole sign is counted as such exalatiotn set at degree 1 Rahu ketu have exaltation points ref Astroloy for Beginners pg. 12 
        :return: ZodiacSign
         """
        ...
    def PlanetDebilitationPoint(planetName: PlanetName) -> ZodiacSign:
        """
         Gets the exact sign longitude where planet is DebilitatedDebility TODO method needs testing Note Rahu ketu have debilitation points ref Astroloy for Beginners pg. 12 planet to sign relationship is the whole sign this is just a point The 7th house or the 180th degree from the place of exaltation is the place of debilitation or fall. The Sun is debilitated in the 10th degree of Libra the Moon 3rd of Scorpio and so on. For Upagrahas no exact degree for exaltation the whole sign is counted as such exalatiotn set at degree 1 The debilitation or depression points are found by adding 180 to the maximum points given above. While in a state of fall planets give results contrary to those when in exaltation. ref Astroloy for Beginners pg. 11 
        :return: ZodiacSign
         """
        ...
    def IsEvenSign(planetSignName: ZodiacName) -> Boolean:
        """
         Returns true if zodiac sign is an Even sign Yugma Rasis 
        :return: Boolean
         """
        ...
    def IsOddSign(planetSignName: ZodiacName) -> Boolean:
        """
         Returns true if zodiac sign is an Odd sign Oja Rasis 
        :return: Boolean
         """
        ...
    def IsFixedSign(sunSign: ZodiacName) -> Boolean:
        """
         Fixed signs Taurus Leo Scropio Aquarius. 
        :return: Boolean
         """
        ...
    def IsMovableSign(sunSign: ZodiacName) -> Boolean:
        """
         Movable signs Aries Cancer Libra Capricorn. 
        :return: Boolean
         """
        ...
    def IsCommonSign(sunSign: ZodiacName) -> Boolean:
        """
         Common signs Gemini Virgo Sagitarius Pisces. 
        :return: Boolean
         """
        ...
    def PlanetPermanentRelationshipWithPlanet(mainPlanet: PlanetName, secondaryPlanet: PlanetName) -> PlanetToPlanetRelationship:
        """
         Gets a planets permenant relationship. Based on Hindu Predictive Astrology pg. 21 Note Rahu Ketu are not mentioned in any permenant relatioship by Raman. But some websites do mention this. As such Ramans take is taken as final. Since theres so far no explanation by Raman on Rahu Ketu permenant relation it is assumed that such relationship is not needed and to make them up for conveniece sake could result in wrong prediction down the line. But temporary relationship are mentioned by Raman for Rahu Ketu so explicitly use Temperary relationship where needed. 
        :return: PlanetToPlanetRelationship
         """
        ...
    def ConvertJulianTimeToNormalTime(julianTime: Double) -> DateTime:
        """
         Converts julian time to normal time normal time can be lmt lat utc 
        :return: DateTime
         """
        ...
    def GreenwichTimeFromJulianDays(julianTime: Double) -> DateTimeOffset:
        """
         Gets Greenwich time in normal format from Julian days at Greenwich Note Inputed time is Julian days at greenwich callers reponsibility to make sure 
        :return: DateTimeOffset
         """
        ...
    def GreenwichLmtInJulianDays(time: Time) -> Double:
        """
         Gets Local mean time LMT at Greenwich UTC in Julian days based on the inputed time 
        :return: Double
         """
        ...
    def LmtToUtc(time: Time) -> DateTimeOffset:
        """
         Converts Local Mean Time LMT to Universal Time UTC 
        :return: DateTimeOffset
         """
        ...
    def SarvashtakavargaChart(birthTime: Time) -> Sarvashtakavarga:
        """
         When the benefic points contributed by each planet in Bhinnashtakavargas different signs are added we get a Sarvashtakavarga. A total of 337 benefic points are contributed by the seven planets to various houses in relation to seven planets and the lagna. 
        :return: Sarvashtakavarga
         """
        ...
    def BhinnashtakavargaChart(birthTime: Time) -> Bhinnashtakavarga:
        """
         Seven different charts are thus possible for the seven different planets. These are called as Bhinnashtakavargas. The position of each planet in the natal chart is of primary consideration. 
        :return: Bhinnashtakavarga
         """
        ...
    def PlanetAshtakvargaBindu(planet: PlanetName, signToCheck: ZodiacName, time: Time) -> Int32:
        """
         Give a planet and sign and ashtakvarga bindu can be calculated uses Bhinnashtakavarga EXP In the Suns own Ashtakvarga there are 5 bindus in Aries NOTE ON USE Ashtakvarga System pg.128 For example in the Standard Horoscope the Suns transit of Aries 3rd from Moon should prove favorable. In the Suns own Ashtakvarga there are 5 bindus in Aries. Therefore the good effects produced should be to the extent of 62. The Suns transit of Capricorn 12th from the Moon should prove adverse. Capricorn has no bindus.Therefore the evil results to be produced by this transit are to the brim. 
        :return: Int32
         """
        ...
    def PlanetAshtakvargaBinduByPlanet(mainAshtakvargaPlanet: PlanetName, planetToCheck: PlanetName, time: Time) -> Int32:
        """
         Example Get Venus bindu in Mercurys Ashtakvarga main planet 
        :return: Int32
         """
        ...
    def PlanetOwnAshtakvargaBindu(planet: PlanetName, time: Time) -> Int32:
        """
         Gets bindus for planet in its own Ashtakavarga in the sign it is in 
        :return: Int32
         """
        ...
    def GocharaKakshas(checkTime: Time, birthTime: Time) -> GocharaKakshas:
        """
         Kakshyas for daily use The concept of Kakshyas can be employed for daily use. The method of this application is simple. Prepare the Prastaraka charts for the seven planets. Then find out the longitudes of each of the seven planets on a given day. In the Prastaraka of the Sun see if the transiting Sun is passing through a Kakshya with a benefic point. For the Moons transit consider the Prastaraka of the Moon. See for all the planets. When several planets are transiting the Kakshyas where the natal planets have contributed benefic points that day is auspicious. When several planets transit the Kakshyas where there are no benefic points it is adverse time for the native The Concept of Kakshya The Prastaraka charts for different planets can be represented in a different manner to make use of the concept of Kakshyas. Each rashi or sign is divided into eight equal parts or Kakshyas The Prastaraka chart for each planet can thus be readjusted to bring in the concept of the Kakshyas. A planet is considered to be productive of benefic results when it transits a Kakshya where there is a benefic point 
        :return: GocharaKakshas
         """
        ...
    def GocharaZodiacSignCountFromMoon(birthTime: Time, currentTime: Time, planet: PlanetName) -> Int32:
        """
         Gets the Gochara sign number which is the count from birth Moon sign janma rasi to the sign the planet is at the current time. Gochara Transits 
        :return: Int32
         """
        ...
    def IsGocharaObstructed(planet: PlanetName, gocharaHouse: Int32, birthTime: Time, currentTime: Time) -> Boolean:
        """
         Check if there is an obstruction to a given Gochara obstructing housepoint Vedhanka 
        :return: Boolean
         """
        ...
    def PlanetsInGocharaHouse(birthTime: Time, currentTime: Time, gocharaHouse: Int32) -> Any:
        """
         Gets all the planets in a given Gochara House Note Gochara House number is the count from birth Moon sign janma rasi to the sign the planet is at the current time. Gochara Transits 
        :return: List`1
         """
        ...
    def Vedhanka(planet: PlanetName, house: Int32) -> Int32:
        """
         Gets the Vedhanka point of obstruction used for Gohchara calculations. The data returned comes from a fixed table. NOTE Planet exceptions are not accounted for here. Return 0 when no obstruction point exists Reference Hindu Predictive Astrology pg. 257 
        :return: Int32
         """
        ...
    def IsGocharaOccurring(birthTime: Time, time: Time, planet: PlanetName, gocharaHouse: Int32) -> Boolean:
        """
         Is SunGocharaInHouse1 Checks if a Gochara is occuring for a planet in a given house without any obstructions at a given time Note Basically a wrapper method for Gochra event calculations 
        :return: Boolean
         """
        ...
    def IsPlanetGocharaBindu(birthTime: Time, nowTime: Time, planet: PlanetName, bindu: Int32) -> Boolean:
        """
         Checks if a given planets with given number of bindu is transiting now Gochara 
        :return: Boolean
         """
        ...
    def GetCharaDasaAtTime(birthTime: Time, checkTime: Time) -> DashaPeriod:
        """
         Calculates the Chara Dasa sign at the specified checkTime based on the birthTime. 
        :return: DashaPeriod
         """
        ...
    def DasaForLife(birthTime: Time, levels: Int32, precisionHours: Int32, scanYears: Int32) -> JObject:
        """
         Given a start time and end time and birth time will calculate all dasa periods in nice JSON table format You can also set how many levels of dasa you want to calculate default is 4 7 Levels Dasa Bhukti Antaram Sukshma Prana Avi Prana Viprana 
        :return: JObject
         """
        ...
    def DasaAtRange(birthTime: Time, startTime: Time, endTime: Time, levels: Int32, precisionHours: Int32) -> JObject:
        """
         Calculates dasa for a specific time frame 
        :return: JObject
         """
        ...
    def DasaAtTime(birthTime: Time, checkTime: Time, levels: Int32) -> JObject:
        """
        Empty sample text
        :return: JObject
         """
        ...
    def DasaForNow(birthTime: Time, levels: Int32) -> JObject:
        """
        Empty sample text
        :return: JObject
         """
        ...
    def IsMercuryAfflicted(time: Time) -> Boolean:
        """
         Whenever an affiiction by way of a malefic occupying a certain house or joining with a certain planet is suggested by implication an aspect is also meant though an affliction caused by aspect.is comparatively less malevolent Note TODO presently not 100 sure if what is meant by affliction is solely only limited to aspects conjunction with bad planets. Or Located in enemy sign an affliction Low shadbala an affliction Low drikbala an affliction At present malefic aspects conjunctions are used becasue it seems based on texts that this is correct. But it seems mercury in enemny sign or position in a house should also play a role. There must be a corelation between shadbala or drikbala to aspects conjucntion A more precise way of mesurement it could be via the bala method. Needs testing for sure to find out what bala values determine an afflicted mercury 
        :return: Boolean
         """
        ...
    def IsMercuryMalefic(time: Time) -> Boolean:
        """
         Check if Mercury is malefic true returns false if benefic References Mercury by nature is called sournya or good. And if he is in conjunction with the Sun Saturn Mars Rahu or Ketu he will be a malefic. His conjunction with beneficial planets like Full Moon Jupiter or Venus will classify him as a benefic. Benefic means a good and malefic means an evil planet. TODO Does malefic moon make it malefic atm malefic moon makes it malefic Though in the earlier pages Mercury is defined either as a subba benefic or papa malefic according to its association is with a benefic or malefic Mercury for purposes of calculating Drisbtibala of Bbavas is to be deemed as a full benefic. This is in accord with the injunctions of classical writers Gurugnabbyam tu yuktasya poomamekam tu yojayet. 11. Benefics and Malefics. Among these Srya ani Mangal decreasing Candr Rahu and Ketu the ascending and the descending nodes of Candr are malefics while the rest are benefics. Budh however is a malefic if he joins a malefic. Note ATM malefic planets override benefic TODO not sure if malefic planet overrides benefic if both are conjunct 
        :return: Boolean
         """
        ...
    def IsMoonBenefic(time: Time) -> Boolean:
        """
         Moon is a benefic from the 8th day of the bright half of the lunar month to the 8th day of the dark half of the lunar month and a malefic in the rest of the days. Returns true if benefic false if malefic 
        :return: Boolean
         """
        ...
    def IsPlanetBenefic(planetName: PlanetName, time: Time) -> Boolean:
        """
         Checks if a given planet is benefic 
        :return: Boolean
         """
        ...
    def BeneficPlanetList(time: Time) -> Any:
        """
         Gets all planets that are benefics at a given time since moon mercury changes Benefics on the other hand tend to do good but sometimes they also become capable of doing harm. 
        :return: List`1
         """
        ...
    def IsPlanetMalefic(planetName: PlanetName, time: Time) -> Boolean:
        """
         Checks if a given planet is Malefic 
        :return: Boolean
         """
        ...
    def MaleficPlanetList(time: Time) -> Any:
        """
         Gets list of permanent malefic planets for moon mercury it is based on changing factors Malefics are always inclined to do harm but under certain conditions the intensity of the mischief is tempered. 
        :return: List`1
         """
        ...
    def PlanetsInAspect(inputPlanet: PlanetName, time: Time) -> Any:
        """
         Gets all planets the inputed planet is transmitting aspect to 
        :return: List`1
         """
        ...
    def PlanetAspectDegree(receiver: PlanetName, trasmitter: PlanetName, time: Time) -> Double:
        """
         Calculate aspect angle between 2 planets 
        :return: Double
         """
        ...
    def PlanetsAspectingPlanet(receivingAspect: PlanetName, time: Time) -> Any:
        """
         Gets all planets the transmitting aspect to inputed planet 
        :return: List`1
         """
        ...
    def HousesInAspect(planet: PlanetName, time: Time) -> Any:
        """
         Gets houses aspected by the inputed planet 
        :return: List`1
         """
        ...
    def PlanetsAspectingHouse(inputHouse: HouseName, time: Time) -> Any:
        """
         Gets all planets aspecting inputed house 
        :return: List`1
         """
        ...
    def IsPlanetAspectedByPlanet(receiveingAspect: PlanetName, transmitingAspect: PlanetName, time: Time) -> Boolean:
        """
         Checks if the a planet is aspected by another planet 
        :return: Boolean
         """
        ...
    def IsHouseAspectedByPlanet(receiveingAspect: HouseName, transmitingAspect: PlanetName, time: Time) -> Boolean:
        """
         Checks if a house is aspected by a planet 
        :return: Boolean
         """
        ...
    def IsPlanetConjunctWithPlanet(planetA: PlanetName, planetB: PlanetName, time: Time) -> Boolean:
        """
         Checks if the a planet is conjunct with another planet Based on longitudes Note Both planets A B are checked if they are in conjunct with each other performance might be effected mildly but errors in conjunction calculation would be caught here. Can be removed once conjunction calculator is confirmed accurate. 
        :return: Boolean
         """
        ...
    def IsPlanetConjunctWithBeneficPlanets(inputPlanet: PlanetName, time: Time) -> Boolean:
        """
         Check if benefic planets are conjunct with specified planet 
        :return: Boolean
         """
        ...
    def PlanetPowerPercentage(inputPlanet: PlanetName, time: Time) -> Double:
        """
         convert the planets strength into a value over hundred with max min set by strongest weakest planet 
        :return: Double
         """
        ...
    def PickOutStrongestPlanet(relatedPlanets: Any, birthTime: Time) -> PlanetName:
        """
         Given a list of planets will pick out the strongest planet based on Shadbala 
        :return: PlanetName
         """
        ...
    def AllPlanetOrderedByStrength(time: Time) -> Any:
        """
         Returns an array of all planets sorted by strenght 0 index being strongest to 8 index being weakest Note Significance of being Powerful.Among the several planets associated with a bhava that which has the greatest Sbadbala influences the bhava most. 
        :return: List`1
         """
        ...
    def IsPlanetStrongInShadbala(planet: PlanetName, time: Time) -> Boolean:
        """
         Significance of being Powerful.Among the several planets associated with a bhava that which has the greatest Sbadbala influences the bhava most. Powerful Planets.Ravi is befd to be powerful when his Shadbala Pinda is 5 or more rupas. Chandra becomes strong when his Shadbala Pinda is 6 or more rupas. Kuja becomes powerful when bis Shadbala Pinda does not fall short of 5 rupas.Budha becomes potent by having his Sbadbala Pinda as 7 rupas Guru Sukra and Sani become thoroughly powerful if their Shadbala Pindas are 6.5 5.5 and 5 rupas or more respectively. 
        :return: Boolean
         """
        ...
    def IsHouseBeneficInShadbala(house: HouseName, birthTime: Time, threshold: Double) -> Boolean:
        """
         sets benefic if above 450 score 
        :return: Boolean
         """
        ...
    def AllPlanetStrength(time: Time) -> Any:
        """
         Gets strength shadbala of all 9 planets 
        :return: List`1
         """
        ...
    def AllHousesOrderedByStrength(time: Time) -> HouseName:
        """
         Returns an array of all houses sorted by strength 0 index being strongest to 11 index being weakest 
        :return: HouseName[]
         """
        ...
    def PlanetShadbalaPinda(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         THE FINAL TOTAL STRENGTH Shadbala the six sources of strength and weakness the planets The importance of and the part played by the Shadbalas in the science of horoscopy are manifold In order to obtain the total strength of the Shadbala Pinda of each planet we have to add together its Sthana Bala Dik Bala Kala Bala. Chesta Bala and Naisargika Bala. And the Grahas Drik Bala must be added to or subtracted from the above sum according as it is positive or negative. The result obtained is the Shadbala Pinda of the planet in Shashtiamsas. Note Rahu Ketu supported via house lord 
        :return: Shashtiamsa
         """
        ...
    def PlanetStrength(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         get total combined strength of the inputed planet input birth time to get strength in horoscope note an alias method to GetPlanetShadbalaPinda strength is easier to remember 
        :return: Shashtiamsa
         """
        ...
    def PlanetDrikBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Aspect strength This strength is gained by the virtue of the aspect Graha Dristi of different planets on other planet. The aspect of benefics is considered to be strength and the aspect of malefics is considered to be weaknesses. Drik Bala.This means aspect strength. The Drik Bala of a Gqaha is onefourth of the Drishti Pinda on it. It is positive or negative according as the Drishti Pinda is positive or negative. See the formula given on page 85. There is special aspect for Jupiter Mars and Saturn on the 5th and 9th 4th and 8th and 3rd and 10th signs respectively. 
        :return: Shashtiamsa
         """
        ...
    def FindViseshaDrishti(dk: Double, p: PlanetName) -> Double:
        """
         Get special aspect if any of Kuja Guru and Sani 
        :return: Double
         """
        ...
    def FindDrishtiValue(dk: Double) -> Double:
        """
        Empty sample text
        :return: Double
         """
        ...
    def PlanetNaisargikaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Nalsargika Bala.This is the natural strength that each Graha possesses. The value assigned to each depends upon its luminosity. Ravi the brightest of all planets has the greatest Naisargika strength while Sani the darkest has the least Naisargika Bala. This is the natural or inherent strength of a planet. 
        :return: Shashtiamsa
         """
        ...
    def PlanetChestaBala(planetName: PlanetName, time: Time, useSpecialSunMoon: Boolean) -> Shashtiamsa:
        """
         NOTE sun moon get score for ISHTAKESHA calculation only when specified for IshataKashta MOTIONAL STRENGTH Chesta here means Vakra Chesta or act of retrogression. Each planet except the Sun and the Moon and shadowy planets get into the state of Vakra or retrogression when its distance from the Sun exceeds a particular limit. And the strength or potency due to the planet on account of the arc of the retrogression is termed as Chesta Bala Deduct from the Seeghrocbcha half the sum of the True and Mean Longitudes of planets and divide the difference by 3. The quotient is the Chestabala. Max 60 meaning RetrogradeVakra When the distance of any one planet from the Sun exceeds a particular limit it becomes retrograde i.e. when the planet goes from perihelion the point in a planets orbit nearest to the Sun to aphelion the part of a planets oroit most distant from the Sun as it recedes from the Sun it gradually loses the power of the Suns gravitation and consequently 
        :return: Shashtiamsa
         """
        ...
    def SunChestaBala(inputTime: Time) -> Shashtiamsa:
        """
         special function to get chesta score for IshtaKashta score Bala book pg. 108 Sun has no Chesta kendra or Chesta bala as he never gets into retrogression. But still a method is prescribed to find his Chesla Bala which is necessary to ascertain the lshta and Kashta Phalas. 
        :return: Shashtiamsa
         """
        ...
    def MoonChestaBala(inputTime: Time) -> Shashtiamsa:
        """
         special function to get chesta score for IshtaKashta score Bala book pg. 108 
        :return: Shashtiamsa
         """
        ...
    def Madhya(epochToBirthDays: Double, time1: Time) -> Any:
        """
         The mean position of a planet is the position which it would have attained at a uniform rate of motion and the corrections to be applied in respect of the eccentricity of the orbit are not considered 
        :return: Dictionary`2
         """
        ...
    def EpochInterval(time1: Time) -> Double:
        """
         Get interval from the epoch to the birth date in days The result represents the interval from the epoch to the birth date. 
        :return: Double
         """
        ...
    def PlanetMotionName(planetName: PlanetName, time: Time) -> PlanetMotion:
        """
         Gets the planets motion name can be Retrograde Direct Stationary a name version of Chesta Bala 
        :return: PlanetMotion
         """
        ...
    def IsPlanetRetrograde(planetName: PlanetName, time: Time) -> Boolean:
        """
         A retrograde planet moves in the reverse direction and instead of increasing its longitude decreases as the time elapses. Rahu and Ketu often move in retrograde direction only. Other planets except the Sun and the Moon are subject to retrogression from time to time. 
        :return: Boolean
         """
        ...
    def IsPlanetCombust(planetName: PlanetName, time: Time) -> Boolean:
        """
         Determines if a given planet is combust at a specific time. Combustion of planets Planets when too close to the Sun become invisible and are labelled as combust. A combust planet loses its strength and tends to behave adversely according to predictive astrology. Aryabhata has the following to say about combustion When the Moon has no latitude i.e. when it is at zero degree of latitude it is visible when situated at a distance of 12 degrees from the Sun. Venus is visible when 9 degrees distant from the Sun. The other planets taken in the order of decreasing sizes viz. Jupiter Mercury Saturn and Mars are visible when they are 9 degrees increased by twos i.e. when they are 11 13 15 and 17 degrees distant from the Sun. The degrees as mentioned above are generally taken as the limits within which the respective planets are said to be combust. 
        :return: Boolean
         """
        ...
    def PlanetCirculationTime(planetName: PlanetName) -> Double:
        """
         circulation time of the objects in years used by cheshta bala calculation 
        :return: Double
         """
        ...
    def PlanetSaptavargajaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Sapthavargajabala This is the strength of a planet due to its residence in the seven subdivisions according to its relation with the dispositor. Saptavargaja bala means the strength a planet gets by virtue of its disposition in a friendly neutral or inimical Rasi Hora Drekkana Sapthamsa Navamsa Dwadasamsa and Thrimsamsa. 
        :return: Shashtiamsa
         """
        ...
    def PlanetSthanaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         residence of the planet and as such a certain degree of strength or weakness attends on it Positonal strength A planet occupies a certain sign in a Rasi and friendly neutrai or inimical varga. It is either exalted or debilitated lt ocupies its Moolathrikona or it has its own varga. All these states refer to the position or residence of the planet and as such a certain degree of strength or weakness attends on it. This strength or potency is known as the Sthanabala. 1.Uccha Bala Uccha means exaltation. When a planet is placed in its highest exaltation point it is of full strength and when it is in its deepest debilitation point it is devoid of any strength. When in between the strength is calculated proportionately dependent on the distance these planets are placed from the highest exaltation or deepest debilitation point. 2.Sapta Vargiya Bala Rashi Hora Drekkana Saptamsha Navamsha Dwadasamsha and Trimsamsha constitute the Sapta Varga. The strength of the planets in these seven divisional charts based on their placements in Mulatrikona own sign friendly sign etc. constitute the Sapta vargiya bala. 3.OjaYugma RashiAmsha Bala Oja means odd signs and Yugma means even signs. Thus as the name imply this strength is derived from a planets placement in the odd or even signs in the Rashi and Navamsha. 4.Kendradi Bala The name itself implies how to compute this strength. A planet in a Kendra 14710 gets full strength while one in Panapara 25811 gets half and the one in Apoklimas 12369 gets quarter strength. 5.Drekkana Bala Due to placement in first second or third Drekkana of a sign male female and hermaphrodite planets respectively get a quarter strength according to placements in the first second and third Drekkana. 
        :return: Shashtiamsa
         """
        ...
    def PlanetDrekkanaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Drekkanabala The Sun Jupiter and Mars in the lst Saturn and Mercury in the 2nd and the Moon and Venus in the last Drekkana get full strength of 60 shashtiamsas. 
        :return: Shashtiamsa
         """
        ...
    def PlanetKendraBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Kendrtzbala Planets in Kendras get 60 shashtiamsas in Panapara 30 and in Apoklima 15. 
        :return: Shashtiamsa
         """
        ...
    def PlanetOjayugmarasyamsaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Ojayugmarasyamsa In odd Rasi and Navamsa the Sun Mars Jupiter Mercury and Saturn get strength and the rest in even signs 
        :return: Shashtiamsa
         """
        ...
    def PlanetKalaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Gets a planets Kala Bala or Temporal strength 
        :return: Shashtiamsa
         """
        ...
    def PlanetYuddhaBala(inputedPlanet: PlanetName, preKalaBalaValues: Any, time: Time) -> Shashtiamsa:
        """
         Two planets are said to be in Yuddha or fight when they are in conjunction and the distance between them is less than one degree. TODO Not fully tested Yuddhabala All planets excepting the Sun and the Moon enter into war when two planets are in the same degree. The pJanet having the lesser longitude is the winner. Find out the sum total of the SthanabaJa Kalabala and Digbala of these two planets. Difference between the two divided by the difference of their diameters of its disc gives the Yuddhabala. Add this to the victorious planet and dedu_ct it from the vanquished. 
        :return: Shashtiamsa
         """
        ...
    def PlanetAyanaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Ayanabala All planets get 30 shasbtiamsas at the equator. For the Sun Jupiter Mars and Venus add proportionately when they are in northern course and for the Moon and Saturn when in southern course. Deduct proportionately when they are in the opposite direction. Unit of strength is 60 shashtiamsas. TODO some values for calculation with standard hooscope out of whack it seems small differences in longitude seem magnified at final value not 100 sure need further testing for confirmation but final values seem ok so far 
        :return: Shashtiamsa
         """
        ...
    def PlanetDeclination(planetName: PlanetName, time: Time) -> Double:
        """
         A heavenly body moves northwards the equator for sometime and then gets southwards. This angular distance from the equinoctial or celestial equator is Kranti or the declination. Declinations are reckoned plus or minus according as the planet is situated in the northern or southern celestial hemisphere 
        :return: Double
         """
        ...
    def EclipticObliquity(time: Time) -> Double:
        """
         true obliquity of the Ecliptic includes nutation 
        :return: Double
         """
        ...
    def PlanetHoraBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Hora Bala AKA Horadhipathi Bala 
        :return: Shashtiamsa
         """
        ...
    def PlanetAbdaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         The planet who is the king of the year of birth is assigned a value of 15 Shashtiamsas as his Abdabala. 
        :return: Shashtiamsa
         """
        ...
    def PlanetMasaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Gets a planets masa bala the lord of the month of birth is assigned a value of 30 Shashtiamsas as his Masabala 
        :return: Shashtiamsa
         """
        ...
    def PlanetVaraBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
        Empty sample text
        :return: Shashtiamsa
         """
        ...
    def YearAndMonthLord(time: Time) -> Object:
        """
         Gets year month lord at inputed time 
        :return: Object
         """
        ...
    def PlanetTribhagaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Thribhagabala Mercury the Sun and Saturn get 60 shashtiamsas each during the lst 2nd and 3rd onethird positions of the day respectively. The Moon Venus and Mars govern the lst 2nd and 3rd onethird portion of the night respectively. Jupiter is always strong and gets 60 shashtiamsas of strength. 
        :return: Shashtiamsa
         """
        ...
    def PlanetOchchaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Oochchabala The distance between the planets longitude and its debilitation point divided by 3 gives its exaltation strength or oochchabaJa. 
        :return: Shashtiamsa
         """
        ...
    def PlanetPakshaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Pakshabala When the Moon is waxing take the distance from the Sun to the Moon and divide it by 3. The quotient is the Pakshabala. When the Moon is waning take the distance from the Moon to the Sun and divide it by 3 for assessing Pakshabala. Moon Jupiter Venus and Mercury are strong in Sukla Paksha and the others in Krishna Paksha. Note Mercury is benefic or malefic based on planets conjunct with it 
        :return: Shashtiamsa
         """
        ...
    def PlanetNathonnathaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Nathonnathabala Midnight to midday the Sun Jupiter and Venus gain strength proportionately till they get maximum at zenith. The other planets except Mercury. are gaining strength from midday to midnight proportionately. In the same way Mercury is always strong and gets 60 shashtiamsas. 
        :return: Shashtiamsa
         """
        ...
    def PlanetDigBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Gets Dig Bala of a planet. Jupiter and Mercury are strong in Lagna Ascendant the Sun and Mars in the 10th Saturn in the 7th and the Moon and Venus in the 4th. The opposite houses are weak points. Divide the distance between the longitude of the planet and its depression point by 3. Quotient is the strength. 
        :return: Shashtiamsa
         """
        ...
    def HouseStrength(inputHouse: HouseName, time: Time) -> Shashtiamsa:
        """
         Bhava Bala.Bhava means house and Bala means strength. Bhava Bala is the potency or strength of the house or bhava or signification. We have already seen that there are 12 bhavas which comprehend all human events. Each bhava signifies or indicates certain events or functions. For instance the first bhava represents Thanu or body the appearance of the individual his complexion his disposition his stature etc. If it attains certain strength the native will enjoy the indications of the bhava fully otherwise he will not sufficiently enjoy them. The strength of a bhava is composed of three factors viz. 1 Bhavadhipathi Bala 2 Bhava Digbala 3 Bhava Drishti Bala. 
        :return: Shashtiamsa
         """
        ...
    def BhavaDrishtiBala(time: Time) -> HouseSubStrength:
        """
         House received aspect strength Bhavadrishti Bala.Each bhava in a horoscope remains aspected by certain planets. Sometimes the aspect cast on a bhava will be positive and sometimes it will be negative according as it is aspected by benefics or malefics. For all 12 houses 
        :return: HouseSubStrength
         """
        ...
    def BhavaDigBala(time: Time) -> HouseSubStrength:
        """
         House strength from different types of signs Bhava Digbala.This is the strength acquired by the different bhavas falling in the different groups or types of signs. For all 12 houses 
        :return: HouseSubStrength
         """
        ...
    def BhavaAdhipathiBala(time: Time) -> HouseSubStrength:
        """
         Bhavadhipatbi Bala This is the potency of the lord of the bhava. For all 12 houses 
        :return: HouseSubStrength
         """
        ...
    def BeneficPlanetListByShadbala(personBirthTime: Time, threshold: Int32) -> Any:
        """
         0 index is strongest 
        :return: List`1
         """
        ...
    def BeneficPlanetListByShadbala(personBirthTime: Time) -> Any:
        """
        Empty sample text
        :return: List`1
         """
        ...
    def BeneficHouseListByShadbala(personBirthTime: Time, threshold: Int32) -> Any:
        """
         0 index is strongest 
        :return: List`1
         """
        ...
    def BeneficHouseListByShadbala(personBirthTime: Time) -> Any:
        """
        Empty sample text
        :return: List`1
         """
        ...
    def MaleficPlanetListByShadbala(personBirthTime: Time, threshold: Int32) -> Any:
        """
        Empty sample text
        :return: List`1
         """
        ...
    def MaleficPlanetListByShadbala(personBirthTime: Time) -> Any:
        """
         0 index is most malefic 
        :return: List`1
         """
        ...
    def MaleficHouseListByShadbala(personBirthTime: Time, threshold: Int32) -> Any:
        """
         0 index is most malefic 
        :return: List`1
         """
        ...
    def MaleficHouseListByShadbala(personBirthTime: Time) -> Any:
        """
        Empty sample text
        :return: List`1
         """
        ...
    def GetAllEventDataGroupedByTag(cls) -> JObject:
        """
         Gets all events names grouped by tags for printing on website for user selection when generating events chart. 
        :return: JObject
         """
        ...
    def GetAllEventsChartAlgorithms(cls) -> JArray:
        """
         Gets all possible algorithm functions for printing on website for user selection when generating events chart. 
        :return: JArray
         """
        ...
    def GetHouseTags(house: HouseName) -> String:
        """
         keywords or tag related to a house 
        :return: String
         """
        ...
    def GetSignTags(zodiacName: ZodiacName) -> String:
        """
         Given a zodiac sign will return astro keywords related to sign These details would be highly useful in the delineation of character and mental disposition SourceHindu Predictive Astrology pg.16 
        :return: String
         """
        ...
    def GetPlanetTags(planetList: Any) -> String:
        """
        Empty sample text
        :return: String
         """
        ...
    def GetPlanetTags(lordOfHouse: PlanetName) -> String:
        """
         Get keywords related to a planet. 
        :return: String
         """
        ...
    def GetHouseType(houseNumber: HouseName) -> String:
        """
         Source Hindu Predictive Astrology pg.17 
        :return: String
         """
        ...
    def GetDasaInfoForAscendant(ascendantName: ZodiacName) -> String:
        """
         Get general planetary info for persons dasa hardcoded table It is intended to be used to interpret dasa predictions as such should be displayed next to dasa chart. This method is direct translation from the book. Similar to method GetPlanetDasaNature Data from pg 80 of Keyplanets for Each Sign in Hindu Predictive Astrology 
        :return: String
         """
        ...
    def SignProperties(inputSign: ZodiacName) -> SignProperties:
        """
         Gets the characteristic of signs 
        :return: SignProperties
         """
        ...
    def HousesOwnedByPlanet(inputPlanet: PlanetName, time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def HouseFromSignName(zodiacName: ZodiacName, inputTime: Time) -> HouseName:
        """
        NO DESC FOUND!! ERROR
        :return: HouseName
         """
        ...
    def DayDurationHours(time: Time) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def IsNightBirth(birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsDayBirth(birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def GhatakaChakra(time: Time, birthTime: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def LordOfConstellation(constellation: ConstellationName) -> PlanetName:
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        ...
    def IsPlanetInWaterySign(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def ResidentialStrength(planetName: PlanetName, time: Time) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def LunarDay(time: Time) -> LunarDay:
        """
        NO DESC FOUND!! ERROR
        :return: LunarDay
         """
        ...
    def MoonConstellation(time: Time) -> Constellation:
        """
        NO DESC FOUND!! ERROR
        :return: Constellation
         """
        ...
    def PlanetConstellation(planet: PlanetName, time: Time) -> Constellation:
        """
        NO DESC FOUND!! ERROR
        :return: Constellation
         """
        ...
    def Tarabala(time: Time, person: Person) -> Tarabala:
        """
        NO DESC FOUND!! ERROR
        :return: Tarabala
         """
        ...
    def Chandrabala(time: Time, person: Person) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def MoonSignName(time: Time) -> ZodiacName:
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        ...
    def LagnaSignName(time: Time) -> ZodiacName:
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        ...
    def NithyaYoga(time: Time) -> NithyaYoga:
        """
        NO DESC FOUND!! ERROR
        :return: NithyaYoga
         """
        ...
    def Karana(time: Time) -> Karana:
        """
        NO DESC FOUND!! ERROR
        :return: Karana
         """
        ...
    def SunSign(time: Time) -> ZodiacSign:
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacSign
         """
        ...
    def TimeSunEnteredCurrentSign(time: Time) -> Time:
        """
        NO DESC FOUND!! ERROR
        :return: Time
         """
        ...
    def TimeSunLeavesCurrentSign(time: Time) -> Time:
        """
        NO DESC FOUND!! ERROR
        :return: Time
         """
        ...
    def PlanetsInHouse(houseNumber: HouseName, time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def PlanetsInHouseBasedOnSign(houseNumber: HouseName, time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def PlanetsInSign(signName: ZodiacName, time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def AllPlanetLongitude(time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def AllPlanetFixedLongitude(time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def HousePlanetOccupiesBasedOnLongitudes(planetName: PlanetName, time: Time) -> HouseName:
        """
        NO DESC FOUND!! ERROR
        :return: HouseName
         """
        ...
    def HousePlanetOccupiesBasedOnSign(planetName: PlanetName, time: Time) -> HouseName:
        """
        NO DESC FOUND!! ERROR
        :return: HouseName
         """
        ...
    def HouseAllPlanetOccupiesBasedOnLongitudes(time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: Dictionary`2
         """
        ...
    def LordOfHouse(houseNumber: HouseName, time: Time) -> PlanetName:
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        ...
    def PlanetLordOfZodiacSign(inputPlanet: PlanetName, time: Time) -> PlanetName:
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        ...
    def PlanetLordOfConstellation(inputPlanet: PlanetName, time: Time) -> PlanetName:
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        ...
    def LordOfHouseList(houseList: Any, time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def AllHouseConstellationLord(time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: Dictionary`2
         """
        ...
    def HouseConstellationLord(houseNumber: HouseName, time: Time) -> PlanetName:
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        ...
    def HouseConstellation(houseNumber: HouseName, time: Time) -> Constellation:
        """
        NO DESC FOUND!! ERROR
        :return: Constellation
         """
        ...
    def AllHousePlanetsInHouseBasedOnSign(time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: Dictionary`2
         """
        ...
    def SignCountedFromInputSign(inputSign: ZodiacName, countToNextSign: Int32) -> ZodiacName:
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        ...
    def SignCountedFromPlanetSign(countToNextSign: Int32, startPlanet: PlanetName, inputTime: Time) -> ZodiacName:
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        ...
    def SignCountedFromLagnaSign(countToNextSign: Int32, inputTime: Time) -> ZodiacName:
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        ...
    def HouseCountedFromInputHouse(inputHouseNumber: Int32, countToNextHouse: Int32) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def IsPlanetInSign(planetName: PlanetName, signInput: ZodiacName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def SignsPlanetIsAspecting(planetName: PlanetName, time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def IsPlanetInMoolatrikona(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def PlanetRelationshipWithSign(planetName: PlanetName, zodiacSignName: ZodiacName, time: Time) -> PlanetToSignRelationship:
        """
        NO DESC FOUND!! ERROR
        :return: PlanetToSignRelationship
         """
        ...
    def PlanetCombinedRelationshipWithPlanet(mainPlanet: PlanetName, secondaryPlanet: PlanetName, time: Time) -> PlanetToPlanetRelationship:
        """
        NO DESC FOUND!! ERROR
        :return: PlanetToPlanetRelationship
         """
        ...
    def PlanetRelationshipWithHouse(house: HouseName, planet: PlanetName, time: Time) -> PlanetToSignRelationship:
        """
        NO DESC FOUND!! ERROR
        :return: PlanetToSignRelationship
         """
        ...
    def PlanetTemporaryRelationshipWithPlanet(mainPlanet: PlanetName, secondaryPlanet: PlanetName, time: Time) -> PlanetToPlanetRelationship:
        """
        NO DESC FOUND!! ERROR
        :return: PlanetToPlanetRelationship
         """
        ...
    def PlanetInSign(signName: ZodiacName, time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def PlanetTemporaryFriendList(planetName: PlanetName, time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def HouseLongitude(houseNumber: HouseName, time: Time) -> House:
        """
        NO DESC FOUND!! ERROR
        :return: House
         """
        ...
    def Panchaka(time: Time) -> PanchakaName:
        """
        NO DESC FOUND!! ERROR
        :return: PanchakaName
         """
        ...
    def LordOfWeekday(time: Time) -> PlanetName:
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        ...
    def LordOfWeekday(weekday: DayOfWeek) -> PlanetName:
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        ...
    def IshtaKaala(birthTime: Time) -> Angle:
        """
        NO DESC FOUND!! ERROR
        :return: Angle
         """
        ...
    def IsBeforeSunrise(birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def HoraAtBirth(time: Time) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def SunriseTime(time: Time) -> Time:
        """
        NO DESC FOUND!! ERROR
        :return: Time
         """
        ...
    def SunsetTime(time: Time) -> Time:
        """
        NO DESC FOUND!! ERROR
        :return: Time
         """
        ...
    def NoonTime(time: Time) -> DateTime:
        """
        NO DESC FOUND!! ERROR
        :return: DateTime
         """
        ...
    def IsPlanetInGoodAspectToPlanet(receivingAspect: PlanetName, transmitingAspect: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInGoodAspectToHouse(receivingAspect: HouseName, transmitingAspect: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def PlanetSthanaBalaNeutralPoint(planet: PlanetName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def IsPlanetInTrikona(planet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInKendra(planet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInUpachaya(planet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInKendra(planetList: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInKendraFromPlanet(kendraFrom: PlanetName, kendraTo: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def SignDistanceFromPlanetToPlanet(startPlanet: PlanetName, endPlanet: PlanetName, time: Time) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def IsHouseLordInHouseBasedOnLongitudes(lordHouse: HouseName, occupiedHouse: HouseName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsHouseLordInHouseBasedOnSign(lordHouse: HouseName, occupiedHouse: HouseName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetConjunctWithMaleficPlanets(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetConjunctWithEnemyPlanets(inputPlanet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetConjunctWithFriendPlanets(inputPlanet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsMaleficPlanetInHouse(houseNumber: HouseName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsBeneficPlanetInHouse(houseNumber: HouseName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsBeneficsInKendra(time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsAllMaleficsInUpachayas(time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsMaleficPlanetInSign(sign: ZodiacName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def MaleficPlanetListInSign(sign: ZodiacName, time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def IsBeneficPlanetInSign(sign: ZodiacName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def BeneficPlanetListInSign(sign: ZodiacName, time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def IsMaleficPlanetAspectHouse(house: HouseName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsBeneficPlanetAspectHouse(house: HouseName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetAspectedByMaleficPlanets(planetReceivingAspect: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def GetAllMaleficPlanetsAspecting(planetReceivingAspect: PlanetName, time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def IsPlanetAspectedByBeneficPlanets(lord: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetAspectedByEnemyPlanets(inputPlanet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetAspectedByFriendPlanets(inputPlanet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def ArudhaLagnaSign(time: Time) -> ZodiacName:
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        ...
    def CountFromSignToSign(startSign: ZodiacName, endSign: ZodiacName) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def CountFromConstellationToConstellation(start: Constellation, end: Constellation) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def IsPlanetInHouse(planet: PlanetName, houseNumber: HouseName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInHouseKP(cusps: Any, planetNirayanaDegrees: Angle, house: HouseName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsAllPlanetsInHouse(planetList: Any, houseNumber: HouseName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsAnyPlanetsInHouse(planetList: Any, houseNumber: HouseName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetDebilitated(planet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetExaltedDegree(planet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetExaltedSign(planet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsFullMoon(time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsNewMoon(time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsWaterSign(moonSign: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsFireSign(moonSign: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsEarthSign(moonSign: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsAirSign(moonSign: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetBeneficToLagna(planetName: PlanetName, birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetMaleficToLagna(planetName: PlanetName, birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetYogakarakaToLagna(planetName: PlanetName, birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetMarakaToLagna(planetName: PlanetName, birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInOwnHouse(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInOwnSign(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInFriendSign(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInEnemySign(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInEnemyHouse(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInFriendHouse(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def BirthVarna(birthTime: Time) -> Varna:
        """
        NO DESC FOUND!! ERROR
        :return: Varna
         """
        ...
    def AllPlanetsSignsFromPlanet(signsFromMoon: Int32, startPlanet: PlanetName, birthTime: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def AllPlanetsInASignFromLagna(signsFromLagna: Int32, birthTime: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def AllPlanetsSignsFromPlanet(signsFromList: Int32, startPlanet: PlanetName, birthTime: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def AllPlanetsSignsFromPlanet(signsFromList: Int32, birthTime: Time, startPlanet: PlanetName) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def AllPlanetsSignsFromPlanet(signsFromMoon: Int32, birthTime: Time, startPlanet: PlanetName) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def AllPlanetsInSignsFromLagna(signsFromList: Int32, birthTime: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def IsPlanetsInSignsFromPlanet(signsFromList: Int32, planetList: PlanetName, startPlanet: PlanetName, birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetsInSignsFromLagna(signsFromList: Int32, planetList: PlanetName, birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsBeneficsInSignsFromPlanet(signsFromList: Int32, startPlanet: PlanetName, birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsBeneficsInSignsFromLagna(signsFromList: Int32, birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def GetAllHouseNirayanaMiddleLongitudes(time: Time) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double[]
         """
        ...
    def AllHouseLongitudes(time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def PlanetsInConjunction(inputPlanet: PlanetName, time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def BirthNumber(birthTime: Time) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def DestinyNumber(birthTime: Time) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def NameNumber(inputText: String) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def NameNumberPrediction(fullName: String) -> NumerologyPrediction:
        """
        NO DESC FOUND!! ERROR
        :return: NumerologyPrediction
         """
        ...

