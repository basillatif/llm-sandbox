# Personalized Email Drafting Assistant

## Overview
This API generates draft emails tailored to individual customers using the OpenAI GPT API.

## Features
- JSON input for customer and goal details
- LLM-powered text generation
- REST API endpoint
- Docker deployment

## Example Request
POST /generate-email

{
  "customer_name": "Alex",
  "company": "Acme Corp",
  "recent_event": "completed a demo",
  "goal": "schedule a follow-up call"
}

## Example Response
{
  "email_text": "Hi Alex,..."
}

## Setup Instructions
...

## Architecture Diagram
...

## Deployment
...
