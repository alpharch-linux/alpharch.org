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
 desk:{src:'/images/hyprland-desk.jpg',alt:'Three Alpharch chart windows tiled by Hyprland on Omarchy: Bitcoin candles and time and sales on the left, a liquidity heatmap on the right, with the desktop bar and wallpaper visible.',caption:'Hyprland desk · three real chart windows on Omarchy · captured September 6, 2026.',width:1920,height:1080},
 focus:{src:'/images/hyprland-chart-focus.jpg',alt:'A focused Alpharch Bitcoin chart with the left drawing toolbar, a marked horizontal price level, exact prices and volume below.',caption:'Chart focus · draw a level and zoom into price · captured September 6, 2026.',width:1920,height:1080},
 flow:{src:'/images/hyprland-order-flow.jpg',alt:'The Omarchy Hyprland desk with a Bitcoin chart and RSI, time and sales, and a liquidity heatmap with trade bubbles in separate native windows.',caption:'Order flow · RSI, liquidity, trade bubbles and the tape · captured September 6, 2026.',width:1920,height:1080}
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
