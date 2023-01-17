# selenium_issue_11528

Goal: 
  Reproduce the docker network issue raised in my ticket: https://github.com/SeleniumHQ/selenium/issues/11528
  
The environment is made of:

./selenium_grid
./selenium_tests (2 python scripts: test_google.py and test_webA.py)
./webA (nodeJS Hello World App)
./webB (nodeJS Hello World App)


Networking:
  
    selenium-hub:
      networks:
        - selenium-network

    node-docker:
      networks:
      - selenium-network
      - networkA
      - networkB
      
    webA:
      networks:
      - networkA
    
    webB:
      networks:
      - networkB
      
test_google: OK
    docker-compose run --rm selenium-tests test_google
    
    output:
      Welcome to the Python selenium test executor
      Running test script: /app/test_google.py
      https://www.google.com/?gws_rd=ssl

test_webA: OK
    docker-compose run --rm selenium-tests test_webA
    
    Welcome to the Python selenium test executor
    Running test script: /app/test_webA.py
    Press Enter to continue...
    http://weba:3000/

    >>> Here we are lucky because the node inspect its networks, and takes the first in the list and create a selenium chrome container on the networkA
    so it is able to resolve 'webA'. The same as if you take the first network returned by the command:
    
     docker inspect --format='{{json .NetworkSettings.Networks}}' selenium_grid-node-docker-1 | jq
     
 test_webB: KO
    docker-compose run --rm selenium-tests test_webB
    
    This test is failing because the selenium container is not able to resolve webB since it is only visible from networkB.
