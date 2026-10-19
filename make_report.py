#!/usr/bin/env python3
import json, pathlib
payload=json.load(open("/tmp/payload.json", encoding="utf-8"))
p=json.dumps(payload, ensure_ascii=False)

out="/home/user/auslastung/index.html"
f=open(out,"w",encoding="utf-8")

def w(s): f.write(s)

# HEADER
w("""<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>PACS-Auslastung Q1–Q3 2026 — BD-Bereitschaftsdienst · St. Georg Leipzig</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script>tailwind.config={theme:{extend:{fontFamily:{sans:['Inter','sans-serif'],mono:['JetBrains Mono','monospace'],serif:['Instrument Serif','serif']}}}}</script>
<style>
*{scroll-behavior:smooth}body{background:#040711;color:#eef2ff;overflow-x:hidden}
::-webkit-scrollbar{width:10px}::-webkit-scrollbar-thumb{background:rgba(124,108,255,.4);border-radius:999px}
.glass{background:linear-gradient(180deg,rgba(255,255,255,.08),rgba(255,255,255,.03));backdrop-filter:blur(24px) saturate(1.4);-webkit-backdrop-filter:blur(24px) saturate(1.4);border:1px solid rgba(255,255,255,.10);box-shadow:0 8px 32px rgba(0,0,0,.35),inset 0 1px 0 rgba(255,255,255,.08)}
.glass-strong{background:linear-gradient(180deg,rgba(255,255,255,.12),rgba(255,255,255,.04));backdrop-filter:blur(28px) saturate(1.6);border:1px solid rgba(255,255,255,.14)}
.glass-subtle{background:rgba(255,255,255,.04);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.06)}
.mesh{position:fixed;inset:0;z-index:-2;background:radial-gradient(1200px 600px at 20% -10%,rgba(124,108,255,.28),transparent 60%),radial-gradient(900px 700px at 90% 0%,rgba(14,165,233,.22),transparent 60%),radial-gradient(800px 600px at 70% 80%,rgba(255,59,130,.16),transparent 60%),radial-gradient(700px 500px at 10% 90%,rgba(163,255,18,.08),transparent 60%),#040711}
.blob{position:absolute;border-radius:50%;filter:blur(60px);opacity:.6;mix-blend-mode:screen;animation:float 18s ease-in-out infinite}
.blob1{width:700px;height:700px;background:radial-gradient(circle at 30% 30%,#7c6cff,transparent 70%);left:-120px;top:-160px}
.blob2{width:600px;height:600px;background:radial-gradient(circle at 50% 50%,#0ea5e9,transparent 70%);right:-80px;top:10%;animation-delay:-6s}
.blob3{width:650px;height:650px;background:radial-gradient(circle at 40% 40%,#ff3b82,transparent 70%);right:20%;bottom:-120px;animation-delay:-12s}
@keyframes float{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(30px,-20px) scale(1.05)}66%{transform:translate(-20px,20px) scale(.98)}}
.progress{position:fixed;top:0;left:0;height:2px;background:linear-gradient(90deg,#7c6cff,#0ea5e9,#ff3b82);z-index:100;width:0%}
.kpi-number{font-variant-numeric:tabular-nums}.heat-cell{transition:.2s}.heat-cell:hover{transform:scale(1.08);z-index:2;box-shadow:0 4px 20px rgba(0,0,0,.4)}
.shimmer{position:relative;overflow:hidden}.shimmer::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.08),transparent);transform:translateX(-100%);animation:shimmer 3.2s infinite}
@keyframes shimmer{100%{transform:translateX(100%)}}canvas{max-width:100%!important}
</style></head><body class="antialiased selection:bg-[#7c6cff]/30">
<div class="progress" id="progress"></div><div class="mesh"><div class="blob blob1"></div><div class="blob blob2"></div><div class="blob blob3"></div>
<div style="position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(255,255,255,.015) 0 1px,transparent 1px 3px);opacity:.4"></div></div>
<header class="sticky top-0 z-40"><div class="mx-auto max-w-[1440px] px-4 sm:px-6 lg:px-8 pt-4">
<div class="glass rounded-[18px] flex items-center justify-between px-3 sm:px-5 py-3 gap-3">
<div class="flex items-center gap-3 min-w-0">
<div class="w-10 h-10 rounded-xl bg-gradient-to-br from-[#7c6cff] to-[#0ea5e9] grid place-items-center shadow-lg shrink-0">
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M9 3H5c-1 0-2 1-2 2v4"/><path d="M19 9V5c0-1-1-2-2-2h-4"/><path d="M15 21h4c1 0 2-1 2-2v-4"/><path d="M5 15v4c0 1 1 2 2 2h4"/><circle cx="12" cy="12" r="3.5"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22"/></svg></div>
<div class="min-w-0"><div class="font-semibold tracking-tight leading-none text-sm sm:text-[15px]">PACS<span class="text-white/60"> ·</span> St. Georg Leipzig</div>
<div class="text-[11px] tracking-[0.14em] uppercase text-white/55 font-medium">Auslastung Q1–Q3 2026 · BD-Analyse</div></div>
<div class="hidden lg:flex items-center gap-2 ml-4">
<span class="px-2.5 py-1 rounded-full text-[11px] font-semibold bg-white/10 border border-white/10">67 321 Studien</span>
<span class="px-2.5 py-1 rounded-full text-[11px] font-semibold bg-[#7c6cff] text-white">BD 35,0 %</span>
<span class="px-2.5 py-1 rounded-full text-[11px] font-semibold bg-white/5 border border-white/10">273 Tage</span></div></div>
<div class="hidden md:flex items-center gap-2 text-xs">
<a href="#executive" class="px-3 py-2 rounded-full bg-white text-zinc-900 font-semibold">Report starten</a>
<a href="#methodik" class="px-3 py-2 rounded-full glass-subtle hover:bg-white/10">Methodik</a></div>
<button id="menuBtn" class="md:hidden w-9 h-9 grid place-items-center rounded-full glass-subtle"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M4 6h16M4 12h16M4 18h16"/></svg></button>
</div>
<div class="mt-3 hidden lg:block"><div class="glass rounded-full px-2 py-1.5 flex items-center gap-1 overflow-x-auto">
<a href="#bdmodell" class="px-3 py-1.5 rounded-full text-xs font-medium bg-white text-zinc-900 shrink-0">BD-Modell</a>
<a href="#kpi" class="px-3 py-1.5 rounded-full text-xs font-medium hover:bg-white/10 shrink-0">KPIs</a>
<a href="#temporal" class="px-3 py-1.5 rounded-full text-xs font-medium hover:bg-white/10 shrink-0">Temporal</a>
<a href="#modal" class="px-3 py-1.5 rounded-full text-xs font-medium hover:bg-white/10 shrink-0">Modalitäten</a>
<a href="#institution" class="px-3 py-1.5 rounded-full text-xs font-medium hover:bg-white/10 shrink-0">Institutionen</a>
<a href="#abteilung" class="px-3 py-1.5 rounded-full text-xs font-medium hover:bg-white/10 shrink-0">Abteilungen</a>
<a href="#personen" class="px-3 py-1.5 rounded-full text-xs font-medium hover:bg-white/10 shrink-0">Radiolog:innen</a>
<a href="#telerad" class="px-3 py-1.5 rounded-full text-xs font-medium hover:bg-white/10 shrink-0">Teleradiologie</a>
<a href="#workflow" class="px-3 py-1.5 rounded-full text-xs font-medium hover:bg-white/10 shrink-0">Durchsatz</a>
<a href="#anomalien" class="px-3 py-1.5 rounded-full text-xs font-medium hover:bg-white/10 shrink-0">Anomalien</a>
<a href="#empfehlungen" class="px-3 py-1.5 rounded-full text-xs font-medium hover:bg-white/10 shrink-0">Empfehlungen</a>
</div></div></div></header>
<main class="mx-auto max-w-[1440px] px-4 sm:px-6 lg:px-8 pb-16">
""")

