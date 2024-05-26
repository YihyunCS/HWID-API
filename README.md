# HWID-API
HWID lock your software for free


## Features

- Register HWIDs for specific software
- Verify registered HWIDs
- List all registered HWIDs

### Prerequisites

- Python 3.x
- `pip` (Python package installer)
- `requests` library for Python
- A Vercel account

- Deploy using the Vercel Dashboard:

Go to the Vercel dashboard.
Click on the "New Project" button.
Select the Git provider where your repository is hosted (e.g., GitHub).
Import the repository you just pushed.
Follow the prompts to configure and deploy your project.

### Usage

- To register an HWID, send a POST request to the /register endpoint:
- curl -X POST https://<your-vercel-project>.vercel.app/register -H "Content-Type: application/json" -d '{"hwid":"YOUR_HWID","softwareId":"YOUR_SOFTWARE_ID"}'

- To verify a registered HWID, send a POST request to the /verify endpoint:
- curl -X POST https://<your-vercel-project>.vercel.app/verify -H "Content-Type: application/json" -d '{"hwid":"YOUR_HWID","softwareId":"YOUR_SOFTWARE_ID"}'

- To list all registered HWIDs, send a GET request to the /list endpoint:
- curl -X GET https://<your-vercel-project>.vercel.app/list

If you have any issues, let me know and I will fix it!


