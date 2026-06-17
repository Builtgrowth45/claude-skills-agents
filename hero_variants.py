mini_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 605 605" width="605" height="605"><circle cx="302.5" cy="302.5" r="302.5" class="bg-circle"/><circle cx="302.5" cy="302.5" r="301" fill="none" stroke="currentColor" stroke-width="1" opacity="0.2"/></svg>'

badge_d = '<div class="hv-bdg hv-bdg-d"><span class="hv-dot"></span>14 February 2024</div>'
badge_l = '<div class="hv-bdg hv-bdg-l">&#128205; London, UK</div>'

def map_col(extra_r1='', extra_r2='', extra_bdg=''):
    return (
        '<div class="hv-right"><div class="hv-mc">'
        + f'<div class="hv-r1 {extra_r1}"></div>'
        + f'<div class="hv-r2 {extra_r2}"></div>'
        + f'<div class="hv-mw">{mini_svg}</div>'
        + badge_d.replace('class="hv-bdg', f'class="hv-bdg {extra_bdg}')
        + badge_l.replace('class="hv-bdg', f'class="hv-bdg {extra_bdg}')
        + '</div></div>'
    )

css = """
<style data-impeccable-css="3efa9edf">
.hv-section{min-height:100vh;display:grid;grid-template-columns:1fr 1fr;align-items:center;padding:100px 52px 60px;gap:60px;position:relative;overflow:hidden}
.hv-left{position:relative;z-index:2}
.hv-eyebrow{font-family:'Space Mono',monospace;font-size:9px;letter-spacing:0.32em;text-transform:uppercase;margin-bottom:22px;display:flex;align-items:center;gap:10px}
.hv-h1{font-family:'Cormorant Garamond',serif;font-size:clamp(46px,6vw,96px);font-weight:300;line-height:1.06;letter-spacing:-0.02em;margin-bottom:20px;color:var(--text)}
.hv-h1 em{font-style:italic;color:var(--gold)}
.hv-rule{width:40px;height:1px;margin-bottom:18px;background:var(--text3)}
.hv-sub{font-size:15px;line-height:1.75;max-width:420px;margin-bottom:10px;color:var(--text2)}
.hv-nudge{font-family:'Space Mono',monospace;font-size:8px;letter-spacing:0.2em;text-transform:uppercase;margin-bottom:28px;opacity:0.55}
.hv-btns{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:36px}
.hv-btn-p{padding:15px 34px;border-radius:9px;font-size:12px;letter-spacing:0.14em;text-transform:uppercase;text-decoration:none;display:inline-flex;align-items:center;gap:10px;font-family:'DM Sans',sans-serif;border:none;cursor:pointer;transition:opacity 0.22s cubic-bezier(0.22,1,0.36,1),transform 0.22s cubic-bezier(0.22,1,0.36,1)}
.hv-btn-p:hover{opacity:0.85;transform:translateY(-1px)}
.hv-btn-s{padding:15px 28px;border-radius:9px;font-size:12px;letter-spacing:0.14em;text-transform:uppercase;text-decoration:none;display:inline-flex;align-items:center;gap:8px;font-family:'DM Sans',sans-serif;cursor:pointer;background:transparent;transition:color 0.2s,border-color 0.2s}
.hv-trust{display:flex;align-items:center;gap:14px}
.hv-stars{color:#d4a843;font-size:13px;letter-spacing:2px}
.hv-trust-t{font-family:'Space Mono',monospace;font-size:9px;letter-spacing:0.1em;color:var(--text3)}
.hv-right{display:flex;align-items:center;justify-content:center;position:relative}
.hv-mc{position:relative;width:min(520px,90vw)}
.hv-r1{position:absolute;inset:-20px;border-radius:50%;border:1px solid var(--border2);animation:spin 60s linear infinite}
.hv-r2{position:absolute;inset:-40px;border-radius:50%;border:1px dashed var(--border);opacity:0.5;animation:spin 90s linear infinite reverse}
.hv-mw{border-radius:50%;overflow:hidden;position:relative;box-shadow:0 24px 80px var(--shadow)}
.hv-mw svg{width:100%;height:auto;display:block}
.hv-mw .bg-circle{fill:var(--map-bg)}
.hv-bdg{position:absolute;background:var(--surface);backdrop-filter:blur(12px);border:1px solid var(--border);border-radius:10px;padding:10px 16px;font-family:'Space Mono',monospace;font-size:9px;letter-spacing:0.1em;color:var(--text2);white-space:nowrap;box-shadow:0 4px 20px var(--shadow)}
.hv-bdg-d{bottom:-10px;left:30px}
.hv-bdg-l{top:30px;right:-20px}
.hv-dot{width:7px;height:7px;border-radius:50%;background:var(--teal);display:inline-block;margin-right:6px;animation:pulse 2s infinite}
@media(max-width:900px){.hv-section{grid-template-columns:1fr;padding:100px 24px 60px;text-align:center}.hv-right{order:-1;max-width:380px;margin:0 auto}.hv-btns,.hv-trust{justify-content:center}.hv-sub{margin:0 auto 10px}}

/* V1: Highland Dawn */
@scope ([data-impeccable-variant="1"]) {
  .hv1{background:var(--bg)}
  .hv1::before{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
    background:
      radial-gradient(ellipse calc(680px * var(--p-glow,0.7)) calc(560px * var(--p-glow,0.7)) at 72% 50%, oklch(18% 0.025 255 / 0.28) 0%, oklch(54% 0.10 182 / 0.04) 45%, transparent 70%),
      radial-gradient(ellipse 900px 600px at 100% 100%, oklch(50% 0.09 70 / 0.06) 0%, transparent 60%)}
  .v1-bp{background:var(--text);color:var(--bg)}
  .v1-bs{color:var(--text2);border:1px solid var(--border2)}
  .v1-bs:hover{color:var(--text);border-color:var(--text2)}
  .v1-ng{color:var(--text3)}
}

/* V2: Midnight at the Stones */
@scope ([data-impeccable-variant="2"]) {
  .hv2{background:#06080f}
  .hv2::before{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
    background:
      radial-gradient(ellipse calc(700px * var(--p-glow,0.8)) 600px at 70% 50%, oklch(54% 0.10 182 / 0.12) 0%, oklch(50% 0.09 70 / 0.05) 50%, transparent 75%),
      radial-gradient(ellipse 400px 400px at 15% 80%, oklch(50% 0.09 70 / 0.07) 0%, transparent 60%)}
  .hv2::after{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
    background-image:radial-gradient(circle 1px at 50% 50%, oklch(87% 0.016 255 / 0.12) 1px, transparent 1px);
    background-size:48px 48px;
    mask-image:radial-gradient(ellipse 80% 80% at 50% 50%, black, transparent)}
  .hv2 .hv-h1{color:#d4dae8}
  .hv2 .hv-h1 em{color:#c9a96e!important}
  .hv2 .hv-rule{background:#3a4460}
  .hv2 .hv-sub{color:#7a8aaa}
  .hv2 .hv-trust-t{color:#3a4460}
  .hv2 .hv-stars{color:#c9a96e}
  .hv2 .hv-eyebrow{color:#14b8a6}
  .hv2 .hv-dot{background:#14b8a6}
  .hv2 .hv-r1{border-color:rgba(80,100,180,0.22)}
  .hv2 .hv-r2{border-color:rgba(80,100,180,0.12)}
  .hv2 .hv-bdg{background:rgba(13,16,32,0.9);border-color:rgba(80,100,180,0.22);color:#7a8aaa}
  .v2-bp{background:#14b8a6;color:#06080f}
  .v2-bs{color:#7a8aaa;border:1px solid rgba(80,100,180,0.22)}
  .v2-bs:hover{color:#d4dae8;border-color:#7a8aaa}
  .v2-ng{color:#3a4460}
}

/* V3: Editorial Archive */
@scope ([data-impeccable-variant="3"]) {
  .hv3{background:var(--bg);grid-template-columns:5fr 4fr;gap:80px}
  .hv3::before{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
    background-image:linear-gradient(var(--border) 1px, transparent 1px),linear-gradient(90deg, var(--border) 1px, transparent 1px);
    background-size:52px 52px;opacity:var(--p-grid,0.5);
    mask-image:radial-gradient(ellipse 60% 70% at 30% 50%, black 20%, transparent 80%)}
  .hv3::after{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
    background:
      radial-gradient(ellipse 500px 400px at 0% 50%, oklch(50% 0.09 70 / 0.06) 0%, transparent 70%),
      radial-gradient(ellipse 600px 500px at 65% 50%, oklch(12% 0.02 255 / 0.15) 0%, transparent 65%)}
  .v3-li{border-top:1px solid var(--border2);padding-top:24px}
  .hv3 .hv-eyebrow{color:var(--teal)}
  .v3-bp{background:var(--text);color:var(--bg)}
  .v3-bs{color:var(--text2);border:1px solid var(--border2)}
  .v3-bs:hover{color:var(--text);border-color:var(--text2)}
  .v3-ng{color:var(--teal)}
  .v3-pq{margin-top:40px;padding-top:24px;border-top:1px solid var(--border);font-family:'Cormorant Garamond',serif;font-size:17px;font-weight:300;font-style:italic;color:var(--text2);line-height:1.55;max-width:380px}
  .v3-pa{display:block;margin-top:10px;font-family:'Space Mono',monospace;font-size:9px;letter-spacing:0.15em;text-transform:uppercase;color:var(--text3)}
}

/* V4: The Threshold */
@scope ([data-impeccable-variant="4"]) {
  .hv4{background:var(--bg)}
  .hv4::before{content:'';position:absolute;inset:0;z-index:0;pointer-events:none;
    background:
      radial-gradient(ellipse 110% 110% at 50% 50%, var(--bg) 0%, oklch(50% 0.09 70 / calc(0.06 * var(--p-depth,1))) 40%, oklch(12% 0.02 255 / calc(0.18 * var(--p-depth,1))) 70%, oklch(6% 0.015 265 / calc(0.25 * var(--p-depth,1))) 100%),
      radial-gradient(ellipse 700px 600px at 68% 50%, oklch(54% 0.10 182 / calc(0.09 * var(--p-depth,1))) 0%, transparent 65%)}
  .hv4 .hv-rule{background:var(--gold);opacity:0.4}
  .hv4 .hv-eyebrow{color:var(--teal)}
  .hv4 .hv-r1{border-color:rgba(139,110,58,0.18)}
  .v4-bp{background:var(--text);color:var(--bg);padding:17px 40px!important;font-size:13px!important}
  .v4-bs{color:var(--text2);border:1px solid var(--border2)}
  .v4-bs:hover{color:var(--text);border-color:var(--text2)}
  .v4-ng{color:var(--teal)}
}

@media(prefers-reduced-motion:reduce){.hv-r1,.hv-r2{animation:none!important}}
</style>
"""