# HERO
w("""
<section class="mt-6 lg:mt-8 grid grid-cols-12 gap-4 lg:gap-6">
<div class="col-span-12 lg:col-span-8"><div class="glass rounded-[28px] p-6 sm:p-8 lg:p-10 overflow-hidden relative">
<div class="absolute -top-24 -right-24 w-[520px] h-[520px] rounded-full bg-gradient-to-br from-[#7c6cff]/30 to-[#0ea5e9]/20 blur-[60px] pointer-events-none"></div>
<div class="flex flex-wrap items-center gap-2 mb-4">
<span class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white text-zinc-900 text-xs font-bold tracking-wide"><span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span> LIVE AUSWERTUNG · 01.01.–30.09.2026</span>
<span class="px-3 py-1.5 rounded-full glass-subtle text-xs font-medium">273 Tage · 6 Feiertage · 78 Wochenendtage</span>
<span class="px-3 py-1.5 rounded-full bg-[#ff3b82] text-white text-xs font-bold">Q3 vollständig</span></div>
<h1 class="font-serif text-[32px] sm:text-[44px] lg:text-[52px] leading-[0.92] tracking-[-0.03em]">Wer hält die Stellung,<br>
<span class="bg-gradient-to-r from-[#7c6cff] via-[#0ea5e9] to-[#ff3b82] bg-clip-text text-transparent">wenn die Klinik schläft?</span></h1>
<p class="mt-5 text-[15px] sm:text-[16px] leading-relaxed text-white/70 max-w-[720px]">
Vollständige PACS-Auswertung der Quartale 1–3 2026 (67 321 Studien) unter dem BD-Modell: werktags 16:00–07:30, Freitag 16:00–Samstag 09:00, Samstag 09:00–09:00, Sonntag 09:00–Montag 07:30, Feiertag 09:00–09:00/07:30.
Diese Analyse zerlegt jede Minute, Modalität und Abteilung — und zeigt, wo der einzelne BD-Arzt überproportional trägt.</p>
<div class="mt-7 flex flex-wrap gap-3">
<a href="#temporal" class="px-5 py-3 rounded-full bg-white text-zinc-900 font-semibold text-sm">Zeitsignatur entdecken →</a>
<a href="#empfehlungen" class="px-5 py-3 rounded-full glass-subtle font-semibold text-sm border border-white/15">Direkt zu Konsequenzen</a>
<div class="flex items-center gap-3 pl-2"><div class="flex -space-x-2">
<img src="https://i.pravatar.cc/100?img=11" class="w-8 h-8 rounded-full border-2 border-zinc-900"><img src="https://i.pravatar.cc/100?img=14" class="w-8 h-8 rounded-full border-2 border-zinc-900"><img src="https://i.pravatar.cc/100?img=32" class="w-8 h-8 rounded-full border-2 border-zinc-900"></div>
<div class="text-xs text-white/60 leading-tight">Für<br><span class="text-white font-semibold">Radiologie · Klinikleitung</span></div></div></div>
<div class="mt-8 grid grid-cols-3 gap-3 max-w-[560px]">
<div class="glass-subtle rounded-2xl p-3"><div class="text-[11px] tracking-widest uppercase text-white/50">Ø / Tag</div><div class="text-xl font-extrabold kpi-number" data-target="247">0</div><div class="text-[11px] text-white/50">Spanne 93–398</div></div>
<div class="glass-subtle rounded-2xl p-3 border border-[#7c6cff]/30"><div class="text-[11px] tracking-widest uppercase text-white/60">BD-Anteil</div><div class="text-xl font-extrabold text-[#7c6cff]">35,0 %</div><div class="text-[11px] text-white/50">23 540 von 67 321</div></div>
<div class="glass-subtle rounded-2xl p-3"><div class="text-[11px] tracking-widest uppercase text-white/50">Kern/h</div><div class="text-xl font-extrabold">27,3 / h</div><div class="text-[11px] text-white/50">vs. 4,8 / h BD (5,7×)</div></div></div>
</div></div>
<div class="col-span-12 lg:col-span-4 grid gap-4 lg:gap-6">
<div class="glass rounded-[24px] p-5 sm:p-6 relative overflow-hidden"><div class="absolute inset-0 bg-gradient-to-br from-white/[0.06] to-transparent pointer-events-none"></div>
<div class="flex items-start justify-between gap-4"><div><div class="text-xs tracking-[0.14em] uppercase text-white/50 font-semibold">BD im Überblick</div><h3 class="mt-1 font-semibold leading-tight">Ein Radiologe. 24 h. 7 Tage.</h3></div>
<div class="w-9 h-9 rounded-full bg-white grid place-items-center shrink-0"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#0a1020" stroke-width="1.8"><path d="M12 6v6l4 2"/><circle cx="12" cy="12" r="9"/></svg></div></div>
<div class="mt-4 space-y-2.5 text-xs">
<div class="flex items-center justify-between glass-subtle rounded-full px-3 py-2"><span class="font-medium">Mo–Do</span><span class="font-mono">16:00 → 07:30</span><span class="w-2 h-2 rounded-full bg-[#7c6cff]"></span></div>
<div class="flex items-center justify-between glass-subtle rounded-full px-3 py-2 border border-[#ff3b82]/30"><span class="font-medium">Fr</span><span class="font-mono">16:00 → Sa 09:00</span><span class="w-2 h-2 rounded-full bg-[#ff3b82]"></span></div>
<div class="flex items-center justify-between glass-subtle rounded-full px-3 py-2"><span class="font-medium">Sa</span><span class="font-mono">09:00 → So 09:00</span><span class="w-2 h-2 rounded-full bg-[#0ea5e9]"></span></div>
<div class="flex items-center justify-between glass-subtle rounded-full px-3 py-2"><span class="font-medium">So</span><span class="font-mono">09:00 → Mo 07:30</span><span class="w-2 h-2 rounded-full bg-[#a3ff12]"></span></div>
<div class="flex items-center justify-between rounded-full px-3 py-2 bg-white text-zinc-900 font-semibold"><span>Feiertag</span><span class="font-mono">09:00 → 09:00 / 07:30</span><span class="w-2 h-2 rounded-full bg-zinc-900"></span></div></div>
<p class="mt-3 text-[11px] leading-relaxed text-white/55">Kern = Mo–Fr 07:30–16:00 <span class="text-white">ohne Feiertag</span>. Alles andere = BD. Feiertag 09:00-Verschiebung = Nacht +90 min.</p></div>
<div class="glass rounded-[24px] p-5 sm:p-6"><div class="text-xs tracking-widest uppercase text-white/50 font-semibold">Belastung</div>
<div class="mt-2 flex items-baseline gap-2"><div class="text-[28px] font-black">1 : 5,7</div><div class="text-xs text-white/60">Kern : BD / h</div></div>
<div class="mt-3 h-2.5 rounded-full bg-white/10 overflow-hidden flex"><div class="h-full bg-[#0ea5e9]" style="width:85%"></div><div class="h-full bg-[#7c6cff]" style="width:15%"></div></div>
<div class="mt-2 flex justify-between text-[11px] text-white/60"><span>27,3 / h Kern</span><span>4,8 / h BD</span></div>
<p class="mt-3 text-xs leading-relaxed text-white/65">Ein BD-Arzt stemmt 1/6 der Kern-Rate — aber 48 % CT-Neuro-Anteil = medizinisch überproportional schwer.</p></div>
</div></section>
""")

# Executive Summary
w("""
<section id="executive" class="mt-6"><div class="glass-strong rounded-[24px] p-6 sm:p-8">
<div class="flex flex-wrap items-start justify-between gap-4"><div>
<div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white text-zinc-900 text-xs font-bold">EXECUTIVE SUMMARY</div>
<h2 class="mt-3 font-serif text-[26px] sm:text-[30px] leading-none tracking-tight">Das Wesentliche in 60 Sekunden</h2></div>
<div class="text-xs text-white/55 max-w-[420px] text-right hidden sm:block">Wenn Sie nur eine Seite lesen — lesen Sie diese.</div></div>
<div class="mt-6 grid grid-cols-12 gap-4"><div class="col-span-12 lg:col-span-8">
<div class="grid sm:grid-cols-3 gap-3">
<div class="glass-subtle rounded-2xl p-4"><div class="w-8 h-8 rounded-full bg-[#0ea5e9] grid place-items-center"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M13 2L3 14h8l-1 8 10-12h-8l1-8z"/></svg></div>
<div class="mt-3 text-sm font-semibold leading-tight">ZNA treibt BD zu 66 %</div><p class="mt-1 text-xs leading-relaxed text-white/60">ZNA 13 620 von 20 620 ZNA-Studien im BD. ROE nur 17,8 % BD.</p></div>
<div class="glass-subtle rounded-2xl p-4 border border-[#7c6cff]/30"><div class="w-8 h-8 rounded-full bg-[#7c6cff] grid place-items-center"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></div>
<div class="mt-3 text-sm font-semibold leading-tight">Nacht = CT-Kopf</div><p class="mt-1 text-xs leading-relaxed text-white/60">48 % CT-Neuro, 63 % CT Abdomen im BD — schwere Fälle nachts.</p></div>
<div class="glass-subtle rounded-2xl p-4"><div class="w-8 h-8 rounded-full bg-[#ff3b82] grid place-items-center"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8"><path d="M17 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
<div class="mt-3 text-sm font-semibold leading-tight">Telerad = fast nur BD</div><p class="mt-1 text-xs leading-relaxed text-white/60">Wurzen 99,6 % BD, Torgau 98,3 %, Grimma 96,4 %. 751 Fremdbefunde = Nacht.</p></div></div>
<div class="mt-4 glass-subtle rounded-2xl p-4"><div class="flex items-center gap-2 text-xs font-semibold tracking-wide"><span class="w-2 h-2 rounded-full bg-[#a3ff12]"></span> DREI SOFORT-MASSNAHMEN</div>
<div class="mt-3 grid sm:grid-cols-3 gap-3 text-xs leading-relaxed">
<div><span class="font-semibold text-white">1. ZNA-CT entzerren:</span> <span class="text-white/65">10–11:30 + 18–20 Uhr Peaks entkoppeln — MTA 16–20 Uhr.</span></div>
<div><span class="font-semibold text-white">2. BD-Split freitags:</span> <span class="text-white/65">Fr 16→Sa 09 = 17 h am Stück — geteilt prüfen.</span></div>
<div><span class="font-semibold text-white">3. 07:30-Flut:</span> <span class="text-white/65">07:30 1 310 vs. 07:00 252 (+420 %). Frühdienst 07:15.</span></div></div></div></div>
<div class="col-span-12 lg:col-span-4"><div class="glass rounded-2xl p-4 h-full">
<div class="text-xs font-semibold text-white/80">Top-Risiko (BD)</div><div class="mt-3 space-y-2">
<div class="flex items-center justify-between p-3 rounded-xl bg-[#7c6cff] text-white"><div><div class="text-xs font-bold">Fr 16:00 – Sa 09:00</div><div class="text-[11px] opacity-80">17 h, Mai 41,7 % BD</div></div><div class="text-lg font-black">17h</div></div>
<div class="flex items-center justify-between p-3 rounded-xl glass-subtle"><div><div class="text-xs font-bold">Sa 09:00 – So 09:00</div><div class="text-[11px] text-white/60">133,9 / Sa + 127,7 / So</div></div><div class="text-sm font-bold">24h</div></div>
<div class="flex items-center justify-between p-3 rounded-xl glass-subtle"><div><div class="text-xs font-bold">22:00–06:00</div><div class="text-[11px] text-white/60">5 344 (7,9 %) CT-lastig</div></div><div class="text-sm font-bold">8h</div></div>
<div class="mt-3 p-3 rounded-xl bg-amber-400 text-zinc-900"><div class="text-xs font-bold">⚡ 07:30–08:30 Flut</div><div class="text-[11px] font-medium">3 918 Studien in 60 min — Nacht-Stau.</div></div></div></div></div></div></div></section>
""")

