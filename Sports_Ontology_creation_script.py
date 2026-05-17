from owlready2 import *

onto = get_ontology("http://example.org/sports.owl")

# needed locally in order for owlready2 to work correctly 
owlready2.JAVA_EXE = "C:\\Program Files\\Java\\jdk-21\\bin\\java.exe"

with onto:
    # Main Concepts
    class Sport(Thing): pass
    class Place(Thing): pass
    class Equipment(Thing): pass
    class PhysicalActivity(Thing): pass
    class Person(Thing): pass
    class SportParticipant(Thing): pass


    # Concepts related to sports venues
    class OutdoorPlace(Place): pass
    class IndoorPlace(Place): pass

    class Stadium(OutdoorPlace): pass
    class Track(OutdoorPlace): pass
    class Beach(OutdoorPlace): pass
    class Pitch(OutdoorPlace): pass
    class GolfCourse(OutdoorPlace): pass

    class Arena(IndoorPlace): pass
    class SwimmingPool(IndoorPlace): pass
    class IceRink(IndoorPlace): pass
    class IndoorCourt(IndoorPlace): pass
    class SportsHall(IndoorPlace): pass


    # Concepts related to sports equipment
    class Ball(Equipment): pass
    class Racquet(Equipment): pass
    class Net(Equipment): pass
    class Board(Equipment): pass
    class MotorVehicle(Equipment): pass
    class Club(Equipment): pass


    # Concepts related to sports physical activity
    class LowPhysicalActivity(PhysicalActivity): pass
    class MediumPhysicalActivity(PhysicalActivity): pass
    class HighPhysicalActivity(PhysicalActivity): pass


    # Concepts related to athletes and teams
    class Athlete(Person, SportParticipant): pass
    class Team(SportParticipant): pass
    class TeamAthlete(Athlete): pass


    # Object Properties
    class PlayedAt(Sport >> Place): pass

    class PlayedWith(Sport >> Equipment): pass

    class PhysicalActivityLevel(Sport >> PhysicalActivity): pass

    class PlaysSport(SportParticipant >> Sport): pass

    class HasTeamMember(Team >> Athlete): pass
    
    class IsPartOfTeam(Athlete >> Team):
        Inverse(HasTeamMember)
    
    class HasTeammate(Athlete >> Athlete):
        symmetric = True

    # Data Properties
    class IsTeamSport(Sport >> bool): 
        functional = True

    class HasTeamSize(Sport >> int):
        functional = True

    class HasPhysicalContact(Sport >> bool):
        functional = True

    class FirstName(Person >> str):
        functional = True

    class LastName(Person >> str):
        functional = True

    class DateOfBirth(Person >> str):
        functional = True

    class PlaceOfBirth(Person >> str):
        functional = True

    class TeamName(Team >> str):
        functional = True
    
    class Country(Team >> str):
        functional = True


    # Sports according to whether they are individual or team sports
    class IndividualSport(Sport):
        equivalent_to = [
            IsTeamSport.value(False),
            HasTeamSize.exactly(1)
        ]

    class TeamSport(Sport):
        equivalent_to = [
            IsTeamSport.value(True),
            HasTeamSize.min(2)
        ]


    # Sports according to their venue 
    class OutdoorSport(Sport):
        equivalent_to = [
            PlayedAt.some(OutdoorPlace)
        ]

    class IndoorSport(Sport):
        equivalent_to = [
            PlayedAt.some(IndoorPlace)
        ]

    class StadiumSport(OutdoorSport):
        equivalent_to = [
            PlayedAt.some(Stadium)
        ]

    class TrackSport(OutdoorSport):
        equivalent_to = [
            PlayedAt.some(Track)
        ]

    class BeachSport(OutdoorSport):
        equivalent_to = [
            PlayedAt.some(Beach)
        ]

    class PitchSport(OutdoorSport):
        equivalent_to = [
            PlayedAt.some(Pitch)
        ]

    class GolfCourseSport(OutdoorSport):
        equivalent_to = [
            PlayedAt.some(GolfCourse)
        ]

    class ArenaSport(IndoorSport):
        equivalent_to = [
            PlayedAt.some(Arena)
        ]

    class SwimmingPoolSport(IndoorSport):
        equivalent_to = [
            PlayedAt.some(SwimmingPool)
        ]

    class IceRinkSport(IndoorSport):
        equivalent_to = [
            PlayedAt.some(IceRink)
        ]

    class IndoorCourtSport(IndoorSport):
        equivalent_to = [
            PlayedAt.some(IndoorCourt)
        ]

    class SportsHallSport(IndoorSport):
        equivalent_to = [
            PlayedAt.some(SportsHall)
        ]


    # Sports according to their equipment
    class BallSport(Sport):
        equivalent_to = [
            PlayedWith.some(Ball)
    ]

    class RacquetSport(Sport):
        equivalent_to = [
            PlayedWith.some(Racquet)
    ]

    class NetSport(Sport):
        equivalent_to = [
            PlayedWith.some(Net)
    ]

    class BoardSport(Sport):
        equivalent_to = [
            PlayedWith.some(Board)
    ]

    class MotorSport(Sport): 
        equivalent_to = [
            PlayedWith.some(MotorVehicle)
    ]

    class ClubSport(Sport): 
        equivalent_to = [
            PlayedWith.some(Club)
    ]


    # Sports according to their physical contact
    class ContactSport(Sport):
        equivalent_to = [
            HasPhysicalContact.value(True)
        ]

    class NonContactSport(Sport):
        equivalent_to = [
            HasPhysicalContact.value(False)
        ]


    # Sports according to their physical activity
    class LowPhysicalActivitySport(Sport):
        equivalent_to = [
            PhysicalActivityLevel.some(LowPhysicalActivity)
        ]

    class MediumPhysicalActivitySport(Sport):
        equivalent_to = [
            PhysicalActivityLevel.some(MediumPhysicalActivity)
        ]

    class HighPhysicalActivitySport(Sport):
        equivalent_to = [
            PhysicalActivityLevel.some(HighPhysicalActivity)
        ]


    Person.equivalent_to = [
        FirstName.exactly(1),
        LastName.exactly(1),
        DateOfBirth.exactly(1),
        PlaceOfBirth.exactly(1)
    ]

    SportParticipant.equivalent_to = [
        PlaysSport.some(Sport)
    ]

    Team.equivalent_to = [
            PlaysSport.exactly(1, Sport),
            TeamName.exactly(1),
            Country.exactly(1),
            HasTeamMember.min(2, Athlete)
        ]

    TeamAthlete.equivalent_to = [
        IsPartOfTeam.some(Team)
    ]


    # Individuals
    footballStadium = Stadium("FootballStadium")
    footballBall = Ball("FootballBall")
    footballNet = Net("FootballNet")
    footballHighPhysicalActivity = HighPhysicalActivity("Running")

    football = Sport("Football", 
                    IsTeamSport = [True], 
                    HasTeamSize = [11], 
                    PlayedAt = [footballStadium], 
                    PlayedWith = [footballBall, footballNet],
                    HasPhysicalContact = [True],
                    PhysicalActivityLevel = [footballHighPhysicalActivity])


    sprintTrack = Track("SprintTrack")
    sprintHighPhysicalActivity = HighPhysicalActivity("Running")

    sprint = Sport("Sprint", 
                IsTeamSport = [False],
                PlayedAt = [sprintTrack],
                HasPhysicalContact = [False],
                PhysicalActivityLevel = [sprintHighPhysicalActivity])


    golfCourseVenue = GolfCourse("GolfCourseVenue")
    golfBall = Ball("GolfBall")
    golfClub = Club("GolfClub")
    golfHighPhysicalActivity = LowPhysicalActivity("Walking")

    golf = Sport("Golf", 
                IsTeamSport = [False],
                PlayedAt = [golfCourseVenue],
                PlayedWith = [golfBall, golfClub],   
                HasPhysicalContact = [False],
                PhysicalActivityLevel = [golfHighPhysicalActivity])


    tableTennisSportsHall = SportsHall("TableTennisSportsHall")
    tableTennisRacquet = Racquet("TableTennisRacquet")
    tableTennisfBall = Ball("TableTennisfBall")
    tableTennisNet = Net("TableTennisNet")
    tableTennisHighPhysicalActivity = MediumPhysicalActivity("ActiveMovements")

    tableTennis = Sport("TableTennis", 
                IsTeamSport = [False],
                PlayedAt = [tableTennisSportsHall],
                PlayedWith = [tableTennisRacquet, tableTennisfBall, tableTennisNet],   
                HasPhysicalContact = [False],
                PhysicalActivityLevel = [tableTennisHighPhysicalActivity])


    surfingBeach = Beach("SurfingBeach")
    surfingBoard = Board("SurfingBoard")
    surfingHighPhysicalActivity = HighPhysicalActivity("DynamicStrenghtSwimming")

    surfing = Sport("Surfing", 
                IsTeamSport = [False],
                PlayedAt = [surfingBeach],
                PlayedWith = [surfingBoard],   
                HasPhysicalContact = [False],
                PhysicalActivityLevel = [surfingHighPhysicalActivity])


    volleyballSportsHall = SportsHall("VolleyballSportsHall")
    volleyballBall = Ball("VolleyballBall")
    volleyballNet = Net("VolleyballNet")
    volleyballHighPhysicalActivity = HighPhysicalActivity("JumpingRunning")

    volleyball = Sport("Volleyball", 
                    IsTeamSport = [True],
                    HasTeamSize = [6],
                    PlayedAt = [volleyballSportsHall], 
                    PlayedWith = [volleyballBall, volleyballNet],
                    HasPhysicalContact = [True],
                    PhysicalActivityLevel = [volleyballHighPhysicalActivity])


    kiril_despodov = Athlete("KirilDespodov",
                        FirstName = ["Kiril"],
                        LastName = ["Despodov"],
                        DateOfBirth = ["1996-11-11"],
                        PlaceOfBirth = ["Bulgaria"],
                        PlaysSport = [football])


    dimitar_mitov = Athlete("DimitarMitov",  
                        FirstName = ["Dimitar"],
                        LastName = ["Mitov"],
                        DateOfBirth = ["1997-01-22"],
                        PlaceOfBirth = ["Bulgaria"],
                        PlaysSport = [football],
                        HasTeammate = [kiril_despodov])


    dominik_kotarski = Athlete("DominikKotarski",  
                        FirstName = ["Dominik"],
                        LastName = ["Kotarski"],
                        DateOfBirth = ["2000-02-10"],
                        PlaceOfBirth = ["Croatia"],
                        PlaysSport = [football],
                        HasTeammate = [kiril_despodov])


    bulgaria_national_football_team = Team("BulgariaNationalFootballTeam", 
                                        PlaysSport = [football],
                                        TeamName = ["Bulgaria_National_Football_Team"],
                                        Country = ["Bulgaria"],
                                        HasTeamMember = [kiril_despodov, dimitar_mitov])


    paok_fc = Team("PaokFC", 
                PlaysSport = [football],
                TeamName = ["PAOK_FC"],
                Country = ["Greece"],
                HasTeamMember = [kiril_despodov, dominik_kotarski])


    kiril_despodov.IsPartOfTeam = [bulgaria_national_football_team, paok_fc]
    kiril_despodov.HasTeammate = [dimitar_mitov]
    kiril_despodov.HasTeammate = [dominik_kotarski]

    dimitar_mitov.IsPartOfTeam = [bulgaria_national_football_team]

    dominik_kotarski.IsPartOfTeam = [paok_fc]


    ivet_lalova = Athlete("IvetLalova", 
                    FirstName = ["Ivet"],
                    LastName = ["Lalova"],
                    DateOfBirth = ["1984-05-18"],
                    PlaceOfBirth = ["Bulgaria"],
                    PlaysSport = [sprint])


    aleks_grozdanov = Athlete("AleksGrozdanov",
                        FirstName = ["Aleks"],
                        LastName = ["Grozdanov"],
                        DateOfBirth = ["1998-03-28"],
                        PlaceOfBirth = ["Bulgaria"],
                        PlaysSport = [volleyball])


    matey_kaziyski = Athlete("MateyKaziyski",
                        FirstName = ["Matey"],
                        LastName = ["Kaziyski"],
                        DateOfBirth = ["1984-09-23"],
                        PlaceOfBirth = ["Bulgaria"],
                        PlaysSport = [volleyball])


    bulgaria_national_volleyball_team = Team("BulgariaNationalVolleyballTeam", 
                                        PlaysSport = [volleyball],
                                        TeamName = ["Bulgaria_National_Volleyball_Team"],
                                        Country = ["Bulgaria"],
                                        HasTeamMember = [aleks_grozdanov, matey_kaziyski])


    aleks_grozdanov.IsPartOfTeam = [bulgaria_national_volleyball_team]

    matey_kaziyski.IsPartOfTeam = [bulgaria_national_volleyball_team]


