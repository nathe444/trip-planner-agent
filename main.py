import os
from crewai import Crew, Process

from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks

from dotenv import load_dotenv
load_dotenv()



class TripCrew:
    def __init__(self, origin , cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):
        agents = TravelAgents()
        tasks = TravelTasks()

        local_tour_guide = agents.local_tour_guide_expert()
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()

        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.date_range,
            self.interests
        )
        identify_city = tasks.identify_city(
            city_selection_expert, 
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.date_range, 
            self.interests
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("## Welcome to Trip planner Crew")
    print("-------------------------------")
    origin = input(dedent("""From where do you want to start your trip? """))
    cities = input(dedent("""What cities are you interested in visiting? """))
    date_range = input(dedent("""What is your travel date range? """))
    interests = input(dedent("""What are your travel interests and hobbies? """))

    trip_crew = TripCrew(origin, cities, date_range, interests)
    result = trip_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)