# BD Modell
w("""
<section id="bdmodell" class="mt-6"><div class="flex items-center gap-3"><div class="w-9 h-9 rounded-full bg-white grid place-items-center text-zinc-900 font-bold text-sm">01</div>
<h2 class="font-serif text-2xl tracking-tight">BD-Schichtmodell — visuell entschlüsselt</h2><div class="hidden sm:block h-px flex-1 bg-white/10 ml-4"></div></div>
<div class="mt-4 grid lg:grid-cols-12 gap-4">
<div class="lg:col-span-8 glass rounded-[24px] p-5 sm:p-6">
<div class="flex flex-wrap items-center gap-2 text-xs">
<span class="px-2.5 py-1 rounded-full bg-[#0ea5e9] text-white font-semibold">Kern Mo–Fr 07:30–16:00</span>
<span class="px-2.5 py-1 rounded-full bg-[#7c6cff] text-white font-semibold">BD</span>
<span class="px-2.5 py-1 rounded-full bg-white/10 border border-white/15">Feiertag 09:00</span>
<span class="ml-auto text-white/50">1 606,5 h Kern vs. 4 945,5 h BD</span></div>
<div class="mt-5 space-y-4">
<div><div class="flex items-center justify-between text-xs font-semibold"><span>Mo–Do</span><span class="text-white/50">z. B. Di 07.01. — 370 Studien</span></div>
<div class="mt-2 h-[46px] rounded-full bg-white/5 border border-white/10 p-1.5 flex gap-1">
<div class="w-[28%] rounded-full bg-white/10 grid place-items-center text-[10px] font-mono text-white/70">00:00–07:30 BD</div>
<div class="flex-1 rounded-full bg-[#0ea5e9] grid place-items-center text-[11px] font-bold text-white">07:30–16:00 KERN (8,5 h) · 62–68 %</div>
<div class="w-[30%] rounded-full bg-[#7c6cff] grid place-items-center text-[10px] font-mono text-white">16:00–24:00 BD</div></div></div>
<div><div class="flex items-center justify-between text-xs font-semibold"><span>Freitag</span><span class="text-white/50">Ø 263 — niedrigster WT</span></div>
<div class="mt-2 h-[46px] rounded-full bg-white/5 border border-white/10 p-1.5 flex gap-1">
<div class="flex-[0.32] rounded-full bg-white/10 grid place-items-center text-[10px] font-mono">00:00–07:30 BD</div>
<div class="flex-1 rounded-full bg-[#0ea5e9] grid place-items-center text-[11px] font-bold text-white">07:30–16:00 KERN</div>
<div class="flex-[0.68] rounded-full bg-[#ff3b82] grid place-items-center text-[11px] font-bold text-white shimmer">16:00 → Sa 09:00 · 17 h BD</div></div></div>
<div><div class="flex items-center justify-between text-xs font-semibold"><span>Samstag</span><span class="text-white/50">Ø 133,9 — 100 % BD</span></div>
<div class="mt-2 h-[46px] rounded-full bg-[#7c6cff] border border-white/10 p-1.5 grid place-items-center text-xs font-bold text-white">Sa 09:00 → So 09:00 · 24 h BD</div></div>
<div><div class="flex items-center justify-between text-xs font-semibold"><span>Sonntag</span><span class="text-white/50">Ø 127,7 — 100 % BD</span></div>
<div class="mt-2 h-[46px] rounded-full bg-[#7c6cff]/90 border border-white/10 p-1.5 flex gap-1">
<div class="flex-1 rounded-full bg-[#7c6cff] grid place-items-center text-xs font-bold text-white">So 09:00 → Mo 07:30 · 22,5 h BD</div>
<div class="w-[12%] rounded-full bg-[#0ea5e9]/70 grid place-items-center text-[10px]">Kern</div></div></div>
<div class="p-3 rounded-2xl bg-amber-400 text-zinc-900"><div class="flex items-center justify-between text-xs font-bold"><span>Feiertag Sachsen — 01.01. 119, 03.04. 133, 06.04. 105, 01.05. 161, 14.05. 148, 25.05. 111</span><span>09:00</span></div>
<div class="mt-2 h-[34px] rounded-full bg-zinc-900 text-white grid place-items-center text-xs font-semibold">Feiertag 09:00 → 09:00/07:30 — ganzer Tag BD (777 Studien = 3,3 % BD)</div>
<div class="mt-2 text-[11px] font-medium">Neujahr, Karfreitag, Ostermontag, Tag der Arbeit, Himmelfahrt, Pfingstmontag. 6 Tage, 100 % BD.</div></div>
</div></div>
<div class="lg:col-span-4 space-y-4">
<div class="glass rounded-[24px] p-5"><div class="text-xs tracking-widest uppercase font-semibold text-white/60">Zeitanteile</div>
<div class="mt-3 h-44"><canvas id="timeShareChart"></canvas></div>
<div class="mt-3 grid grid-cols-2 gap-2 text-[11px]">
<div class="glass-subtle rounded-xl p-2.5"><div class="font-bold">1 606,5 h Kern (24,5 %)</div><div class="text-white/60">8,5 h × 189 Tage</div></div>
<div class="glass-subtle rounded-xl p-2.5 border border-[#7c6cff]/30"><div class="font-bold text-[#7c6cff]">4 945,5 h BD (75,5 %)</div><div class="text-white/60">15,5 h/WT + 24 h WE</div></div></div></div>
<div class="glass rounded-[24px] p-5"><div class="text-xs font-bold">09:00-Blindstelle</div>
<p class="mt-2 text-xs leading-relaxed text-white/70">Ostersonntag 05.04. nur 99 Studien — zweitwenigster Tag, obwohl kein Feiertag. Klinik im Feiertagsmodus, Modell nicht. WE-Besetzung reicht, aber 09:00-Regel sollte für „stille“ Feiertage gelten.</p>
<div class="mt-3 flex items-center gap-2 text-[11px]"><span class="px-2 py-1 rounded-full bg-white text-zinc-900 font-semibold">Takeaway</span><span class="text-white/60">Ostersonntag/Pfingstsonntag als Feiertag führen.</span></div></div>
</div></div></section>
""")

# KPI
w("""
<section id="kpi" class="mt-6"><div class="flex items-center gap-3"><div class="w-9 h-9 rounded-full bg-white grid place-items-center text-zinc-900 font-bold text-sm">02</div>
<h2 class="font-serif text-2xl tracking-tight">KPI-Cockpit — 67 321 Studien</h2></div>
<div class="mt-4 grid grid-cols-12 gap-3 sm:gap-4">
<div class="col-span-12 sm:col-span-6 lg:col-span-3 glass rounded-[20px] p-5"><div class="flex items-start justify-between"><div class="text-[11px] tracking-[0.14em] uppercase text-white/50 font-semibold">Gesamt</div><span class="text-[10px] px-2 py-1 rounded-full bg-white text-zinc-900 font-bold">Q1–Q3</span></div>
<div class="mt-2 text-[32px] font-black leading-none kpi-number" data-target="67321">0</div><div class="text-xs text-white/60">Ø 247/Tag · Median 253</div>
<div class="mt-3 flex gap-1.5"><span class="flex-1 h-2 rounded-full bg-[#0ea5e9]"></span><span class="flex-1 h-2 rounded-full bg-[#7c6cff]"></span></div><div class="mt-2 flex justify-between text-[11px] text-white/50"><span>Kern 65,0 %</span><span>BD 35,0 %</span></div></div>
<div class="col-span-12 sm:col-span-6 lg:col-span-3 glass rounded-[20px] p-5 border border-[#7c6cff]/30"><div class="text-[11px] tracking-[0.14em] uppercase text-white/50 font-semibold">BD</div><div class="mt-2 text-[32px] font-black text-[#7c6cff]">23 540</div><div class="text-xs text-white/60">5 344 Nacht 22–06 (22,7 % BD)</div><div class="mt-3 glass-subtle rounded-full px-3 py-2 flex justify-between text-xs"><span>WT-Nacht 12 559</span><span class="font-bold">53,4 %</span></div></div>
<div class="col-span-12 sm:col-span-6 lg:col-span-3 glass rounded-[20px] p-5"><div class="text-[11px] tracking-[0.14em] uppercase text-white/50 font-semibold">Kern</div><div class="mt-2 text-[32px] font-black text-[#0ea5e9]">43 781</div><div class="text-xs text-white/60">1 606,5 h → 27,3 / h</div><div class="mt-3 h-2 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-[#0ea5e9]" style="width:85%"></div></div><div class="mt-1 text-[11px] text-white/50">5,7× > BD</div></div>
<div class="col-span-12 sm:col-span-6 lg:col-span-3 glass rounded-[20px] p-5"><div class="text-[11px] tracking-[0.14em] uppercase text-white/50 font-semibold">Ø Tag</div><div class="mt-2 flex items-baseline gap-2"><span class="text-[32px] font-black">247</span><span class="text-xs px-2 py-1 rounded-full bg-amber-400 text-zinc-900 font-bold">93–398</span></div><div class="text-xs text-white/60">Max 25.02.+04.05. 398 · Min 13.09. 93</div><div class="mt-3 text-[11px] text-white/50">Feiertag Ø 130, Sa 134, So 128</div></div>
<div class="col-span-12 lg:col-span-8 glass rounded-[24px] p-5 sm:p-6"><div class="flex items-center justify-between"><h3 class="font-semibold">Ø / Stunde: Kern vs BD</h3><span class="text-xs px-2.5 py-1 rounded-full bg-white/10 border border-white/10">effektive Stunden</span></div><div class="mt-4 h-[220px]"><canvas id="throughputChart"></canvas></div><p class="mt-3 text-xs text-white/60">Kern 27,3 / h (Team), BD 4,8 / h (Einzel). Schwere/H ist im BD höher — Stückzahl unterschätzt.</p></div>
<div class="col-span-12 lg:col-span-4 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold text-sm">Ø pro Wochentag</h3><div class="mt-4 h-[200px]"><canvas id="weekdayAvgChart"></canvas></div>
<div class="mt-3 space-y-1.5 text-xs">
<div class="flex justify-between glass-subtle rounded-full px-3 py-2"><span><b>Mi</b> stärkster</span><span class="font-mono font-bold">320,8 / Mi</span></div>
<div class="flex justify-between glass-subtle rounded-full px-3 py-2 border border-[#7c6cff]/30"><span><b>Fr</b> schwächster WT</span><span class="font-mono">263,1 (-18 %)</span></div>
<div class="flex justify-between glass-subtle rounded-full px-3 py-2"><span><b>WE</b> 134 / 128</span><span class="font-mono">-58 %</span></div></div></div>
</div></section>
""")

