https://www.youtube.com/watch?v=KvrJaGqHz14&t=21s

MIT researchers introduced Recursive Language Models (RLMs), a new approach to handling massive datasets that far exceed the context window limits of current LLMs. Instead of feeding documents directly into a model, RLMs store the data in a Python environment and let the LLM explore it programmatically by writing code and spawning sub-LLM calls to process chunks. In testing, RLMs successfully handled inputs up to 10 million tokens — roughly 40x beyond GPT-5's 272K context window — while maintaining strong performance and comparable or lower costs. The paper demonstrates significant improvements over base models on tasks requiring dense information processing, with GPT-5 scoring near zero on complex cross-referencing tasks while RLM achieved 58%.

⏰TIMESTAMPS:
0:00 - Intro
1:00 - Study Results
5:15 - RLMs Explained
13:19 - Study Observations