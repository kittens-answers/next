# next

```
dokku builder:set <front-app> build-dir front
dokku builder:set <api-app> build-dir api
dokku builder:set <tg-app> build-dir tg
dokku config:set --no-restart <tg-app> TG_TOKEN=<tg-token>
```