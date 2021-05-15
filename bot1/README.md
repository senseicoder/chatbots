# Déploiement en dev

* lancement container
```
docker run -ti debian:9 -v /home/cedric/www/c/chatbots:/chatbots  bash
```

* dans le container
```
pip3 install --upgrade httplib2 flask daemonize oauth2client google-api-python-client google-auth-oauthlib pyyaml
mkdir -p /space/etc/google_api
mv chatbot1.json /space/etc/google_api/
```

# Test manuel

```
curl -i -H 'Accept: application/json' -X POST -d '{"event":"CRITICAL","msg":"ceci est un test","classe":"perso"}' http://172.17.0.2:8001/simple
```