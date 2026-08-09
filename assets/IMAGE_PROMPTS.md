# Loom — Image Generation Prompts

Two images make the repo look premium: a **banner** (top of README + GitHub social preview) and a square
**icon/logo** (avatar + favicon). Both prompts are model-agnostic (Midjourney, DALL·E, Firefly, Nano
Banana, Flux, etc.) and tuned to sit beside the sibling projects — **Cairn** (stacked guide-stones),
**Bastion** (guardian shield) — as a matched set; Loom's symbol is a **weaver's loom with threads
converging into one fabric**.

**Shared visual language (keep consistent across both):**
- Premium, minimal, modern open-source dev-tool branding. Flat-geometric with subtle depth, not cartoonish.
- Dark background: deep slate / steel navy (`#0d1117` → `#161b22`, GitHub-dark family).
- Primary mark in brushed steel / cool silver (`#c9d1d9`, `#8b98a5`).
- One accent glow — **thread gold** (`#e3b341`): a single glowing warp thread running through the mark.
- Clean, lots of negative space. Crisp edges. No clutter, no stock-photo realism, no busy textures.

---

## 1) Banner — `loom-banner.png` (≈1774×887, 2:1)

**Prompt:**
> A premium, minimalist horizontal banner for an open-source developer tool called **"Loom"**.
> Centered-left: a sleek geometric emblem of a **stylized weaver's loom frame — vertical warp threads in
> brushed steel converging into a woven fabric grid at the base**, with **one single thread glowing in
> warm gold** running through the weave. To its right, the wordmark **"Loom"** in a clean modern bold
> sans-serif, and beneath it the tagline **"Where one ask becomes the whole fabric"** in a smaller
> light-weight sans-serif. Deep slate / steel-navy background with a very subtle radial glow behind the
> loom. Flat, elegant, high-end, lots of negative space, crisp vector-like edges, soft depth. Tech-brand
> aesthetic, aligned with sibling tools' stone-cairn and shield logos. No people, no realism, no clutter.

**Aspect ratio / size:** 2:1, export ~1774×887 PNG.
**Style keywords:** minimal, geometric, brushed metal, premium SaaS branding, flat with subtle depth, dark mode.
**Negative prompt:** photorealism, busy background, gradients overload, cartoon, mascot, drop-shadow
excess, lens flare, stock imagery, watermark, text errors, misspelled words, low contrast, tangled
threads, sewing machine.

> Tip: if the model misspells "Loom", generate the art WITHOUT text and add the wordmark + tagline
> yourself in Figma/Canva — cleaner typography and guaranteed-correct spelling.

---

## 2) Icon / Logo — `loom-icon.png` (1024×1024, square)

**Prompt:**
> A square app-icon logo for a developer tool called **"Loom"**. A single, bold, minimal emblem: a
> **geometric loom frame with parallel warp threads weaving into a tight fabric grid**, symmetrical,
> brushed steel / cool silver, with **exactly one thread glowing warm gold** woven through the pattern.
> Centered, generous padding, flat-geometric with subtle depth, crisp edges. Deep slate / steel-navy
> background (or transparent). Scales cleanly to a tiny favicon and reads instantly as "weaving /
> completeness". No text, no letters. Modern, premium, open-source brand mark that pairs with sibling
> stone-cairn and shield logos.

**Aspect ratio / size:** 1:1, export 1024×1024 PNG (optionally a transparent-background variant).
**Style keywords:** logomark, emblem, minimal, geometric, symmetric, brushed metal, scalable, dark mode.
**Negative prompt:** text, letters, words, photorealism, clutter, multiple objects, gradients overload,
cartoon, mascot, 3D render noise, watermark, busy detail, sewing machine, spinning wheel.

---

## After you generate them

1. Save the files in this `assets/` folder with the **exact** names above (`loom-banner.png`,
   `loom-icon.png`).
2. The main `README.md` already embeds the banner — it will render automatically.
3. On GitHub: **Settings → General → Social preview** → upload `loom-banner.png`; set the org/profile
   avatar to `loom-icon.png`.
4. Commit and push.