def left_col(variant, bp_cls, bs_cls, ng_cls, extra=''):
    stars = '&#9733;' * 5
    return f"""    <div class="hv-left">
      {extra}<div class="hv-eyebrow">Custom Star Maps</div>
      <h1 class="hv-h1">The sky on<br><em>your night</em></h1>
      <div class="hv-rule"></div>
      <p class="hv-sub">A precise map of the stars exactly as they appeared on the night that changed your world. Beautifully printed and yours to keep forever.</p>
      <p class="hv-nudge {ng_cls}">Free preview &mdash; order only when it&rsquo;s perfect</p>
      <div class="hv-btns">
        <a href="stellar-atlas_4.html" class="hv-btn-p {bp_cls}">Create your map &rarr;</a>
        <a href="#how" class="hv-btn-s {bs_cls}">See how it works</a>
      </div>
      <div class="hv-trust"><span class="hv-stars">{stars}</span><span class="hv-trust-t">20,000+ maps created worldwide</span></div>
    </div>"""

v1 = f"""<div data-impeccable-variant="1" data-impeccable-params='[{{"id":"glow","kind":"range","min":0.2,"max":1.2,"step":0.1,"default":0.7,"label":"Atmospheric glow"}},{{"id":"cta","kind":"steps","default":"nudge","label":"CTA style","options":[{{"value":"minimal","label":"Minimal"}},{{"value":"nudge","label":"With nudge"}},{{"value":"full","label":"Full emphasis"}}]}}]'>
  <section class="hv-section hv1">
{left_col(1,'v1-bp','v1-bs','v1-ng')}
{map_col()}
  </section>
</div>"""

