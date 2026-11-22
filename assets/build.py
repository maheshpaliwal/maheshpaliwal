#!/usr/bin/env python3
"""Generates the SVGs used by the profile README. Run: python3 assets/build.py"""
from pathlib import Path

OUT = Path(__file__).parent
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "dark": dict(bg="#0a0f1a", bg2="#0e1626", border="#1e293b", ink="#f1f5f9", muted="#94a3b8",
                 faint="#334155", accent="#5eead4", accent2="#60a5fa", dot="#1e293b", glow=0.22),
    "light": dict(bg="#ffffff", bg2="#f6f8fa", border="#d0d7de", ink="#0f172a", muted="#57606a",
                  faint="#c4ccd6", accent="#0f766e", accent2="#2563eb", dot="#dde3ea", glow=0.12),
}

# ---- content -----------------------------------------------------------------
NAME = "Mahesh Paliwal"
ROLE = "SDE-3 at Zomato · 6+ years building scalable systems"
STATUS = "currently building golb · tsession"
CHIPS = ["Go", "Node.js", "WebRTC", "Rust"]
CARDS = {
    "golb": ("golb", ["A load balancer in a single static binary:", "HTTP reverse proxy and TCP proxy, one YAML file."], "Go", "#00ADD8"),
    "tsession": ("agentic-test-session", ["Session-scoped tracing and data-mutation", "capture for test environments."], "Go", "#00ADD8"),
}
SKILLS = [
    ("languages", ["Go", "Node.js", "Python", "Rust"]),
    ("data", ["DynamoDB", "MySQL", "PostgreSQL", "Redis"]),
    ("infra", ["Kafka", "AWS", "WebRTC"]),
    ("craft", ["System design", "Problem solving"]),
]
# ------------------------------------------------------------------------------


def hero(t):
    chips, x = [], 56
    for c in CHIPS:
        w = round(len(c) * 9.2 + 30)
        chips.append(
            f'<rect x="{x}" y="232" width="{w}" height="32" rx="16" fill="{t["bg2"]}" stroke="{t["border"]}"/>'
            f'<text x="{x + w / 2}" y="253" text-anchor="middle" class="mono" font-size="15" fill="{t["muted"]}">{c}</text>'
        )
        x += w + 10

    lb = (760, 160)
    backends = [(888, 76), (888, 160), (888, 244)]
    paths = [f"M{lb[0]},{lb[1]} C{lb[0] + 70},{lb[1]} {bx - 80},{by} {bx - 16},{by}" for bx, by in backends]
    wires = "".join(f'<path d="{p}" fill="none" stroke="{t["faint"]}" stroke-width="1.5"/>' for p in paths)
    packets = "".join(
        f'<circle r="3.5" fill="{t["accent"]}" class="pkt"><animateMotion dur="{d}s" begin="{b}s" repeatCount="indefinite" path="{p}"/></circle>'
        for p, d, b in zip(paths, (2.4, 2.0, 2.8), (0, 0.7, 1.3))
    )
    nodes = "".join(
        f'<rect x="{bx - 16}" y="{by - 16}" width="32" height="32" rx="9" fill="{t["bg2"]}" stroke="{t["border"]}" stroke-width="1.5"/>'
        f'<circle cx="{bx}" cy="{by}" r="3.5" fill="{t["accent"]}" class="pulse" style="animation-delay:{i * .5}s"/>'
        for i, (bx, by) in enumerate(backends)
    )
    inbound = f"M650,160 L{lb[0] - 26},160"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 320" role="img" aria-label="{NAME} — {ROLE}">
<title>{NAME} — {ROLE}</title>
<defs>
  <clipPath id="clip"><rect width="960" height="320" rx="20"/></clipPath>
  <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.2" fill="{t["dot"]}"/></pattern>
  <linearGradient id="fade" x1="0" x2="1"><stop offset=".35" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/></linearGradient>
  <mask id="m"><rect width="960" height="320" fill="url(#fade)"/></mask>
  <radialGradient id="g1"><stop offset="0" stop-color="{t["accent"]}" stop-opacity="{t["glow"]}"/><stop offset="1" stop-color="{t["accent"]}" stop-opacity="0"/></radialGradient>
  <radialGradient id="g2"><stop offset="0" stop-color="{t["accent2"]}" stop-opacity="{t["glow"]}"/><stop offset="1" stop-color="{t["accent2"]}" stop-opacity="0"/></radialGradient>
</defs>
<style>
  .sans{{font-family:{SANS}}} .mono{{font-family:{MONO}}}
  .pulse{{animation:pulse 2.4s ease-in-out infinite}}
  .drift{{animation:drift 14s ease-in-out infinite alternate}}
  @keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.35}}}}
  @keyframes drift{{to{{transform:translate(-50px,24px)}}}}
  @media (prefers-reduced-motion:reduce){{.pulse,.drift{{animation:none}}.pkt{{display:none}}}}
