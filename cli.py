# cli.py
import asyncio
import typer
from services import Greeter, SimpleGreeter

app_cli = typer.Typer(help="Greeter CLI powered by Typer")


def get_greeter() -> Greeter:
    # 필요 시 환경변수/설정에 따라 다른 구현으로 스위칭 가능
    return SimpleGreeter()


@app_cli.command()
def hello(name: str = "World"):
    """
    동일한 서비스 레이어(SimpleGreeter)를 사용해 CLI에서 인사 메시지를 출력합니다.
    """
    greeter = get_greeter()
    msg = asyncio.run(greeter.greet(name))
    typer.echo(msg)


if __name__ == "__main__":
    app_cli()
