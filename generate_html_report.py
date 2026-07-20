# 종목별 데이터를 samsung.html 스타일 템플릿에 채워 리포트 HTML을 생성하는 도구
import json, sys, os

TEMPLATE = '''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name}({ticker}) AI 멀티에이전트 분석 리포트</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;500;700&family=Noto+Sans+KR:wght@300;400;500;700&display=swap" rel="stylesheet">

  <style>
    :root {{
      --colors-canvas: #ffffff;
      --colors-surface-soft: #f5f7f8;
      --colors-primary: #004bff;
      --colors-primary-deep: #0038c7;
      --colors-primary-soft: rgba(0, 75, 255, 0.15);
      --colors-meta-link: #0064e0;

      --colors-ink-deep: #0a1317;
      --colors-ink: #1c2b33;
      --colors-charcoal: #2a3c46;
      --colors-slate: #5b6b73;
      --colors-steel: #8a969c;
      --colors-stone: #b0b8bc;

      --colors-hairline: rgba(10, 19, 23, 0.15);
      --colors-hairline-soft: rgba(10, 19, 23, 0.08);

      --colors-success: #008060;
      --colors-attention: #ffc400;
      --colors-warning: #ffd200;
      --colors-critical: #e11900;

      --font-display: 'Montserrat', sans-serif;
      --font-body: 'Noto Sans KR', sans-serif;

      --rounded-sm: 4px;
      --rounded-md: 6px;
      --rounded-lg: 8px;
      --rounded-xl: 16px;
      --rounded-xxl: 24px;
      --rounded-xxxl: 32px;
      --rounded-full: 100px;

      --spacing-xxs: 4px;
      --spacing-xs: 8px;
      --spacing-md: 12px;
      --spacing-base: 16px;
      --spacing-lg: 20px;
      --spacing-xl: 24px;
      --spacing-xxl: 32px;
      --spacing-xxxl: 40px;
      --spacing-section-sm: 48px;
      --spacing-section: 64px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      background-color: var(--colors-canvas);
      color: var(--colors-ink);
      font-family: var(--font-body);
      font-size: 16px;
      line-height: 1.5;
      letter-spacing: -0.16px;
      -webkit-font-smoothing: antialiased;
    }}

    h1, h2, h3, h4, h5, h6 {{
      font-family: var(--font-display);
      color: var(--colors-ink-deep);
      font-variant-numeric: tabular-nums;
      letter-spacing: -0.02em;
    }}

    a {{ color: var(--colors-meta-link); text-decoration: none; }}

    .top-nav {{
      position: sticky; top: 0; height: 64px;
      background-color: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--colors-hairline-soft);
      z-index: 100; display: flex; align-items: center;
      justify-content: space-between; padding: 0 var(--spacing-xxl);
    }}

    .meta-logo {{
      font-family: var(--font-display); font-weight: 700; font-size: 18px;
      letter-spacing: 0.05em; color: var(--colors-ink-deep);
      display: flex; align-items: center; gap: 6px;
      cursor: pointer;
    }}
    .meta-logo svg {{ fill: var(--colors-primary); }}

    .top-nav-right {{ display: flex; align-items: center; gap: var(--spacing-base); }}
    .btn-nav-back {{
      background: none; border: 1px solid var(--colors-hairline);
      padding: 8px 16px; border-radius: var(--rounded-full);
      font-weight: 500; font-size: 14px; cursor: pointer;
      color: var(--colors-charcoal); transition: all 0.2s;
    }}
    .btn-nav-back:hover {{
      background-color: var(--colors-surface-soft);
      border-color: var(--colors-ink-deep);
    }}

    .promo-banner {{
      background-color: var(--colors-surface-soft);
      padding: var(--spacing-xxl) var(--spacing-xxl);
      border-bottom: 1px solid var(--colors-hairline-soft);
      display: flex; flex-direction: column; gap: var(--spacing-xs);
    }}
    .banner-meta {{
      font-family: var(--font-display); font-weight: 700; font-size: 13px;
      color: var(--colors-slate); letter-spacing: 0.05em;
    }}
    .banner-title {{ font-size: 32px; font-weight: 700; color: var(--colors-ink-deep); }}
    .banner-subtitle {{ font-size: 16px; color: var(--colors-slate); }}

    .main-layout {{
      display: grid; grid-template-columns: 1fr 340px;
      max-width: 1200px; margin: 0 auto;
      padding: var(--spacing-xxl) var(--spacing-xxl);
      gap: var(--spacing-xxxl);
    }}

    .content-area {{ display: flex; flex-direction: column; gap: var(--spacing-section-sm); }}

    .card-feature {{
      background: var(--colors-canvas);
      display: flex; flex-direction: column; gap: var(--spacing-base);
    }}
    .card-title {{
      font-size: 20px; font-weight: 700; color: var(--colors-ink-deep);
      border-bottom: 2px solid var(--colors-ink-deep);
      padding-bottom: var(--spacing-xs);
    }}

    .accordion-group {{ display: flex; flex-direction: column; gap: var(--spacing-xs); }}
    .accordion-item {{
      border: 1px solid var(--colors-hairline-soft);
      border-radius: var(--rounded-lg); overflow: hidden;
      background-color: var(--colors-canvas); transition: border-color 0.2s;
    }}
    .accordion-item:hover {{ border-color: var(--colors-hairline); }}
    .accordion-header {{
      padding: var(--spacing-base); display: flex; justify-content: space-between;
      align-items: center; cursor: pointer; background-color: var(--colors-surface-soft);
      user-select: none;
    }}
    .accordion-title {{ font-size: 16px; font-weight: 700; color: var(--colors-ink-deep); }}
    .accordion-chevron {{
      width: 20px; height: 20px; fill: var(--colors-slate);
      transition: transform 0.2s;
    }}
    .accordion-content {{
      max-height: 0; overflow: hidden; transition: max-height 0.3s ease-out;
    }}
    .accordion-item.open .accordion-content {{
      max-height: 1000px; transition: max-height 0.5s ease-in;
    }}
    .accordion-item.open .accordion-chevron {{ transform: rotate(180deg); }}
    .accordion-inner {{
      padding: var(--spacing-base); border-top: 1px solid var(--colors-hairline-soft);
      display: flex; flex-direction: column; gap: var(--spacing-xs);
      font-size: 15px; color: var(--colors-charcoal);
    }}
    .accordion-inner p {{ margin-bottom: 6px; line-height: 1.6; }}
    .accordion-inner ul {{ padding-left: 20px; margin-bottom: 8px; }}
    .accordion-inner li {{ margin-bottom: 6px; line-height: 1.5; }}

    .info-table {{
      width: 100%; border-collapse: collapse; margin-top: var(--spacing-xs);
      font-size: 14px;
    }}
    .info-table th, .info-table td {{
      padding: 10px 12px; text-align: left;
      border-bottom: 1px solid var(--colors-hairline-soft);
    }}
    .info-table th {{
      background-color: var(--colors-surface-soft);
      color: var(--colors-slate); font-weight: 700;
    }}
    .info-table td {{ color: var(--colors-charcoal); }}

    .case-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: var(--spacing-base); }}
    .case-card {{
      border: 1px solid var(--colors-hairline-soft);
      border-radius: var(--rounded-lg); padding: var(--spacing-base);
    }}
    .case-card.bull {{ border-left: 4px solid var(--colors-success); }}
    .case-card.bear {{ border-left: 4px solid var(--colors-critical); }}
    .case-header {{ font-weight: 700; font-size: 15px; margin-bottom: var(--spacing-xs); }}
    .bull-text {{ color: var(--colors-success); }}
    .bear-text {{ color: var(--colors-critical); }}
    .case-list {{ list-style-type: none; padding-left: 0; }}
    .case-list li {{
      font-size: 14px; color: var(--colors-charcoal); margin-bottom: 8px;
      line-height: 1.5; position: relative; padding-left: 14px;
    }}
    .case-list li::before {{
      content: "•"; position: absolute; left: 0; color: var(--colors-slate);
    }}

    .sticky-rail {{ position: relative; }}
    .card-checkout-summary {{
      position: sticky; top: 88px;
      border: 1px solid var(--colors-hairline);
      border-radius: var(--rounded-xl); padding: var(--spacing-xl);
      background-color: var(--colors-canvas);
      display: flex; flex-direction: column; gap: var(--spacing-base);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
    }}
    .summary-eyebrow {{
      font-family: var(--font-display); font-weight: 700; font-size: 11px;
      color: var(--colors-slate); letter-spacing: 0.05em;
    }}
    .summary-title {{ font-size: 22px; font-weight: 700; color: var(--colors-ink-deep); }}
    .summary-price {{ font-size: 24px; font-weight: 700; color: var(--colors-ink-deep); font-family: var(--font-display); }}
    .summary-divider {{ height: 1px; background-color: var(--colors-hairline-soft); }}

    .options-group-title {{
      font-size: 12px; font-weight: 700; color: var(--colors-slate);
      text-transform: uppercase; letter-spacing: 0.05em;
    }}

    .radio-option {{
      border: 1px solid {accent};
      border-radius: var(--rounded-md); padding: 12px;
      display: flex; justify-content: space-between; align-items: center;
      background-color: {accent_soft};
    }}
    .radio-option-info {{ display: flex; flex-direction: column; gap: 2px; }}
    .radio-title {{ font-size: 14px; font-weight: 700; color: {accent_deep}; }}
    .radio-subtitle {{ font-size: 11px; color: var(--colors-slate); }}
    .radio-badge {{
      background-color: {accent}; color: white;
      font-size: 10px; font-weight: 700; padding: 4px 8px;
      border-radius: var(--rounded-full); font-family: var(--font-display);
    }}

    .detail-row {{ display: flex; justify-content: space-between; font-size: 13px; }}
    .detail-label {{ color: var(--colors-slate); }}
    .detail-val {{ font-weight: 700; color: var(--colors-ink-deep); text-align: right; }}

    .btn-buy-cta {{
      background-color: {accent}; color: white;
      border: none; padding: var(--spacing-base) var(--spacing-base);
      border-radius: var(--rounded-md); font-weight: 700; font-size: 15px;
      cursor: pointer; transition: background-color 0.2s;
    }}
    .btn-buy-cta:hover {{ background-color: {accent_deep}; }}

    .mobile-checkout-bar {{
      display: none; position: fixed; bottom: 0; left: 0; right: 0;
      background-color: var(--colors-canvas);
      border-top: 1px solid var(--colors-hairline);
      padding: var(--spacing-base) var(--spacing-base);
      justify-content: space-between; align-items: center; z-index: 100;
    }}
    .btn-mobile-buy {{
      background-color: {accent}; color: white;
      border: none; padding: 10px 20px; border-radius: var(--rounded-md);
      font-weight: 700; font-size: 14px; cursor: pointer;
    }}

    @media (max-width: 768px) {{
      .main-layout {{ grid-template-columns: 1fr; padding-bottom: 90px; }}
      .sticky-rail {{ display: none; }}
      .mobile-checkout-bar {{ display: flex; }}
    }}
  </style>
</head>
<body>

  <nav class="top-nav">
    <div class="meta-logo" onclick="location.href='../../index.html'">
      <svg width="24" height="24" viewBox="0 0 24 24">
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-2h2v2zm2.07-7.75l-.9.92C13.45 12.9 13 13.5 13 15h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H7c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.04-.42 1.99-1.07 2.75z"/>
      </svg>
      TradingAgents
    </div>
    <div class="top-nav-right">
      <button class="btn-nav-back" onclick="location.href='../../index.html'">목록으로 돌아가기</button>
    </div>
  </nav>

  <header class="promo-banner">
    <span class="banner-meta">AI MULTI-AGENT GENERAL ANALYSIS REPORT</span>
    <h1 class="banner-title">{name} ({ticker})</h1>
    <p class="banner-subtitle">분석 기준일: {date} | 시스템 버전: TradingAgents v0.3.0</p>
  </header>

  <main class="main-layout">

    <div class="content-area">

      <section class="card-feature" id="decision-section">
        <h2 class="card-title">🎯 최종 매매 판단 및 요약</h2>
        <table class="info-table">
          <thead>
            <tr>
              <th style="width: 30%;">항목</th>
              <th>결정 내용</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>최종 판단 (Rating)</strong></td>
              <td><span style="color:{accent}; font-weight:700;">{emoji} {rating_kr}</span></td>
            </tr>
            <tr>
              <td><strong>트레이더 제안 (Action)</strong></td>
              <td><strong>{action}</strong></td>
            </tr>
{extra_rows}
          </tbody>
        </table>

        <div style="margin-top: var(--spacing-base); padding: var(--spacing-base); background-color: var(--colors-surface-soft); border-radius: var(--rounded-md); border-left: 4px solid {accent};">
          <strong>💡 핵심 요약 (Executive Summary):</strong><br>
          <p style="margin-top: 6px; line-height: 1.6; font-size: 14px; color: var(--colors-charcoal);">{summary}</p>
        </div>
      </section>

      <section class="card-feature" id="analysts-section">
        <h2 class="card-title">📊 에이전트별 상세 분석</h2>
        <div class="accordion-group">
{accordion_items}
        </div>
      </section>

      <section class="card-feature" id="bullbear-section">
        <h2 class="card-title">시나리오 분석 (Bull &amp; Bear Case)</h2>
        <div class="case-grid">
          <div class="case-card bull">
            <div class="case-header bull-text">긍정적 요인 (Bull Case)</div>
            <ul class="case-list">
{bull_items}
            </ul>
          </div>
          <div class="case-card bear">
            <div class="case-header bear-text">리스크 요인 (Bear Case)</div>
            <ul class="case-list">
{bear_items}
            </ul>
          </div>
        </div>
      </section>

    </div>

    <aside class="sticky-rail">
      <div class="card-checkout-summary">
        <div class="summary-eyebrow">{name} / {ticker} · {exchange}</div>
        <h3 class="summary-title">{name_en}</h3>
        <div class="summary-price">{price}</div>
        <div class="summary-divider"></div>
        <div class="options-group-title">추천 결론</div>
        <div class="radio-option">
          <div class="radio-option-info">
            <span class="radio-title">{radio_title}</span>
            <span class="radio-subtitle">{radio_subtitle}</span>
          </div>
          <span class="radio-badge">{rating_en}</span>
        </div>
        <div class="summary-divider"></div>
        <div class="options-group-title">가이드라인</div>
{rail_rows}
        <button class="btn-buy-cta" onclick="alert('{name} {rating_kr} 전략을 반영했습니다.')">{cta_label}</button>
      </div>
    </aside>

  </main>

  <div class="mobile-checkout-bar">
    <div>
      <div style="font-size:11px; color:{accent}; font-weight:700;">{emoji} {rating_en}</div>
      <div style="font-family:var(--font-display); font-size:18px; font-weight:700;">{price}</div>
    </div>
    <button class="btn-mobile-buy" onclick="alert('{rating_kr} 전략 반영!')">{cta_label}</button>
  </div>

  <script>
    document.querySelector('.accordion-item').classList.add('open');
  </script>
</body>
</html>
'''

