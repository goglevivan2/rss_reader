FROM python:3
ADD rss_reader.py  logics.py cache.py convert.py version.py web.py requirements.txt /
RUN python3 -m venv env
CMD ['source', 'env/bin/activate']
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "rss_reader.py"]
