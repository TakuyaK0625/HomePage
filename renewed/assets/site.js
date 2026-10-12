const menu = document.querySelector('.menu');
menu.addEventListener('click', () => {
 const open = menu.getAttribute('aria-expanded') !== 'true';
 menu.setAttribute('aria-expanded', String(open));
 document.querySelector('#navigation').classList.toggle('open', open);
});
document.addEventListener('keydown', e => { if(e.key === 'Escape') {menu.setAttribute('aria-expanded','false');document.querySelector('#navigation').classList.remove('open');} });
const search = document.querySelector('#record-search');
if(search) search.addEventListener('input', () => {
 const q = search.value.trim().normalize('NFKC').toLocaleLowerCase('ja');
 let count = 0;
 document.querySelectorAll('.record-section').forEach(section => {
  let visible = 0;
  section.querySelectorAll('li').forEach(item => {item.hidden = !item.textContent.normalize('NFKC').toLocaleLowerCase('ja').includes(q); if(!item.hidden) {visible++;count++;}});
  section.hidden = visible === 0;
 });
 document.querySelector('#search-status').textContent = q ? `${count}件の業績が見つかりました。` : '';
});
