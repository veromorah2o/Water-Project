Steps to run locally:

1. Set up a virtual environment and activate it:
```
python3 -m venv water-env
source water-env/bin/activate
```

2. Run the flask web app:
```
python -m flask run
```

Notes:
This repo contains three heroku apps:
- two for hosting the 1D and 2D graphs
- one for hosting the static webpages that contain those graphs in iframes
