# Profanitionary

This repository contains a comprehensive list of profanities for use in for e.g. content-filtering systems (or anything else really).

## Disclaimer (⚠️ Important! ⚠️)

This repository contains offensive language and profanities. If you are offended by such content, please do not continue to browse or use this repository.

## Usage

### Profanity List

The list of profanities can be found in the `data/list.json` file. The list is an array of strings containing the profanities. If you need more information about each profanity, you can refer to the `src/definitions.json` file or straight up use the latter file.

### Adding New Profanities

To add a new profanity with its variations, abbreviations, acronyms, and definition, edit the `src/definitions.json` file and create a pull request.

### Generating the Profanity List

The `data/list.json` file is automatically generated from the `src/definitions.json` file using a GitHub Action. To manually trigger the generation, you can use the workflow dispatch feature in GitHub Actions.

### Rules (⚠️ Important! ⚠️)

- Submissions containing personal names are strictly prohibited.
- Pull requests from newly created GitHub accounts that appear to be for the purpose of trolling will be closed.

### Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Add your profanities to `src/definitions.json`.
4. Commit and push your changes.
5. Create a pull request.

Please ensure all entries include variations, abbreviations, acronyms, and a definition where applicable.
