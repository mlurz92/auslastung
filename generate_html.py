import json, pathlib
payload_path="/tmp/payload.json"
with open(payload_path, encoding='utf-8') as f:
    payload=json.load(f)
payload_str=json.dumps(payload, ensure_ascii=False)

html_template = open("/tmp/template.html", encoding="utf-8").read() if pathlib.Path("/tmp/template.html").exists() else None
if not html_template:
    print("template missing")
    raise SystemExit(1)

html_content = html_template.replace('__PAYLOAD__', payload_str)
out_path = "/home/user/auslastung/index.html"
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"Written {len(html_content)} chars to {out_path}")
