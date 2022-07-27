# Ploto

A distributed scheduling platform for plotting system in NWPC.

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

Copyright 2017-2020, perillaroc at nwpc-oper.

`ploto` is licensed under [GPL-3.0](./LICENSE.md).