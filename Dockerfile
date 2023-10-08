FROM --platform=linux/amd64 python:3.10-slim
# I stick to 3.9 because upper versions result in errors when pip is building the requirements.txt file

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

LABEL org.opencontainers.image.source=https://github.com/julien040/blog-embed
LABEL org.opencontainers.image.description="A streamlit app to embed small snippets in my blog posts"
LABEL org.opencontainers.image.licenses=MIT

# Writing CMD ["streamlit run app.py"] will result in an error
# But not when the container was built once.
# I don't know why this is happening.
# I love Python and Docker
CMD ["streamlit", "run", "app.py"]

