# ✈️ TripPilot AI (MVP)

An AI-powered travel planning assistant that creates personalized travel itineraries through a natural conversation.

> **Status:** 🚧 MVP (Work in Progress)

---

## Overview

TripPilot AI is a conversational travel assistant built with Python and Streamlit. Instead of filling in forms, users simply chat with the assistant about their travel plans. The application gathers the necessary information, remembers the conversation, and automatically generates a personalized travel itinerary.

The project has been designed with a modular architecture, allowing support for multiple AI providers and future integrations such as weather, maps, and web search.


---
## Deployed on Streamlit Cloud:

https://trippilotai.streamlit.app


---

## Current MVP Features

* 💬 Conversational travel planning
* 🧠 Conversation memory
* ✈️ Automatic itinerary generation
* 📅 Day-by-day travel schedule
* 💰 Estimated travel budget
* 💡 Travel tips
* 📄 Markdown itinerary export
* ⚙️ Modular AI provider architecture

---

## Planned Features (Version 1.1)

* Google Gemini support
* Mistral AI support
* Weather forecasts
* OpenStreetMap integration
* Web search for attractions and local recommendations
* PDF itinerary export
* Streaming AI responses
* Improved error handling and logging

---

## Project Structure

```text
trip-pilot-ai/

├── app.py
├── config.py
├── prompts.py
├── requirements.txt
│
├── ai/
│   ├── base.py
│   ├── factory.py
│   └── openai_provider.py
│
├── conversation/
│   ├── manager.py
│   └── message.py
│
├── core/
│   └── enums.py
│
├── models/
│
├── planner/
│
├── utils/
│
└── assets/
```

---

## Technology Stack

* Python 3.12+
* Streamlit
* OpenAI Responses API
* Pydantic
* python-dotenv

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/trippilot-ai.git

cd trippilot-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
OPENAI_API_KEY=your_openai_api_key
```

Run the application:

```bash
streamlit run app.py
```

---

## Streamlit Cloud Deployment

Store your API key in **Secrets**:

```text
OPENAI_API_KEY = your_api_key
```

No `.env` file is required when deploying to Streamlit Community Cloud.

---

## Example Conversation

**User**

> I would like to visit Japan.

**TripPilot AI**

> Great choice! How many days are you planning to stay?

**User**

> 10 days.

**TripPilot AI**

> What kinds of activities are you interested in?

**User**

> Food, temples and hiking.

**TripPilot AI**

> What's your approximate budget?

**User**

> Around €2,000.

🎉 TripPilot AI automatically generates a complete travel itinerary.

---

## Architecture

```text
Streamlit
      │
      ▼
Conversation Manager
      │
      ▼
AI Provider
(OpenAI)
      │
      ▼
Trip State
      │
      ▼
Trip Model
      │
      ▼
Markdown Export
```

The architecture has been designed to support multiple AI providers without changing the application logic.

<br>

---

## Memory Management

The application maintains two complementary forms of memory: a conversation history that preserves context for the LLM, and a structured TripState that extracts only the information needed to plan the trip. This keeps prompts context-aware while giving the application reliable, structured data to drive itinerary generation.

<br>

---

## Current Status

| Component             | Status |
| --------------------- | ------ |
| Streamlit UI          | ✅      |
| Conversation Memory   | ✅      |
| OpenAI Integration    | ✅      |
| Trip State Management | ✅      |
| Itinerary Generation  | ✅      |
| Markdown Export       | ✅      |
| Gemini Provider       | 🚧     |
| Mistral Provider      | 🚧     |
| Weather Service       | 🚧     |
| OpenStreetMap         | 🚧     |
| Web Search            | 🚧     |

---

## Roadmap

### Version 1.0 (MVP)

* Stable OpenAI integration
* Conversational travel planning
* Automatic itinerary generation
* Markdown export
* Streamlit deployment

### Version 1.1

* Gemini integration
* Mistral integration
* Weather information
* OpenStreetMap integration
* Web search
* Better logging
* Retry mechanisms
* Improved structured output handling

---

## License

This project is intended for educational and portfolio purposes.

---

## Author

Developed as part of an AI Engineering portfolio project.

Future releases will continue expanding TripPilot AI into a multi-provider travel planning platform powered by modern LLMs.