def render(d):
    if d['rating_en'] == 'UNDERWEIGHT':
        accent = 'var(--colors-critical)'
        accent_soft = 'rgba(225,25,0,0.12)'
    elif d['rating_en'] == 'HOLD':
        accent = 'var(--colors-slate)'
        accent_soft = 'rgba(91,107,115,0.12)'
    else:
        accent = 'var(--colors-success)'
        accent_soft = 'var(--colors-primary-soft)'
    accent_deep = accent
    emoji = '🔴' if d['rating_en'] == 'UNDERWEIGHT' else ('⚪' if d['rating_en'] == 'HOLD' else '🟢')

    accordion_items = []
    for i, a in enumerate(d['analysts'], 1):
        lis = '\n'.join(f'  <li><strong>{pt["t"]}:</strong> {pt["d"]}</li>' for pt in a['points'])
        accordion_items.append(f'''          <div class="accordion-item" onclick="this.classList.toggle('open')">
            <div class="accordion-header">
              <span class="accordion-title">{i}️⃣ {a['title']}</span>
              <svg class="accordion-chevron" viewBox="0 0 24 24"><path d="M7.41 8.59L12 13.17l4.59-4.58L18 10l-6 6-6-6 1.41-1.41z"/></svg>
            </div>
            <div class="accordion-content">
              <div class="accordion-inner">
                <ul>
{lis}
</ul>
              </div>
            </div>
          </div>''')

    bull_items = '\n'.join(f'  <li><strong>{p["t"]}:</strong> {p["d"]}</li>' for p in d['bull'])
    bear_items = '\n'.join(f'  <li><strong>{p["t"]}:</strong> {p["d"]}</li>' for p in d['bear'])

    extra_rows = ''
    for label, val in d.get('extra_rows', []):
        extra_rows += f'            <tr>\n              <td><strong>{label}</strong></td>\n              <td>{val}</td>\n            </tr>\n'

    rail_rows = ''
    for label, val, red in d.get('rail_rows', []):
        style = ' style="color:var(--colors-critical);"' if red else ''
        rail_rows += f'        <div class="detail-row">\n          <span class="detail-label">{label}</span>\n          <span class="detail-val"{style}>{val}</span>\n        </div>\n'

    html = TEMPLATE.format(
        name=d['name'], ticker=d['ticker'], date=d['date'],
        accent=accent, accent_deep=accent_deep, accent_soft=accent_soft,
        emoji=emoji, rating_kr=d['rating_kr'], action=d['action'],
        extra_rows=extra_rows, summary=d['summary'],
        accordion_items='\n\n'.join(accordion_items),
        bull_items=bull_items, bear_items=bear_items,
        exchange=d['exchange'], name_en=d['name_en'], price=d['price'],
        radio_title=d['radio_title'], radio_subtitle=d['radio_subtitle'],
        rating_en=d['rating_en'], rail_rows=rail_rows, cta_label=d['cta_label'],
    )
    return html

if __name__ == '__main__':
    data_path = sys.argv[1]
    out_path = sys.argv[2]
    with open(data_path, encoding='utf-8') as f:
        d = json.load(f)
    html = render(d)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'생성됨: {out_path}')
