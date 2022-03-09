# SailDB
The succesor to ReflectDB. Sail (Space and Integer Interaction Language) is a custom made language than uses seperate spaces as a type of directory system. The code to SailDB is fully open-source and light weight.
## Performance
All tests were run on a 2017 MacBook Pro with 256gb of Flash Storage
| Database          | Benchmark Score |
|-------------------|-----------------|
| SAIL (Python)     | 250000/s        |
| Reflect           | 9975/s          |
| JSON              | 400000/s        |
| JSON Indented (2) | 142857/s        |    


NOTE: JSON is a builtin library that probably is running C instead of just Python
