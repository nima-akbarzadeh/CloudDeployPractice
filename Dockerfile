FROM public.ecr.aws/lambda/python:3.8

RUN mkdire -p app
COPY ./main.py /app/
COPY library/ /app/library/
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt 
WORKDIR /app
EXPOSE 8080
CMD ["main.py"]
ENTRYPOINT ["python"]