# Temporal
w("""
<section id="temporal" class="mt-6"><div class="flex items-center gap-3"><div class="w-9 h-9 rounded-full bg-white grid place-items-center text-zinc-900 font-bold text-sm">03</div>
<h2 class="font-serif text-2xl tracking-tight">Temporale Signatur — wann PACS glüht</h2></div>
<div class="mt-4 glass rounded-[24px] p-5 sm:p-6"><div class="flex flex-wrap items-start justify-between gap-3"><div><h3 class="font-semibold">24-h-Profil</h3><p class="text-xs text-white/60">07:30 Start, 16:00 Ende. Summiert über 273 Tage.</p></div><div class="flex items-center gap-2 text-xs"><span class="w-3 h-1.5 rounded-full bg-[#0ea5e9]"></span>Kern <span class="w-3 h-1.5 rounded-full bg-[#7c6cff] ml-2"></span>BD</div></div>
<div class="mt-4 h-[320px]"><canvas id="hourlyChart"></canvas></div>
<div class="mt-4 grid sm:grid-cols-3 gap-3 text-xs">
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">Peak 10:00 — 7 748</div><div class="text-white/60">6 765 Kern (87 %).</div></div>
<div class="glass-subtle rounded-xl p-3 border border-amber-400/30"><div class="font-bold">Abriss 15:30→16:00</div><div class="text-white/60">1 502 → 1 349 — BD übernimmt fliegend.</div></div>
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">Tief 05:30 — 116</div><div class="text-white/60">22–06 = 5 344 (7,9 %). Tiefstpunkt, dann Aufwachen.</div></div></div></div>
<div class="mt-4 grid lg:grid-cols-12 gap-4">
<div class="lg:col-span-7 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">Halbstunden-Lupe — 07:30-Flut</h3><p class="text-xs text-white/60">07:00 252 → 07:30 1 310 (+420 %).</p><div class="mt-4 h-[260px]"><canvas id="slotChart"></canvas></div>
<div class="mt-3 p-3 rounded-xl bg-amber-400 text-zinc-900 text-xs"><b>Erkenntnis:</b> 07:30 = Warteschlange aus 15,5 h BD. Frühdienst 07:15 / Staffel halbiert.</div></div>
<div class="lg:col-span-5 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">10-Minuten 07–09</h3><div class="mt-4 h-[260px]"><canvas id="detailChart"></canvas></div>
<div class="mt-3 space-y-2 text-xs"><div class="flex justify-between glass-subtle rounded-full px-3 py-2"><span>07:40</span><span class="font-mono font-bold">474</span><span class="text-white/50">erster Volllast</span></div>
<div class="flex justify-between glass-subtle rounded-full px-3 py-2 border border-[#0ea5e9]/30"><span>08:50</span><span class="font-mono font-bold">1 166</span><span class="text-white/50">Max Mikro</span></div></div>
<p class="mt-3 text-xs text-white/60">07:30–09:30 = 39 % Tages-Stau — Stufe, keine Kurve.</p></div></div>
<div class="mt-4 glass rounded-[24px] p-5 sm:p-6"><div class="flex flex-wrap items-start justify-between gap-3"><h3 class="font-semibold">Wochentag × Stunde — Heatmap</h3><span class="text-xs px-3 py-1 rounded-full glass-subtle">Max 1 659 (Mi 10) · Min 21 (Mo 03)</span></div>
<div class="mt-4 overflow-x-auto"><div id="heatmap" class="min-w-[720px]"></div></div>
<div class="mt-4 grid sm:grid-cols-3 gap-3 text-xs">
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">Mi-Spitze</div><div class="text-white/60">Mi 10 1 659, 11 1 433 = OP/Ambulanz.</div></div>
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">Fr-Loch</div><div class="text-white/60">Fr 15 446 vs Mi 603 — Freitag leer gefahren.</div></div>
<div class="glass-subtle rounded-xl p-3 border border-[#7c6cff]/30"><div class="font-bold">WE-Grundrauschen</div><div class="text-white/60">Sa/So 154–493 — Notfall, CT-lastig.</div></div></div></div>
<div class="mt-4 grid lg:grid-cols-12 gap-4">
<div class="lg:col-span-5 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">Wochentag-Bilanz</h3><div class="mt-4 h-[280px]"><canvas id="weekdayChart"></canvas></div><p class="mt-3 text-xs text-white/60">Mo 12 063, Di 11 237, Mi 12 512, Do 11 044, Fr 10 261. Mi +9 % Ø. BD: Mo 23 %, Do 26,2 %.</p></div>
<div class="lg:col-span-7 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">Monat + Woche</h3><div class="mt-4 h-[280px]"><canvas id="monthChart"></canvas></div>
<div class="mt-3 grid grid-cols-3 gap-2 text-xs"><div class="glass-subtle rounded-xl p-2.5 text-center"><div class="font-bold">Feb 7 290</div><div class="text-white/60">32,6 % BD</div></div><div class="glass-subtle rounded-xl p-2.5 text-center border border-[#ff3b82]/30"><div class="font-bold text-[#ff3b82]">Mai 7 629 · 41,7 % BD</div><div class="text-white/60">Feiertag-Monat</div></div><div class="glass-subtle rounded-xl p-2.5 text-center"><div class="font-bold">Aug 6 850</div><div class="text-white/60">Ferien -8 %</div></div></div>
<div class="mt-4 h-[180px]"><canvas id="weeklyChart"></canvas></div><p class="mt-2 text-xs text-white/55">KW 19 1 952, KW 02 1 921 Max; KW 01 613, KW 40 821 Min. Ferien 8 % Dämpfung — Notfall bleibt.</p></div></div>
<div class="mt-4 grid lg:grid-cols-12 gap-4">
<div class="lg:col-span-7 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">Tages-Outlier (273 Tage)</h3><div class="mt-4 h-[220px]"><canvas id="dailyChart"></canvas></div>
<div class="mt-3 flex flex-wrap gap-2 text-xs"><span class="px-2.5 py-1 rounded-full bg-emerald-500 text-white font-semibold">Max 398: 25.02.+04.05.</span><span class="px-2.5 py-1 rounded-full bg-rose-500 text-white font-semibold">Min 93: 13.09. Sa</span><span class="px-2.5 py-1 rounded-full glass-subtle">Ø 247 · σ 38</span></div><p class="mt-3 text-xs text-white/60">Top10 Mo–Mi, Flop10 Sa/So/Feiertag — planbar vs notfallgetrieben.</p></div>
<div class="lg:col-span-5 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">Feiertage — 777 = 3,3 % BD</h3><div class="mt-4 h-[220px]"><canvas id="holidayChart"></canvas></div>
<div class="mt-3 space-y-1.5 text-xs"><div class="flex justify-between glass-subtle rounded-full px-3 py-2"><span>Neujahr 01.01.</span><span class="font-mono">119</span></div><div class="flex justify-between glass-subtle rounded-full px-3 py-2"><span>Karfreitag 03.04.</span><span class="font-mono">133</span></div><div class="flex justify-between glass-subtle rounded-full px-3 py-2 border border-amber-400/30"><span>Ostersonntag 05.04.*</span><span class="font-mono">99</span><span class="text-amber-300">kein Gesetz, aber Feiertag-Verhalten</span></div><div class="flex justify-between glass-subtle rounded-full px-3 py-2"><span>Ostermontag 06.04.</span><span class="font-mono">105</span></div><div class="flex justify-between glass-subtle rounded-full px-3 py-2"><span>Tag d. Arbeit 01.05.</span><span class="font-mono">161</span></div><div class="flex justify-between glass-subtle rounded-full px-3 py-2"><span>Himmelfahrt 14.05.</span><span class="font-mono">148</span></div></div><p class="mt-3 text-xs text-white/60">Ø 130/Feiertag vs 247 normal (-48 %). 09:00 = +90 min Nacht.</p></div></div>
<div class="mt-4 glass rounded-[24px] p-5 sm:p-6"><div class="flex items-center gap-2"><h3 class="font-semibold">ZNA vs ROE — zwei Welten</h3><span class="ml-auto text-xs px-2.5 py-1 rounded-full bg-[#7c6cff] text-white font-semibold">ZNA 66,1 % BD</span><span class="text-xs px-2.5 py-1 rounded-full bg-[#0ea5e9] text-white font-semibold">ROE 17,8 %</span></div><div class="mt-4 h-[300px]"><canvas id="znaRoeChart"></canvas></div>
<div class="mt-4 grid sm:grid-cols-2 gap-3 text-xs leading-relaxed">
<div class="glass-subtle rounded-xl p-3"><b>ZNA 20 620:</b> <span class="text-white/70">22–02 >500/h, 06 296, Peak 14 1 457, 16 noch 1 288 BD. BD = ZNA.</span></div>
<div class="glass-subtle rounded-xl p-3"><b>ROE 15 528:</b> <span class="text-white/70">08 1 326 → 10 2 746 Peak → 14 1 019 → 15 447 → 16 328 → 23 63. Rein Kern.</span></div></div></div>
</section>
""")

w("""
<section id="modal" class="mt-6"><div class="flex items-center gap-3"><div class="w-9 h-9 rounded-full bg-white grid place-items-center text-zinc-900 font-bold text-sm">04</div><h2 class="font-serif text-2xl tracking-tight">Modalitäten — was wann?</h2></div>
<div class="mt-4 grid lg:grid-cols-12 gap-4"><div class="lg:col-span-5 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">Mix (67 321)</h3><div class="mt-4 h-[280px] flex items-center justify-center"><canvas id="modalityDoughnut"></canvas></div>
<div class="mt-4 grid grid-cols-2 gap-2 text-xs">
<div class="glass-subtle rounded-xl p-2.5"><div class="font-bold">Röntgen 60,2 %</div><div class="text-white/60">40 546</div></div>
<div class="glass-subtle rounded-xl p-2.5"><div class="font-bold">CT Neuro 8,9 %</div><div class="text-white/60">5 975 · 48,2 % BD</div></div>
<div class="glass-subtle rounded-xl p-2.5"><div class="font-bold">MRT Kopf 2,7 %</div><div class="text-white/60">1 797 · 93 % Kern</div></div>
<div class="glass-subtle rounded-xl p-2.5 border border-[#7c6cff]/30"><div class="font-bold text-[#7c6cff]">CT Body 3,2 %</div><div class="text-white/60">2 151 · 20,6 % BD</div></div></div></div>
<div class="lg:col-span-7 glass rounded-[24px] p-5 sm:p-6"><div class="flex items-center justify-between"><h3 class="font-semibold">BD-Affinität</h3><span class="text-xs px-2 py-1 rounded-full bg-amber-400 text-zinc-900 font-bold">>30 % = BD-lastig</span></div><div class="mt-4 h-[340px]"><canvas id="modalityBdChart"></canvas></div>
<div class="mt-4 p-3 rounded-xl glass-subtle text-xs"><b>Lesart:</b> <span class="text-white/70">CT Abd/Becken 63,1 % BD — Akutes Abdomen nachts. CT Neuro 48,2 % BD — Stroke. Rö 42,9 % BD — Trauma. Mammo 0 % BD — elektiv. Nuklear 0,1 % — Termin.</span></div></div></div>
<div class="mt-4 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">Top-20 Untersuchungen — Kern vs BD</h3><div class="mt-4 h-[520px]"><canvas id="studienChart"></canvas></div>
<div class="mt-4 grid sm:grid-cols-3 gap-3 text-xs">
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">Rö Thorax 3 711 + Bett 1 298</div><div class="text-white/60">7 365 gesamt — 16–22 % BD.</div></div>
<div class="glass-subtle rounded-xl p-3 border border-rose-400/30"><div class="font-bold">CCT Spirale 1 043 (58 % BD)</div><div class="text-white/60">ICB-Ausschluss Xarelto — BD-Klassiker.</div></div>
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">Fremd 751 (99,7 % BD)</div><div class="text-white/60">Wurzen 300 + Grimma 200 CT Schädel.</div></div></div>
<div class="mt-3 p-3 rounded-xl bg-white text-zinc-900 text-xs"><b>Detail:</b> Becken 603 (34 % BD), Hand li 317 (53 % BD), Thorax_Abd venös 289 (0 % BD — elektiv), Kopf Stroke 271 (62 % BD), SOKI 309 (0 % BD).</div></div></section>
""")

w("""
<section id="institution" class="mt-6"><div class="flex items-center gap-3"><div class="w-9 h-9 rounded-full bg-white grid place-items-center text-zinc-900 font-bold text-sm">05</div><h2 class="font-serif text-2xl tracking-tight">Institutionen — wer schickt wann?</h2></div>
<div class="mt-4 glass rounded-[24px] p-5 sm:p-6"><div class="flex flex-wrap items-start justify-between gap-3"><h3 class="font-semibold">Volumen & BD-Quote</h3><span class="text-xs px-3 py-1 rounded-full bg-white text-zinc-900 font-bold">St. Georg 85,5 %</span></div><div class="mt-4 h-[360px]"><canvas id="institutionChart"></canvas></div>
<div class="mt-4 grid lg:grid-cols-3 gap-3 text-xs">
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">St. Georg 57 563 (35,9 % BD)</div><div class="text-white/60">87,7 % aller BD — BD lebt hier.</div></div>
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">Bad Düben 4 908 (23,1 % BD)</div><div class="text-white/60">Eigene Radiologie tags.</div></div>
<div class="glass-subtle rounded-xl p-3 border border-[#7c6cff]/30"><div class="font-bold text-[#7c6cff]">Wurzen 464 (99,6 % BD)</div><div class="text-white/60">Telerad pur. Torgau 98,3 %, Grimma 96,4 %.</div></div></div>
<div class="mt-3 p-3 rounded-xl bg-[#0ea5e9] text-white text-xs"><b>Erkenntnis:</b> Externe = Nacht-Telerad. Tags selbst, nachts Leipzig. Erklärt CT-Neuro-BD.</div></div></section>
<section id="abteilung" class="mt-6"><div class="flex items-center gap-3"><div class="w-9 h-9 rounded-full bg-white grid place-items-center text-zinc-900 font-bold text-sm">06</div><h2 class="font-serif text-2xl tracking-tight">Abteilungen — wer braucht BD?</h2></div>
<div class="mt-4 glass rounded-[24px] p-5 sm:p-6"><div class="flex flex-wrap items-center justify-between gap-3"><h3 class="font-semibold">Top-15 Abteilungen</h3><span class="text-xs px-3 py-1 rounded-full glass-subtle">Balken = Volumen · Farbe = BD</span></div><div class="mt-4 h-[480px]"><canvas id="abteilungChart"></canvas></div>
<div class="mt-4 grid md:grid-cols-3 gap-3 text-xs">
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">ZNA 20 620 (66,1 % BD)</div><div class="text-white/60">57,9 % aller BD — ohne ZNA kein BD.</div></div>
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">ROE 15 528 (17,8 % BD)</div><div class="text-white/60">Planbar, Kern.</div></div>
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">UCH 6 748 (32,1 % BD)</div><div class="text-white/60">Trauma 24 h, aber OP senkt BD.</div></div></div>
<div class="mt-3 grid md:grid-cols-4 gap-2 text-xs">
<div class="glass-subtle rounded-xl p-2.5 text-center"><div class="font-bold">ABZ 1 492 (1,4 % BD)</div><div class="text-white/60">Ambulanz elektiv</div></div>
<div class="glass-subtle rounded-xl p-2.5 text-center"><div class="font-bold">PNEU 1 503 (11,2 %)</div><div class="text-white/60">Station</div></div>
<div class="glass-subtle rounded-xl p-2.5 text-center"><div class="font-bold">KCH 1 307 (34,4 %)</div><div class="text-white/60">Kinder-Notfall</div></div>
<div class="glass-subtle rounded-xl p-2.5 text-center border border-[#7c6cff]/30"><div class="font-bold text-[#7c6cff]">KAIM 2 830 (31,2 %)</div><div class="text-white/60">ITS-lastig</div></div></div></div></section>
""")

