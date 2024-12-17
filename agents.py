# from crewai import Agent
# from textwrap import dedent
# from langchain_groq import ChatGroq

# class CustomAgents:
#     def __init__(self):
#         self.groq = ChatGroq()
        

#     def expert_travel_agent(self):
#         return Agent(
#             role="Expert travel agent",
#             backstory=dedent(f"""I am an expert travel agent.I am expert in travel planning
#                                  and logistics.I have decades of experience making travel iteneraries"""),
#             goal=dedent(f"""Create a 7 day itinerary with a detailed plan for each day,
#                             include budget,packaging suggestions and safety tips"""),
#             # tools=[tool_1, tool_2],
#             verbose=True,
#             llm=self.groq,
#         )

#     def city_selection_expert(self):
#         return Agent(
#             role="City selection expert",
#             backstory=dedent(f"""I am a city search expert.I have decades of experience"""),
#             goal=dedent(f"""Define agent 2 goal here"""),
#             # tools=[tool_1, tool_2],
#             verbose=True,
#             llm=self.OpenAIGPT35,
#         )