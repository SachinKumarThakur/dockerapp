# We are using python 3.6.4 like base image
FROM python:3.6.4

# I've install flask
RUN pip install Flask==1.0.2

# We add a new user admin and create a 
# home directory for this admin user and

RUN useradd -ms /bin/bash admin

# we are setting the default shell of this
# admin user to bash to runnig the app server
# under the admin user

# In general you sould always set the user 
# instruction in your docker file to run your
# process as a non-privileged user
# within the containers. Otherwise your 
# process will be running as a root within
# the container.

# It is concerned that if an attacker breaks 
# the container he would have root access in 
# the host machine, because the UIDs are the
# same. In theory a root user within a docker 
# or container cannot escalate to be root on 
# the host machine. But many people believe 
# that it's possible to do so as far as I 
# know It is certainly harder to do so with 
# docker containers because of the capacity 
# restrictions enforced by docker.
USER admin

# Sets the working directory for any run cmd 
# the entry point copy and add instructions
# Here we are using slash app as our working 
# directory
WORKDIR /app

# That we copy the app directory to the container.
COPY app /app

# Run our flask application.
# So here I can just use the relative path of 
# the app.py file.
CMD ["python", "app.py"] 
