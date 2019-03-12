# Flask microservice start example

This is an simple project to start a flask microservices application.

It starts a httpserver and expose an endpoint.

To run the application you need to install the requirements and run the app:

<code>pip install -r requirements.txt

python app.py
</code>

If you want to run in a docker container:

<code>make image

make run
</code>

After run the app, you can test it by browsing:

<code>http://localhost:5000/api/Hello</code>