w("""
<section id="personen" class="mt-6"><div class="flex items-center gap-3"><div class="w-9 h-9 rounded-full bg-white grid place-items-center text-zinc-900 font-bold text-sm">07</div><h2 class="font-serif text-2xl tracking-tight">Radiolog:innen — Freigabe im Schichtspiegel</h2></div>
<div class="mt-4 glass rounded-[24px] p-5 sm:p-6"><div class="flex flex-wrap items-start justify-between gap-3"><div><h3 class="font-semibold">Freigabe je Ärzt:in — Kern vs BD</h3><p class="text-xs text-white/60">19 Ärzt:innen. 14,8 % Verfasser ≠ Freigebender.</p></div><span class="text-xs px-3 py-1 rounded-full bg-amber-400 text-zinc-900 font-bold">Bettina Dalitz 52 % BD — Top BD-Quote</span></div>
<div class="mt-4 h-[420px]"><canvas id="freigebenderChart"></canvas></div>
<div class="mt-4 grid sm:grid-cols-3 gap-3 text-xs">
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">MLURZ 11 800 (35,1 % BD)</div><div class="text-white/60">4 142 BD = 17,6 % aller BD.</div></div>
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">Bettina Dalitz 6 412 (52 % BD)</div><div class="text-white/60">3 336 BD — Nacht-Schwerpunkt.</div></div>
<div class="glass-subtle rounded-xl p-3 border border-rose-400/30"><div class="font-bold">RSEBASTIAN 6 802 (12 % BD)</div><div class="text-white/60">88 % Kern — kaum Nacht.</div></div></div>
<div class="mt-3 p-3 rounded-xl glass-subtle text-xs"><b>Auffällig:</b> <span class="text-white/70">ENICKEL 904 (0 % BD), TKLUGE 605 (0 % BD), ASCHAEFER 2 638 (0,5 % BD) — reine Kern-Ärzt:innen. BD-Kollektiv kleiner als Liste.</span></div>
<div class="mt-3 grid sm:grid-cols-2 gap-3 text-xs">
<div class="glass rounded-xl p-3"><div class="font-bold">Verfasser ≠ Freigebender 9 952 (14,8 %)</div><div class="text-white/60">MLURZ 2 089, JUBECKER 1 879, Polednia 1 867 — Supervision Kern, BD 0 %.</div></div>
<div class="glass rounded-xl p-3"><div class="font-bold">Implikation</div><div class="text-white/60">BD isoliert — Vier-Augen fehlt nachts bei CT-Neuro. Second-Read prüfen.</div></div></div></div></section>
<section id="telerad" class="mt-6"><div class="flex items-center gap-3"><div class="w-9 h-9 rounded-full bg-white grid place-items-center text-zinc-900 font-bold text-sm">08</div><h2 class="font-serif text-2xl tracking-tight">Teleradiologie — Nacht = extern</h2></div>
<div class="mt-4 grid lg:grid-cols-12 gap-4"><div class="lg:col-span-7 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">Fremdbefunde 751 — 100 % BD</h3>
<div class="mt-3 grid grid-cols-3 gap-2 text-xs"><div class="glass-subtle rounded-xl p-3 text-center"><div class="text-[11px] text-white/50">CT Schädel Wurzen</div><div class="text-xl font-black">300</div><div class="text-[11px] text-white/60">99,7 % BD</div></div><div class="glass-subtle rounded-xl p-3 text-center"><div class="text-[11px] text-white/50">CT Schädel Grimma</div><div class="text-xl font-black">200</div><div class="text-[11px] text-white/60">100 % BD</div></div><div class="glass-subtle rounded-xl p-3 text-center border border-[#7c6cff]/30"><div class="text-[11px] text-white/50">Rest</div><div class="text-xl font-black">251</div><div class="text-[11px] text-white/60">Abd/Wirbel/Thorax</div></div></div>
<div class="mt-4 p-3 rounded-xl bg-[#7c6cff] text-white text-xs"><b>Befund:</b> Wurzen 430 + Grimma 296 = 726/751 (96,7 %). Tags eigen, nachts Leipzig.</div>
<div class="mt-4"><div class="text-xs font-semibold">Institutionale BD-Quote</div><div class="mt-3 space-y-2">
<div class="flex items-center gap-3"><span class="w-32 text-xs font-mono">Wurzen</span><div class="flex-1 h-3 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-[#7c6cff]" style="width:99.6%"></div></div><span class="text-xs font-bold">99,6 %</span></div>
<div class="flex items-center gap-3"><span class="w-32 text-xs font-mono">Torgau</span><div class="flex-1 h-3 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-[#7c6cff]" style="width:98.3%"></div></div><span class="text-xs font-bold">98,3 %</span></div>
<div class="flex items-center gap-3"><span class="w-32 text-xs font-mono">Grimma</span><div class="flex-1 h-3 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-[#7c6cff]" style="width:96.4%"></div></div><span class="text-xs font-bold">96,4 %</span></div>
<div class="flex items-center gap-3"><span class="w-32 text-xs font-mono">St. Georg</span><div class="flex-1 h-3 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-[#0ea5e9]" style="width:35.9%"></div></div><span class="text-xs">35,9 %</span></div>
<div class="flex items-center gap-3"><span class="w-32 text-xs font-mono">Bad Düben</span><div class="flex-1 h-3 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-white/40" style="width:23.1%"></div></div><span class="text-xs">23,1 %</span></div></div></div></div>
<div class="lg:col-span-5 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">Was das heißt</h3>
<div class="mt-3 space-y-3 text-xs leading-relaxed">
<div class="glass-subtle rounded-xl p-3"><b>1. Schwere-Shift:</b> <span class="text-white/70">Extern = CT Schädel/HWS + Abdomen — 69 % + 63 % BD-Quote. BD trägt Fremd-Notfälle.</span></div>
<div class="glass-subtle rounded-xl p-3"><b>2. Volatilität:</b> <span class="text-white/70">1,8 % gesamt, 3,9 % BD. Sa +40 % extern — WE = Telerad-Spitze.</span></div>
<div class="glass-subtle rounded-xl p-3"><b>3. Ökonomie:</b> <span class="text-white/70">751/273 = 2,75/Tag BD. 15 min/Befund = 41 min/Tag für Externe.</span></div>
<div class="p-3 rounded-xl bg-amber-400 text-zinc-900"><b>Empfehlung:</b> SLA 22–06 leistungsbezogen, Second-Read CT-Neuro extern nächsten Tag 08:00.</div></div></div></div></section>
""")

