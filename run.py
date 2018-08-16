from flask import Flask
from app import *


# app.run()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)



