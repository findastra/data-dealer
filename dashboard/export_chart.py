"""Export the process-flow canvas as a PNG chart.

    pip install playwright && playwright install chromium
    python3 dashboard/build.py
    python3 dashboard/export_chart.py dashboard/index.html diagrams/pipeline-v2.png
"""
import sys, asyncio
from playwright.async_api import async_playwright
src, out = sys.argv[1], sys.argv[2]
JS = r"""
() => {
  const svg = document.querySelector('#pfd');
  svg.setAttribute('width', 1600); svg.setAttribute('height', 1010);
  const style = document.querySelector('style').outerHTML;
  svg.querySelectorAll('.band-note').forEach(t=>{ if(t.textContent.startsWith('Hover')) t.textContent='Blue = AI. Grey = deterministic code.'; });
  svg.querySelectorAll('.hchip text').forEach(t=>{ if(t.textContent.startsWith('This panel')) t.textContent='Ops dashboard · brief · audit feed'; });
  const wrap = document.createElement('div');
  wrap.id = 'export';
  wrap.style.cssText = 'background:#040605;padding:28px 28px 22px;width:1656px;color:#e7ede9;font-family:var(--f-body)';
  wrap.innerHTML = `<div style="display:flex;align-items:baseline;gap:16px;margin-bottom:14px">
     <div style="font:800 30px/1 var(--f-display)">Data Dealer — process flow v2</div>
     <div style="font:500 14px/1 var(--f-mono);color:#8c9a92;letter-spacing:.08em">VERIFIED DATA SUPPLY CHAIN FOR AI · BY ASTRA · OCT 2026</div></div>
     <div style="font:400 14px/1.4 var(--f-body);color:#8c9a92;margin-bottom:12px">Green = money · Red = information / data · Amber = audit / control · Violet = provenance proof · Dotted white = human decision. Blue outline = AI; everything that holds a key or moves money is plain code.</div>`;
  wrap.appendChild(svg);
  document.body.innerHTML = style; document.body.appendChild(wrap);
  return wrap.getBoundingClientRect().height;
}
"""
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":1720,"height":1200}, device_scale_factor=2)
        html = open(src).read()
        await pg.set_content("<!doctype html><html><head><meta charset=utf8></head><body style='margin:0;background:#040605'>"+html+"</body></html>")
        await pg.wait_for_timeout(400)
        await pg.evaluate("document.getElementById('pause').click()")
        h = await pg.evaluate(JS)
        await pg.wait_for_timeout(200)
        await pg.locator('#export').screenshot(path=out)
        print('height', h)
        await b.close()
asyncio.run(main())
