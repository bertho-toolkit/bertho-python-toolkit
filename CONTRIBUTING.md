
# Contributing to Bertho Toolkit 🚀

First of all, thank you for considering contributing to **bertho-toolkit**! 🎉  
We welcome all kinds of contributions: new features, bug fixes, improvements, documentation, etc.

---

## Getting Started 🛠️

### 1. Fork the repository

Click on the "Fork" button at the top right corner of the [repository page](https://github.com/bertho-toolkit/bertho-python-toolkit).

### 2. Clone your fork

```bash
git clone https://github.com/your-username/bertho-python-toolkit.git
cd bertho-python-toolkit
```

### 3. Set up a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate    # Windows
```

### 4. Install development dependencies

```bash
pip install -r requirements-dev.txt
```

---

## Making Changes ✏️

1. Create a new branch:

```bash
git checkout -b feature/your-feature-name
```

2. Make your changes.

3. Ensure your code follows PEP8 formatting:
   - You can use `black` and `isort`:

```bash
black src/
isort src/
```

4. If possible, write unit tests for any new features or bug fixes.

5. Commit your changes following Conventional Commits format:

```bash
git commit -m "feat: add a new utility for managing environment variables"
```

6. Push to your fork:

```bash
git push origin feature/your-feature-name
```

7. Open a Pull Request (PR) to `main` branch.

---

## Pull Request Guidelines 📋

- Describe what your PR does.
- Reference related issues if applicable.
- Keep the PR focused on a single feature or fix.

---

## Code of Conduct 📜

By participating, you are expected to uphold the [Code of Conduct](CODE_OF_CONDUCT.md).

Thank you again for helping make **bertho-toolkit** better! 🎉
