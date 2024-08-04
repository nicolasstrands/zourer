# profanitionary-mu

This repository contains a comprehensive list of profanities for use in for e.g. content-filtering systems (or anything else really).

## Disclaimer (⚠️ Important! ⚠️)

This repository contains offensive language and profanities. If you are offended by such content, please do not continue to browse or use this repository.

## Usage

### Profanity List

The list of profanities can be found in the `data/profanity_list.json` file. Each entry includes variations, abbreviations, acronyms, and a definition.

### Adding New Profanities

To add a new profanity with its variations, abbreviations, acronyms, and definition, edit the `src/profanity_defs.json` file and create a pull request.

### Generating the Profanity List

The `data/profanity_list.json` file is automatically generated from the `src/profanity_defs.json` file using a GitHub Action. To manually trigger the generation, you can use the workflow dispatch feature in GitHub Actions.

### Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Add your profanities to `src/profanity_defs.json`.
4. Commit and push your changes.
5. Create a pull request.

Please ensure all entries include variations, abbreviations, acronyms, and a definition where applicable.
