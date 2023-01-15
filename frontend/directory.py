import click
from cli import cli, url
import requests

url_local = url + "/directory"


@cli.group()
@click.pass_context
def directory(ctx):
    pass


@directory.command("get")
@click.pass_context
@click.argument("path", nargs=1, default="/")
def get(ctx, path):
    try:
        response = requests.get(url_local + "?path=" + path)
        if response.status_code == 404:
            print("Not found")
        elif response.status_code == 400:
            print(response.text)
        else:
            print(response.json())
    except requests.exceptions.RequestException as e:
        print(e.__dict__["doc"])


@directory.command("create")
@click.argument("name", nargs=1, default="/")
@click.argument("max_elems", nargs=1, default="/")
@click.argument("path", nargs=1, default="/")
@click.pass_context
def create(ctx, name, max_elems, path):
    try:
        response = requests.post(
            url_local, json={"name": name, "max_elems": max_elems, "path": path}
        )
        if response.status_code == 404:
            print("Not found")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(e.__dict__["doc"])


@directory.command("delete")
@click.argument("path", nargs=1, default="/")
@click.pass_context
def delete(ctx, path):
    try:
        response = requests.delete(url_local + "?path=" + path)
        if response.status_code == 404:
            print("Not found")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(e.__dict__["doc"])


@directory.command("move")
@click.argument("path", nargs=1, default="/")
@click.argument("new_path", nargs=1, default="/")
@click.pass_context
def move(ctx, path, new_path):
    try:
        response = requests.request(
            "UPDATE", url_local + "?path=" + path + "&new_path=" + new_path
        )
        if response.status_code == 404:
            print("Not found")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(e.__dict__["doc"])
