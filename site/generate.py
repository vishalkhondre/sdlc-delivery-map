"""Generate a static teaching reference under dist/. Run from any directory.

The shell, self-hosted fonts, colour tokens and documentation layout are adapted
from vishalkhondre/ai-sdlc-map. All routes are relative to the deployment path.
"""
from __future__ import annotations

import html
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
SITE = ROOT / "site"
OUT = ROOT / "dist"
PHASES = ("Define", "Build", "Prove", "Release", "Learn", "Reference")
PHASE_BANDS = {
    "Define": ("define", "Decide & Define"),
    "Build": ("build", "Build & Prove"),
    "Prove": ("build", "Build & Prove"),
    "Release": ("release", "Release & Learn"),
    "Learn": ("release", "Release & Learn"),
    "Reference": ("reference", "Reference"),
}
TECHNICAL_VALUE = re.compile(r"\b(?:CC-\d+|AC-\d+|sha256:[a-fA-F0-9]{8,64})\b")
NAV = (("Map", "index.html"), ("Guided tour", "tour.html"), ("Topics", "topics.html"), ("Sources", "references.html"))
SECTIONS = (("inputs", "Before you begin"), ("steps", "How it works"), ("example", "Worked example"),
            ("evidence", "What to record"), ("failure", "When it goes wrong"), ("measure", "How to measure it"),
            ("next-decision", "Follow the workflow"), ("sources", "Sources"))
