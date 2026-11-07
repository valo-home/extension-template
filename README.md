# Valo extension template

A template for writing an extension for [Valo](https://github.com/valo-home/valo), the local smart home hub
for Zigbee, MQTT and IP cameras. It contains a working example `my.home.hello`: a virtual counter device, a
flow trigger and a page, with tests that run without the hub.

Press **Use this template** on GitHub, then rename the package.

> Valo is in early development, before beta. The SDK is small, but names and fields can
> still change. Watch the [valo](https://github.com/valo-home/valo) repository for changes.

## What an extension can do

An extension is a small Python program. Valo runs it as a separate process with memory and CPU limits, it
talks to the core over MQTT and gets only the permissions listed in its manifest and granted by the owner.
An extension can

- add devices with their own state and commands, for example a cloud device, a meter or a virtual sensor
- add triggers, conditions and actions to the automation editor
- add pages to the menu and widgets to dashboards
- read devices and home state, send notifications, store its own settings
- act as a camera driver for a camera family

Installed extensions appear in Valo under Extensions, community ones are marked as such in the catalog.

![Extension catalog in Valo with official and community extensions](https://raw.githubusercontent.com/valo-home/valo/main/assets/screenshots/catalog.webp)

![A page added by the Open-Meteo weather extension](https://raw.githubusercontent.com/valo-home/valo/main/assets/screenshots/ext-weather.webp)

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
