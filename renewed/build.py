#!/usr/bin/env python3
"""Build the homepage with Python's standard library only."""
import json, html, shutil
from pathlib import Path
ROOT = Path(__file__).resolve().parent
D = json.loads((ROOT / 'content.json').read_text(encoding='utf-8'))
OUT = ROOT / 'dist'
OUT.mkdir(exist_ok=True)
(OUT / 'assets').mkdir(exist_ok=True)
for f in (ROOT / 'assets').iterdir():
 if f.is_file(): shutil.copy(str(f),str(OUT / 'assets' / f.name))
def e(s): return html.escape(str(s),quote=True)
def listing(items): return '<ul class="records">'+''.join('<li>'+e(i)+'</li>' for i in items)+'</ul>'
def social_links(prefix='./', link_class=''):
 icons={'facebook':'M13.5 22v-9h3l.5-3h-3.5V8c0-.9.3-1.5 1.5-1.5h2V3.8c-.4-.1-1.6-.3-2.9-.3-2.9 0-4.6 1.8-4.6 4.9V10H6.5v3h3v9z','twitter':'M18.9 2H22l-6.8 7.8L23.2 22h-6.3l-5-7.6L5.2 22H2l8.4-9.7L.8 2h6.5l4.6 7zM17.8 20h1.7L6.2 4H4.4z'}
 links=[]
 for key,label in [('facebook','Facebook'),('twitter','X')]:
  links.append('<a class="'+link_class+'" href="'+e(D[key])+'"><svg class="social-icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="'+icons[key]+'"/></svg>'+label+'</a>')
 links.append('<a class="'+link_class+'" href="'+e(D['researchmap'])+'">researchmap ↗</a>')
 return ''.join(links)
def page(slug,title,body):
 prefix='./' if not slug else '../'
 nav=''.join('<a '+('aria-current="page" ' if slug==key else '')+'href="'+prefix+key+'/">'+label+'</a>' for key,label in [('profile','プロフィール'),('career','経歴'),('works','研究業績'),('tools','公開ツール'),('training','人材育成')])
 markup='''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+e(title)+' | '+e(D['english'])+'''</title><meta name="description" content="'''+e(D['description'])+'''"><meta name="theme-color" content="#fafafa"><link rel="icon" href="'''+prefix+'''assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="'''+prefix+'''assets/site.css?v=story-headings-1"><script defer src="'''+prefix+'''assets/site.js"></script></head><body><a class="skip" href="#main">本文へ移動</a><header class="header"><a class="brand" href="'''+prefix+'''">Takuya Kubo</a><button class="menu" aria-expanded="false" aria-controls="navigation">メニュー</button><nav id="navigation" aria-label="メインナビゲーション">'''+nav+'''</nav></header><main id="main">'''+body+'''</main><footer><div><a class="brand" href="'''+prefix+'''">Takuya Kubo</a></div><div>'''+social_links(prefix)+'''<p>© 2026 Takuya Kubo</p></div></footer></body></html>'''
 target=OUT / slug if slug else OUT; target.mkdir(exist_ok=True); (target/'index.html').write_text(markup,encoding='utf-8')
def profile_story():
 headings={0:'日本語教育から心理言語学へ',1:'URAから研究IRへ',4:'転職とキャリア',6:'これからの人材育成'}
 parts=[]
 for index,paragraph in enumerate(D['profile_paragraphs']):
  if index in headings: parts.append('<h3 class="story-subheading">'+headings[index]+'</h3>')
  parts.append('<p>'+e(paragraph).replace('「ゆるコンペ」','「<a class="text-link" href="https://ra-skillpro.github.io/Yuru-Competition/">ゆるコンペ</a>」')+'</p>')
 return ''.join(parts)