v2 = f"""<div data-impeccable-variant="2" style="display:none" data-impeccable-params='[{{"id":"glow","kind":"range","min":0.3,"max":1.5,"step":0.1,"default":0.8,"label":"Night glow"}},{{"id":"stars","kind":"toggle","default":true,"label":"Star field bg"}}]'>
  <section class="hv-section hv2">
{left_col(2,'v2-bp','v2-bs','v2-ng')}
{map_col()}
  </section>
</div>"""

v3_extra = '<div class="v3-li">'
v3_end = '</div>'
v3_left = f"""    <div class="hv-left">
      <div class="v3-li">
        <div class="hv-eyebrow">Custom Star Maps</div>
        <h1 class="hv-h1">The sky on<br><em>your night</em></h1>
        <div class="hv-rule"></div>
        <p class="hv-sub">A precise map of the stars exactly as they appeared on the night that changed your world. Beautifully printed and yours to keep forever.</p>
        <p class="hv-nudge v3-ng">Free preview &mdash; order only when it&rsquo;s perfect</p>
        <div class="hv-btns">
          <a href="stellar-atlas_4.html" class="hv-btn-p v3-bp">Create your map &rarr;</a>
          <a href="#how" class="hv-btn-s v3-bs">See how it works</a>
        </div>
        <div class="hv-trust"><span class="hv-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span><span class="hv-trust-t">20,000+ maps created worldwide</span></div>
        <blockquote class="v3-pq">&ldquo;It&rsquo;s not just a map &mdash; it&rsquo;s a modern heirloom.&rdquo;<cite class="v3-pa">A. Cormac &middot; London, UK</cite></blockquote>
      </div>
    </div>"""

