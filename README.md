# Jelloow

Repository for company and agency data collection and integration code

**NOTE**: You will need to install docker for this project to work. You can find the installation instructions [here](https://docs.docker.com/get-docker/).

## Container and dev environment setup

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

To run the scrapy spiders, use the following command:

```bash
scrapy crawl <spider_name>
```

For example:

```bash
scrapy crawl goodfirms
```

To view the data in the MongoDB container, use the web GUI interface by navigating to [http://localhost:8081](http://localhost:8081) in your browser.