w("""
<section id="workflow" class="mt-6"><div class="flex items-center gap-3"><div class="w-9 h-9 rounded-full bg-white grid place-items-center text-zinc-900 font-bold text-sm">09</div><h2 class="font-serif text-2xl tracking-tight">Durchsatz & Workflow</h2></div>
<div class="mt-4 grid lg:grid-cols-12 gap-4">
<div class="lg:col-span-6 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">Stunden-Produktivität — 5,7×</h3>
<div class="mt-4 p-4 rounded-2xl bg-white text-zinc-900"><div class="flex items-baseline justify-between"><div><div class="text-[11px] tracking-widest uppercase font-bold text-zinc-500">Kern</div><div class="text-[26px] font-black">27,3 <span class="text-sm">/ h</span></div><div class="text-xs text-zinc-600">1 606,5 h · 43 781</div></div><div class="text-right"><div class="text-[11px] tracking-widest uppercase font-bold text-zinc-500">BD</div><div class="text-[26px] font-black text-[#7c6cff]">4,8 <span class="text-sm">/ h</span></div><div class="text-xs text-zinc-600">4 945,5 h · 23 540</div></div></div>
<div class="mt-4 h-3 rounded-full bg-zinc-100 flex overflow-hidden"><div class="bg-[#0ea5e9] h-full" style="width:85%"></div><div class="bg-[#7c6cff] h-full" style="width:15%"></div></div><div class="mt-2 flex justify-between text-[11px] font-semibold text-zinc-500"><span>Team 3–5 + MTAs</span><span>Einzel</span></div></div>
<div class="mt-4 grid grid-cols-2 gap-3 text-xs"><div class="glass-subtle rounded-xl p-3"><div class="font-bold">Kern-Peak 08–11:30</div><div class="text-white/60">Ø 1 800/h. 3 Ärzte + 4 MTAs + Sono. Mammo 0 % BD.</div></div><div class="glass-subtle rounded-xl p-3"><div class="font-bold">BD-Peak 22 + 16:30</div><div class="text-white/60">22 Trauma, 16:30 ZNA. 3× Nacht-Ø.</div></div></div><p class="mt-3 text-xs text-white/60">5,7× ist Struktur: Team vs Serial. CT-Schwere/h im BD höher.</p></div>
<div class="lg:col-span-6 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">BD-Kurve / h</h3><div class="mt-4 h-[260px]"><canvas id="loadCurveChart"></canvas></div><div class="mt-3 p-3 rounded-xl glass-subtle text-xs"><b>Nacht 22–06 = 5 344 (7,9 %).</b> <span class="text-white/70">2 268 Früh 00–07:30 (42 % Nacht). Alle 34 min Studie, 72 min CT.</span></div><div class="mt-3 flex gap-2 text-xs"><span class="px-2.5 py-1 rounded-full bg-[#7c6cff] text-white font-semibold">Max 5 / min</span><span class="px-2.5 py-1 rounded-full glass-subtle">Ø 0,08 / min Nacht</span></div></div></div>
<div class="mt-4 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">24-h-Beispiel Mittwoch</h3><div class="mt-4 grid grid-cols-12 gap-1 text-[11px]"><div class="col-span-3 glass-subtle rounded-xl p-3 text-center"><div class="font-bold">00–07:30 BD Früh</div><div class="text-white/60">22 % Nacht</div><div class="mt-1 font-mono font-bold">8,3 / h</div></div><div class="col-span-5 bg-[#0ea5e9] rounded-xl p-3 text-center text-white"><div class="font-bold">07:30–16:00 KERN</div><div class="opacity-80">8,5 h · 68 %</div><div class="mt-1 font-mono font-bold">27,3 / h</div></div><div class="col-span-4 bg-[#7c6cff] rounded-xl p-3 text-center text-white"><div class="font-bold">16:00–24:00 BD Spät</div><div class="opacity-80">8 h · 32 %</div><div class="mt-1 font-mono font-bold">7,1 / h</div></div></div>
<div class="mt-4 grid sm:grid-cols-3 gap-3 text-xs"><div class="glass-subtle rounded-xl p-3"><div class="font-bold">Früh 00–07:30 (2 268)</div><div class="text-white/60">58 % CT — jede 2. CT.</div></div><div class="glass-subtle rounded-xl p-3"><div class="font-bold">Spät 16–24 (10 291)</div><div class="text-white/60">ZNA 18–20 Peak. Rö+CT Kopf.</div></div><div class="glass-subtle rounded-xl p-3 border border-amber-400/30"><div class="font-bold">Fr 17 h am Stück</div><div class="text-white/60">16→09 = längste Schicht.</div></div></div></div></section>
<section id="anomalien" class="mt-6"><div class="flex items-center gap-3"><div class="w-9 h-9 rounded-full bg-white grid place-items-center text-zinc-900 font-bold text-sm">10</div><h2 class="font-serif text-2xl tracking-tight">Anomalien & Datenqualität — die kleinen Details</h2></div>
<div class="mt-4 grid lg:grid-cols-12 gap-4">
<div class="lg:col-span-6 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">4 Datenbefunde</h3><div class="mt-4 space-y-2.5">
<div class="glass-subtle rounded-xl p-3 flex gap-3"><span class="w-7 h-7 rounded-full bg-amber-400 grid place-items-center text-zinc-900 font-bold text-xs">!</span><div><div class="text-xs font-bold">41,6 % ohne Arzt (28 047)</div><div class="text-xs text-white/60">ROE + ZNA leer — keine Rückfrage im BD.</div></div></div>
<div class="glass-subtle rounded-xl p-3 flex gap-3"><span class="w-7 h-7 rounded-full bg-rose-500 grid place-items-center text-white font-bold text-xs">!</span><div><div class="text-xs font-bold">BAD DUEBEN (53) vs DÜBEN (4 908)</div><div class="text-xs text-white/60">Typo ohne Umlaut = eigene Kennzahl.</div></div></div>
<div class="glass-subtle rounded-xl p-3 flex gap-3"><span class="w-7 h-7 rounded-full bg-[#0ea5e9] grid place-items-center text-white font-bold text-xs">i</span><div><div class="text-xs font-bold">Befund gespeichert = Freitext, kein Timestamp</div><div class="text-xs text-white/60">Keine Durchlaufzeit messbar.</div></div></div>
<div class="glass-subtle rounded-xl p-3 flex gap-3"><span class="w-7 h-7 rounded-full bg-[#7c6cff] grid place-items-center text-white font-bold text-xs">i</span><div><div class="text-xs font-bold">Verfasser ≠ Freigebender 14,8 % (9 952)</div><div class="text-xs text-white/60">Supervision Kern, BD 0 % — Vier-Augen fehlt nachts.</div></div></div></div></div>
<div class="lg:col-span-6 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">Versteckte Muster</h3><div class="mt-4 space-y-3 text-xs leading-relaxed">
<div class="glass-subtle rounded-xl p-3"><b>Ostersonntag 05.04. 99</b> <span class="text-white/70">Zweitwenigster Tag, kein Feiertag in Sachsen. Klinik im Feiertagsmodus, Modell nicht — Unterbesetzung im Kopf.</span></div>
<div class="glass-subtle rounded-xl p-3"><b>Mai 41,7 % BD</b> <span class="text-white/70">Höchster BD-Monat — 01.05., 14.05., 25.05. + Ferien-Sog. Juni 34,4 %.</span></div>
<div class="glass-subtle rounded-xl p-3"><b>Fr 263 vs Mi 321 (-18 %)</b> <span class="text-white/70">Fr leer gefahren, aber 17 h Schicht + WE dran — Erholung frisst Entlastung.</span></div>
<div class="glass-subtle rounded-xl p-3 border border-amber-400/30"><b>07:30 Stufe</b> <span class="text-white/70">07:00 252 → 07:30 1 310 — keine Rampe. 07:30–08:30 = Nacht-Stau, nicht Tagesgeschäft.</span></div></div></div></div>
<div class="mt-4 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">1-%-Ecken mit 100 % Ärger</h3><div class="mt-4 grid md:grid-cols-3 gap-3 text-xs">
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">„Bettina, Dalitz“ Format</div><div class="text-white/60">Komma+Leer inkonsistent (MLURZ vs Name). Trim/Upper nötig.</div></div>
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">5 / min — Artefakt</div><div class="text-white/60">04.05. 09:41 etc. PACS-Burst, nicht 5× Akquisition.</div></div>
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">MEDICLIN 969 (0,4 % BD)</div><div class="text-white/60">Tags eigen, nachts 4/273 — kein Telerad-Kunde. Wurzen/Grimma schon.</div></div></div>
<div class="mt-3 grid md:grid-cols-2 gap-3 text-xs"><div class="glass-subtle rounded-xl p-3"><div class="font-bold">D-Arzt Böhme 3 508 (1 227 BD)</div><div class="text-white/60">BG-Fälle 35 % nachts — Nachtzuschlag prüfen.</div></div><div class="glass-subtle rounded-xl p-3"><div class="font-bold">ITS-Stroke 324 BD</div><div class="text-white/60">324/3 361 ZNA-CT Kopf = Stroke-Unit im BD.</div></div></div></div></section>
""")

