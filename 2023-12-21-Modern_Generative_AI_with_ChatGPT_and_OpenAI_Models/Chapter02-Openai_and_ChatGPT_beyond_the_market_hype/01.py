import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Moderation.create(input="I want to kill him")
print(response)

content_to_classify = "the driver was involved in a car accident with several explosions"

response = openai.Completion.create(
      model="content-filter-alpha",
      prompt="<|endoftext|>"+content_to_classify+"\n--\nLabel:",
      temperature=0,
      max_tokens=1,
      top_p=0,
      logprobs=10
    )
print(response.choices[0].text)
