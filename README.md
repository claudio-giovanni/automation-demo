<div align="center" >
  <a href="#" ><img  height="350" src="https://preview.redd.it/butter-bot-is-one-of-my-favorite-small-moments-what-are-v0-jq6l5lqqhfxa1.jpg?width=640&crop=smart&auto=webp&s=35280773aa4ede82a6cc13a570d018ac799e39e2" alt="img"></a>
<u>
  <h2>Automation Demo</h2>
    <p>End-to-End Testing with Playwright and Pytest</p>
</u>
</div>

## Configuration

- Language: Python
- Testing Library: Pytest + Playwright
- Configure with e2e/.env file (commited for demo purposes)

## Getting Started

### Prerequisites

- Install [Python 3.9+](https://www.python.org/downloads/)
- Install [Docker Compose](https://docs.docker.com/compose/install/) (For running the WebApp)
- Run the WebApp locally or use the provided Docker Compose file to run it in a container  
  `cd app`  
  Depending on your installation method, you can use either *docker* or *docker-compose*  
  `docker compose up -d` or `docker-compose up`

### Install dependencies:

Recommended to use a virtual environment, but this is optional and outside the scope of this demo.  
`cd e2e`  
`pip install -r requirements.txt`  
`playwright install`

### Run tests

`pytest tests`

## Improvements / Next Steps

- Shortcuts taken with some of the selectors. Instead, we should add test-ids to the WebApp
- Implement parallel test execution for faster results.
- Decouple some of the test cases to make them more modular and reusable.
- Integrate with CI/CD pipeline for automated testing.
- Add reporting and logging for better test visibility.
- Add retry mechanism for any flaky tests. Monitor pipeline for any flaky tests.
