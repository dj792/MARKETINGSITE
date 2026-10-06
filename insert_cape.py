# -*- coding: utf-8 -*-
"""Insert the CAPE mission slide before the close, then renumber every slide by position."""
import re

P = '/sessions/beautiful-bold-dijkstra/mnt/outputs/build_board_deck.js'
EM = '—'
BANNER = '/* =====================================================================\n   SLIDE '

txt = open(P, encoding='utf-8').read()
assert 'HOW THIS SERVES THE MISSION' not in txt, "CAPE slide already present"

CAPE = '''/* =====================================================================
   SLIDE 17 — Their mission and the four CAPE objectives, made measurable
   ===================================================================== */
{
  const s = pres.addSlide();
  s.background = { color: C.bg };
  eyebrow(s, "HOW THIS SERVES THE MISSION");
  title(s, "Four objectives. Now measurable.", 34, 11.6, 0.60);
  s.addText("\\u201cTo promote and sustain economic prosperity in South Palm Beach County.\\u201d", {
    x: X_LEFT, y: 1.54, w: 11.7, h: 0.32,
    fontFace: F.light, fontSize: 15.5, italic: true, color: C.body,
    valign: "top", margin: 0, isTextBox: true,
  });

  const cape = [
    ["C", "CONNECTING MEMBERS",  "Engagement, event participation, and who is actually showing up.",          "IN THE BUILD", "E3EEF8", C.blue],
    ["A", "ADVANCING COMMERCE",  "Member growth, retention, and which tiers hold over time.",                "LIVE TODAY",   "EEF6E4", "5B9724"],
    ["P", "PROTECTING BUSINESS", "The composition of the businesses we speak for \\u2014 tier, tenure, place.", "LIVE TODAY",   "EEF6E4", "5B9724"],
    ["E", "ENHANCING COMMUNITY", "Reach across the county, city by city, and where it thins out.",            "LIVE TODAY",   "EEF6E4", "5B9724"],
  ];
  const gap = 0.22;
  const cw = (W_CONTENT - gap * 3) / 4;
  const cy = 2.26, ch = 2.86;

  cape.forEach((c, i) => {
    const cx = X_LEFT + i * (cw + gap);
    whiteCard(s, { x: cx, y: cy, w: cw, h: ch });
    s.addText(c[0], {
      x: cx + 0.28, y: cy + 0.22, w: 0.70, h: 0.56,
      fontFace: F.bold, fontSize: 36, bold: true, color: C.blue,
      valign: "middle", margin: 0, isTextBox: true,
    });
    s.addText(c[1], {
      x: cx + 0.28, y: cy + 0.84, w: cw - 0.56, h: 0.46,
      fontFace: F.bold, fontSize: 11.5, bold: true, color: C.navy, charSpacing: 0.8,
      lineSpacingMultiple: 1.06, valign: "top", margin: 0, isTextBox: true,
    });
    s.addText(c[2], {
      x: cx + 0.28, y: cy + 1.34, w: cw - 0.56, h: 0.94,
      fontFace: F.light, fontSize: 11, color: C.body, lineSpacingMultiple: 1.14,
      valign: "top", margin: 0, isTextBox: true,
    });
    s.addShape(pres.ShapeType.roundRect, {
      x: cx + 0.28, y: cy + ch - 0.52, w: 1.36, h: 0.28, rectRadius: 0.5,
      fill: { color: c[4] }, line: { type: "none" },
    });
    s.addText(c[3], {
      x: cx + 0.28, y: cy + ch - 0.52, w: 1.36, h: 0.28,
      fontFace: F.bold, fontSize: 8.5, bold: true, color: c[5], charSpacing: 0.8,
      align: "center", valign: "middle", margin: 0, isTextBox: true,
    });
  });

  s.addText(
    [
      { text: "Your words: ", options: { fontFace: F.light, color: C.muted } },
      { text: "everything we do should ultimately advance this mission.", options: { fontFace: F.bold, bold: true, color: C.ink } },
      { text: "  Now each objective has numbers attached.", options: { fontFace: F.light, color: C.body } },
    ],
    { x: X_LEFT, y: 5.32, w: 11.9, h: 0.38, fontSize: 14,
      valign: "middle", margin: 0, isTextBox: true }
  );
  s.addText("The mission and the four strategic objectives are the Chamber\\u2019s own, from its strategic plan.", {
    x: X_LEFT, y: 5.78, w: 11.9, h: 0.30,
    fontFace: F.light, fontSize: 11, color: C.muted,
    valign: "middle", margin: 0, isTextBox: true,
  });

  footer(s, 17);
  s.addNotes(
    "THIS IS THE CREDIBILITY SLIDE, AND IT IS THEIRS, NOT OURS. The mission and the four CAPE objectives " +
    "are lifted from the Chamber's own strategic plan. Say that out loud \\u2014 you are not proposing a " +
    "framework, you are attaching numbers to the one they already adopted.\\n\\n" +
    "WALK IT IN 45 SECONDS, THEN STOP. Read the mission line, then say that everything in the last twenty " +
    "minutes maps to one of these four.\\n\\n" +
    "THE STATUS TAGS ARE THE HONEST PART, AND THEY MATTER. Three objectives have numbers today; Connecting " +
    "Members does not yet, because engagement and event participation are not captured. Do not gloss that. " +
    "It is the same 'beginning to' promise from the cover, and naming the one gap is what makes the other " +
    "three believable.\\n\\n" +
    "IF A DIRECTOR ASKS WHICH OBJECTIVE IS WEAKEST ON DATA, the answer is Connecting Members \\u2014 and that " +
    "is a good conversation to have, because it is a capture decision they can make now.\\n\\n" +
    "THEN GO TO THE CLOSE. The bridge: three of these four depend on knowing who we are trying to reach, " +
    "which is the one thing the data cannot decide."
  );
}

'''

close_at = [m.start() for m in re.finditer(re.escape(BANNER), txt)
            if 'Closing' in txt[m.start():m.start() + 200]][0]
txt = txt[:close_at] + CAPE + txt[close_at:]

# renumber banners and footers by slide position
idxs = [m.start() for m in re.finditer(re.escape(BANNER), txt)]
out = [txt[:idxs[0]]]
pat = re.compile(r'SLIDE \d+ ' + EM + r' ([^\n]+)')
for i, (a, b) in enumerate(zip(idxs, idxs[1:] + [len(txt)]), 1):
    body = txt[a:b]
    body = re.sub(r'   SLIDE \d+ ' + EM + ' ', '   SLIDE %d %s ' % (i, EM), body, count=1)
    body = re.sub(r'footer\(s, \d+\);', 'footer(s, %d);' % i, body, count=1)
    name = pat.search(body).group(1).strip()[:54]
    print('%2d. %s' % (i, name))
    out.append(body)

open(P, 'w', encoding='utf-8').write(''.join(out))
print('\nCAPE slide inserted and all slides renumbered.')
