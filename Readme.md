# 🏳️‍⚧ Gender Neutralisation 🏳️‍⚧

Simple FastAPI project to neutralise gendered langauge (pronouns etc.) within a 
provided text. Making use of OpenAI GPT-3.  
(If the Trans Pride Flags in the title are showing as 2 distinct symbols blame 
Microsoft :( for Window's weird emoji support)

## Examples
### Gendered:
Example paragraph from: http://www.uni-koeln.de/owc/descperson.htm
>"Mary is as beautiful as a Hollywood star. Her thick, wavy, long black hair gracefully falls down to her shoulders and encircles her diamond-shaped face. A golden suntan usually brings out her smooth, clear complexion and high cheek bones. Her slightly arched chestnut brown eyebrows highlight her emotions by moving up and down as she reacts to her world around her. Her large deep blue eyes, remind me of a lake on a stormy day. Her curved nose gives her a little girl look that makes me want to smile when she talks. And her mouth is a small mouth outlined by puffy lips that she often accentuates with glossy pink lipstick. When she smiles, which is often, her well formed and even, white teeth brighten up her whole face. I guess you can tell that I am head over heals in love with Mary."
### Gender Neutral:
>"Mary is as beautiful as a Hollywood star. Their thick, wavy, long black hair gracefully falls down to their shoulders and encircles their diamond-shaped face. A golden suntan usually brings out their smooth, clear complexion and high cheek bones. Their slightly arched chestnut brown eyebrows highlight their emotions by moving up and down as they react to their world around them. Their large deep blue eyes, remind me of a lake on a stormy day. Their curved nose gives them a youthful look that makes me want to smile when they talk. And their mouth is a small mouth outlined by puffy lips that they often accentuate with glossy pink lipstick. When they smile, which is often, their well formed and even, white teeth brighten up their whole face. I guess you can tell that I am head over heels in love with Mary."

### Needlesly Gendered Legal Stuff:
>"If the tenant wishes to terminate the lease early, he will be required to pay a fee equal to the greater of..."
### Gender Neutral Legal Stuff:
>"If the tenant wishes to terminate the lease early, they will be required to pay a fee equal to the greater of..."

## Usage - Local
- Install requirements to a python-3.8 environment: `pip3 install -r setup/requirements.txt`
- Configure environment variables - see .env file for the default values. The most important
value to set is `OPEN_AI_KEY` as this is used to gain access to the GPT-3 api.
- Launch API adding `src` to path : `PYTHONPATH="${PYTHONPATH}:src/" python3 src/main.py`

## Usage - Docker
- Set environment variables in .env file (these are passed in by docker-compose so no need to worry
about leaking your API key if you push the docker image somewhere)
- Run: `make build`
- Run: `make deploy`
- To bring down the API, run: `make down`

## Getting Your OpenAI API key
Curently this API only supports gender neutralisation making use of OpenAI's GPT API. As such,
you'll need to follow these steps to get the API key mentioned in the usage sections.
- Create an Account & Login to [OpenAI](https://openai.com/api/)
- Goto `account/api-keys`
- Select Create new Secret Key
- Copy the resulting Key

## Future Plans
- Wrap the API in some form SPA
- Rate limiting
- Provide alternative non GPT-3 methods to achieve the same objective cheaper and faster

## Contribution
Help is always appreciated, feel free to open issues, or better yet Branches and PR's ❤
