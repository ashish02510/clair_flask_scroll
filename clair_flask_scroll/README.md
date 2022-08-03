# clair_flask_scroll
Created it for educational purposes only.
Simple flask application integrated a scrollable cotent through Stylesheet Css.
  Below are the steps required to get this working on a base linux system.
  
  - Install all required dependencies
    - apt-get install -y python python-setuptools python-dev build-essential python-pip python-mysqldb
  - Install and Configure Web Server
    - pip install flask
    - pip install flask-mysql
  - Start Web Server
     -FLASK_APP=app.py flask run 
  - go to 
    - http://127.0.0.1:5000                   > scrollable content
    - http://127.0.0.1:5000/next              > This could be the next page!!
