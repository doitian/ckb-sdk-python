# CKB SDK Python

This is my personal side project, which is not an official SDK. The project is
still in an early stage, the interfaces are unstable, and I may add breaking
changes without notifications.

The library works only with Python 3.

## Quick Start

Install in a virtualenv

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
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
