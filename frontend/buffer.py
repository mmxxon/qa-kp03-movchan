import click
import requests
from cli import cli, url

url_local = url + "/buffer"


@cli.group()
@click.pass_context
def buffer(ctx):
    pass


@buffer.command("get")
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


@buffer.command("create")
@click.argument("name", nargs=1, default="/")
@click.argument("max_size", nargs=1, default="/")
@click.argument("path", nargs=1, default="/")
@click.pass_context
def create(ctx, name, max_size, path):
    try:
        response = requests.post(
            url_local, json={"name": name, "max_size": max_size, "path": path}
        )
        if response.status_code == 404:
            print("Not found")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(e.__dict__["doc"])


@buffer.command("delete")
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


@buffer.command("move")
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


@buffer.command("push")
@click.argument("elem", nargs=1, default="/")
@click.argument("path", nargs=1, default="/")
@click.pass_context
def push(ctx, elem, path):
    try:
        response = requests.patch(
            url_local + "?path=" + path + "&action=push&element=" + elem
        )
        if response.status_code == 404:
            print("Not found")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(e.__dict__["doc"])


@buffer.command("pop")
@click.argument("path", nargs=1, default="/")
@click.pass_context
def pop(ctx, path):
    try:
        response = requests.patch(url_local + "?path=" + path + "&action=pop")
        if response.status_code == 404:
            print("Not found")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(e.__dict__["doc"])
