FROM python:3
ADD rss_reader.py logics.py	version.py web.py convert.py cache.py templates/index.html requirements.txt /
RUN python3 -m venv env
CMD ['source', '.']
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "rss_reader.py"]
