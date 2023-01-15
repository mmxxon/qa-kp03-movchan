import binary
import buffer
import log
import directory
import os
import requests
from cli import cli, url

if __name__ == "__main__":
    res = requests.get(url + "/directory?path=/")
    if not res.status_code == 200:
        raise RuntimeError("Server down")
    else:
        cli()
