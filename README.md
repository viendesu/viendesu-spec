# viendesu-spec

This is only a design file at the moment.

# Developing

## Using nix flakes

```shell
$ nix develop
$ uv venv && uv pip install -r pyproject.toml
$ # Run spec
$ .venv/bin/python main.py > spec.yml
```

## Without flakes

1. Install `uv` from your package manager
2. Run just like with flakes without `nix develop`, `nix develop` additionally setups developer environment
