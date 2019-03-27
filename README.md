# Test for tails.com

This test app renders stores from a json file into a webpage and gets the latitude and longitude from postcodes.io

This repo has been formatted with black to follow PEP8 conventions. (It's to python what prettier for js is.)

## How to run it

First and foremost, please do clone the repo with
`git clone && cd test-tails.com`

Once you're in there, you should do the following:

`docker build -t test-tails.com . && docker run -p 38080:80 test-tails.com`

If that doesn't work for you, please use sudo (and later fix your docker installation).

Now you should be good to go. If still you can't start the app because it has some sort of error please do send me an email at ialbetsram@gmail.com with the error trace from your command line (pipe it into a file with `> file.txt`) and your system specs (if you're using linux/UNIX send me the output of `uname -v` and `cat /proc/version` and your docker version `docker -v`).

If you want to run it without docker, you should do the following (assuming you're already in the repo):

`pip install -r requirements.txt`

and then you can either run,
```
flask run
```
or if you change the env var FLASK_ENV to be production and then,   

```
pip install uwsgi && \
uwsgi --socket 0.0.0.0:8082 --protocol=http -w "main.main:app"
```

You should be good to go. You can either post via

`curl --header "Content-Type: application/json"   --request POST   --data '{"url":"https://www.w3.org/History/1989/proposal.html"}'   http://0.0.0.0:8082/shorten-url`

Or by going in your browser to http://0.0.0.0:8000 where you will have a UI to do that. Enjoy :)

## Design decisions

I have decided to use flask because of the simplicity of the task and the simplicity to set it up. It was the best tool for the job yet I would probably have been faster with Django because of the experience I have setting it up and could probably have added almost all of the things I wrote on the notes. (Yet -again- it wouldn't be the best tool for the job.)

Used a template I wrote for generating most the server configuration (so it might be a little bit outdated now) and that speed me up a tiny bit.

## Tests

The test suite is very small and is not being set up properly. I started by using unittest so I can use it as a test runner. Then I added pytest but since I have never set it up on a Flask project this slowed me down quite a lot and finally resorted to just use what

I also wanted to show both types of test and not just one.

To run the functional test on the root of the repository run. (You need to have requirements installed). You can do the same inside the repo. Also, you  need to have the latest Chrome drive installed - you can do so from [here](https://chromedriver.storage.googleapis.com/index.html?path=2.36/)
`python main/app/tests/functional_tests.py`

For the unit tests to run you need to do
`cd main && python -m unittest main.app.tests.unit_tests`


### Notes

I was going to add a map and to position the list on the side. A database, database schema and a dumper of the json into the database so we could load some fixtures like these easily. Also wanted to add a celery task which got the locations for the new postcodes and insert them once a day - as you can see I already had supervisord so it would be fairly simple to add just a task in there that executes once a day.

It took me bit longer than expected as I was unhappy with my submission. It had been a while since the last time I used Flask (*even though I'm a big fan*) and I had to do some more configuration to set up the app to be easily extended.

I would have added a way to only check for the postcodes if they change and to not allow for repetitions. It would also be nice to add a message to each row if the postcode is invalid.

Also as you can see for the extension of this I did quite some preparation before I went on with the test. I gathered all data, read all documentation, did a refresher on Flask and testing with it, and use my boilerplate code to get started. I took an extra hour to do it all, but if you have the best tools (and snippets) you can do so much more :)

I'm not that happy with the algorithm for the last task but that's another story.
