import click
from cli import cli, url
import requests

url_local = url + "/log_text_file"


@cli.group()
@click.pass_context
def log(ctx):
    pass


@log.command("get")
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


@log.command("create")
@click.argument("name", nargs=1, default="/")
@click.argument("path", nargs=1, default="/")
@click.pass_context
def create(ctx, name, path):
    try:
        response = requests.post(url_local, json={"name": name, "path": path})
        if response.status_code == 404:
            print("Not found")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(e.__dict__["doc"])


@log.command("delete")
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


@log.command("move")
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


@log.command("append")
@click.argument("path", nargs=1, default="/")
@click.argument("info", nargs=1, default="/")
@click.pass_context
def pop(ctx, path, info):
    try:
        response = requests.patch(url_local + "?path=" + path + "&info" + info)
        if response.status_code == 404:
            print("Not found")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(e.__dict__["doc"])