</style>
<g clip-path="url(#clip)">
  <rect width="960" height="320" fill="{t["bg"]}"/>
  <rect width="960" height="320" fill="url(#dots)" mask="url(#m)"/>
  <circle class="drift" cx="800" cy="60" r="260" fill="url(#g1)"/>
  <circle class="drift" cx="560" cy="330" r="220" fill="url(#g2)" style="animation-delay:-6s"/>

  <g>
    <circle cx="62" cy="71" r="4.5" fill="{t["accent"]}" class="pulse"/>
    <text x="78" y="76" class="mono" font-size="15" fill="{t["muted"]}">{STATUS}</text>
  </g>
  <text x="54" y="150" class="sans" font-size="60" font-weight="700" letter-spacing="-1.8" fill="{t["ink"]}">{NAME}</text>
  <text x="56" y="194" class="sans" font-size="20" fill="{t["muted"]}">{ROLE}</text>
  <g>{"".join(chips)}</g>

  <g>
    <path d="{inbound}" stroke="{t["faint"]}" stroke-width="1.5" stroke-dasharray="3 5"/>
    {wires}
    <circle r="3.5" fill="{t["accent2"]}" class="pkt"><animateMotion dur="1.6s" repeatCount="indefinite" path="{inbound}"/></circle>
    {packets}
    {nodes}
    <circle cx="{lb[0]}" cy="{lb[1]}" r="26" fill="{t["bg2"]}" stroke="{t["accent"]}" stroke-width="1.5"/>
    <path d="M{lb[0] - 9},{lb[1]} h8 m0,0 l9,-8 m-9,8 h10 m-10,0 l9,8" fill="none" stroke="{t["accent"]}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</g>
<rect x=".5" y=".5" width="959" height="319" rx="19.5" fill="none" stroke="{t["border"]}"/>
</svg>
'''


def card(t, title, lines, lang, lang_color):
    desc = "".join(
        f'<text x="24" y="{74 + i * 21}" class="sans" font-size="14.5" fill="{t["muted"]}">{l}</text>' for i, l in enumerate(lines)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 150" role="img" aria-label="{title}: {" ".join(lines)}">
<title>{title}</title>
<style>.sans{{font-family:{SANS}}} .mono{{font-family:{MONO}}}</style>
<rect x=".5" y=".5" width="479" height="149" rx="13.5" fill="{t["bg"]}" stroke="{t["border"]}"/>
<path d="M24,31 v-7 a2,2 0 0 1 2,-2 h5 l2,2.5 h7 a2,2 0 0 1 2,2 v9.5 a2,2 0 0 1 -2,2 h-14 a2,2 0 0 1 -2,-2 z" fill="none" stroke="{t["accent"]}" stroke-width="1.5" stroke-linejoin="round"/>
<text x="52" y="38" class="mono" font-size="17" font-weight="600" fill="{t["ink"]}">{title}</text>
<path d="M444,26 h10 v10 M454,26 l-11,11" fill="none" stroke="{t["muted"]}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
{desc}
<circle cx="30" cy="124" r="5" fill="{lang_color}"/>
<text x="42" y="129" class="sans" font-size="13" fill="{t["muted"]}">{lang}</text>
</svg>
'''


def skills(t):
    row_h, top = 50, 26
    h = top * 2 + row_h * len(SKILLS) - 14
    rows = []
    for i, (label, items) in enumerate(SKILLS):
        y = top + i * row_h
        rows.append(f'<text x="30" y="{y + 23}" class="mono" font-size="13" letter-spacing="1.2" fill="{t["accent"]}">{label.upper()}</text>')
        x = 170
        for it in items:
            w = round(len(it) * 9.1 + 32)
            rows.append(
                f'<rect x="{x}" y="{y}" width="{w}" height="36" rx="18" fill="{t["bg2"]}" stroke="{t["border"]}"/>'
                f'<text x="{x + w / 2}" y="{y + 23}" text-anchor="middle" class="mono" font-size="15" fill="{t["ink"]}">{it}</text>'
            )
            x += w + 10
        if i:
            rows.append(f'<path d="M30,{y - 7.5} H810" stroke="{t["border"]}" stroke-dasharray="2 6"/>')
    label = "; ".join(f"{l}: {', '.join(v)}" for l, v in SKILLS)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 {h}" role="img" aria-label="Skills — {label}">
<title>Skills</title>
<style>.mono{{font-family:{MONO}}}</style>
<rect x=".5" y=".5" width="839" height="{h - 1}" rx="13.5" fill="{t["bg"]}" stroke="{t["border"]}"/>
{"".join(rows)}
</svg>
'''


for name, t in THEMES.items():
    (OUT / f"skills-{name}.svg").write_text(skills(t))
    (OUT / f"hero-{name}.svg").write_text(hero(t))
    for slug, args in CARDS.items():
        (OUT / f"card-{slug}-{name}.svg").write_text(card(t, *args))
print("wrote", len(list(OUT.glob("*.svg"))), "svgs")
