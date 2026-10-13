#!/usr/bin/env python3
"""Builds index.html (English), ar/index.html (Arabic), thanks.html, robots.txt, sitemap.xml."""
import json, html, os

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC) if os.path.basename(SRC) == "_build" else SRC
SITE = "https://pr0fes0rx.github.io/3d-print-calculator-site"
DL = "https://github.com/Pr0fes0rx/3d-print-calculator/releases/latest"
PAYPAL_REG = "https://www.paypal.com/ncp/payment/NK9VRK3VGKW9U"   # regular price $39.99
PAYPAL = "https://www.paypal.com/ncp/payment/GMKFUCEG2VFYJ"       # Halloween price $19.99
PROMO_END = "2026-10-31T23:59:59+03:00"   # sale + Halloween theme end (Syria time). After this date the page switches back by itself.
TRUST = "https://link.trustwallet.com/send?asset=c195_tTR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t&amp;address=TFe3n6CLqt4D2rHTPWeDfpFdnEMXyJRfoz&amp;amount=39.99"
TRUST_REG = TRUST
TRUST = TRUST.replace("amount=39.99", "amount=19.99")
ADDR = "TFe3n6CLqt4D2rHTPWeDfpFdnEMXyJRfoz"
MAIL = "ahmwho@gmail.com"
WEB3 = "2daa2a69-d0e0-4723-9e68-b8472fbb72f6"
QR = open(os.path.join(SRC, "qr.svg")).read()

# ---- same formula as site.js, used to pre-render the default numbers (no-JS and crawlers see real values)
def calc(w=150, h=6, price=17, pw=200, kwh=.12, mt=.4, fl=10, m=40):
    mat = w / 1000 * price; ele = h * pw / 1000 * kwh; mnt = h * mt
    base = mat + ele + mnt; fail = base * fl / 100; cost = base + fail
    profit = cost * m / 100
    return dict(mat=mat, ele=ele, mnt=mnt, fail=fail, cost=cost, profit=profit, price=cost + profit)
C = calc()
def usd(v): return "$%.2f" % v
def pct(v): return round(v / C["cost"] * 100)
SVG = '<svg id="sc" viewBox="0 -24 200 214" role="img" aria-label="%s">\n<defs><linearGradient id="pg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3a4f9a"/><stop offset=".5" stop-color="#6a84d8"/><stop offset="1" stop-color="#2a3a7c"/></linearGradient><linearGradient id="pb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a63b8"/><stop offset="1" stop-color="#1f2c63"/></linearGradient></defs>\n<rect x="10" y="172" width="180" height="14" rx="6" fill="url(#pb)"/><rect x="150" y="176" width="26" height="6" rx="2" fill="#0c1530"/><circle cx="156" cy="179" r="1.6" fill="var(--fil)"/><circle cx="36" cy="179" r="3" fill="#dbe3f7"/>\n<rect x="18" y="186" width="14" height="3" rx="1.5" fill="#22306a"/><rect x="168" y="186" width="14" height="3" rx="1.5" fill="#22306a"/>\n<rect x="30" y="164" width="140" height="8" rx="3" fill="#1c2a55"/><rect x="30" y="164" width="140" height="2.6" rx="1.3" fill="#7d90d8" opacity=".55"/>\n<rect x="12" y="18" width="12" height="154" rx="4" fill="url(#pg)"/><rect x="176" y="18" width="12" height="154" rx="4" fill="url(#pg)"/>\n<path d="M18 26v138M182 26v138" stroke="rgba(255,255,255,.2)" stroke-width="1"/>\n<rect x="12" y="12" width="176" height="9" rx="4.5" fill="url(#pb)"/>\n<path d="M100 -4v18" stroke="#3b4f9c" stroke-width="3" stroke-linecap="round"/>\n<g id="lay"></g>\n<path id="fil" d="M100 -2C100 40 100 70 100 118" fill="none" stroke="var(--fil)" stroke-width="2.2" stroke-linecap="round"/>\n<g id="gan" transform="translate(0,150)"><rect x="24" y="0" width="152" height="8" rx="3" fill="#3b4f9c"/><rect x="24" y="1.5" width="152" height="2" rx="1" fill="rgba(255,255,255,.22)"/><rect x="18" y="-3" width="10" height="14" rx="3" fill="#5a73c8"/><rect x="172" y="-3" width="10" height="14" rx="3" fill="#5a73c8"/></g>\n<g id="car"><rect x="0" y="0" width="28" height="14" rx="5" fill="#5a73c8"/><rect x="4" y="3" width="8" height="3" rx="1.5" fill="#c2cce8"/><path d="M8 14h12l-4.2 7h-3.6z" fill="#dbe3f7"/><circle cx="14" cy="22" r="3" fill="var(--fil)"/><circle cx="14" cy="22" r="5.5" fill="var(--fil)" opacity=".25"/></g>\n<g class="pspool"><circle cx="100" cy="-4" r="14.5" fill="rgba(200,215,255,.12)" stroke="rgba(225,235,255,.85)" stroke-width="1.4"/><circle cx="100" cy="-4" r="12.2" fill="var(--fil)"/><circle cx="100" cy="-4" r="12.2" fill="rgba(255,255,255,.2)"/><circle cx="100" cy="-4" r="11.6" fill="none" stroke="rgba(255,255,255,.35)" stroke-width=".4"/><circle cx="100" cy="-4" r="10.8" fill="none" stroke="rgba(20,0,60,.2)" stroke-width=".4"/><circle cx="100" cy="-4" r="10.1" fill="none" stroke="rgba(255,255,255,.35)" stroke-width=".4"/><circle cx="100" cy="-4" r="9.3" fill="none" stroke="rgba(20,0,60,.2)" stroke-width=".4"/><circle cx="100" cy="-4" r="8.6" fill="none" stroke="rgba(255,255,255,.35)" stroke-width=".4"/><circle cx="100" cy="-4" r="7.8" fill="none" stroke="rgba(20,0,60,.2)" stroke-width=".4"/><circle cx="100" cy="-4" r="7.1" fill="none" stroke="rgba(255,255,255,.35)" stroke-width=".4"/><circle cx="100" cy="-4" r="6.3" fill="none" stroke="rgba(20,0,60,.2)" stroke-width=".4"/><circle cx="100" cy="-4" r="6.2" fill="#0c1022"/><path d="M100 -9.9v0" stroke="none"/><g stroke="rgba(190,200,230,.5)" stroke-width="1" stroke-linecap="round"><path d="M103.4 -4.0 L105.9 -4.0"/><path d="M101.7 -1.1 L103.0 1.1"/><path d="M98.3 -1.1 L97.0 1.1"/><path d="M96.6 -4.0 L94.1 -4.0"/><path d="M98.3 -6.9 L97.0 -9.1"/><path d="M101.7 -6.9 L103.0 -9.1"/></g><circle cx="100" cy="-4" r="6.2" fill="none" stroke="rgba(235,242,255,.85)" stroke-width="1.1"/></g>\n</svg>'

SHOW_SCENE = True   # set to False to remove the animated printer scene from the hero (nothing else depends on it)
def scene_html(t):
    if not SHOW_SCENE: return ""
    return '<div class="scene">' + SVG % e(t["sceneAlt"]) + '</div>'