def heading(kicker,title,desc=''): return '<section class="page-head"><p class="eyebrow">'+kicker+'</p><h1>'+title+'</h1><p>'+desc+'</p></section>'
def toolcards(prefix='./'):
 return ''.join('<a class="tool-card" href="'+e(t['url'])+'"><div class="tool-image"><img loading="lazy" src="'+prefix+'assets/'+t['image']+'" alt="'+e(t['title'])+'の画面"></div><div class="tool-copy"><span class="eyebrow">'+e(t['category'])+'</span><h3>'+e(t['title'])+' <span>↗</span></h3><p>'+e(t['description'])+'</p></div></a>' for t in D['tools'] if t['slug'] in ('kaken_app','sanren_app'))
body='<section class="home-intro"><div class="home-bio"><h1>'+e(D['name'])+'</h1><p class="english-name">'+e(D['english'])+' / '+e(D['degree'])+'</p><p>'+e(D['affiliation'])+'<br>'+e(D['position'])+'</p><p class="intro">'+e(D['home_description']).replace('\n','<br>')+'</p><div class="external-links">'+social_links('./')+'</div></div><img class="home-portrait" src="./assets/portrait-researchmap.jpg" alt="久保琢也の顔写真"></section>'
body+='<section class="section recent-activities"><h2>最近の取り組み</h2><div class="activities-grid">'
for activity in D['recent_activities']:
 body+='<article class="recent-activity"><h3>'+e(activity['title'])+'</h3>'
 if activity.get('image'): body+='<figure class="activity-preview'+(' yuru-preview' if activity['image']=='yuru-home.jpg' else '')+'"><img loading="lazy" src="./assets/'+e(activity['image'])+'" alt="'+e(activity.get('image_alt',activity['title']))+'"><figcaption>'+e(activity.get('image_caption',activity.get('image_alt',activity['title'])))+'</figcaption></figure>'
 if activity['description']: body+='<p>'+e(activity['description'])+'</p>'
 if activity['url']:
  activity_url=activity['url'] if activity['url'].startswith('https://') else './'+activity['url']
  body+='<a class="text-link" href="'+e(activity_url)+'">'+e(activity.get('link_label','詳しく見る →'))+'</a>'
 body+='</article>'
body+='</div></section>'
page('','ホーム',body)
page('profile','プロフィール',heading('ABOUT','プロフィール','これまでのこと、今のこと')+'<section class="section family-section"><div class="family-copy"><h2>わが家</h2><p>妻と私、子ども2人、猫2匹と暮らしています。<br>横浜市在住</p></div><figure class="family-drawing"><img src="../assets/family.svg?v=9" alt="妻と私、長女と長男、ハチワレとキジトラの猫2匹の家族図"></figure></section><section class="section hobbies-section"><h2>趣味</h2><p>小学校から大学までバスケットボールをしてきましたが、働き出してからは殆どボールに触れず、子供が生まれてからは運動もろくにできませんでした。子供がある程度大きくなってからは一緒に動物園に行ったりサファリに行ったりするのが休日の楽しみです。最近はやっとジムに行けるようになったので、ぼちぼち肉体改造に取り組んでいます。</p></section><section class="section profile-story"><h2>これまでの歩み</h2>'+profile_story()+'<a class="text-link" href="../career/">詳しい経歴を見る →</a></section>')
career_body=heading('CAREER','経歴','職歴・学歴・委員歴・受賞歴の記録。')+'<section class="section"><nav class="section-nav" aria-label="経歴の分類">'+''.join('<a href="#'+key+'">'+label+'</a>' for key,label in [('career','職歴'),('education','学歴'),('committees','委員歴'),('awards','受賞歴')])+'</nav>'
for key,label in [('career','職歴'),('education','学歴'),('committees','委員歴'),('awards','受賞歴')]:
 career_body+='<section class="record-section" id="'+key+'"><h2>'+label+'</h2>'+listing(D[key])+'</section>'
