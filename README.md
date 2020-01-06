# Ploto

A distributed scheduling platform for plotting system in NWPC.

## Docker

### Build

earth base. This build may take a lot of time. It should be run only one time.

```
sudo docker build --rm --tag nwpc-oper/ploto-earth:base -f docker/earth/base/Dockerfile .
```

earth consumer:

```
sudo docker build --rm --tag nwpc-oper/ploto-earth:consumer -f docker/earth/consumer/Dockerfile .
```

server:

```
sudo docker build --rm --tag nwpc-oper/ploto-server -f docker/server/Dockerfile .
```

## LICENSE

Copyright 2017-2020, perillaroc at nwpc-oper.

`ploto` is licensed under [GPL-3.0](./LICENSE.md).

Components named `esmdiag` are based on [dongli/esmdiag](https://github.com/dongli/esmdiag).