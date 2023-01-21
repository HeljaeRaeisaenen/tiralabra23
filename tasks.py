from invoke import task

@task
def run(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("cd src/ && pytest", pty=True)

@task
def coverage(ctx):
    ctx.run("export COVERAGE_RCFILE=../.coveragerc && cd src/ && coverage run --branch -m pytest && coverage html && firefox htmlcov/index.html", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src/", pty=True)

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")
