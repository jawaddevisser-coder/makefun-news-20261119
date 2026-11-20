#!/usr/bin/env python3
"""Draw the 19 Nov 2026 world-news front page, 1024x1024 PNG.
Deterministic: no network, no random, no time-dependent input.
Run: python3 draw_news.py  -> writes entry.png next to this file.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (247, 243, 234)
NAVY = (11, 31, 58)
RED = (178, 34, 34)
GOLD = (201, 162, 39)
INK = (20, 20, 20)
GREY = (90, 90, 90)
CARD = (255, 255, 255)
LINE = (210, 205, 190)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_text_block(draw, x, y, max_w, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Masthead
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((36, 18), "THE WORLD IN ONE DAY", font=font(SERIF_B, 44), fill=(255, 255, 255))
d.text((36, 72), "THURSDAY  •  19 NOVEMBER 2026", font=font(SANS_B, 24), fill=GOLD)
d.text((36, 104), "World news, summed up in one picture", font=font(SANS, 20), fill=(220, 225, 235))
d.rectangle([W - 210, 22, W - 36, 118], outline=GOLD, width=3)
d.text((W - 192, 34), "19", font=font(SERIF_B, 44), fill=(255, 255, 255))
d.text((W - 192, 84), "NOV 2026", font=font(SANS_B, 20), fill=GOLD)
d.rectangle([0, 148, W, 156], fill=RED)

# Lead story
y = 176
d.rectangle([28, y, 996, 398], fill=CARD, outline=LINE, width=2)
d.rectangle([28, y, 996, y + 8], fill=RED)
d.text((52, y + 22), "1  •  JUSTICE  •  THE HAGUE", font=font(SANS_B, 20), fill=RED)
d.text((52, y + 52), "WORLD COURT: MYANMAR", font=font(SERIF_B, 40), fill=INK)
d.text((52, y + 98), "COMMITTED GENOCIDE", font=font(SERIF_B, 40), fill=INK)
lead = "The International Court of Justice rules, 9-6, that Myanmar committed genocide against the Rohingya - the first such finding against a state."
yy = draw_text_block(d, 52, y + 150, 920, wrap(d, lead, font(SANS, 21), 920), font(SANS, 21), (50, 50, 50), 28)

# Grid stories
stories = [
    ("2", "SUMMIT • SHENZHEN", (11, 31, 58), "TRUMP, XI & PUTIN MEET", "First three-way summit ends with a joint peace declaration — but no breakthrough on Ukraine."),
    ("3", "WAR • CRIMEA", (178, 34, 34), "UKRAINE HITS CRIMEA BRIDGE", "Third strike on the bridge: the rail section is hit and train traffic is halted."),
    ("4", "CONFLICT • GAZA", (120, 60, 10), "TANKS PUSH INTO GAZA", "Israeli tanks cross the ceasefire line near Nuseirat; the push ends a day after it began."),
    ("5", "MARKETS • NEW YORK", (0, 110, 60), "ANTHROPIC IPO SETS RECORD", "Shares priced at $83, about $81.3bn raised — a record IPO. Trading starts today."),
    ("6", "CULTURE • WORLD", (60, 60, 160), "GTA 6 RELEASES TODAY", "The most anticipated game of the decade launches worldwide; a Van Gogh sells for $190.4m, a record."),
    ("7", "EUROPE • BRUSSELS", (0, 130, 130), "EU OFFERS UKRAINE €45BN", "The European Commission proposes a new €45 billion loan to support Ukraine."),
]

x0, y0 = 28, 418
cw, ch, gap = 476, 168, 16
for i, (num, kicker, color, head, body) in enumerate(stories):
    cx = x0 + (i % 2) * (cw + gap)
    cy = y0 + (i // 2) * (ch + gap)
    d.rectangle([cx, cy, cx + cw, cy + ch], fill=CARD, outline=LINE, width=2)
    d.rectangle([cx, cy, cx + cw, cy + 6], fill=color)
    d.ellipse([cx + 16, cy + 22, cx + 52, cy + 58], fill=color)
    d.text((cx + 27, cy + 28), num, font=font(SANS_B, 22), fill=(255, 255, 255))
    d.text((cx + 66, cy + 24), kicker, font=font(SANS_B, 17), fill=color)
    d.text((cx + 66, cy + 48), head, font=font(SANS_B, 21), fill=INK)
    draw_text_block(d, cx + 16, cy + 82, cw - 32, wrap(d, body, font(SANS, 18), cw - 32), font(SANS, 18), (60, 60, 60), 24)

# Footer strip
fy = 962
d.rectangle([28, fy, 996, 1004], fill=NAVY)
d.text((44, 972), "US Senate blocks Iran war powers 51-48  •  North Korea expands enrichment  •  Bangladesh unrest", font=font(SANS, 17), fill=(255, 255, 255))

img.save("entry.png", "PNG", optimize=True)
print("saved entry.png", img.size)
