import click
from cli import cli, url
import requests

url_local = url + "/binary"


@cli.group()
@click.pass_context
def binary(ctx):
    pass


@binary.command("get")
@click.pass_context
@click.argument("path", nargs=1, default="/")
def get(ctx, path):
    try:
        response = requests.get(url_local + "?path=" + path)
        if response.status_code == 404:
            print("Not found")
        elif response.status_code == 400:
            print("Wrong path")
        else:
            print(response.json())
    except requests.exceptions.RequestException as e:
        print(e.__dict__["doc"])


@binary.command("create")
@click.argument("name", nargs=1, default="/")
@click.argument("info", nargs=1, default="/")
@click.argument("path", nargs=1, default="/")
@click.pass_context
def create(ctx, name, info, path):
    try:
        response = requests.post(
            url_local, json={"name": name, "info": info, "path": path}
        )
        if response.status_code == 404:
            print("Not found")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(e.__dict__["doc"])


@binary.command("delete")
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


@binary.command("move")
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
