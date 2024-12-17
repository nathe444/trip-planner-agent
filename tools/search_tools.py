from langchain.tools import tool
import json, requests, os

class SearchTool():
    @tool("Search the internet")
    def search_internet(query):
        """
        Search the internet using Serper API and return top search results.

        Args:
            query (str): Search query to look up.

        Returns:
            list: Top search results containing title, link, and snippet.
        """
        top_results_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            "X-API-KEY": os.environ['SERPER_API_KEY'], 
            "content-type": 'application/json'
        }
        response = requests.request(
            "POST",
            url,
            headers=headers,
            data=payload
        )

        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that. There could be an error with your server."
        else:
            results = response.json()['organic']
            string = []
            for result in results[:top_results_to_return]:
                string.append("; ".join([
                    f"Title: {result['title']}", f"Link: {result['link']}", f"Snippet: {result['snippet']}"
                ]))
            return string
