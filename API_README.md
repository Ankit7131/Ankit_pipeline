# GitHub Gists API
A simple web API that shows you someone's public GitHub Gists (code snippets).

## What it does
Give it a GitHub username, and it will show you all their public code snippets!

**Try it:** Visit `http://localhost:8080/octocat` to see GitHub user "octocat's" gists.

## Example
**Request:** `GET /octocat`
**Response:**
```json
[
  {
    "id": "abc123",
    "description": "My awesome script",
    "url": "https://gist.github.com/octocat/abc123"
  }
]
```

## How to run it
### Option 1: With Python (Easy)

```bash
# Install what you need
pip install -r requirements.txt

# Start the server
python app.py

# Test it works
curl http://localhost:8080/octocat
```

### Option 2: With Docker

```bash
# Build it
docker build -t github-gists-api .

# Run it
docker run -p 8080:8080 github-gists-api
```

## Testing
Make sure it works:

```bash
python -m pytest test_app.py -v
```

This tests that the API correctly gets gists for the "octocat" user.

## What's files included in this project

- `app.py` - The main web server
- `test_app.py` - Tests to make sure it works  
- `requirements.txt` - What Python packages you need
- `Dockerfile` - For running in Docker

## What can go wrong

- If you ask for a user that doesn't exist, you'll get a "User not found" error
- If GitHub's servers are having problems, you might get an "API error"

That's it! Simple web API that shows GitHub gists.