with onto:
    sync_reasoner(debug=3)
print('\n')

onto.save(file="Sports_Ontology_8MI3400591.owl", format="rdfxml")
print("Ontology is succcessfully saved as 'Sports_Ontology_8MI3400591.owl' \n")

print(f"The following classes are inconsistent in the ontology: {list(onto.inconsistent_classes())} \n")

print(f"footballBall IS-A: {footballBall.is_a} \n")
print(f"tableTennisSportsHall IS-A: {tableTennisSportsHall.is_a} \n")

print(f"football IS-A: {football.is_a} \n")
print(f"sprint IS-A: {sprint.is_a} \n")
print(f"golf IS-A: {golf.is_a} \n")
print(f"tableTennis IS-A: {tableTennis.is_a} \n")
print(f"surfing IS-A: {surfing.is_a} \n")
print(f"volleyball IS-A: {volleyball.is_a} \n")
print(f"kiril_despodov IS-A: {kiril_despodov.is_a} \n")
print(f"dimitar_mitov IS-A: {dimitar_mitov.is_a} \n")
print(f"ivet_lalova IS-A: {ivet_lalova.is_a} \n")
print(f"aleks_grozdanov IS-A: {aleks_grozdanov.is_a} \n")
print(f"matey_kaziyski IS-A: {matey_kaziyski.is_a} \n")
print(f"bulgaria_national_football_team IS-A: {bulgaria_national_football_team.is_a} \n")
print(f"paok_fc IS-A: {paok_fc.is_a} \n")
print(f"bulgaria_national_volleyball_team IS-A: {bulgaria_national_volleyball_team.is_a} \n")


