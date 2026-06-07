# FetchMark - Setup Guide

FetchMark allows you to view Markdown files hosted on services like GitHub Pages.

## 1. Hosting your Markdown

Upload your `.md` files to a web server (e.g., a GitHub repository with Pages enabled).

## 2. Setting up index.json

The app requires an `index.json` file in the root of your web server to discover the files.

### JSON Format

```json
[
  "README.md",
  {
    "docs": [
      "setup.md",
      "guide.md"
    ]
  }
]
```

## 3. Automation

[GitHub](https://github.com/YoshitoSuzuki/FetchMark-template)
We provide a Python script to generate this JSON automatically.

1. Copy the `scripts/` folder to your repository.
2. Run `python3 scripts/generate_index.py`.

### GitHub Actions

Copy the `.github/workflows/generate-index.yml` file to your repository to automate the indexing every time you push.

## 4. Custom CSS

- **Local**: Place a `style.css` in any folder.
- **Global**: Provide a CSS URL in the app's repository settings.
