the front end is in a working state, with a defined game Mario-Kart for the N64.

to run the game, run the following command:

docker build -t <some-name> .
    # replace some-name with whatever you want
docker run -d --name frontend_test -p 80:80 <image-name>