w("""
<section class="mt-6"><div class="flex items-center gap-3"><div class="w-9 h-9 rounded-full bg-white grid place-items-center text-zinc-900 font-bold text-sm">11</div><h2 class="font-serif text-2xl tracking-tight">Zusammenhänge — wer mit wem</h2></div>
<div class="mt-4 grid lg:grid-cols-12 gap-4"><div class="lg:col-span-8 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">Korrelations-Matrix</h3>
<div class="mt-4 grid grid-cols-3 gap-3 text-xs">
<div class="glass-subtle rounded-xl p-3 text-center"><div class="font-bold">ZNA ↔ CT Neuro</div><div class="text-white/60 mt-1">62,4 % ZNA-CT im BD.</div><div class="mt-2 h-2 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-[#7c6cff]" style="width:62%"></div></div></div>
<div class="glass-subtle rounded-xl p-3 text-center"><div class="font-bold">ROE ↔ Mammo/Nuk</div><div class="text-white/60 mt-1">0–0,2 % BD — planbar.</div><div class="mt-2 h-2 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-[#0ea5e9]" style="width:8%"></div></div></div>
<div class="glass-subtle rounded-xl p-3 text-center border border-[#7c6cff]/30"><div class="font-bold">Extern ↔ BD</div><div class="text-white/60 mt-1">96–99 % BD.</div><div class="mt-2 h-2 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-[#7c6cff]" style="width:98%"></div></div></div>
<div class="glass-subtle rounded-xl p-3 text-center"><div class="font-bold">UCH ↔ Rö Skelett</div><div class="text-white/60 mt-1">OSG 74,9 % BD.</div><div class="h-2 rounded-full bg-white/10"><div class="h-full bg-[#7c6cff]" style="width:70%"></div></div></div>
<div class="glass-subtle rounded-xl p-3 text-center"><div class="font-bold">Nacht ↔ Schwere</div><div class="text-white/60 mt-1">CT 41 % vs 12 % Kern (3,4×).</div><div class="mt-2 h-2 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-amber-400" style="width:68%"></div></div></div>
<div class="glass-subtle rounded-xl p-3 text-center"><div class="font-bold">Ferien ↔ Dämpfung</div><div class="text-white/60 mt-1">-8 % KW28–31, ZNA stabil.</div><div class="mt-2 h-2 rounded-full bg-white/10 overflow-hidden"><div class="h-full bg-white/40" style="width:22%"></div></div></div></div>
<div class="mt-4 p-3 rounded-xl glass-subtle text-xs"><b>Stärkste:</b> <span class="text-white/70">ZNA+CT Neuro+Nacht+Extern = 68 % BD. Wer BD entlastet, ändert ZNA-CT, nicht Mammo.</span></div></div>
<div class="lg:col-span-4 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">3 unintuitive Schlüsse</h3><div class="mt-4 space-y-3 text-xs leading-relaxed">
<div class="p-3 rounded-xl bg-white text-zinc-900"><div class="font-bold">1. Weniger = mehr Risiko</div><div class="mt-1">35 % Volumen, 48 % CT Neuro → 1,4× schwerer pro Studie.</div></div>
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">2. Fr ist leise, aber schwer</div><div class="text-white/60">Wenig Volumen, aber 17 h + WE — Erholung frisst Entlastung.</div></div>
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">3. Telerad finanziert Nacht?</div><div class="text-white/60">2,75/Tag = 34 min/Tag Telerad-Arbeit — Bereitschaft, nicht Leistung.</div></div></div></div></div></section>
<section id="empfehlungen" class="mt-6"><div class="flex items-center gap-3"><div class="w-9 h-9 rounded-full bg-[#a3ff12] grid place-items-center text-zinc-900 font-bold text-sm">12</div><h2 class="font-serif text-2xl tracking-tight">Konsequenzen — was zu tun ist</h2><span class="hidden sm:inline-flex text-xs px-3 py-1 rounded-full bg-[#a3ff12] text-zinc-900 font-bold">Priorisiert · machbar</span></div>
<div class="mt-4 grid lg:grid-cols-12 gap-4"><div class="lg:col-span-8 grid sm:grid-cols-2 gap-4">
<div class="glass rounded-[20px] p-5 border border-[#0ea5e9]/30"><div class="flex items-center gap-2"><span class="w-7 h-7 rounded-full bg-[#0ea5e9] grid place-items-center text-white font-bold text-xs">1</span><span class="text-xs font-bold uppercase text-white/60">Sofort · 0 €</span></div><div class="mt-3 font-semibold">07:15-Frühdienst + Staffel</div><p class="mt-2 text-xs text-white/65">1 310 in 07:30 = Stau. 07:15 + 07:45 halbiert. KPI: 07:30 <800 in 4 Wo.</p><div class="mt-3 flex gap-2"><span class="text-[11px] px-2 py-1 rounded-full bg-white text-zinc-900 font-semibold">Eigner Chefarzt</span><span class="text-[11px] px-2 py-1 rounded-full glass-subtle">KPI <800</span></div></div>
<div class="glass rounded-[20px] p-5 border border-[#7c6cff]/30"><div class="flex items-center gap-2"><span class="w-7 h-7 rounded-full bg-[#7c6cff] grid place-items-center text-white font-bold text-xs">2</span><span class="text-xs font-bold uppercase text-white/60">Sofort</span></div><div class="mt-3 font-semibold">Fr-BD splitten 16–24 + 00–09</div><p class="mt-2 text-xs text-white/65">17 h Fr→Sa längste Schicht, Mai 41,7 % BD. Split reduziert Fehler.</p><div class="mt-3 flex gap-2"><span class="text-[11px] px-2 py-1 rounded-full bg-white text-zinc-900 font-semibold">Dienstplan</span><span class="text-[11px] px-2 py-1 rounded-full glass-subtle">Fr→Sa Zeit</span></div></div>
<div class="glass rounded-[20px] p-5"><div class="flex items-center gap-2"><span class="w-7 h-7 rounded-full bg-[#ff3b82] grid place-items-center text-white font-bold text-xs">3</span><span class="text-xs font-bold uppercase text-white/60">Q1 2027</span></div><div class="mt-3 font-semibold">ZNA-CT Fast-Track 16–20</div><p class="mt-2 text-xs text-white/65">ZNA 66 % + CT 48 % BD = 18–20 Engpass. MTA 16–20 + 2 Slots/h = -12 % BD.</p><div class="mt-3 flex gap-2"><span class="text-[11px] px-2 py-1 rounded-full bg-white text-zinc-900 font-semibold">ZNA+Radiologie</span><span class="text-[11px] px-2 py-1 rounded-full glass-subtle">Door→CT <25m</span></div></div>
<div class="glass rounded-[20px] p-5"><div class="flex items-center gap-2"><span class="w-7 h-7 rounded-full bg-amber-400 grid place-items-center text-zinc-900 font-bold text-xs">4</span><span class="text-xs font-bold uppercase text-white/60">Q1 2027</span></div><div class="mt-3 font-semibold">Telerad-SLA + Second-Read</div><p class="mt-2 text-xs text-white/65">751 extern ohne Zweit. 00–06 leistungsbezogen, CT Neuro extern Second-Read 08:00.</p><div class="mt-3 flex gap-2"><span class="text-[11px] px-2 py-1 rounded-full bg-white text-zinc-900 font-semibold">Verwaltung</span><span class="text-[11px] px-2 py-1 rounded-full glass-subtle">100 % SR</span></div></div>
</div><div class="lg:col-span-4 glass rounded-[24px] p-5 sm:p-6"><h3 class="font-semibold">Wirtschaft & Personal</h3><div class="mt-4 space-y-3 text-xs">
<div class="p-3 rounded-xl bg-white text-zinc-900"><div class="font-bold">BD-Stunde = CT-Geld</div><div class="mt-1">4,8/h × 189 Nächte = 9 060 Nacht-Studien. 40 € = 362 k€ in Bereitschaft — ohne Tages-Team.</div></div>
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">Stille Feiertage</div><div class="text-white/60">Ostersonntag 99 (-60 %) → Feiertags-BD ausweiten.</div></div>
<div class="glass-subtle rounded-xl p-3"><div class="font-bold">D-Arzt BG</div><div class="text-white/60">1 227 BD-Fälle. 10 % Zuschlag = 12 k€/Q.</div></div><div class="flex items-center gap-2"><span class="flex-1 h-1 rounded-full bg-[#a3ff12]"></span><span class="text-[11px] font-bold uppercase text-[#a3ff12]">ROI <3 Mo</span></div></div>
<div class="mt-4 p-3 rounded-xl bg-[#a3ff12] text-zinc-900"><div class="text-xs font-black">Nächster Schritt</div><div class="mt-1 text-xs font-medium">Als Dashboard verankern (wöchentlich). BD-Heatmap + 07:30 live. Wer misst, steuert.</div><a href="#methodik" class="mt-2 inline-flex px-3 py-1.5 rounded-full bg-zinc-900 text-white text-xs font-bold">Dashboard →</a></div></div></div></section>
<section id="methodik" class="mt-6 mb-8"><div class="glass rounded-[24px] p-6 sm:p-8"><div class="flex items-center gap-3"><div class="w-9 h-9 rounded-full bg-white grid place-items-center text-zinc-900 font-bold text-sm">13</div><h2 class="font-serif text-xl tracking-tight">Anhang — Methodik, Grenzen & Rohdaten</h2><span class="hidden sm:inline-flex ml-auto text-xs px-3 py-1 rounded-full glass-subtle">19.10.2026 · 67 324 → 67 321 valide</span></div>
<div class="mt-6 grid lg:grid-cols-12 gap-6 text-xs leading-relaxed"><div class="lg:col-span-6"><div class="font-bold text-sm">Wie gerechnet</div><ul class="mt-2 space-y-1.5 text-white/70 list-disc list-inside">
<li><b class="text-white">BD:</b> Kern = Mo–Fr 07:30–16:00 ohne Feiertag (01.01.,03.04.,06.04.,01.05.,14.05.,25.05.). Rest = BD. Feiertag 09:00 = ganzer Tag BD.</li>
<li><b class="text-white">Stunden:</b> 1 606,5 h Kern (8,5×189), 4 945,5 h BD (15,5×189 + 24×84).</li>
<li><b class="text-white">Modalität:</b> Regel aus Beschreibung (Rö., CCT, Mammo, SOKI etc.) — 11 Gruppen, 99,2 %.</li>
<li><b class="text-white">Topologie:</b> 3 ungültige Timestamps entfernt. Tag 00:00.</li></ul>
<div class="mt-4 font-bold text-sm">Grenzen</div><ul class="mt-2 space-y-1.5 text-white/70 list-disc list-inside"><li>Kein Befund-Timestamp → keine Durchlaufzeit.</li><li>Arzt 41,6 % leer — keine Arzt-Auslastung.</li><li>Befund = Freitext — keine Qualitäts-Auto.</li><li>Nur gesetzliche Feiertage — Ostersonntag unterschätzt.</li></ul></div>
<div class="lg:col-span-6"><div class="font-bold text-sm">Steckbrief</div><div class="mt-2 grid grid-cols-2 gap-2"><div class="glass-subtle rounded-xl p-3"><div class="font-mono font-bold">67 321 Studien</div><div class="text-white/60">01.01. 00:47–30.09. 23:01</div></div><div class="glass-subtle rounded-xl p-3"><div class="font-mono font-bold">273 Tage</div><div class="text-white/60">Ø 247 · σ 38</div></div><div class="glass-subtle rounded-xl p-3"><div class="font-mono font-bold">19 Freigebende</div><div class="text-white/60">MLURZ 11 800</div></div><div class="glass-subtle rounded-xl p-3"><div class="font-mono font-bold">~280 Arten</div><div class="text-white/60">Rö Thorax 3 711</div></div><div class="glass-subtle rounded-xl p-3"><div class="font-mono font-bold">59 Abt.</div><div class="text-white/60">ZNA 20 620</div></div><div class="glass-subtle rounded-xl p-3"><div class="font-mono font-bold">11 Inst.</div><div class="text-white/60">St. Georg 57 563</div></div></div>
<div class="mt-4 p-3 rounded-xl bg-white text-zinc-900"><b>Reproduzierbar:</b> Export Q1 22 981 + Q2 22 592 + Q3 21 751. Skript + BD-Regel versioniert. Stand 19.10.2026.</div>
<div class="mt-3 flex flex-wrap gap-2"><span class="px-3 py-1.5 rounded-full bg-[#7c6cff] text-white font-semibold">PACS Q1–Q3 2026</span><span class="px-3 py-1.5 rounded-full glass-subtle">Sachsen-Feiertage</span><span class="px-3 py-1.5 rounded-full glass-subtle">BD v1.0</span></div></div></div>
<div class="mt-6 pt-6 border-t border-white/10 flex flex-wrap items-center justify-between gap-3 text-xs text-white/50"><div>© 2026 St. Georg Leipzig · Radiologie · Vertraulich</div><div class="flex gap-2"><span class="px-2.5 py-1 rounded-full glass-subtle">67 321</span><span class="px-2.5 py-1 rounded-full bg-white text-zinc-900 font-bold">273 Tage lückenlos</span></div></div></div></section>
</main>
""")

