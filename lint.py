#!/usr/bin/env python3
"""Lint tool for Strands puzzle codebase.

Validates:
- Files are in src/ layer directories only
- Imports respect forward dependency direction (types → config → repo → service → runtime → ui)
- providers and utils are only imported where allowed
- Files are under 300 lines
"""

import ast
import os
import sys
from pathlib import Path

# Layer chain - imports can only go forward in this list
LAYERS = ["types", "config", "repo", "service", "runtime", "ui"]
ALLOWED_PROVIDER_IMPORTS = {
    "types": [],
    "config": [],
    "repo": [],
    "service": [],
    "runtime": ["providers"],
    "ui": ["providers", "service"],
}
ALLOWED_UTILS_IMPORTS = {
    "types": [],
    "config": [],
    "repo": [],
    "service": ["utils"],
    "runtime": ["utils"],
    "ui": ["utils", "service"],
}

SRC_DIR = Path(__file__).parent / "src"
MAX_LINES = 300


def get_layer(filepath: Path) -> str | None:
    """Get the layer name for a file path, or None if not in a layer."""
    filepath = filepath.resolve()
    src_dir = SRC_DIR.resolve()
    try:
        rel_path = filepath.relative_to(src_dir)
    except ValueError:
        return None
    
    parts = rel_path.parts
    if len(parts) < 1:
        return None
    
    layer = parts[0]
    if layer in LAYERS:
        return layer
    if layer == "providers" and len(parts) > 1:
        return "providers"
    if layer == "utils" and len(parts) > 1:
        return "utils"
    return None


def check_layer_directory(filepath: Path) -> list[tuple[str, int, str]]:
    """Check that file is in a valid layer directory."""
    errors = []
    layer = get_layer(filepath)
    if layer is None:
        errors.append((
            str(filepath),
            1,
            f"File must be in src/<layer>/ directory. "
            f"Move to src/<layer>/{filepath.name}."
        ))
    return errors


def check_imports(filepath: Path, tree: ast.AST) -> list[tuple[str, int, str]]:
    """Check that imports respect the forward dependency direction."""
    errors = []
    current_layer = get_layer(filepath)
    
    if current_layer is None:
        return errors
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                error = _check_import_alias(alias.name, current_layer, filepath, node.lineno)
                if error:
                    errors.append(error)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                error = _check_import_alias(node.module, current_layer, filepath, node.lineno)
                if error:
                    errors.append(error)
    
    return errors


def _check_import_alias(module_name: str, current_layer: str, filepath: Path, lineno: int) -> tuple[str, int, str] | None:
    """Check a single import alias for validity."""
    parts = module_name.split(".")
    top_level = parts[0]
    
    # Check if importing from allowed providers/utils
    if top_level in ["providers", "utils"]:
        allowed_providers = ALLOWED_PROVIDER_IMPORTS.get(current_layer, [])
        allowed_utils = ALLOWED_UTILS_IMPORTS.get(current_layer, [])
        
        if top_level == "providers" and top_level not in allowed_providers:
            return (
                str(filepath),
                lineno,
                f"Cannot import 'providers' from {current_layer}. "
                f"providers is only allowed in: {', '.join(ALLOWED_PROVIDER_IMPORTS.keys()) if allowed_providers else 'none'}."
            )
        if top_level == "utils" and top_level not in allowed_utils:
            return (
                str(filepath),
                lineno,
                f"Cannot import 'utils' from {current_layer}. "
                f"utils is only allowed in: {', '.join(ALLOWED_UTILS_IMPORTS.keys()) if allowed_utils else 'none'}."
            )
        return None
    
    # Check if importing from a layer (types, config, repo, service, runtime, ui)
    if top_level in LAYERS:
        current_idx = LAYERS.index(current_layer)
        import_idx = LAYERS.index(top_level)
        
        if import_idx <= current_idx:
            return (
                str(filepath),
                lineno,
                f"Import violates forward dependency direction. "
                f"{current_layer} cannot import from {top_level} (only forward imports allowed)."
            )
    
    return None


def check_line_count(filepath: Path) -> list[tuple[str, int, str]]:
    """Check that file does not exceed MAX_LINES."""
    errors = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        if len(lines) > MAX_LINES:
            errors.append((
                str(filepath),
                len(lines),
                f"File has {len(lines)} lines, but maximum is {MAX_LINES}. "
                f"Reduce file size or refactor into smaller modules."
            ))
    except Exception:
        pass
    
    return errors


def process_python_file(filepath: Path) -> list[tuple[str, int, str]]:
    """Process a single Python file and return all violations."""
    errors = []
    
    errors.extend(check_layer_directory(filepath))
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source, filename=str(filepath))
    except SyntaxError as e:
        errors.append((
            str(filepath),
            getattr(e, "lineno", 1),
            f"Syntax error: {e.msg}. Fix the syntax error."
        ))
        return errors
    
    errors.extend(check_imports(filepath, tree))
    errors.extend(check_line_count(filepath))
    
    return errors


def find_python_files() -> list[Path]:
    """Find all Python files in the repository."""
    python_files = []
    
    # Look for .py files in src/ and at repo root
    for root, dirs, files in os.walk(Path(".")):
        # Skip hidden directories and common exclusions
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in {"__pycache__", "venv", ".venv"}]
        
        for file in files:
            if file.endswith(".py"):
                python_files.append(Path(root) / file)
    
    return python_files


def main() -> int:
    """Run the linter and return exit code."""
    all_errors = []
    python_files = find_python_files()
    
    for filepath in python_files:
        if filepath.is_relative_to(SRC_DIR) or str(filepath).startswith("src/"):
            errors = process_python_file(filepath)
            all_errors.extend(errors)
    
    if all_errors:
        print("Lint violations found:\n")
        for filepath, lineno, message in all_errors:
            print(f"{filepath}:{lineno}: {message}")
        print(f"\n{len(all_errors)} violation(s) found.")
        return 1
    
    print("No lint violations found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
