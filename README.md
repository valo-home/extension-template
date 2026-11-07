# Valo extension template

A starting point for a [Valo](https://github.com/valo-home/valo) extension. It contains a working example
`my.home.hello`: a virtual counter device, a flow trigger and a page.

Press **Use this template** on GitHub, then rename the package.

## Layout

```
my.home.hello/
  manifest.json      id, version, permissions, settings, blocks, pages
  hello.py           the module, built on valo_sdk
  hellologic.py      logic without the broker, covered by tests
  docs/en.md         description shown in Valo, also uk.md and ru.md
tests/               pytest for the logic and the manifest
```

## Rename

1. Pick an id in reverse domain form, for a GitHub account `io.github.<you>.<name>`
2. Rename the folder, set `id`, `module`, `author`, `name` and `description` in `manifest.json`
3. Rename `hello.py` to the new `module` name

## Run it in Valo

1. Clone the hub: `git clone https://github.com/valo-home/valo.git`
2. Copy the package folder into `valo/extensions/packages/`
3. Add `{"source": "packages/<your id>"}` to `valo/extensions/catalog.json`
4. Start the demo: `./valo demo up`, open http://localhost:3000, login `mikko` / `valo-demo`
5. Extensions, find your extension, Install. Its log is in the extension card

Set `"trust": "local"` while developing: the extension then runs from the package folder and restarts when
`.py` and `.json` files change.

The full developer guide (manifest fields, permissions, SDK calls, camera drivers, pages and widgets) is
in Valo, Documentation, For developers, Extension development.

## Checks

```
uv run --group dev ruff check .
uv run --group dev pytest -q
```

## Publish

Open a pull request to [valo-home/valo](https://github.com/valo-home/valo) that adds your package to
`extensions/packages` and the catalog. Keep descriptions in English, Ukrainian and Russian, and raise
`version` with every change.

## License

Apache License 2.0. Your extension can use any license compatible with it.
