# Ploto

A distributed scheduling platform for plotting system in CEMC.

## Docker

### Build

Base image.

```
sudo docker build --rm --tag nwpc-oper/ploto:base -f docker/base/Dockerfile .
```

Consumer image.

```
sudo docker build --rm --tag nwpc-oper/ploto:consumer -f docker/consumer/Dockerfile .
```

Server image.

```
sudo docker build --rm --tag nwpc-oper/ploto-server -f docker/server/Dockerfile .
```
 
## LICENSE

Copyright 2017-2022, perillaroc at cemc-oper.

`ploto` is licensed under [Apache License, Version 2.0](./LICENSE).