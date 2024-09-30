from tomli import load as load_toml

CONFIG: dict = dict()

with open('./static/config.toml', 'rb') as file:
    CONFIG = load_toml(file)
