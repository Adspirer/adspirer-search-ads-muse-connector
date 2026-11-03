"""Validate and bundle an explicit public-file allowlist; no network or submission."""
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FILES = ["README.md", "SECURITY.md", "submission/connector.json",
         "submission/FORM.md", "submission/REVIEWER.md", "submission/TOOLS.md",
         "assets/icon.svg"]


def validate():
    data = json.loads((ROOT / "submission/connector.json").read_text())
    assert data["format"] == "adspirer-submission-kit-v1"
    assert re.fullmatch(r"\d+\.\d+\.\d+", data["version"])
    assert data["endpoint"] == "https://mcp.adspirer.com/search-ads"
    classes = {"Read", "Write", "Sensitive write"}
    assert data["tools"] and all(t["class"] in classes for t in data["tools"])
    tools_md = (ROOT / "submission/TOOLS.md").read_text()
    assert all(f"`{t['name']}`" in tools_md for t in data["tools"]), "TOOLS.md out of sync"
    assert data["authentication"] == "OAuth with PKCE" and data["pkceMethod"] == "S256"
    for key in ["repository", "productWebsite", "documentation", "mcpDocumentation",
                "privacyPolicy", "termsOfService"]:
        assert data[key].startswith("https://"), key
    for key in ["name", "company", "description", "contactEmail", "supportEmail", "accessRequirements"]:
        assert isinstance(data[key], str) and data[key].strip(), key
    assert len(data["examplePrompts"]) >= 3
    assert all(isinstance(p, str) and len(p) > 50 for p in data["examplePrompts"])
    assert data["icon"] == "assets/icon.svg"
    for name in FILES:
        assert (ROOT / name).is_file(), name
    icon = ET.parse(ROOT / data["icon"]).getroot()
    assert icon.tag == "{http://www.w3.org/2000/svg}svg"
    assert icon.attrib.get("width") == "512" and icon.attrib.get("height") == "512"
    return data


def main():
    data = validate()
    print("Submission-kit checks passed (not live MCP or Muse verification).")
    if "--check" in sys.argv:
        return
    out = ROOT / "dist"
    out.mkdir(exist_ok=True)
    path = out / f"adspirer-search-ads-muse-connector-{data['version']}.zip"
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        for name in sorted(FILES):
            entry = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, (ROOT / name).read_bytes())
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    (out / "SHA256SUMS").write_text(f"{digest}  {path.name}\n")
    print(path)


if __name__ == "__main__":
    main()