career_body+='<p class="note">職歴・委員歴・受賞歴はresearchmap、学歴は旧サイトの情報を参照しています。確認日：'+e(D['source_date'])+'。<a href="'+e(D['researchmap'])+'">researchmap ↗</a></p></section>'
page('career','経歴',career_body)
page('works','研究業績',heading('RESEARCH ARCHIVE','研究業績','論文、学会発表、研究助成の記録。')+'<section class="section"><label class="search-label" for="record-search">業績を検索</label><input id="record-search" type="search" placeholder="キーワード・著者・年で検索"><p id="search-status" role="status"></p><nav class="section-nav" aria-label="業績の分類">'+''.join('<a href="#'+key+'">'+label+'</a>' for key,label in [('publications','論文'),('talks','発表'),('funding','研究助成')])+'</nav>'+''.join('<section class="record-section" id="'+key+'"><h2>'+label+'</h2>'+listing(D[key])+'</section>' for key,label in [('publications','論文'),('talks','発表'),('funding','研究助成')])+'<p class="note">researchmapの掲載情報を反映しています（2026年10月11日確認）。<a href="https://researchmap.jp/kubotaku">researchmapで最新情報を見る ↗</a></p></section>')
page('tools','公開ツール',heading('OPEN TOOLS','公開ツール','オープンデータを活用した研究IRのための分析ツール')+'<section class="section"><div class="tool-grid tools-list">'+toolcards('../')+'</div><p class="note">外部アプリの運用状況・収録データの更新時点は、リンク先でご確認ください。</p></section>')
for t in D['tools']:
 page(t['slug'],t['title'],heading(e(t['category']),e(t['title']),e(t['description']))+'<section class="section tool-detail"><a class="button" href="'+e(t['url'])+'">アプリを開く ↗</a><p class="note">外部サービス（shinyapps.io）へ移動します。</p><img src="../assets/'+t['image']+'" alt="'+e(t['title'])+'の画面"><a class="text-link" href="../tools/">← ツール一覧へ</a></section>')

training=heading('LEARNING & DEVELOPMENT','人材育成','勉強会や実践を通じて、学び合う場をつくる。')
training+='<section class="section"><h2>研究IRのためのR言語勉強会</h2><p>他機関のURA等を対象に、研究IRのためのR言語の勉強会を開催してきました。研究IRの実務を想定し、必要な知識やスキルから逆算して手を動かしながらR言語を学習できるよう工夫を行いました。</p><ul class="training-records"><li>R言語勉強会（2020年10月〜2021年3月）</li><li>R言語勉強会（2021年11月〜2022年7月）</li><li>R言語勉強会（2023年5月〜2024年4月）</li></ul></section>'
training+='<section class="section"><h2>RA協議会スキルプログラム専門委員会</h2><p>URA等の研究開発マネジメント人材向けの研修の企画、運営に携わってきました。特に、私自身が主体として行ってきた企画は以下のとおりです。</p><ul class="training-records"><li>研究IRハンズオン：Power BI研修（2025年11月）</li><li><a class="text-link" href="https://ra-skillpro.github.io/Yuru-Competition/">ゆるコンペ ↗</a></li></ul></section>'
training+='<section class="section"><h2>信州大学研究開発マネジメント人材育成プログラム</h2><p>文科省による「研究開発マネジメント人材に関する体制整備事業」の採択を受け、信州大学では信州大学研究開発マネジメント人材育成プログラムを実施しています。私は本事業の企画や運営に携わるとともに、「研究力分析、経営戦略」の科目を担当します。</p><a class="text-link" href="https://www.shinshu-u.ac.jp/institution/suirlo/rdm/">プログラムの公式ページ ↗</a></section>'
training+='<section class="section"><h2>その他</h2><ul class="training-records"><li>ロジックモデルワークショップ（2025年10月）</li></ul></section>'
page('training','人材育成',training)

(OUT/'.nojekyll').write_text('')
print('Built {} pages in {}'.format(len(list(OUT.rglob('index.html'))),OUT))