v3 = f"""<div data-impeccable-variant="3" style="display:none" data-impeccable-params='[{{"id":"grid","kind":"range","min":0.1,"max":1.0,"step":0.1,"default":0.5,"label":"Grid opacity"}},{{"id":"quote","kind":"toggle","default":true,"label":"Pull quote"}}]'>
  <section class="hv-section hv3">
{v3_left}
{map_col()}
  </section>
</div>"""

v4 = f"""<div data-impeccable-variant="4" style="display:none" data-impeccable-params='[{{"id":"depth","kind":"range","min":0.3,"max":1.8,"step":0.1,"default":1.0,"label":"Atmosphere depth"}},{{"id":"cta-size","kind":"toggle","default":true,"label":"Commanding CTA"}}]'>
  <section class="hv-section hv4">
{left_col(4,'v4-bp','v4-bs','v4-ng')}
{map_col('','','',)}
  </section>
</div>"""

variants_html = css + '\n' + v1 + '\n' + v2 + '\n' + v3 + '\n' + v4 + '\n'

with open('C:/GrowthMedia/Stargaze/stellar-atlas-landing.html', 'r', encoding='utf-8') as f:
    content = f.read()

marker = '  <!-- Variants: insert below this line -->\n'
pos = content.find(marker)
if pos == -1:
    print("ERROR: marker not found"); exit(1)
insert_at = pos + len(marker)
content = content[:insert_at] + variants_html + content[insert_at:]

with open('C:/GrowthMedia/Stargaze/stellar-atlas-landing.html', 'w', encoding='utf-8', errors='replace') as f:
    f.write(content)
print(f"Done. {len(content)} chars")
