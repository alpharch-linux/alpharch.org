'use strict';
const film=document.getElementById('deskFilm');
const playFilm=document.getElementById('playFilm');
if(film&&playFilm){
 const status=document.getElementById('film-status');
 const showControls=()=>{film.controls=true;playFilm.hidden=true;};
 const showError=()=>{
  showControls();
  status.textContent='The film couldn’t start here. Try the player controls or use Download film below.';
  status.hidden=false;
 };
 playFilm.addEventListener('click',async()=>{
  showControls();
  status.hidden=true;
  try{await film.play();film.focus({preventScroll:true});}
  catch{showError();}
 });
 film.addEventListener('play',()=>{showControls();status.hidden=true;});
 film.addEventListener('error',showError);
 film.querySelector('source').addEventListener('error',showError);
 // Keep native controls as the fallback when JavaScript is unavailable.
 film.controls=false;
 playFilm.hidden=false;
}
const shots={
 desk:{src:'/images/desk.png',alt:'Alpharch with a Bitcoin liquidity heatmap, an Ethereum candle chart and a Bitcoin perpetual volume profile in resizable tiles.',caption:'The workspace · heatmap, candles and volume profile · captured September 5, 2026.',width:1440,height:900},
 studies:{src:'/images/studies.png',alt:'An Ethereum chart with Bollinger Bands and separate volume and stochastic indicator panes.',caption:'Studies · Bollinger Bands, volume and stochastic · captured September 5, 2026.',width:1440,height:900},
 bitcoin:{src:'/images/bitcoin-desk.jpg',alt:'The Bitcoin starting desk with a one-minute chart on the left and liquidity heatmap and time and sales on the right.',caption:'Bitcoin starter · one market, three views · captured September 6, 2026.',width:734,height:720}
};
for(const button of document.querySelectorAll('[data-shot]'))button.addEventListener('click',()=>{
 const shot=shots[button.dataset.shot];if(!shot)return;
 const image=document.getElementById('deskShot');image.src=shot.src;image.alt=shot.alt;image.width=shot.width;image.height=shot.height;
 for(const link of ['shotLink','fullShot'])document.getElementById(link).href=shot.src;
 document.getElementById('shotLink').setAttribute('aria-label','Open '+button.textContent.toLowerCase()+' screenshot at full size');
 document.getElementById('shotCaption').textContent=shot.caption;
 for(const option of document.querySelectorAll('[data-shot]'))option.setAttribute('aria-pressed',String(option===button));
});
for(const button of document.querySelectorAll('#copyInstall'))button.addEventListener('click',async()=>{
 const status=document.getElementById('copyStatus');
 try{await navigator.clipboard.writeText('curl -fsSL https://alpharch.org/install | bash');status.textContent='Install command copied.';button.textContent='Copied';}
 catch{status.textContent='Select the command above to copy it.';}
});