SHOW_FLOATERS = True   # floating filament spools + icon chips around the calculator; set False to remove
_IC = {
 "file":'<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
 "trend":'<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
 "bolt":'<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "wrench":'<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/>'}
def _chip(cls, ic, txt):
    return ('<span class="fl chip %s" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">%s</svg>%s</span>' % (cls, _IC[ic], txt))
_SPOOL_IMG = {"s1": "rainbow", "s2": "gloss", "s3": "glow", "s4": "pink"}   # 1 kg spool render, img/spool-<colour>.webp
def _spool(cls, P=""):
    return '<img class="fl spool %s" src="%simg/spool-%s.webp" width="340" height="391" alt="" aria-hidden="true" decoding="async">' % (cls, P, _SPOOL_IMG[cls])
def floaters_html(t):
    if not SHOW_FLOATERS: return ""
    P = "../" if t["lang"] == "ar" else ""
    return (_spool("s1", P) + _spool("s2", P) + _spool("s3", P) + _spool("s4", P)
      + _chip("c1","file","INV-000001 \u00b7 PDF") + _chip("c2","trend",t["cProfit"]) + _chip("c3","bolt","kWh") + _chip("c4","wrench","$/h"))

# ---- countries panel: one row per country. rate = units of local currency per 1 USD, kwh = tier-1 electricity price.
# ap=1 marks values that are approximate (shown with a "~" sign). These are illustrative sample values for the website demo.
COUNTRIES = [
 # code, en, ar, cur, cur_en, cur_ar, kwh, rate_txt, rate, approx
 ("SY","Syria","سوريا","SYP","Syrian pound","ليرة سورية","6","138.25",138.25,0),
 ("IQ","Iraq","العراق","IQD","Iraqi dinar","دينار عراقي","10","1,310",1310,0),
 ("JO","Jordan","الأردن","JOD","Jordanian dinar","دينار أردني","0.033","0.709",0.709,0),
 ("SA","Saudi Arabia","السعودية","SAR","Saudi riyal","ريال سعودي","0.18","3.75",3.75,0),
 ("EG","Egypt","مصر","EGP","Egyptian pound","جنيه مصري","0.68","48",48,1),
 ("DZ","Algeria","الجزائر","DZD","Algerian dinar","دينار جزائري","1.78","130",130,1),
 ("US","USA","أمريكا","USD","US dollar","دولار أمريكي","0.17","1",1,0),
 ("DE","Germany","ألمانيا","EUR","Euro","يورو","0.38","0.86",0.86,1),
]
def fmt_amt(n):
    s = ("{:,.0f}" if n >= 100 else "{:,.2f}").format(n)
    return s.rstrip("0").rstrip(".") if "." in s else s
def countries_html(t):
    L = t["lang"]; ni = 1 if L == "en" else 2; ci = 4 if L == "en" else 5
    c0 = COUNTRIES[0]
    P = "../" if L == "ar" else ""
    fp = lambda code: "%simg/flags/%s.webp" % (P, code.lower())
    chips = ""
    for k, c in enumerate(COUNTRIES):
        chips += ('<button type="button" role="radio" aria-checked="%s" tabindex="%d" data-code="%s" data-flag="%s" data-n="%s" data-cur="%s" data-curn="%s" data-kwh="%s" data-rt="%s" data-r="%s" data-ap="%d"><img class="fg" src="%s" width="21" height="16" alt="" decoding="async">%s</button>'
                  % ("true" if k == 0 else "false", 0 if k == 0 else -1, c[0], fp(c[0]), e(c[ni]), c[3], e(c[ci]), c[6], c[7], c[8], c[9], fp(c[0]), e(c[ni])))
    return f'''<div class="cx" id="cx">
          <div class="cx-top"><img class="cx-code" id="cxCode" src="{fp(c0[0])}" width="126" height="94" alt=""><div><small>{t["ctry"]}</small><b id="cxName">{e(c0[ni])}</b></div></div>
          <div class="ctries" role="radiogroup" aria-label="{e(t["ctry"])}">{chips}</div>
          <div class="rows" aria-live="polite">
            <div class="row"><span>{t["cur"]}</span><b><bdi dir="ltr" id="cxCur">{c0[3]}</bdi><span class="cn"> &middot; <span id="cxCurN">{e(c0[ci])}</span></span></b></div>
            <div class="row"><span>{t["tier"]}</span><b dir="ltr" id="cxKwh">{c0[6]} {c0[3]} / kWh</b></div>
            <div class="row"><span>{t["rate"]}</span><b dir="ltr" id="cxRate">1 $ = {c0[7]} {c0[3]}</b></div>
            <div class="row ex"><span>{t["cxExL"]}</span><b dir="ltr" id="cxEx">$10 = {fmt_amt(10*c0[8])} {c0[3]}</b></div>
          </div>
          <p class="cx-note">{t["cxNote"]}</p>
        </div>'''

def ui_card(t):
    IC = {'m': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3"/><path d="M12 3v6M12 15v6M3 12h6M15 12h6"/>', 'e': '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>', 'w': '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/>', 's': '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>', 't': '<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>', 'f': '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>'}
    COL = ['#a78bfa', '#f4b942', '#35d6c3', '#ff7b8b', '#46d6a0', '#6e97ff']
    out = '<div class="xp-ui"><p class="xp-ui-h">%s</p><div class="xp-ui-g">' % e(t["uiH"])
    for k,(key,lab) in enumerate(zip("mewstf", t["ui"])):
        out += ('<div class="ui-t u%d" style="--c:%s"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg><span>%s</span></div>' % (k+1, COL[k], IC[key], lab))
    return out + '</div></div>\n'

# icons + accent colours for the four explorer tabs
XT = [
 ('#6e97ff', '<rect x="3" y="4" width="18" height="16" rx="2.5"/><path d="M3 9h18M7 6.5h.01M10 6.5h.01"/>'),
 ('#a78bfa', '<path d="M4 7h9M17 7h3M4 17h3M11 17h9"/><circle cx="15" cy="7" r="2"/><circle cx="9" cy="17" r="2"/><path d="M4 12h5M13 12h7"/><circle cx="11" cy="12" r="2"/>'),
 ('#ff7ab6', '<circle cx="12" cy="12" r="9"/><circle cx="8.5" cy="10" r="1.2"/><circle cx="12" cy="7.5" r="1.2"/><circle cx="15.5" cy="10" r="1.2"/>'),
 ('#5ec8ff', '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>'),
 ('#7be37b', '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 13a3 3 0 0 1 5.2-2M15 13a3 3 0 0 1-5.2 2"/>'),
 ('#f4b942', '<path d="M12 3v18"/><path d="M16.5 7.5C16.5 6 14.5 5 12 5S7.5 6 7.5 7.8 9.5 10.5 12 11s4.5 1.3 4.5 3.2S14.5 18 12 18s-4.5-1-4.5-2.5"/>'),
 ('#35d6c3', '<path d="M12 3a9 9 0 1 0 9 9h-9z"/><path d="M15.5 3.6A9 9 0 0 1 20.4 8.5H15.5z"/>'),
]

T = {
"en": dict(
 lang="en", dir="ltr", home="/", alt="ar", altlabel="عربي", altlink="ar/index.html", locale="en_US",
 title="3D Print Calculator | Real cost, profit and price for every 3D print",
 desc="Windows app that works out the real cost, net profit and selling price of every 3D print, including material, electricity, maintenance and failure risk. Analyzes G-code, 3MF and STL files. Free forever, with an optional Pro license for PDF invoices, multi-material pricing and business costs.",
 ogt="3D Print Calculator | Know what every print really costs",
 ogd="Real cost, profit and selling price for every 3D print. Free forever for Windows. Pro unlocks PDF invoices, multi-material pricing and business costs.",
 skip="Skip to content", logoalt="3D Print Calculator logo",
 themeLbl="Dark / light mode", nTry="Try it", nApp="Inside the app", nFeat="Features", nGet="Pricing", nFaq="FAQ", nDl="Download",
 h1a="Know what every print", h1b="really costs.",
 sub="Enter the material, weight and print time. 3D Print Calculator adds electricity, maintenance and failure risk, then shows your real cost, your profit and the price to charge.",
 dl="Download Latest Version", buy="Buy Pro License — $39.99",
 meta="Windows · Free forever, Pro is optional",
 labT="Try it with your numbers", reset="Reset", sMat="Material", sW="Model weight", sH="Print time", sM="Profit margin",
 more="More settings", fPr="Material price ($/kg)", fPw="Printer power", fKw="Electricity ($/kWh)", fMt="Maintenance ($/hour)", fFl="Failure risk (%)",
 cProfit="Profit +40%", tFil="Filament cost", tCost="Total real cost", tProfit="Estimated net profit", tPrice="Suggested selling price",
 bMat="Material", bEle="Electricity", bMnt="Maintenance", bFail="Failure protection",
 printed="Printed so far", sceneAlt="Animation of a vase being 3D printed layer by layer while the cost so far counts up",
 note="Quick demo: filament cost only. The free app also adds electricity, maintenance, failure risk and profit. Pro adds PDF invoices and business costs.",
 unitH="h",
 aH="Your whole order in one window",
 aP="Fill in the job on one side, and read the cost, profit and selling price at the top.",
 x0="Full window", x0d="Everything for one order on a single screen.",
 x1="Print parameters", x1d="Material, weight, time, failure risk, electricity and margin.",
 x2="Multi-color (Pro)", x2d="Price each color or material separately.",
 x3="File analysis", x3d="Drop G-code, 3MF or STL. Analyzed offline.",
 x4="Folder watch", x4d="Reads new print files from a folder automatically.",
 x5="Cost, profit and price", x5d="Real cost, net profit and suggested selling price.",
 x6="Cost breakdown", x6d="Material, electricity, maintenance and failure protection.",
 ui=["Material","Electricity","Maintenance","Failure risk","Profit","PDF invoice"], uiH="Inside the window",
 cxExL="Example: a $10 sale", cxNote="Pick a country. Currency, electricity price and exchange rate change with it. Sample values for illustration.", xOpen="Open full size", xAlt="3D Print Calculator app, English interface: print order parameters, cost, profit and selling price tiles and cost breakdown",
 fH="What you get",
 f1h="Cost and profit", f1p="Material, electricity, maintenance and failure risk in one result. Drop a G-code, 3MF or STL file and weight and time are read for you.",
 f2h="PDF invoices (Pro)", f2p="Create invoices in Arabic, English, French or German, with preview and automatic numbering (INV-000001).",
 f3h="Countries and currencies (Pro)", f3p="Supports many Arab and international countries, with their currencies, electricity prices and exchange rates. Free uses the default currency; advanced currency settings are in Pro.",
 f4h="Customer and invoice details (Pro)", f4p="Customer and delivery info, line items, discount, shipping, tax and notes, with multi-page tables.",
 f5h="Remembers your setup", f5p="Language, theme, printer, material and results are saved automatically.",
 f6h="Fast and compact", f6p="Smooth scrolling and a compact layout that fits small screens.",
 amt="Amount", invL="Invoice language",
 ctry="Country", cur="Currency", tier="Electricity, tier 1", rate="Exchange rate", syria="Syria",
 k1="Customer", k2="Delivery", k3="Line items", k4="Discount", k5="Shipping", k6="Tax", k7="Notes", k8="Multi-page tables",
 s1="Language", s2="Theme", s3="Printer", s4="Material", s5="Latest results",
 fit="Window width",
 gH="Free forever. Pro when you need more.",
 g1h="Free — forever", g1p="Download the app and use it as long as you like. No trial, no expiry, no code needed.",
 g1a="Real cost, profit and selling price", g1b="Material, electricity, maintenance, failure risk and margin", g1c="Printer selection, G-code and 3MF analysis", g1d="Single-material workflow, always the latest version",
 g2h="Pro License", g2p="One payment unlocks the business tools. Pay with PayPal or a debit/credit card.",
 g2a="One-time payment, no subscription", g2b="PDF invoices, multi-material and multi-color pricing", g2c="Platform, payment, shipping, packaging and labor costs, plus advanced currencies", g2d="Secure PayPal checkout. Activation Code sent after payment",
 tPP="PayPal / Card", tCR="Crypto (USDT)", cNet="Network", cAmt="Amount", cQr="Scan with Trust Wallet to pay directly", cAddr="Wallet address",
 cTrust="Pay with Trust Wallet", cCopy="Copy address", cOk="Copied ✅", cMail="Email payment screenshot",
 cWarn="Send only USDT on the TRON (TRC20) network. Other networks or coins are lost. After paying, take a screenshot of the payment (showing the TXID) and email it to us with your Device ID.",
 stH="Free needs no code. To upgrade to Pro:",
 steps=["Download and install the program. Free works right away, no code.","To upgrade, open it and copy your Device ID.","Buy the Pro License.","Send us your Device ID (and a payment screenshot if you paid with crypto).","Enter the Activation Code we send you. Pro features unlock."],
 qH="Frequently asked questions",
 faq=[("Is the free version a trial?","No. Free is permanent: no trial period and no expiry. You can calculate core print costs, edit material, failure, electricity, maintenance and margin, choose your printer, and analyze G-code and 3MF files."),
      ("What is locked in Free?","PDF invoices, multi-material and multi-color printing, extra business costs (platform fee, payment fee, shipping, packaging, labor), and advanced currency and country settings. These unlock with Pro."),
      ("What does Pro add?","PDF invoices, multi-material and multi-color pricing, the business-cost fields above, and advanced currency settings with exchange rates. Pro is a one-time payment, no subscription."),
      ("What is a Device ID?","A code the program shows on the activation screen. You only need it for Pro. We use it to create an Activation Code for your device."),
      ("How do I get my Activation Code?","After payment, send your Device ID to us and we reply with your Activation Code. Enter it in the program to unlock Pro."),
      ("How can I pay?","PayPal or a debit/credit card through the PayPal checkout, or USDT on the TRON (TRC20) network. Apple Pay appears where your region and browser support it."),
      ("Which system does it run on?","Windows. Download the installer (Setup.exe) and run it."),
      ("Will I get new versions?","Yes. The Download button always gives the latest release.")],
 fCon="Contact us", chBtn="Message us", chT="Message us",
 chH="Leave your email and message. We will reply to your email. For activation, include your Device ID (and the TXID if you paid with crypto).",
 chN="Name (optional)", chE="Your email", chM="Your message", chS="Send", chClose="Close",
 mOk="Sent ✅ We will reply to your email.", mBad="Enter a valid email and a message.", mErr="Could not send. Email us directly at "+MAIL, mSend="Sending…",
 ver="Version",
 inv=dict(inv="Invoice", item="Item", qty="Qty", amt="Amount", sub="Subtotal", ship="Shipping", total="Total"),
),
"ar": dict(
 lang="ar", dir="rtl", home="/ar/", alt="en", altlabel="English", altlink="../index.html", locale="ar_AR",
 title="حاسبة الطباعة ثلاثية الأبعاد | التكلفة الحقيقية والربح وسعر البيع لكل طبعة",
 desc="برنامج ويندوز يحسب التكلفة الحقيقية وصافي الربح وسعر البيع لكل طبعة ثلاثية الأبعاد، شاملًا الخامة والكهرباء والصيانة واحتمال الفشل. يحلّل ملفات G-code و3MF و STL. مجاني دائمًا، مع ترخيص Pro اختياري لفواتير PDF والتسعير متعدد المواد وتكاليف الأعمال.",
 ogt="حاسبة الطباعة ثلاثية الأبعاد | اعرف التكلفة الحقيقية لكل طبعة",
 ogd="التكلفة الحقيقية والربح وسعر البيع لكل طبعة ثلاثية الأبعاد. مجاني دائمًا لويندوز. ترخيص Pro يفتح فواتير PDF والتسعير متعدد المواد وتكاليف الأعمال.",
 skip="تخطَّ إلى المحتوى", logoalt="شعار 3D Print Calculator",
 themeLbl="الوضع الداكن / الفاتح", nTry="جرّب الآن", nApp="داخل البرنامج", nFeat="المميزات", nGet="الأسعار", nFaq="الأسئلة الشائعة", nDl="تحميل",
 h1a="اعرف التكلفة الحقيقية", h1b="لكل طبعة.",
 sub="أدخل الخامة والوزن ووقت الطباعة. يضيف البرنامج الكهرباء والصيانة واحتمال الفشل، ثم يعرض لك التكلفة الحقيقية وربحك والسعر الذي تطلبه من الزبون.",
 dl="تحميل أحدث إصدار", buy="شراء ترخيص Pro — $39.99",
 meta="ويندوز · مجاني دائمًا، وPro اختياري",
 labT="جرّب بأرقامك أنت", reset="إعادة ضبط", sMat="الخامة", sW="وزن المجسم", sH="وقت الطباعة", sM="هامش الربح",
 more="إعدادات إضافية", fPr="سعر الخامة ($/كغ)", fPw="استهلاك الطابعة", fKw="الكهرباء ($/ك.و.س)", fMt="الصيانة ($/ساعة)", fFl="احتمال الفشل (%)",
 cProfit="ربح +40%", tFil="تكلفة الفيلمنت", tCost="إجمالي التكلفة الحقيقية", tProfit="صافي الربح المتوقع", tPrice="سعر البيع المقترح",
 bMat="الخامة", bEle="الكهرباء", bMnt="الصيانة", bFail="حماية ضد الفشل",
 printed="المطبوع حتى الآن", sceneAlt="رسم متحرك لمزهرية تُطبع طبقة فوق طبقة بينما تزداد التكلفة المتراكمة",
 note="عرض سريع: يحسب تكلفة الفيلمنت فقط. النسخة المجانية من البرنامج تضيف الكهرباء والصيانة واحتمال الفشل والربح. وPro يضيف فواتير PDF وتكاليف الأعمال.",
 unitH="ساعة",
 aH="طلبيتك كاملة في نافذة واحدة",
 aP="املأ بيانات الطلب من جهة، واقرأ التكلفة والربح وسعر البيع من الأعلى.",
 x0="النافذة كاملة", x0d="كل ما يخص الطلب الواحد على شاشة واحدة.",
 x1="معطيات الطباعة", x1d="الخامة والوزن والوقت والفشل والكهرباء والهامش.",
 x2="أكثر من لون (Pro)", x2d="حساب كل لون أو خامة على حدة.",
 x3="تحليل الملف", x3d="اسحب G-code أو 3MF أو STL، والتحليل محلي.",
 x4="مراقبة المجلد", x4d="قراءة ملفات الطباعة الجديدة تلقائيًا من مجلد.",
 x5="التكلفة والربح والسعر", x5d="التكلفة الحقيقية وصافي الربح وسعر البيع المقترح.",
 x6="توزيع التكلفة", x6d="الخامة والكهرباء والصيانة والحماية ضد الفشل.",
 ui=["الخامة","الكهرباء","الصيانة","احتمال الفشل","الربح","فاتورة PDF"], uiH="ما بداخل النافذة",
 cxExL="مثال: بيع بـ 10 $", cxNote="اختر بلدًا فتتغيّر العملة وسعر الكهرباء وسعر الصرف معه. القيم للتوضيح فقط.", xOpen="فتح بالحجم الكامل", xAlt="واجهة برنامج حاسبة تكلفة الطباعة بالعربية: معطيات الطلبية وبطاقات التكلفة والربح وسعر البيع وتوزيع التكلفة وحالة الطابعة المباشرة",
 fH="على ماذا تحصل",
 f1h="التكلفة والربح", f1p="الخامة والكهرباء والصيانة واحتمال الفشل في نتيجة واحدة. اسحب ملف G-code أو 3MF أو STL ويُقرأ الوزن والوقت تلقائيًا.",
 f2h="فواتير PDF (Pro)", f2p="أنشئ فواتير بالعربية والإنجليزية والفرنسية والألمانية، مع معاينة وترقيم تلقائي (INV-000001).",
 f3h="دول وعملات (Pro)", f3p="يدعم أكثر من بلد عربي وأجنبي، مع عملاتهم وأسعار الكهرباء والصرف. النسخة المجانية تعمل بالعملة الافتراضية، وإعدادات العملات المتقدمة في Pro.",
 f4h="بيانات الزبون والفاتورة (Pro)", f4p="بيانات الزبون والتوصيل وبنود الفاتورة والخصم والشحن والضريبة والملاحظات، مع جدول متعدد الصفحات.",
 f5h="يتذكر إعداداتك", f5p="اللغة والثيم والطابعة والخامة والنتائج تُحفظ تلقائيًا.",
 f6h="سريع ومضغوط", f6p="تمرير سلس وواجهة مضغوطة تناسب الشاشات الصغيرة.",
 amt="المبلغ", invL="لغة الفاتورة",
 ctry="البلد", cur="العملة", tier="الكهرباء، الشريحة 1", rate="سعر الصرف", syria="سوريا",
 k1="الزبون", k2="التوصيل", k3="بنود الفاتورة", k4="الخصم", k5="الشحن", k6="الضريبة", k7="الملاحظات", k8="جداول متعددة الصفحات",
 s1="اللغة", s2="الثيم", s3="الطابعة", s4="الخامة", s5="آخر النتائج",
 fit="عرض النافذة",
 gH="مجاني دائمًا. وPro عندما تحتاج أكثر.",
 g1h="مجاني — للأبد", g1p="حمّل البرنامج واستخدمه بدون حدّ زمني. لا تجربة مؤقتة ولا انتهاء ولا حاجة لرمز.",
 g1a="التكلفة الحقيقية والربح وسعر البيع", g1b="الخامة والكهرباء والصيانة واحتمال الفشل وهامش الربح", g1c="اختيار الطابعة وتحليل ملفات G-code و3MF", g1d="سير عمل بمادة واحدة، ودائمًا آخر إصدار",
 g2h="ترخيص Pro", g2p="دفعة واحدة تفتح أدوات الأعمال. ادفع عبر PayPal أو بطاقة خصم/ائتمان.",
 g2a="دفعة واحدة، بدون اشتراك", g2b="فواتير PDF وتسعير متعدد المواد والألوان", g2c="رسوم المنصة والدفع والشحن والتغليف والعمالة، وإعدادات العملات المتقدمة", g2d="دفع آمن عبر PayPal. يصلك رمز التفعيل بعد الدفع",
 tPP="PayPal / بطاقة", tCR="كريبتو (USDT)", cNet="الشبكة", cAmt="المبلغ", cQr="امسح الكود بتطبيق Trust Wallet وادفع مباشرة", cAddr="عنوان المحفظة",
 cTrust="ادفع بمحفظة Trust Wallet", cCopy="نسخ العنوان", cOk="تم النسخ ✅", cMail="إرسال سكرين شوت الدفع بالبريد",
 cWarn="أرسل USDT فقط على شبكة TRON (TRC20). أي شبكة أو عملة أخرى تضيع. بعد الدفع صوّر شاشة عملية الدفع (يظهر فيها رقم المعاملة TXID) وأرسلها لنا على البريد مع Device ID.",
 stH="النسخة المجانية لا تحتاج رمزًا. للترقية إلى Pro:",
 steps=["حمّل البرنامج وثبّته. النسخة المجانية تعمل فورًا بدون رمز.","للترقية، افتحه وانسخ Device ID.","اشترِ ترخيص Pro.","أرسل لنا Device ID (ولقطة شاشة الدفع إذا دفعت بالكريبتو).","أدخل رمز التفعيل الذي نرسله لك. تُفتح ميزات Pro."],
 qH="الأسئلة الشائعة",
 faq=[("هل النسخة المجانية مجرد تجربة؟","لا. النسخة المجانية دائمة: بدون مدة تجريبية وبدون انتهاء. تحسب تكلفة الطباعة الأساسية، وتعدّل الخامة والفشل والكهرباء والصيانة والهامش، وتختار طابعتك، وتحلّل ملفات G-code و3MF."),
      ("ما المقفل في النسخة المجانية؟","فواتير PDF، والطباعة متعددة المواد والألوان، وتكاليف الأعمال الإضافية (رسوم المنصة ورسوم الدفع والشحن والتغليف والعمالة)، وإعدادات العملات والدول المتقدمة. تُفتح كلها بترخيص Pro."),
      ("ماذا يضيف Pro؟","فواتير PDF، وتسعير متعدد المواد والألوان، وحقول تكاليف الأعمال المذكورة، وإعدادات العملات المتقدمة مع أسعار الصرف. Pro دفعة واحدة بدون اشتراك."),
      ("ما هو Device ID؟","رمز يظهره البرنامج في شاشة التفعيل. تحتاجه فقط لـ Pro. نستخدمه لإنشاء رمز تفعيل لجهازك."),
      ("كيف أحصل على رمز التفعيل؟","بعد الدفع أرسل لنا Device ID، ونرد عليك برمز التفعيل. أدخله في البرنامج لتفتح Pro."),
      ("كيف أدفع؟","عبر PayPal أو بطاقة خصم/ائتمان من صفحة الدفع، أو بعملة USDT على شبكة TRON (TRC20). يظهر Apple Pay حيث تدعمه منطقتك ومتصفحك."),
      ("على أي نظام يعمل؟","ويندوز. حمّل ملف التثبيت (Setup.exe) وشغّله."),
      ("هل أحصل على الإصدارات الجديدة؟","نعم. زر التحميل يعطيك دائمًا آخر إصدار.")],
 fCon="راسلنا", chBtn="راسلنا", chT="راسلنا",
 chH="اترك بريدك ورسالتك وسنرد عليك على بريدك. للتفعيل أرسل Device ID (ومعه TXID إذا دفعت بالكريبتو).",
 chN="الاسم (اختياري)", chE="بريدك الإلكتروني", chM="رسالتك", chS="إرسال", chClose="إغلاق",
 mOk="تم الإرسال ✅ سنرد عليك على بريدك.", mBad="اكتب بريدًا صحيحًا ورسالة.", mErr="تعذّر الإرسال. راسلنا مباشرة على "+MAIL, mSend="جارٍ الإرسال…",
 ver="الإصدار",
 inv=dict(inv="فاتورة", item="البند", qty="الكمية", amt="المبلغ", sub="المجموع الفرعي", ship="الشحن", total="الإجمالي"),
),
}
PROMO = dict(
 en=dict(bar="Halloween sale: 50% off Pro", ends="Ends in", pnote="Halloween offer, 50% off until Oct 31", off="-50%", u="d|h|m|s"),
 ar=dict(bar="عرض الهالوين: خصم 50% على Pro", ends="ينتهي بعد", pnote="عرض الهالوين: خصم 50% حتى 31 تشرين الأول", off="-50%", u="يوم|س|د|ث"),
)
for _l in ("en", "ar"):
    T[_l]["buyReg"] = T[_l]["buy"]
    T[_l]["buy"] = T[_l]["buy"].replace("$39.99", "$19.99")
INV = {
 "en": T["en"]["inv"], "ar": T["ar"]["inv"],
 "fr": dict(inv="Facture", item="Article", qty="Qté", amt="Montant", sub="Sous-total", ship="Livraison", total="Total"),
 "de": dict(inv="Rechnung", item="Artikel", qty="Menge", amt="Betrag", sub="Zwischensumme", ship="Versand", total="Gesamt"),
}
# hotspots on the real screenshots, in percent of the image: x, y, w, h
HOT = {
 "en": [(0,0,0,0),(2.1,5.1,46.0,52.8),(2.1,58.8,46.0,8.1),(2.1,71.2,46.0,15.9),(2.1,87.9,46.0,6.9),(50.2,4.6,47.7,11.3),(50.1,16.7,47.9,79.3)],
 "ar": [(0,0,0,0),(51.0,5.1,46.1,52.6),(51.0,58.3,46.1,7.9),(51.0,71.2,46.1,15.7),(51.0,87.6,46.1,7.0),(1.25,4.5,47.7,11.2),(1.0,16.6,48.1,79.5)],
}
CMP = [  # (English, Arabic, Free, Pro)  1 = yes, 0 = no, text = shown as is
 ("No expiry, no trial period", "بدون انتهاء وبدون مدة تجريبية", 1, 1),
 ("Core cost and selling price", "حساب التكلفة وسعر البيع الأساسي", 1, 1),
 ("Edit material, failure risk, electricity, maintenance and margin", "تعديل الخامة والفشل والكهرباء والصيانة والهامش", 1, 1),
 ("Pricing method (net margin or markup)", "طريقة التسعير (هامش صافٍ أو نسبة فوق التكلفة)", 1, 1),
 ("Printer selection", "اختيار الطابعة", 1, 1),
 ("G-code and 3MF analysis (STL estimate)", "تحليل ملفات G-code و3MF (وتقدير STL)", 1, 1),
 ("Automatic folder watch", "مراقبة مجلد تلقائيًا", 1, 1),
 ("Recent operations log", "سجل العمليات الأخيرة", 1, 1),
 ("Electricity tier 2", "شريحة الكهرباء 2", 0, 1),
 ("PDF invoices", "فواتير PDF", 0, 1),
 ("Multi-material and multi-color printing", "الطباعة متعددة المواد والألوان", 0, 1),
 ("Platform fee", "رسوم المنصة", 0, 1),
 ("Payment fee", "رسوم الدفع", 0, 1),
 ("Shipping", "الشحن", 0, 1),
 ("Packaging", "التغليف", 0, 1),
 ("Labor", "العمل اليدوي", 0, 1),
 ("Exchange rate and advanced currency settings", "سعر الدولار وإعدادات العملات المتقدمة", 0, 1),
 ("Country selection", "اختيار الدولة", ("Syria only", "سوريا فقط"), 1),
 ("Needs an Activation Code", "يحتاج رمز تفعيل", 0, 1),
]
CMPT = dict(en=dict(h="Free vs Pro, feature by feature", f="Feature", a="Free", b="Pro", y="Included", n="Not included"),
            ar=dict(h="الفرق بين Free وPro، ميزة بميزة", f="الميزة", a="Free", b="Pro", y="موجود", n="غير موجود"))
def cmp_html(t):
    L = t["lang"]; c = CMPT[L]; i = 0 if L == "en" else 1
    def cell(v):
        if isinstance(v, tuple): return '<td class="cm-t">%s</td>' % v[i]
        return '<td class="cm-y" aria-label="%s">✅</td>' % c["y"] if v else '<td class="cm-n" aria-label="%s">❌</td>' % c["n"]
    rows = "".join('<tr><th scope="row">%s</th>%s%s</tr>\n' % (r[i], cell(r[2]), cell(r[3])) for r in CMP)
    return ('<section class="sec" id="compare"><div class="wrap">\n  <div class="sec-head"><h2>%s</h2></div>\n'
            '  <div class="cm-wrap"><table class="cm">\n  <thead><tr><th scope="col">%s</th><th scope="col">%s</th><th scope="col">%s</th></tr></thead>\n  <tbody>\n%s  </tbody></table></div>\n</div></section>\n\n'
            % (c["h"], c["f"], c["a"], c["b"], rows))
e = html.escape

def head(t, path):
    L = t["lang"]; P = "../" if L == "ar" else ""
    url = SITE + ("/ar/" if L == "ar" else "/")
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": L,
              "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    app_ld = {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "3D Print Calculator",
              "alternateName": "حاسبة الطباعة ثلاثية الأبعاد", "operatingSystem": "Windows",
              "applicationCategory": "BusinessApplication", "description": t["desc"], "url": url,
              "downloadUrl": DL, "image": SITE + "/og.png", "inLanguage": ["en", "ar"],
              "featureList": ["Real cost, net profit and selling price per print", "Material, electricity, maintenance and failure-risk breakdown",
                              "PDF invoices in Arabic, English, French and German"],
              "offers": [{"@type": "Offer", "name": "Free", "price": "0", "priceCurrency": "USD", "availability": "https://schema.org/InStock", "url": DL},
                         {"@type": "Offer", "name": "Pro", "price": "39.99", "priceCurrency": "USD", "availability": "https://schema.org/InStock", "url": url + "#get"}]}
    redirect = ""
    if L == "en":
        redirect = '<script>try{var l=localStorage.getItem("lang");if(l==="ar"||(!l&&/^ar/i.test(navigator.language||"")))location.replace("ar/index.html")}catch(e){}</script>\n'
    return f'''<!DOCTYPE html>
<html lang="{L}" dir="{t["dir"]}" class="hw">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#0a1124">
<script>try{{var t=localStorage.getItem("theme");if(t!=="light"&&t!=="dark")t=matchMedia("(prefers-color-scheme: light)").matches?"light":"dark";document.documentElement.setAttribute("data-theme",t)}}catch(e){{document.documentElement.setAttribute("data-theme","dark")}}</script>
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{SITE}/">
<link rel="alternate" hreflang="ar" href="{SITE}/ar/">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="3D Print Calculator">
<meta property="og:locale" content="{t["locale"]}">
<meta property="og:title" content="{e(t["ogt"])}">
<meta property="og:description" content="{e(t["ogd"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(t["ogt"])}">
<meta name="twitter:description" content="{e(t["ogd"])}">
<meta name="twitter:image" content="{SITE}/og.png">
<link rel="icon" href="{P}favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="{P}favicon.png">
<link rel="preload" href="{P}fonts/poppins-bold.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="{P}fonts/{"ibm-plex-sans-arabic-arabic-600-normal.woff2" if L=="ar" else "poppins-regular.woff"}" as="font" type="font/{"woff2" if L=="ar" else "woff"}" crossorigin>
<script>document.documentElement.className+=" js";if(Date.now()>new Date("{PROMO_END}").getTime())document.documentElement.classList.remove("hw")</script>
{redirect}<link rel="stylesheet" href="{P}site.css">
<script type="application/ld+json">{json.dumps(app_ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
</head>
'''

def page(L):
    t = T[L]; P = "../" if L == "ar" else ""
    o = [head(t, L)]
    A = o.append
    A(f'''<body>
<a class="skip" href="#main">{t["skip"]}</a>
<div class="promo" id="promo" data-promo-only data-end="{PROMO_END}" data-u="{PROMO[L]["u"]}"><span class="pb"><i class="pk"></i>{PROMO[L]["bar"]}</span><span class="pe">{PROMO[L]["ends"]}</span><span class="cd" dir="ltr" data-cd></span><a class="pl" href="#buy">{t["buy"].split(" — ")[0]} →</a></div>
<div class="hwdeco" aria-hidden="true"><svg width="0" height="0" style="position:absolute"><defs>
<symbol id="bat" viewBox="0 0 64 28"><path d="M32 9 L29 3 L27 10 L20 7 L10 8 L0 15 L7 14 L12 18 L18 15 L24 19 L29 17 L32 23 L35 17 L40 19 L46 15 L52 18 L57 14 L64 15 L54 8 L44 7 L37 10 L35 3 L32 9Z" fill="currentColor"/></symbol>
<symbol id="pk" viewBox="0 0 120 100"><defs><radialGradient id="pkg" cx=".5" cy=".4" r=".7"><stop offset="0" stop-color="#ffb347"/><stop offset=".6" stop-color="#ff7a00"/><stop offset="1" stop-color="#c24a00"/></radialGradient></defs>
<path d="M56 20c-1-9 2-14 9-16 0 6-2 11-5 16z" fill="#4c7a1f"/><path d="M54 22c0-6 3-9 8-10l2 4c-3 1-5 3-5 7z" fill="#3b5f17"/>
<ellipse cx="34" cy="58" rx="27" ry="36" fill="url(#pkg)"/><ellipse cx="86" cy="58" rx="27" ry="36" fill="url(#pkg)"/><ellipse cx="60" cy="56" rx="30" ry="39" fill="url(#pkg)"/>
<path d="M40 24c-9 14-9 52 0 66M80 24c9 14 9 52 0 66M60 17v78" stroke="#b83f00" stroke-width="1.6" fill="none" opacity=".5"/>
<path d="M33 52l10-18 10 18z M67 52l10-18 10 18z M54 62l6-10 6 10z" fill="#ffe27a"/>
<path d="M30 68l9 12 8-9 7 10 6-10 7 10 8-9 9 12c-8 10-20 14-27 14s-19-4-27-14z" fill="#ffe27a"/></symbol>
<symbol id="gh" viewBox="0 0 80 100"><path d="M8 96V42C8 18 22 4 40 4s32 14 32 38v54l-11-10-10 10-11-10-10 10-10-10z" fill="#f4eeff"/><ellipse cx="29" cy="40" rx="5" ry="8" fill="#2a1550"/><ellipse cx="51" cy="40" rx="5" ry="8" fill="#2a1550"/><ellipse cx="40" cy="62" rx="7" ry="10" fill="#2a1550"/></symbol>
<symbol id="sp" viewBox="0 0 48 40"><g stroke="#cbb6ff" stroke-width="2" fill="none" stroke-linecap="round"><path d="M18 20L5 10 2 18M18 22L4 24 3 33M19 25L9 36M30 20L43 10 46 18M30 22L44 24 45 33M29 25L39 36"/></g><circle cx="24" cy="26" r="9" fill="#150826" stroke="#cbb6ff" stroke-width="1.2"/><circle cx="24" cy="15" r="6" fill="#150826" stroke="#cbb6ff" stroke-width="1.2"/><circle cx="22" cy="14" r="1.6" fill="#ff5a3c"/><circle cx="26" cy="14" r="1.6" fill="#ff5a3c"/></symbol>
</defs></svg><span class="web wl"></span><span class="web wr"></span><svg class="fl g1" viewBox="0 0 80 100"><use href="#gh"/></svg><svg class="fl g2" viewBox="0 0 80 100"><use href="#gh"/></svg><svg class="fl p1 jl" viewBox="0 0 120 100"><use href="#pk"/></svg><svg class="fl p2 jl" viewBox="0 0 120 100"><use href="#pk"/></svg></div>
<header class="top"><span class="spider hs" aria-hidden="true"><i></i><svg width="40" height="34"><use href="#sp"/></svg></span><div class="wrap bar">
  <a class="logo" href="index.html"><img src="{P}logo.png" width="38" height="38" alt="{e(t["logoalt"])}">3D Print Calculator</a>
  <nav aria-label="Main">
    <a class="nl" href="#try">{t["nTry"]}</a>
    <a class="nl" href="#app">{t["nApp"]}</a>
    <a class="nl" href="#features">{t["nFeat"]}</a>
    <a class="nl" href="#get">{t["nGet"]}</a>
    <a class="nl" href="#faq">{t["nFaq"]}</a>
    <button class="theme" id="theme" type="button" aria-label="{t["themeLbl"]}" title="{t["themeLbl"]}"><svg class="i-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg><svg class="i-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
    <a class="lang" id="lang" href="{t["altlink"]}" hreflang="{t["alt"]}" lang="{t["alt"]}">{t["altlabel"]}</a>
    <a class="btn sm" href="#get">{t["nDl"]}</a>
  </nav>
</div></header>

<main id="main">
<section class="hero" id="top"><div class="hw-moon" aria-hidden="true"><svg class="mb m1" viewBox="0 0 64 28"><use href="#bat"/></svg><svg class="mb m2" viewBox="0 0 64 28"><use href="#bat"/></svg><svg class="mb m3" viewBox="0 0 64 28"><use href="#bat"/></svg></div>
<div class="wrap hero-grid">
  <div class="hero-copy">
    <h1><span class="a">{t["h1a"]}</span><span>{t["h1b"]}</span></h1>
    <p class="hero-sub">{t["sub"]}</p>
    <div class="cta">
      <a class="btn" href="{DL}" rel="noopener">{t["dl"]}</a>
      <a class="btn ghost" href="#buy" data-reg-text="{t["buyReg"]}">{t["buy"]}</a>
    </div>
    <p class="meta"><span id="ver"></span>{t["meta"]}</p>
  </div>

  <div class="stage">{floaters_html(t)}
  <div class="lab" id="lab" style="--fil:#a78bfa"><div id="try"></div>
    <div class="lab-head"><h2>{t["labT"]}</h2><button type="button" id="reset">{t["reset"]}</button></div>
    <div class="lab-top">
      {scene_html(t)}
      <div class="tiles" aria-live="polite">
        <div class="tile t-cost"><span>{t["tFil"]}</span><b id="oc">$1.50</b></div>
        <div class="tile t-profit"><span>{t["tProfit"]}</span><b id="on">$0.60</b></div>
        <div class="tile t-price"><span>{t["tPrice"]}</span><b id="op">$2.10</b></div>
      </div>
    </div>
    <div class="ctl">
      <div>
        <div class="ctl-label"><span id="lm">{t["sMat"]}</span></div>
        <div class="mats" role="radiogroup" aria-labelledby="lm">
          <button type="button" class="mat" role="radio" aria-checked="true" data-m="PLA" data-p="10" data-c="#a78bfa" style="--c:#a78bfa"><i></i>PLA</button>
          <button type="button" class="mat" role="radio" aria-checked="false" data-m="PETG" data-p="11" data-c="#35d6c3" style="--c:#35d6c3"><i></i>PETG</button>
          <button type="button" class="mat" role="radio" aria-checked="false" data-m="ABS" data-p="9" data-c="#fb923c" style="--c:#fb923c"><i></i>ABS</button>
          <button type="button" class="mat" role="radio" aria-checked="false" data-m="TPU" data-p="15" data-c="#f472b6" style="--c:#f472b6"><i></i>TPU</button>
        </div>
      </div>
      <div><label class="ctl-label" for="rw"><span>{t["sW"]}</span><output id="ow" for="rw">150 g</output></label>
        <input id="rw" type="range" min="10" max="1000" step="10" value="150" style="--p:14.1%"></div>
      <div class="ctl-2">
        <div><label class="ctl-label" for="rh"><span>{t["sH"]}</span><output id="oh" for="rh">6 {t["unitH"]}</output></label>
          <input id="rh" type="range" min="0.5" max="48" step="0.5" value="6" style="--p:11.6%"></div>
        <div><label class="ctl-label" for="rm"><span>{t["sM"]}</span><output id="om" for="rm">40%</output></label>
          <input id="rm" type="range" min="0" max="150" step="5" value="40" style="--p:26.7%"></div>
      </div>
    </div>
    <p class="lab-note">{t["note"]}</p>
  </div>
  </div>
</div></section>

<section class="sec alt" id="app"><div class="wrap">
  <div class="sec-head"><h2>{t["aH"]}</h2><p>{t["aP"]}</p></div>
  <div class="xp" id="xp">
''')
    iw, ih = (1920, 1208) if L == "en" else (1920, 1222)
    A(f'''    <div class="xp-frame">
      <div class="xp-bar" aria-hidden="true"><i></i><i></i><i></i><span>3D Print Calculator</span></div>
      <div class="xp-view">
        <div class="xp-stage"><img src="{P}img/app-{L}.webp?v=3" width="{iw}" height="{ih}" loading="lazy" decoding="async" alt="{e(t["xAlt"])}"><div class="xp-hl"></div></div>
        <a class="xp-open" href="{P}img/app-{L}.webp?v=3" target="_blank" rel="noopener">{t["xOpen"]}</a>
      </div>
    </div>
    <div class="xp-tabs" role="tablist" aria-label="{e(t["aH"])}">
''')
    for i in range(7):
        x, y, w, h = HOT[L][i]
        col, ico = XT[i]
        A(f'      <button type="button" role="tab" class="xp-tab" style="--c:{col}" aria-selected="{"true" if i==0 else "false"}" data-x="{x}" data-y="{y}" data-w="{w}" data-h="{h}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ico}</svg><b>{t[f"x{i}"]}</b><span>{t[f"x{i}d"]}</span></button>\n')
    A('    </div>\n')
    A(ui_card(t))
    A(f'''  </div>
</div></section>

<section class="sec" id="features"><div class="wrap">
  <div class="sec-head"><h2>{t["fH"]}</h2></div>
  <div class="ft">
    <div class="ft-list" role="tablist" aria-orientation="vertical">
''')
    for i in range(1, 7):
        A(f'      <button type="button" role="tab" class="ft-tab" aria-selected="{"true" if i==1 else "false"}"><b>{t[f"f{i}h"]}</b><span>{t[f"f{i}p"]}</span></button>\n')
    sub = 15.68 + 6.20
    A(f'''    </div>
    <div class="ft-view">
      <div class="fp on" role="tabpanel">
        <div class="stack"><i style="--w:{pct(C["mat"])}%;--c:var(--blue)"></i><i style="--w:{pct(C["ele"])}%;--c:var(--amber)"></i><i style="--w:{pct(C["mnt"])}%;--c:var(--teal)"></i><i style="--w:{pct(C["fail"])}%;--c:var(--red)"></i></div>
        <ul class="legend">
          <li style="--c:var(--blue)"><i></i>{t["bMat"]}<b>{usd(C["mat"])}</b></li>
          <li style="--c:var(--amber)"><i></i>{t["bEle"]}<b>{usd(C["ele"])}</b></li>
          <li style="--c:var(--teal)"><i></i>{t["bMnt"]}<b>{usd(C["mnt"])}</b></li>
          <li style="--c:var(--red)"><i></i>{t["bFail"]}<b>{usd(C["fail"])}</b></li>
        </ul>
        <div class="legend-sum"><span>{t["tPrice"]}</span><b>{usd(C["price"])}</b></div>
      </div>
      <div class="fp" role="tabpanel" hidden>
        <div class="pills" id="invl" role="group" aria-label="{e(t["invL"])}">
          <button type="button" data-l="en" aria-pressed="{"true" if L=="en" else "false"}">English</button><button type="button" data-l="ar" aria-pressed="{"true" if L=="ar" else "false"}">العربية</button><button type="button" data-l="fr" aria-pressed="false">Français</button><button type="button" data-l="de" aria-pressed="false">Deutsch</button>
        </div>
        <div class="paper" id="paper" dir="{t["dir"]}" lang="{L}">
          <div class="ph"><b data-w="inv">{t["inv"]["inv"]}</b><span>INV-000001</span></div>
          <table>
            <thead><tr><th data-w="item">{t["inv"]["item"]}</th><th data-w="qty">{t["inv"]["qty"]}</th><th data-w="amt">{t["inv"]["amt"]}</th></tr></thead>
            <tbody><tr><td dir="ltr">Phone stand (PLA)</td><td>2</td><td dir="ltr">$15.68</td></tr><tr><td dir="ltr">Box lid (PETG)</td><td>1</td><td dir="ltr">$6.20</td></tr></tbody>
          </table>
          <div class="sum"><span data-w="sub">{t["inv"]["sub"]}</span><span dir="ltr">${sub:.2f}</span></div>
          <div class="sum"><span data-w="ship">{t["inv"]["ship"]}</span><span dir="ltr">$3.00</span></div>
          <div class="sum t"><span data-w="total">{t["inv"]["total"]}</span><span dir="ltr">${sub+3:.2f}</span></div>
        </div>
      </div>
      <div class="fp" role="tabpanel" hidden>
        {countries_html(t)}
      </div>
      <div class="fp" role="tabpanel" hidden>
        <div class="chk">
''')
    for i in range(1, 9):
        A(f'          <span style="--d:{(i-1)*.07:.2f}s">{t[f"k{i}"]}</span>\n')
    A(f'''        </div>
      </div>
      <div class="fp" role="tabpanel" hidden>
''')
    for i in range(1, 6):
        A(f'        <div class="sw" style="--d:{(i-1)*.12:.2f}s"><span>{t[f"s{i}"]}</span><i></i></div>\n')
    A(f'''      </div>
      <div class="fp fit" role="tabpanel" hidden>
        <label class="ctl-label" for="fit"><span id="fitcap">{t["fit"]} 100%</span></label>
        <input id="fit" type="range" min="40" max="100" step="1" value="100" style="--p:100%">
        <div class="fit-box" id="fitbox"><div class="fit-grid"><i></i><i></i><i></i><i></i><i></i><i></i></div></div>
      </div>
    </div>
  </div>
</div></section>

<section class="sec alt" id="get"><div class="wrap">
  <div class="sec-head"><h2>{t["gH"]}</h2></div>
  <div class="two">
    <div class="panel free">
      <h3>{t["g1h"]}</h3>
      <p>{t["g1p"]}</p>
      <ul class="ticks"><li>{t["g1a"]}</li><li>{t["g1b"]}</li><li>{t["g1c"]}</li><li>{t["g1d"]}</li></ul>
      <a class="btn" href="{DL}" rel="noopener">{t["dl"]}</a>
    </div>
    <div class="panel buy" id="buy">
      <h3>{t["g2h"]}</h3>
      <div class="price"><s class="old" data-promo-only>$39.99</s> <span data-reg-text="$39.99">$19.99</span> <em class="off" data-promo-only>{PROMO[L]["off"]}</em></div>
      <p class="promo-row" data-promo-only><i class="pk"></i>{PROMO[L]["pnote"]} · {PROMO[L]["ends"]} <span class="cd" dir="ltr" data-cd></span></p>
      <div class="pay-tabs" role="tablist">
        <button type="button" role="tab" id="tabPP" aria-selected="true" aria-controls="viewPP">{t["tPP"]}</button>
        <button type="button" role="tab" id="tabCR" aria-selected="false" aria-controls="viewCR">{t["tCR"]}</button>
      </div>
      <div class="pay-view" id="viewPP" role="tabpanel" aria-labelledby="tabPP">
        <p>{t["g2p"]}</p>
        <ul class="ticks"><li>{t["g2a"]}</li><li>{t["g2b"]}</li><li>{t["g2c"]}</li><li>{t["g2d"]}</li></ul>
        <a class="btn" href="{PAYPAL}" data-reg-href="{PAYPAL_REG}" data-reg-text="{t["buyReg"]}" target="_blank" rel="noopener">{t["buy"]}</a>
      </div>
      <div class="pay-view" id="viewCR" role="tabpanel" aria-labelledby="tabCR" hidden>
        <div class="crypto-box">
          <div class="crypto-info"><p class="k">{t["cNet"]}</p><p class="v net" dir="ltr">USDT · TRON (TRC20)</p></div>
          <div class="crypto-info"><p class="k">{t["cAmt"]}</p><p class="v" dir="ltr"><span data-reg-text="39.99">19.99</span> USDT</p></div>
        </div>
        <div class="qr-wrap"><div class="qr">{QR}</div><p class="qr-cap">{t["cQr"]}</p></div>
        <p class="addr-k">{t["cAddr"]}</p>
        <code class="addr" id="addr">{ADDR}</code>
        <a class="btn" id="trustPay" href="{TRUST}" data-reg-href="{TRUST_REG}" target="_blank" rel="noopener">{t["cTrust"]}</a>
        <button class="btn ghost" type="button" id="copyBtn">{t["cCopy"]}</button>
        <a class="btn ghost" id="mailProof" href="mailto:{MAIL}?subject=Payment%20proof%20-%203D%20Print%20Calculator&amp;body=Device%20ID%3A%20%0A%0A(Attach%20your%20payment%20screenshot%20to%20this%20email)">{t["cMail"]}</a>
        <p class="warn">{t["cWarn"]}</p>
      </div>
    </div>
  </div>
</div></section>

{cmp_html(t)}<section class="sec alt" id="how"><div class="wrap">
  <div class="sec-head"><h2>{t["stH"]}</h2></div>
  <ol class="steps">
''')
    for s in t["steps"]:
        A(f'    <li>{s}</li>\n')
    A(f'''  </ol>
</div></section>

<section class="sec" id="faq"><div class="wrap">
  <div class="sec-head"><h2>{t["qH"]}</h2></div>
  <div class="faq">
''')
    for q, a in t["faq"]:
        A(f'    <details class="q"><summary>{q}</summary><p>{a}</p></details>\n')
    A(f'''  </div>
</div></section>
</main>

<div class="hw-yard" aria-hidden="true"><svg class="yard" viewBox="0 0 1600 200" preserveAspectRatio="xMidYMax slice"><defs><linearGradient id="yf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="rgba(160,100,255,0)"/><stop offset="1" stop-color="rgba(160,100,255,.45)"/></linearGradient></defs><rect width="1600" height="200" fill="url(#yf)"/><g stroke="#05020a" stroke-linecap="round" fill="none"><path d="M150 200C152 150 146 120 150 70" stroke-width="16"/><path d="M148 110C120 95 100 80 80 50M150 90C175 75 195 62 215 30M149 70C140 50 138 32 128 12M150 80C165 55 170 42 182 18M120 92C100 90 85 98 66 92M176 78C195 80 210 74 228 80" stroke-width="6"/></g><path d="M0 200V150Q150 138 320 152T700 148 1000 152 1300 146 1600 150V200Z" fill="#06030c"/><path d="M300 168V141.0a23.0 23.0 0 0 1 46 0V168z" fill="#0b0516" stroke="rgba(190,160,255,.35)" stroke-width="1.4"/><path d="M323.0 134.1v22.5M310.35 144.45h25.3" stroke="rgba(190,160,255,.5)" stroke-width="2"/><path d="M380 170V151.0a19.0 19.0 0 0 1 38 0V170z" fill="#0b0516" stroke="rgba(190,160,255,.35)" stroke-width="1.4"/><path d="M389.5 147.2h19.0M389.5 152.9h19.0" stroke="rgba(190,160,255,.35)" stroke-width="1.5"/><path d="M540 172V145.0a25.0 25.0 0 0 1 50 0V172z" fill="#0b0516" stroke="rgba(190,160,255,.35)" stroke-width="1.4"/><path d="M552.5 140.8h25.0M552.5 148.6h25.0" stroke="rgba(190,160,255,.35)" stroke-width="1.5"/><path d="M780 170V148.0a20.0 20.0 0 0 1 40 0V170z" fill="#0b0516" stroke="rgba(190,160,255,.35)" stroke-width="1.4"/><path d="M800.0 142.0v18.900000000000002M789.0 151.0h22.0" stroke="rgba(190,160,255,.5)" stroke-width="2"/><path d="M860 172V155.0a17.0 17.0 0 0 1 34 0V172z" fill="#0b0516" stroke="rgba(190,160,255,.35)" stroke-width="1.4"/><path d="M868.5 151.6h17.0M868.5 156.7h17.0" stroke="rgba(190,160,255,.35)" stroke-width="1.5"/><path d="M1010 172V146.0a24.0 24.0 0 0 1 48 0V172z" fill="#0b0516" stroke="rgba(190,160,255,.35)" stroke-width="1.4"/><path d="M1022.0 142.0h24.0M1022.0 149.5h24.0" stroke="rgba(190,160,255,.35)" stroke-width="1.5"/><path d="M1090 172V153.0a19.0 19.0 0 0 1 38 0V172z" fill="#0b0516" stroke="rgba(190,160,255,.35)" stroke-width="1.4"/><path d="M1109.0 147.3v17.1M1098.55 155.85h20.900000000000002" stroke="rgba(190,160,255,.5)" stroke-width="2"/><g fill="#06030c"><rect x="1250" y="96" width="190" height="76"/><path d="M1240 98L1345 40 1450 98z"/><rect x="1400" y="50" width="26" height="46"/><path d="M1396 52L1413 22 1430 52z"/><rect x="1262" y="52" width="22" height="46"/><path d="M1258 54L1273 28 1288 54z"/><rect x="1388" y="70" width="14" height="22" fill="#06030c"/></g><g fill="#ffb347" class="win"><rect x="1272" y="110" width="16" height="22"/><rect x="1310" y="110" width="16" height="22"/><rect x="1352" y="110" width="16" height="22"/><rect x="1394" y="110" width="16" height="22"/><rect x="1269" y="70" width="8" height="12"/><rect x="1410" y="68" width="8" height="12"/><rect x="1330" y="76" width="12" height="16"/></g><use href="#pk" class="jl" x="450" y="92" width="84" height="70" style="--d:0.7s"/><use href="#pk" class="jl" x="660" y="100" width="70" height="58" style="--d:0.7s"/><use href="#pk" class="jl" x="940" y="88" width="88" height="73" style="--d:0.7s"/><use href="#pk" class="jl" x="1170" y="104" width="66" height="55" style="--d:0.3s"/><use href="#pk" class="jl" x="250" y="112" width="62" height="52" style="--d:1.7s"/><use href="#pk" class="jl" x="1500" y="96" width="80" height="67" style="--d:0.7s"/></svg></div>
<footer><div class="wrap">
  <span>© 2026 3D Print Calculator</span>
  <nav aria-label="Footer">
    <a href="https://github.com/Pr0fes0rx/3d-print-calculator/releases" rel="noopener">Releases</a>
    <a href="#" id="footContact">{t["fCon"]}</a>
    <a href="{t["altlink"]}" hreflang="{t["alt"]}" lang="{t["alt"]}">{t["altlabel"]}</a>
  </nav>
</div></footer>

<button class="chat-fab" id="chatFab" type="button" aria-expanded="false" aria-controls="chatBox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg><span>{t["chBtn"]}</span></button>
<div class="chat-box" id="chatBox" role="dialog" aria-label="{e(t["chT"])}" hidden>
  <div class="chat-head"><b>{t["chT"]}</b><button type="button" id="chatX" aria-label="{e(t["chClose"])}">&times;</button></div>
  <form id="chatForm" novalidate>
    <p class="chat-hint">{t["chH"]}</p>
    <input id="cn" name="name" type="text" autocomplete="name" placeholder="{e(t["chN"])}" aria-label="{e(t["chN"])}">
    <input id="ce" name="email" type="email" autocomplete="email" required placeholder="{e(t["chE"])}" aria-label="{e(t["chE"])}">
    <textarea id="cm" name="message" required placeholder="{e(t["chM"])}" aria-label="{e(t["chM"])}"></textarea>
    <input class="hp" id="cb" type="text" tabindex="-1" autocomplete="off" aria-hidden="true">
    <button class="btn" type="submit" id="cs">{t["chS"]}</button>
    <div class="chat-msg" id="chatMsg" role="status"></div>
  </form>
</div>

<script>window.I18N={json.dumps(dict(
    ver=t["ver"], copy=t["cCopy"], copied=t["cOk"], mOk=t["mOk"], mBad=t["mBad"], mErr=t["mErr"], mSend=t["mSend"],
    key=WEB3, inv=INV, fit=t["fit"]), ensure_ascii=False)};</script>
<script src="{P}site.js" defer></script>
<script src="{P}promo.js" defer></script>
</body>
</html>
''')
    return "".join(o)

def thanks():
    return f'''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Thank you | 3D Print Calculator</title>
<meta name="theme-color" content="#0a1124">
<script>try{{var t=localStorage.getItem("theme");if(t!=="light"&&t!=="dark")t=matchMedia("(prefers-color-scheme: light)").matches?"light":"dark";document.documentElement.setAttribute("data-theme",t)}}catch(e){{document.documentElement.setAttribute("data-theme","dark")}}</script>
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="preload" href="fonts/poppins-bold.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="site.css">
</head>
<body>
<header class="top scrolled"><div class="wrap bar">
  <a class="logo" href="index.html"><img src="logo.png" width="38" height="38" alt="">3D Print Calculator</a>
  <nav><button class="lang" id="lang" type="button" aria-label="Language" style="background:none;color:inherit;cursor:pointer">عربي</button></nav>
</div></header>
<main class="wrap center">
  <h1 data-t="h">Payment received ✅</h1>
  <p data-t="p">Thank you for your purchase. Download 3D Print Calculator and install it. Open the program, copy your Device ID and send it to us to receive your Activation Code.</p>
  <a class="btn" href="{DL}" data-t="dl">Download 3D Print Calculator</a>
  <p style="margin-top:28px"><span data-t="c">Send your Device ID to:</span> <a href="mailto:{MAIL}">{MAIL}</a></p>
  <p style="font-size:.9rem" data-t="x">Paid with crypto? Attach a screenshot of the payment to the same email.</p>
</main>
<script>
var T={{en:{{}},ar:{{
h:"تم استلام الدفع ✅",
p:"شكرًا لشرائك. حمّل 3D Print Calculator وثبّته. افتح البرنامج، انسخ Device ID وأرسله لنا لتستلم رمز التفعيل.",
dl:"تحميل 3D Print Calculator",
c:"أرسل Device ID إلى:",
x:"دفعت بالكريبتو؟ أرفق لقطة شاشة الدفع في نفس الرسالة."
}}}};
var els=[].slice.call(document.querySelectorAll("[data-t]"));
els.forEach(function(e){{T.en[e.dataset.t]=e.textContent}});
function setLang(l){{
  document.documentElement.lang=l;document.documentElement.dir=l==="ar"?"rtl":"ltr";
  els.forEach(function(e){{e.textContent=T[l][e.dataset.t]}});
  document.getElementById("lang").textContent=l==="ar"?"English":"عربي";
  try{{localStorage.setItem("lang",l)}}catch(x){{}}
}}
var cur="en";
try{{cur=localStorage.getItem("lang")||((navigator.language||"").indexOf("ar")===0?"ar":"en")}}catch(x){{}}
if(cur==="ar")setLang("ar");
document.getElementById("lang").onclick=function(){{cur=cur==="ar"?"en":"ar";setLang(cur)}};
(function(){{
  if(window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches)return;
  var box=document.createElement("div");box.className="confetti";box.setAttribute("aria-hidden","true");
  var cols=["#5b87ff","#35d6c3","#a78bfa","#f4b942","#46d6a0","#f472b6"];
  for(var i=0;i<40;i++){{
    var c=document.createElement("i");
    c.style.left=Math.random()*100+"%";
    c.style.background=cols[i%cols.length];
    c.style.animationDuration=(2.6+Math.random()*2.4)+"s";
    c.style.animationDelay=(Math.random()*1.2)+"s";
    box.appendChild(c);
  }}
  document.body.appendChild(box);
  setTimeout(function(){{box.remove()}},7000);
}})();
</script>
</body>
</html>
'''

def write(path, s):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(s)

write("index.html", page("en"))
write("ar/index.html", page("ar"))
write("thanks.html", thanks())
write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /thanks.html\n\nSitemap: {SITE}/sitemap.xml\n")
write("sitemap.xml", f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url><loc>{SITE}/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE}/"/>
    <xhtml:link rel="alternate" hreflang="ar" href="{SITE}/ar/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/"/>
  </url>
  <url><loc>{SITE}/ar/</loc>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE}/"/>
    <xhtml:link rel="alternate" hreflang="ar" href="{SITE}/ar/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/"/>
  </url>
</urlset>
''')
print("built", {k: round(C[k], 2) for k in C})