# Examples related to Logical Reasoning
print(f"Parents of SwimmingPoolSport are: {onto.get_parents_of(SwimmingPoolSport)} \n")
print(f"Children of IndoorSport are: {onto.get_children_of(IndoorSport)} \n")


print(f"Parents of Athlete are: {onto.get_parents_of(Athlete)} \n")
print(f"Children of SportParticipant are: {onto.get_children_of(SportParticipant)} \n")


# Classification example
with onto:
    class DivingSwimmingPool(SwimmingPool): pass

    class DivingSwimmingPoolSport(SwimmingPoolSport):
        equivalent_to = [
            PlayedAt.some(DivingSwimmingPool)
        ]

print(f"Parents of DivingSwimmingPoolSport are: {onto.get_parents_of(DivingSwimmingPoolSport)} \n")
print(f"Children of SwimmingPoolSport are: {onto.get_children_of(SwimmingPoolSport)} \n")


# Queries example
query_all_ball_sports = """
    PREFIX : <http://example.org/sports.owl#>
    SELECT ?sport
    WHERE {
        ?sport rdf:type :BallSport .
    }
"""
print(f"Sports that are played with ball: {list(onto.world.sparql(query_all_ball_sports))} \n")


query_all_ball_net_stadium_sports = """
    PREFIX : <http://example.org/sports.owl#>
    SELECT ?sport
    WHERE {
        ?sport rdf:type :BallSport .
        ?sport rdf:type :NetSport .
        ?sport rdf:type :StadiumSport .
    }
"""
print(f"Sports that are played with ball and net on stadium: {list(onto.world.sparql(query_all_ball_net_stadium_sports))} \n")

query_all_volleyball_players = """
    PREFIX : <http://example.org/sports.owl#>
    SELECT ?athlete
    WHERE {
        ?athlete rdf:type :Athlete .
        ?athlete :PlaysSport :Volleyball .
    }
"""
print(f"All athletes that play volleyball: {list(onto.world.sparql(query_all_volleyball_players))} \n")

