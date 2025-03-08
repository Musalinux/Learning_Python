"""
Monitor jenkins job, alert if it fails

We use jenkinsapi library to interact with jenkins
smtplib module to send email alerts
"""

from jenkinsapi.jenkins import Jenkins
import smtplib

def get_job_status(jenkins_url, job_name):
    jenkins = Jenkins(jenkins_url) # connect to jenkins server
    job = jenkins.get_job(job_name) # get jenkins job by name
    last_build = job.get_last_build() # get details of last build
    return last_build.get_status() # returns status of last build
    
def send_alert (job_name, status):
    message = f"Subject: Jenkins Job Alert. \n\n Job {job_name} has status {status}"
    with smtplib.SMTP('smtp.example.com') as server:
        server.login("email@example.com", "password")
        server.sendmail("email@example.com", "alert_recipient@example.com")
         
jenkins_url = 'http://jenkins.example.com'
job_name = 'my-job'
status = get_job_status(jenkins_url, job_name)

if status is 'SUCCESS':
    send_alert(job_name, status)