TOUR = [
    ("intent", "Decide & Define", "Choose the change", "Requests wait for someone to assign them. The team proposes a rule that selects the right approver when a request arrives. The goal is a shorter wait for a decision.",
     ("define", "criteria"), "Could a manually assigned request pass the acceptance test?", "Yes, if the test checks only who received the request. Record what triggered the assignment and verify the expected recipient."),
    ("integration", "Build & Prove", "Integrate a change", "A developer links the feature to a short-lived branch. A peer reviews the change. Required checks exercise the proposed code, and the integrated commit identifies what enters the build.",
     ("branch", "pull-request", "ci", "merge"), "What happens when a required check fails?", "The author fixes the change and runs the check again. The unsuccessful run stays in the history of the pull request."),
    ("candidate", "Build & Prove", "Identify the candidate", "The integrated build produces an image. Its digest identifies the candidate as it moves through QA, UAT and Prod. Configuration is recorded separately for each environment.",
     ("build", "digest", "registry", "qa-rollout", "qa-revision"), "What could change even if the digest stays the same?", "An environment can use different rules, roles or external integrations. Record the deployed configuration alongside the image digest."),
    ("qualification", "Build & Prove", "Test and accept", "QA submits a request without a manual assignment. A business user exercises the workflow in UAT. Each decision refers to the candidate that actually ran.",
     ("qa-tests", "uat-promotion", "uat-runtime", "uat-decision", "validation-summary"), "Where does a failed QA check or rejected UAT decision lead?", "Hold the release, link the defect and the unmet criterion, then requalify the corrected candidate. A passing QA run leads to UAT."),
    ("release", "Release & Learn", "Authorize and deploy", "The release identifies the qualified candidate. The production job checks its authorization, deploys the selected digest with Prod configuration and records what is serving traffic.",
     ("release-plan", "release", "policy", "rollout", "deployment-record", "notes"), "Does publishing a release prove that the feature is live?", "No. Trace from the release to the rollout and the runtime revision, then check whether users can actually exercise the feature."),
    ("reliability", "Release & Learn", "Verify service and recover", "A controlled Prod request checks the active routing rule. After rollout, the service owner watches for routing failures and requests left unassigned.",
     ("observe", "smoke", "alert", "incident", "recover"), "How do we know that restoring the service helped the people affected?", "Verify new assignments, identify requests held up during the incident and reconcile those requests. Record the evidence with the incident."),
    ("learning", "Release & Learn", "Decide what to do next", "The Product Owner reviews the time to assignment, the time to decision and the requests still open after one day. Requesters and approvers explain what they experienced.",
     ("measure", "feedback"), "Forty of 100 requests reached a decision by one day. Did the cohort reach its one-day median target?", "With a full day of follow-up, 60% remained open at one day. Fewer than half had received a decision, so the median was not reached by that milestone."),
]
BRANCHES = {
    "define": [("criteria", "Agree the business rules"), ("measure", "Plan how to measure the result")],
    "branch": [("pull-request", "Open the change for review")],
    "pull-request": [("ci", "Run the required checks"), ("branch", "Address review feedback")],
    "merge": [("build", "Build the integrated revision")],
    "build": [("digest", "Identify the output"), ("qa-rollout", "Select the QA candidate")],
    "digest": [("registry", "Locate the artifact"), ("qa-rollout", "Deploy by digest")],
    "qa-rollout": [("registry", "Pull the candidate"), ("qa-revision", "Confirm the running version")],
    "registry": [("qa-revision", "Check the deployed candidate")],
    "qa-revision": [("qa-tests", "Test the running QA revision")],
    "uat-promotion": [("uat-runtime", "Start the UAT revision")],
    "uat-runtime": [("uat-decision", "Exercise the business workflow")],
    "validation-summary": [("release-plan", "Plan the accepted change for release"), ("evidence-record", "Inspect linked evidence")],
    "release-plan": [("release", "Publish the accepted version")],
    "release": [("policy", "Check production eligibility")],
    "rollout": [("observe", "Observe the running revision")],
    "deployment-record": [("notes", "Publish what changed"), ("alert", "Monitor the service")],
    "notes": [("alert", "Operate the feature"), ("measure", "Assess the outcome")],
    "criteria": [("branch", "Criteria agreed"), ("define", "Objective needs work")],
    "ci": [("merge", "Checks pass"), ("branch", "Checks fail")],
    "qa-tests": [("uat-promotion", "QA passes"), ("hold", "QA fails"), ("digest", "Trace the candidate backwards"), ("evidence-record", "Inspect a worked record")],
    "uat-decision": [("validation-summary", "Business accepts"), ("hold", "Business rejects")],
    "hold": [("branch", "Repair the change"), ("qa-tests", "Requalify the candidate")],
    "policy": [("rollout", "Authorized"), ("hold", "Evidence missing or stale")],
    "observe": [("smoke", "Verify production routing"), ("recover", "Health check fails")],
    "smoke": [("deployment-record", "Smoke test passes"), ("recover", "Smoke test fails")],
    "alert": [("incident", "Investigate the affected requests")],
    "incident": [("recover", "Restore and verify the service")],
    "recover": [("smoke", "Verify restored routing"), ("incident", "Reconcile affected requests")],
    "measure": [("feedback", "Review the outcome")],
    "feedback": [("define", "Shape the next change")],
}
ICONS = {
    "search": '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 4.5 4.5"/>',
    "arrow": '<path d="M4 12h15m-6-6 6 6-6 6"/>',
    "theme": '<circle cx="12" cy="12" r="8"/><path fill="currentColor" d="M12 4a8 8 0 0 1 0 16z"/>',
    "download": '<path d="M12 3v11m-4-4 4 4 4-4M5 16v4h14v-4"/>',
    "expand": '<path d="M8 3H3v5m13-5h5v5M8 21H3v-5m13 5h5v-5"/>',
    "list": '<path d="M8 6h12M8 12h12M8 18h12"/><circle cx="4" cy="6" r=".7"/><circle cx="4" cy="12" r=".7"/><circle cx="4" cy="18" r=".7"/>',
}
def icon(name):
    return f'<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>'

def e(text):
    return html.escape(str(text), quote=True)

def lesson_text(value):
    return TECHNICAL_VALUE.sub(lambda m: f"<code>{m.group()}</code>", e(value))

def load():
    result = {}
    for path in sorted(CONTENT.glob("0*.json")):
        for t in json.loads(path.read_text()):
            if t["id"] in result or not re.fullmatch(r"[a-z0-9-]+", t["id"]):
                raise ValueError(f'Duplicate or malformed topic ID: {t["id"]}')
            if t["phase"] not in PHASES:
                raise ValueError(f'Unknown phase: {t["phase"]}')
            result[t["id"]] = t
    if not result:
        raise ValueError("No lessons in content/0*.json")
    return result

