# 🏳️‍⚧ Gender Neutralisation 🏳️‍⚧

Simple FastAPI project to neutralise gendered langauge within a provided text.
Making use of OpenAI GPT-3. (If the Trans Pride Flags in the title are showing
as 2 distinct symbols blame Microsoft :( for Window's weird emoji support)

## Usage - Local
- Install requirements to a python-3.8 environment: `pip3 install -r setup/requirements.txt`
- Configure environment variables - see .env file for the default values. The most important
value to set is `OPEN_AI_KEY` as this is used to gain access to the GPT-3 api.
- Launch API adding `src` to path : `PYTHONPATH="${PYTHONPATH}:src/" python3 src/main.py`

## Usage - Docker
**Coming Soon**

## Future Plans
- Finish docker deployment - Env Variables
- Write tests
- Caching with Redis using has of input text
- Rate limiting
- Provide alternative non GPT-3 methods to achieve the same objective cheaper and faster
- Wrap the API in some form SPA

## Contribution
Help is always appreciated, feel free to open issues, or better yet Branches and PR's
