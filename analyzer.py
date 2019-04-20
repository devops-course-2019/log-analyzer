import sys
import pandas as pd

from flask import Flask

app = Flask(__name__)

log_data = None
access_data = None

def is_valid_system_log_data(data):
    # TODO
    return True

def is_valid_access_log_data(data):
    # TODO
    return True

def usage():
    print("Usage: python analyzer.py logarchive.csv access_archive.csv")

# Flask section
@app.route("/")
def home():
    return "<h1>Welcome to base url of loganalyzer</h1>"

@app.route("/errors")
def errors():
    error_df = log_data[log_data['Severity']=='ERROR']
    json = error_df.to_json(orient='records')
    return json

@app.route("/warnings")
def warnings():
    error_df = log_data[log_data['Severity']=='WARN']
    json = error_df.to_json(orient='records')
    return json

@app.route("/infos")
def infos():
    error_df = log_data[log_data['Severity']=='INFO']
    json = error_df.to_json(orient='records')
    return json

'''
LogAnalyzer:
Software that read aggregated log files at startup and    
'''
if __name__=='__main__':
    if len(sys.argv) != 3:
        print("Too few arguments!")
        usage()
        exit(0)
    log_file = sys.argv[1]        
    access_file = sys.argv[2]
    
    # Import log data
    try:
        log_data = pd.read_csv(log_file, sep=',', names = ["Source", "Logfile","Severity", "Date", "Message"])
        log_data.columns
    except Exception as e:
        print('Import of log data failed!')
        print(e)
        exit(0)
    if not is_valid_system_log_data(log_data):
        print('Invalid error log data')

    # Import access log data
    try:
        access_data = pd.read_csv(access_file, sep=',')
    except Exception as e:
        print('Import of access log data failed!')
        print(e)
        exit(0)
    if not is_valid_access_log_data(log_data):
        print('Invalid error log data')

    # Start server
    app.run()