def source_url(url):
    if not url.startswith(("https://", "http://")):
        raise ValueError(f"Source must be an HTTP(S) URL: {url}")
    return e(url)

def topic_link(topics, key, prefix="", label=None):
    return f'<a href="{prefix}topics/{e(key)}.html">{e(label or topics[key]["title"])}</a>'

def shell(title, summary, body, *, active, prefix=""):
    tabs = "".join(f'<a href="{prefix}{path}"' + (' aria-current="true"' if name == active else '') + f'>{name}</a>' for name, path in NAV)
    mark = '<svg class="brand-mark" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M2 2h20v4H2zm0 8h13v4H2zm0 8h20v4H2z"/></svg>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} · SDLC Delivery Map</title><meta name="description" content="{e(summary)}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(summary)}">
<link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/base.css"><link rel="stylesheet" href="{prefix}assets/delivery.css">
<script>try{{const t=localStorage.getItem('delivery-map-theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
<script src="{prefix}assets/delivery.js" defer></script></head><body data-root="{prefix}">
<a class="skip" href="#content">Skip to content</a><header class="topbar"><div class="topbar-inner">
<a class="brand" href="{prefix}index.html">{mark}<span>SDLC Delivery Map</span></a><nav class="tabs" aria-label="Main navigation">{tabs}</nav>
<div class="tools"><a class="iconbtn" aria-label="Search topics" title="Search topics" href="{prefix}topics.html#topic-search">{icon("search")}</a>
<button id="theme-toggle" class="iconbtn js-only" type="button" aria-label="Switch colour theme" title="Switch colour theme">{icon("theme")}</button></div></div></header>
{body}<footer class="site-footer"><div><a class="brand footbrand" href="{prefix}index.html">{mark}SDLC Delivery Map</a>
<nav aria-label="Footer navigation"><a href="{prefix}topics.html">All topics</a><a href="{prefix}references.html">Sources and credits</a><a href="https://github.com/vishalkhondre/sdlc-delivery-map">Source repository</a><a href="{prefix}assets/delivery-map.png" download>Download diagram</a></nav></div></footer></body></html>'''

def write(path, text):
    dest = OUT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")

def interactive_map(hotspots, topics):
    areas = []
    for i, h in enumerate(hotspots):
        key = h["id"]
        if key not in topics:
            raise ValueError(f'Unresolved hotspot: {key}')
        x,y,w,height = [float(h[k]) for k in ("x","y","w","h")]
        if not (x >= 0 and y >= 0 and w > 0 and height > 0 and x+w <= 2048.1 and y+height <= 1735.1):
            raise ValueError(f'Hotspot outside diagram: {h}')
        anchor = h.get("anchor", "")
        if anchor and anchor not in {sec for sec, _ in SECTIONS}:
            raise ValueError(f"Unknown lesson section: {anchor}")
        fragment = ("#" + e(anchor)) if anchor else ""
        areas.append(f'<a class="map-link" href="topics/{e(key)}.html{fragment}" aria-label="{e(h["label"])}" id="area-{i}" data-topic="{e(key)}"><title>{e(h["label"])}</title><rect x="{x:g}" y="{y:g}" width="{w:g}" height="{height:g}" rx="5"/></a>')
    return f'''<figure class="map-figure" id="map"><div class="map-toolbar"><div><h2>Interactive map</h2><p>Select a label to open its lesson.</p></div>
<div class="map-tools"><a id="text-view" href="topics.html">{icon("list")}Text view</a><button class="js-only" type="button" id="map-expand" aria-pressed="false">{icon("expand")}<span>Expand</span></button></div></div>
<div class="map-scroll" id="map-canvas" aria-label="Interactive delivery diagram" tabindex="0">
<svg id="delivery-map" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2048 1735" width="2048" height="1735" role="group" aria-labelledby="map-title map-desc">
<title id="map-title">From Feature Commit to Production</title><desc id="map-desc">A swimlane diagram with activity, stakeholder, tool and evidence links. Use the Text view link for the same topics as an accessible outline.</desc>
<image href="assets/delivery-map.png" width="2048" height="1735" aria-hidden="true"/>{''.join(areas)}</svg>
</div><figcaption><div class="zoom-group js-only"><button type="button" id="zoom-out" aria-label="Zoom out">−</button><output id="zoom-level" aria-live="polite">100%</output>
<button type="button" id="zoom-in" aria-label="Zoom in">+</button><button type="button" id="zoom-fit">Fit</button></div>
<a href="assets/delivery-map.png" download>{icon("download")}Download PNG</a></figcaption></figure>'''

def home(topics, hotspots):
    body = f'''<main class="home frame" id="content" tabindex="-1">
<section class="intro"><div><h1>From Feature Commit to Production</h1>
<p>Explore how a team defines, builds, tests and releases a change, then uses production evidence to decide what to do next.</p></div>
<div class="start-card"><strong>New to software delivery?</strong><p>Follow one approval-routing feature through seven decisions.</p><a class="primary" href="tour.html">Start the guided tour</a></div></section>
{interactive_map(hotspots, topics)}
<section class="route-section"><h2>Explore by phase</h2><div class="phase-grid">'''
    for phase, title, desc in [
        ("Define","Decide & Define","Frame the problem and agree on a testable outcome."),
        ("Build","Build & Prove","Follow the candidate through source control, CI, QA and business acceptance."),
        ("Release","Release & Learn","Authorize a rollout, recover service and measure whether the feature helped."),
    ]:
        page = f"topics/phase-{phase.lower()}.html" if f"phase-{phase.lower()}" in topics else f"topics.html#phase-{phase.lower()}"
        body += f'<a class="phase-card phase-{phase.lower()}" href="{page}"><h3>{title}</h3><p>{desc}</p></a>'
    body += '</div></section>'
    lookup = [topic_link(topics,k,label=label) for k,label in (("glossary","Glossary"),("evidence-record","Worked evidence record"),("handoffs","Read the handoffs")) if k in topics]
    if lookup:
        body += '<nav class="lookup-links" aria-label="Learning resources">'+ " · ".join(lookup) + '</nav>'
    body += '</main>' 
    return shell("From Feature Commit to Production","Explore the SDLC with a clickable software delivery diagram and guided walkthrough.",body,active="Map")

def tour_page(topics):
    parts=['<main id="content" class="reading frame" tabindex="-1"><div class="page-intro"><h1>Follow one feature</h1><p>Work through seven decisions in the approval-routing example. At each stop, trace the evidence and test what happens when a check fails.</p></div><ol class="tour-list" id="tour-stops">']
    for slug, phase, name, intro, keys, prompt, answer in TOUR:
        items = [topic_link(topics,key) for key in keys if key in topics]
        if slug == "qualification" and "hold" in topics:
            items.append(topic_link(topics,"hold",label="Failure path: hold and requalify"))
        parts.append(f'<li id="{slug}" class="phase-{PHASE_BANDS[topics[keys[0]]["phase"]][0]}"><div class="phase-name">{e(phase)}</div><h2>{e(name)}</h2><p>{e(intro)}</p><div class="topic-links">{"".join(items)}</div><details><summary>{e(prompt)}</summary><p>{e(answer)}</p></details></li>')
    parts.append('</ol><a href="index.html#map" class="primary">Return to the map</a></main>')
    return shell("Guided tour","Follow a fictional feature through seven decisions.",''.join(parts),active="Guided tour")

def topic_index(topics, hotspots):
    aliases = defaultdict(list)
    for h in hotspots:
        if h["label"] not in aliases[h["id"]]:
            aliases[h["id"]].append(h["label"])
    total=len(topics)
    out = ['<main class="frame index-page" id="content" tabindex="-1"><div class="page-intro"><h1>Topic index</h1><p>Open a lesson by activity, tool, role or output. The phase groups provide a text view of the map.</p></div>']
    out.append('<div class="filterbar js-only"><label for="topic-search">Search topics<input type="search" id="topic-search" placeholder="Try UAT, acceptance criteria or image digest" autocomplete="off"></label><label for="phase-select">Phase<select id="phase-select"><option value="">All phases</option>' + ''.join(f'<option value="{p}">{p}</option>' for p in PHASES) + '</select></label><button id="clear-search" type="button">Reset</button></div>')
    out.append(f'<p id="result-count" aria-live="polite">{total} topics</p>')
    for phase in PHASES:
        rows = []
        for key, t in topics.items():
            if t["phase"] != phase:
                continue
            keywords = " ".join([*aliases[key],t["owner"],t["title"], t["summary"], t["evidence"]])
            alt_names = [name for name in aliases[key] if name.lower() != t["title"].lower()]
            note = f'<p class="aliases">On the map · {e(" · ".join(alt_names))}</p>' if alt_names else ""
            rows.append(f'<article class="topic-row" data-phase="{phase}" data-text="{e(keywords)}"><h3>{topic_link(topics,key)}</h3><p>{e(t["summary"])}</p>{note}</article>')
        if rows:
            out.append(f'<section class="index-section phase-{PHASE_BANDS[phase][0]}" id="phase-{phase.lower()}" data-index-phase="{phase}"><h2>{phase}</h2><div class="topic-grid">{"".join(rows)}</div></section>')
    out.append('<p id="no-results" hidden>There are no matching topics. Try a different word or choose another phase.</p></main>')
    return shell("Topic index","Browse or search every topic in the SDLC Delivery Map.",''.join(out),active="Topics")

def refs_page(topics):
    sources = {}
    for key,t in topics.items():
        for s in t["sources"]:
            r = sources.setdefault(s["url"],{"title":s["title"],"items":[]})
            if key not in r["items"]:
                r["items"].append(key)
    result=['<main id="content" class="reading frame" tabindex="-1"><div class="page-intro"><h1>Sources and credits</h1><p>Use these references to inspect a mechanism or practice in more detail. The example feature, work items and measures in this guide are illustrative.</p></div><ul class="sources-list">']
    for url,s in sorted(sources.items(),key=lambda item:item[1]["title"].casefold()):
        links = " · ".join(topic_link(topics,key) for key in s["items"])
        result.append(f'<li><a href="{source_url(url)}">{e(s["title"])}</a><p>Used in {links}</p></li>')
    result.append('</ul><section class="credit"><h2>Site design and publishing</h2><p>The documentation layout, local fonts, colour system and publishing approach are adapted from <a href="https://github.com/vishalkhondre/ai-sdlc-map">The AI SDLC Map</a> by Vishal Khondre. The interactive swimlane follows an illustrative delivery workflow and links to original learning material on this site.</p><p><a href="https://github.com/vishalkhondre/sdlc-delivery-map">Browse the SDLC Delivery Map source repository</a>.</p><p><a href="LICENSE.txt">Content and tooling licences</a> · <a href="assets/fonts/LICENSE-atkinson-hyperlegible.txt">Atkinson Hyperlegible font licence</a> · <a href="assets/fonts/LICENSE-ibm-plex-mono.txt">IBM Plex Mono font licence</a></p></section></main>')
    return shell("Sources and credits","Source index with links back to every lesson using each reference.",''.join(result),active="Sources")

def topic_page(key, topics, area_by_id):
    t=topics[key]
    prefix="../"
    phase=t["phase"]
    band, band_name = PHASE_BANDS[phase]
    activity = t.get("activity", "")
    tag = (f'<span class="activity-tag activity-{e(activity.lower().replace(" ", "-"))}">{e(activity)}</span>'
           if activity else "")
    same_phase = [item for item in topics.values() if item["phase"]==phase]
    keys=list(topics)
    ordinal=keys.index(key)
    nav_items=''.join(f'<li><a href="{e(item["id"])}.html"'+(' aria-current="page"' if item["id"]==key else '')+f'>{e(item["title"])}</a></li>' for item in same_phase)
    back_id = f"area-{area_by_id[key]}" if key in area_by_id else "map"
    top = f'''<div class="docs has-onpage"><nav class="sidenav" aria-label="Topics in {e(phase)}"><p class="sidenav-title">{e(phase)}</p><ul>{nav_items}</ul><a href="../topics.html">All topics</a></nav>
<main id="content" tabindex="-1" class="lesson"><article id="article"><nav aria-label="Breadcrumb" class="crumb phase-{band}"><a href="../index.html#map">Map</a><span>/</span><a class="phase-name" href="../topics.html#phase-{phase.lower()}">{e(band_name)}</a>{tag}</nav>
<h1>{e(t["title"])}</h1><p class="summary">{lesson_text(t["summary"])}</p><div class="owner"><b>Responsible role</b> {e(t["owner"])}</div>'''
    result=[top]
    def section(sec, label, content, cls=""):
        return f'<section class="lesson-block {cls}" id="{sec}"><h2>{label}</h2>{content}</section>'
    def listing(tag, items):
        return f'<{tag}>'+''.join(f'<li>{lesson_text(x)}</li>' for x in items)+f'</{tag}>'
    result.append(section("inputs","Before you begin",listing("ul",t["inputs"])))
    result.append(section("steps","How it works",listing("ol",t["steps"])))
    for sec,heading in SECTIONS[2:6]:
        result.append(section(sec,heading,f'<p>{lesson_text(t[sec])}</p>', "example-panel" if sec=="example" else ""))
    branches=BRANCHES.get(key,[])
    if not branches:
        sequence=[x["id"] for x in same_phase]
        idx=sequence.index(key)
        if idx+1<len(sequence):
            branches=[(sequence[idx+1],"Continue reading")]
        elif ordinal+1<len(keys):
            branches=[(keys[ordinal+1],"Continue reading")]
    choices=''.join(f'<li><span>{e(label)}</span>{topic_link(topics,other,prefix)}</li>' for other,label in branches if other in topics)
    tour_id=next((s[0] for s in TOUR if key in s[4]),None)
    result.append(section("next-decision","Follow the workflow",
                          (f'<ul class="handoffs">{choices}</ul>' if choices else '')+
                          (f'<a href="../tour.html#{tour_id}">Open this stop in the guided tour</a> · ' if tour_id else '')+
                          f'<a href="../index.html#{back_id}">Return to the map</a>'))
    if key == "evidence-record":
        files = sorted((SITE/"assets"/"examples").glob("*"))
        if files:
            links = [f'<li><a href="../assets/examples/{e(f.name)}" download>{e(f.stem.replace("-", " ").replace("_"," ").capitalize())} ({e(f.suffix.lstrip(".").upper())})</a></li>' for f in files if f.is_file()]
            result.append(section("downloads","Download the example records",'<ul>'+''.join(links)+'</ul>'))
    result.append(section("sources","Sources",'<ul class="source-links">'+''.join(f'<li><a href="{source_url(s["url"])}">{e(s["title"])}</a></li>' for s in t["sources"])+'</ul>'))
    result.append('</article><nav class="lesson-pager" aria-label="Reading order">')
    for index,label in ((ordinal-1,"Previous topic"),(ordinal+1,"Next topic")):
        if 0<=index<len(keys):
            other=keys[index]
            result.append(f'<a href="{e(other)}.html"><small>{label}</small><strong>{e(topics[other]["title"])}</strong></a>')
    result.append('</nav></main><nav class="onpage" aria-label="On this page"><p class="onpage-title">On this page</p><ul>'+''.join(f'<li><a href="#{sec}">{label}</a></li>' for sec,label in SECTIONS)+'</ul></nav></div>')
    return shell(t["title"],t["summary"],''.join(result),active="Topics",prefix=prefix)

def generate():
    topics = load()
    spots = json.loads((CONTENT/"hotspots.json").read_text())
    # Sources are validated before writing links. Rebuilding into a clean
    # directory prevents deleted lessons from surviving a release.
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(SITE/"assets",OUT/"assets")
    shutil.copy2(SITE/"favicon.svg",OUT/"favicon.svg")
    shutil.copy2(ROOT/"LICENSE",OUT/"LICENSE.txt")
    write("index.html",home(topics,spots))
    write("tour.html",tour_page(topics))
    write("topics.html",topic_index(topics,spots))
    write("references.html",refs_page(topics))
    by_id={}
    for i,spot in enumerate(spots):
        by_id.setdefault(spot["id"],i)
    for key in topics:
        write(f"topics/{key}.html",topic_page(key,topics,by_id))
    write(".nojekyll","")
    print(f"Built {len(topics)} lessons, {len(spots)} map targets and 4 navigation pages in {OUT.name}/.")

if __name__ == "__main__":
    generate()