w('<script id="payload" type="application/json">')
w(p)
w('</script><script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script><script>')
w("""
const payload=JSON.parse(document.getElementById('payload').textContent);
const fmt=n=>n.toLocaleString('de-DE');
window.addEventListener('scroll',()=>{const h=document.documentElement;const p=(h.scrollTop/(h.scrollHeight-h.clientHeight))*100;document.getElementById('progress').style.width=p+'%';});
const counters=document.querySelectorAll('[data-target]');const io=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){const el=e.target, target=+el.dataset.target;let cur=0;const step=Math.ceil(target/60);const tick=()=>{cur+=step;if(cur>=target)el.textContent=fmt(target);else{el.textContent=fmt(cur);requestAnimationFrame(tick);}};tick();io.unobserve(el);}});},{threshold:.5});counters.forEach(c=>io.observe(c));
Chart.defaults.color='rgba(255,255,255,.72)';Chart.defaults.borderColor='rgba(255,255,255,.08)';Chart.defaults.font.family='Inter';
new Chart(document.getElementById('hourlyChart'),{type:'bar',data:{labels:Array.from({length:24},(_,i)=>String(i).padStart(2,'0')+':00'),datasets:[{label:'Kern',data:payload.hour_kern,backgroundColor:'#0ea5e9',borderRadius:6,barPercentage:.7},{label:'BD',data:payload.hour_bd,backgroundColor:'#7c6cff',borderRadius:6,barPercentage:.7}]},options:{responsive:true,maintainAspectRatio:false,interaction:{mode:'index',intersect:false},plugins:{legend:{position:'bottom',labels:{usePointStyle:true,boxWidth:8}}},scales:{x:{stacked:true,grid:{display:false},ticks:{color:'rgba(255,255,255,.55)',font:{size:10}}},y:{stacked:true,grid:{color:'rgba(255,255,255,.06)'}}}}});
new Chart(document.getElementById('slotChart'),{type:'bar',data:{labels:payload.slot_labels,datasets:[{label:'Studien',data:payload.slot_counts,backgroundColor:payload.slot_labels.map(l=>l==='07:30'?'#f59e0b':l>='07:30'&&l<='09:30'?'#0ea5e9':l>='16:00'?'#7c6cff':'rgba(255,255,255,.75)'),borderRadius:6}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false},ticks:{autoSkip:true,maxTicksLimit:16,color:'rgba(255,255,255,.55)',font:{size:9}}},y:{grid:{color:'rgba(255,255,255,.06)'}}}}});
new Chart(document.getElementById('detailChart'),{type:'line',data:{labels:payload.detail_labels,datasets:[{label:'Studien',data:payload.detail_vals,borderColor:'#0ea5e9',backgroundColor:'rgba(14,165,233,.18)',fill:true,tension:.35,pointRadius:4,pointBackgroundColor:'#0ea5e9',borderWidth:2.5}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false}},y:{grid:{color:'rgba(255,255,255,.06)'}}}}});
new Chart(document.getElementById('weekdayChart'),{type:'bar',data:{labels:payload.wd_names,datasets:[{label:'Kern',data:payload.wd_kern,backgroundColor:'#0ea5e9',borderRadius:8},{label:'BD',data:payload.wd_bd,backgroundColor:'#7c6cff',borderRadius:8}]},options:{responsive:true,maintainAspectRatio:false,indexAxis:'y',scales:{x:{stacked:true,grid:{color:'rgba(255,255,255,.06)'}},y:{stacked:true,grid:{display:false}}},plugins:{legend:{position:'bottom'}}}});
new Chart(document.getElementById('monthChart'),{type:'bar',data:{labels:payload.month_labels,datasets:[{label:'Kern',data:payload.month_kern,backgroundColor:'#0ea5e9',borderRadius:6},{label:'BD',data:payload.month_bd,backgroundColor:'#7c6cff',borderRadius:6}]},options:{responsive:true,maintainAspectRatio:false,interaction:{mode:'index'},scales:{x:{stacked:true,grid:{display:false}},y:{stacked:true,grid:{color:'rgba(255,255,255,.06)'}}},plugins:{legend:{position:'bottom'}}}});
new Chart(document.getElementById('weeklyChart'),{type:'line',data:{labels:payload.weekly_labels,datasets:[{label:'Studien/Woche',data:payload.weekly_vals,borderColor:'#ff3b82',backgroundColor:'rgba(255,59,130,.15)',fill:true,tension:.35,pointRadius:2}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false},ticks:{autoSkip:true,maxTicksLimit:12,font:{size:9}}},y:{grid:{color:'rgba(255,255,255,.06)'}}}}});
new Chart(document.getElementById('dailyChart'),{type:'bar',data:{labels:payload.daily_labels,datasets:[{label:'Kern',data:payload.daily_vals.map((v,i)=>v-payload.daily_bd_vals[i]),backgroundColor:'#0ea5e9',barPercentage:.9},{label:'BD',data:payload.daily_bd_vals,backgroundColor:'#7c6cff',barPercentage:.9}]},options:{responsive:true,maintainAspectRatio:false,interaction:{mode:'index'},scales:{x:{stacked:true,grid:{display:false},ticks:{display:false}},y:{stacked:true,grid:{color:'rgba(255,255,255,.06)'}}},plugins:{legend:{position:'bottom'},tooltip:{callbacks:{title:items=>payload.daily_labels[items[0].dataIndex]}}}}});
new Chart(document.getElementById('holidayChart'),{type:'bar',data:{labels:payload.holiday_names,datasets:[{label:'Studien',data:payload.holiday_vals,backgroundColor:['#f59e0b','#fb7185','#a78bfa','#f43f5e','#38bdf8','#a3e635'],borderRadius:10,barPercentage:.6}]},options:{responsive:true,maintainAspectRatio:false,indexAxis:'y',plugins:{legend:{display:false}},scales:{x:{grid:{color:'rgba(255,255,255,.06)'}},y:{grid:{display:false}}}}});
new Chart(document.getElementById('znaRoeChart'),{type:'line',data:{labels:Array.from({length:24},(_,i)=>String(i).padStart(2,'0')),datasets:[{label:'ZNA (20 620)',data:payload.zna_hour,borderColor:'#7c6cff',backgroundColor:'rgba(124,108,255,.18)',fill:true,tension:.35,borderWidth:2.5,pointRadius:0},{label:'ROE (15 528)',data:payload.roe_hour,borderColor:'#0ea5e9',backgroundColor:'rgba(14,165,233,.10)',fill:true,tension:.35,borderWidth:2.5,pointRadius:0}]},options:{responsive:true,maintainAspectRatio:false,interaction:{mode:'index',intersect:false},plugins:{legend:{position:'bottom'}},scales:{x:{grid:{display:false}},y:{grid:{color:'rgba(255,255,255,.06)'}}}}});
new Chart(document.getElementById('modalityDoughnut'),{type:'doughnut',data:{labels:payload.mod_labels,datasets:[{data:payload.mod_tot,backgroundColor:['#0ea5e9','#7c6cff','#ff3b82','#a3ff12','#f59e0b','#38bdf8','#fb7185','#a78bfa','#f43f5e','#eab308','#22c55e'],borderWidth:0,hoverOffset:8}]},options:{responsive:true,maintainAspectRatio:false,cutout:'58%',plugins:{legend:{position:'bottom',labels:{usePointStyle:true,boxWidth:8,font:{size:11},padding:12}}}}});
new Chart(document.getElementById('modalityBdChart'),{type:'bar',data:{labels:payload.mod_labels,datasets:[{label:'BD %',data:payload.mod_bd_pct,backgroundColor:payload.mod_bd_pct.map(v=>v>30?'#7c6cff':v>10?'#f59e0b':'#0ea5e9'),borderRadius:8,barPercentage:.55}]},options:{responsive:true,maintainAspectRatio:false,indexAxis:'y',plugins:{legend:{display:false}},scales:{x:{max:70,grid:{color:'rgba(255,255,255,.06)'},ticks:{callback:v=>v+'%'}},y:{grid:{display:false}}}}});
new Chart(document.getElementById('studienChart'),{type:'bar',data:{labels:payload.stud_labels.map(l=>l.length>38?l.slice(0,38)+'…':l),datasets:[{label:'Kern',data:payload.stud_tot.map((v,i)=>v-payload.stud_bd[i]),backgroundColor:'#0ea5e9',borderRadius:6,barPercentage:.7},{label:'BD',data:payload.stud_bd,backgroundColor:'#7c6cff',borderRadius:6,barPercentage:.7}]},options:{responsive:true,maintainAspectRatio:false,indexAxis:'y',scales:{x:{stacked:true,grid:{color:'rgba(255,255,255,.06)'}},y:{stacked:true,grid:{display:false},ticks:{font:{size:10}}}},plugins:{legend:{position:'bottom'}}}});
new Chart(document.getElementById('institutionChart'),{type:'bar',data:{labels:payload.inst_labels.map(l=>l.length>34?l.slice(0,34)+'…':l),datasets:[{label:'Kern',data:payload.inst_tot.map((v,i)=>v-payload.inst_bd[i]),backgroundColor:'#0ea5e9',borderRadius:6},{label:'BD',data:payload.inst_bd,backgroundColor:'#7c6cff',borderRadius:6}]},options:{responsive:true,maintainAspectRatio:false,indexAxis:'y',scales:{x:{stacked:true,grid:{color:'rgba(255,255,255,.06)'}},y:{stacked:true,grid:{display:false},ticks:{font:{size:10}}}},plugins:{legend:{position:'bottom'}}}});
new Chart(document.getElementById('abteilungChart'),{type:'bar',data:{labels:payload.abt_labels,datasets:[{label:'Kern',data:payload.abt_tot.map((v,i)=>v-payload.abt_bd[i]),backgroundColor:'#0ea5e9',borderRadius:6},{label:'BD',data:payload.abt_bd,backgroundColor:'#7c6cff',borderRadius:6}]},options:{responsive:true,maintainAspectRatio:false,indexAxis:'y',scales:{x:{stacked:true,grid:{color:'rgba(255,255,255,.06)'}},y:{stacked:true,grid:{display:false}}},plugins:{legend:{position:'bottom'}}}});
new Chart(document.getElementById('freigebenderChart'),{type:'bar',data:{labels:payload.freig_labels,datasets:[{label:'Kern',data:payload.freig_kern,backgroundColor:'#0ea5e9',borderRadius:6},{label:'BD',data:payload.freig_bd,backgroundColor:'#7c6cff',borderRadius:6}]},options:{responsive:true,maintainAspectRatio:false,indexAxis:'y',scales:{x:{stacked:true,grid:{color:'rgba(255,255,255,.06)'}},y:{stacked:true,grid:{display:false}}},plugins:{legend:{position:'bottom'}}}});
new Chart(document.getElementById('timeShareChart'),{type:'doughnut',data:{labels:['Kern 1 606,5 h (24,5 %)','BD 4 945,5 h (75,5 %)'],datasets:[{data:[1606.5,4945.5],backgroundColor:['#0ea5e9','#7c6cff'],borderWidth:0}]},options:{responsive:true,maintainAspectRatio:false,cutout:'64%',plugins:{legend:{position:'bottom',labels:{usePointStyle:true,boxWidth:8}}}}});
new Chart(document.getElementById('throughputChart'),{type:'bar',data:{labels:['Kern Ø','BD Ø','Mo–Do Nacht','Fr 16→Sa 09','Sa 24h','So 22,5h','Nacht 22–06'],datasets:[{label:'Studien / h',data:[27.3,4.76,4.9,6.2,5.6,5.7,4.2],backgroundColor:['#0ea5e9','#7c6cff','#a78bfa','#ff3b82','#f59e0b','#38bdf8','#fb7185'],borderRadius:8}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false},ticks:{font:{size:10}}},y:{grid:{color:'rgba(255,255,255,.06)'}}}}});
new Chart(document.getElementById('loadCurveChart'),{type:'line',data:{labels:Array.from({length:24},(_,i)=>String(i).padStart(2,'0')),datasets:[{label:'BD / h',data:payload.hour_bd,borderColor:'#7c6cff',backgroundColor:'rgba(124,108,255,.18)',fill:true,tension:.35,borderWidth:2.5,pointRadius:0}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false}},y:{grid:{color:'rgba(255,255,255,.06)'}}}}});
new Chart(document.getElementById('weekdayAvgChart'),{type:'bar',data:{labels:['Mo 309','Di 288','Mi 321','Do 283','Fr 263','Sa 134','So 128'],datasets:[{data:[309.3,288.1,320.8,283.2,263.1,133.9,127.7],backgroundColor:['#0ea5e9','#0ea5e9','#f59e0b','#0ea5e9','#f59e0b','#7c6cff','#7c6cff'],borderRadius:8,barPercentage:.6}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{grid:{display:false}},y:{grid:{color:'rgba(255,255,255,.06)'}}}}});
(function(){const c=document.getElementById('heatmap'),max=Math.max(...payload.heat.flat()),min=Math.min(...payload.heat.flat());let h=`<div class="grid" style="grid-template-columns:44px repeat(24,1fr);gap:4px;font-size:11px"><div></div>`;for(let i=0;i<24;i++)h+=`<div class="text-center text-white/45 font-mono">${String(i).padStart(2,'0')}</div>`;for(let wd=0;wd<7;wd++){h+=`<div class="font-semibold text-white/80 flex items-center">${payload.wd_names[wd]}</div>`;for(let hr=0;hr<24;hr++){const v=payload.heat[wd][hr],t=(v-min)/(max-min);let bg=t<.2?'rgba(255,255,255,.06)':t<.4?`rgba(14,165,233,${.25+t*.6})`:t<.65?`rgba(124,108,255,${.35+t*.5})`:`rgba(255,59,130,${.45+t*.4})`;h+=`<div class="heat-cell rounded-lg h-9 grid place-items-center font-mono font-semibold" style="background:${bg};border:1px solid rgba(255,255,255,.06)" title="${payload.wd_names[wd]} ${String(hr).padStart(2,'0')}:00 — ${v}">${v}</div>`;}}h+=`</div><div class="mt-3 flex items-center gap-2 text-xs text-white/50"><span class="w-3 h-3 rounded bg-white/5 border border-white/10"></span> niedrig <span class="flex-1 h-1 rounded-full" style="background:linear-gradient(90deg,rgba(255,255,255,.06),#0ea5e9,#7c6cff,#ff3b82)"></span> hoch (1 659)</div>`;c.innerHTML=h;})();
document.getElementById('menuBtn')?.addEventListener('click',()=>{const n=document.querySelector('header .hidden.lg\\:block');if(n)n.classList.toggle('hidden');n?.classList.toggle('block');});
""")
w("</script></body></html>")
f.close()
print("Written", pathlib.Path(out).stat().st_size)

