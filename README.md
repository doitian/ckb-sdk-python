# CKB SDK Python

This is my personal side project, which is not an official SDK. The project is
still in an early stage, the interfaces are unstable, and I may add breaking
changes without notifications.

## Quick Start

Install

```
pip install -U ckb
```

Example

```
from ckb.rpc import rpc
rpc.get_tip_block_number()
```

## Design Choices

This project does not add model classes, instead it uses the JSON response
dict directly. You can check the dict schema in `ckb/types.py`.

I want to experiment another way to build a CKB SDK. This project will not
support any features that require knowing how a lock or type script works. I'm
going to create various generator library to building transaction, such as
`ckb-sdk-python-secp256k1-generator`.
