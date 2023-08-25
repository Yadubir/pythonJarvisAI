import os
import openai

from config import apikey

openai.api_key= apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a letter to my boss for resignation.",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

'''
{
  "id": "cmpl-7Ol7RkLvYgx1lXQAqxFTveQuqNXxI",
  "object": "text_completion",
  "created": 1686135353,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nDear [Boss Name],\n\nI am writing to inform you of my intention to resign from my current position at [company name]. I have truly loved my time here and appreciate all the experiences I have had over the past [time period]. \n\nI have decided it is time for me to move on and take the next step in my career. This decision was certainly difficult for me, but I am confident it is the correct choice.\n\nI am happy to provide assistance during my transition away from the company. Please let me know what I can do to ensure a smooth transition.\n \nThank you for the opportunity to work at [company name].\n\nSincerely,\n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 147,
    "total_tokens": 156
  }
}
'''