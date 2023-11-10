# Jelloow

Repository for company and agency data collection and integration code

**NOTE**: You will need to install docker for this project to work. You can find the installation instructions [here](https://docs.docker.com/get-docker/).

## Requirements

- Python environment (see requirements.txt for required packages)
- Docker for MongoDB container or MongoDB installed locally or on a remote server

## Container and dev environment setup and configuration

Root directory is considered the same directory as this README.md file.

Create .env file in root directory with the following contents:

```text
# Linked in credentials
LINKEDIN_CLIENT_SECRET=''
LINKEDIN_CLIENT_ID=''
LINKEDIN_ACCESS_TOKEN=''

# Supabase (postgres) credentials
SUPABASE_URL=''
SUPABASE_KEY=''
SUPABASE_ACCESS_TOKEN=''
SUPABASE_PASSWORD=''

# MongoDB configuration
MONGO_INITDB_ROOT_USERNAME=mongo
MONGO_INITDB_ROOT_PASSWORD=
MONGO_HOST=mongo
MONGO_PORT=27017
MONGO_DB=jelloow
MONGO_VERSION=7.0.0
```

Utilize this command to activate the MongoDB container:

```bash
docker compose up -d
```

Ensure you are using a Python environment and install the requirements:

```bash
python -m venv venv

# linux / mac
source venv/bin/activate

# windows
venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

## Utilization

To run the scrapy spiders, use the following command:

```bash
scrapy crawl <spider_name>
```

For example:

```bash
scrapy crawl goodfirms
```

To view the data in the MongoDB container, use the web GUI interface by navigating to [http://localhost:8081](http://localhost:8081) in your browser.

Utilize pyreverse to generate UML diagrams

```bash
pyreverse ./src/company_scraper/company_scraper/ -d ./docs/pyreverse
```

Run tests with pytest

```bash
pytest
```

If there is issues on your environment you can try running pytest python with

```bash
python -m pytest
```

## Notes about proxies

For the spiders to work on websites that block robots, you will need to have a proxy list. A minimum of 10 proxies is recommended with > 100 being ideal. The proxies should be in the following format:

```text
<ip>:<port>
```
