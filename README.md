# JulienC blog embed

This project features small snippets that can be embedded on my website.
To create them, I use [Streamlit](https://streamlit.io/).

## Usage

```bash
poetry install
poetry run streamlit run app.py
```

## FAQ

### Why not include the snippets directly on the website?

Sometimes it's easier to build the logic in Python, and then embed it on the website.

### Why a separate repository?

I want to keep my website repository as clean as possible. It doesn't sense to send Python code to the Vercel build server.

## License

[MIT](https://choosealicense.com/licenses/mit/)
