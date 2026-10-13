/* Halloween sale: countdown + automatic switch back to the regular price/theme when it ends. */
(function(){
  var bar=document.getElementById("promo");if(!bar)return;
  var end=new Date(bar.getAttribute("data-end")).getTime(),U=bar.getAttribute("data-u").split("|"),root=document.documentElement;
  function p(n){return n<10?"0"+n:""+n}
  function stop(){
    root.classList.remove("hw");
    [].forEach.call(document.querySelectorAll("[data-promo-only]"),function(e){e.hidden=true;e.style.display="none"});
    [].forEach.call(document.querySelectorAll("[data-reg-text]"),function(e){e.textContent=e.getAttribute("data-reg-text")});
    [].forEach.call(document.querySelectorAll("[data-reg-href]"),function(e){e.setAttribute("href",e.getAttribute("data-reg-href"))});
  }
  function tick(){
    var ms=end-Date.now();
    if(ms<=0){stop();clearInterval(t);return}
    var s=Math.floor(ms/1000),d=Math.floor(s/86400),h=Math.floor(s%86400/3600),m=Math.floor(s%3600/60),c=s%60;
    var html='<i><b>'+d+'</b>'+U[0]+'</i><i><b>'+p(h)+'</b>'+U[1]+'</i><i><b>'+p(m)+'</b>'+U[2]+'</i><i><b>'+p(c)+'</b>'+U[3]+'</i>';
    [].forEach.call(document.querySelectorAll("[data-cd]"),function(e){e.innerHTML=html});
  }
  var t=setInterval(tick,1000);tick();
})();
