(function(){
"use strict";
var I=window.I18N||{};
var $=function(s,r){return (r||document).querySelector(s)};
var $$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var RM=window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches;
var AR=document.documentElement.lang==="ar";

/* remember the chosen language (used by the redirect in <head> of the English page) */
var lg=$("#lang");
if(lg)lg.addEventListener("click",function(){try{localStorage.setItem("lang",lg.getAttribute("hreflang"))}catch(e){}});

/* theme toggle (dark / light), remembered */
(function(){var b=$("#theme");if(!b)return;var r=document.documentElement;
function set(t,s){r.setAttribute("data-theme",t);var m=$("meta[name=theme-color]");if(m)m.setAttribute("content",t==="light"?"#4A99E9":"#0a1124");b.setAttribute("aria-pressed",t==="light");if(s)try{localStorage.setItem("theme",t)}catch(e){}}
set(r.getAttribute("data-theme")||"dark",false);
b.addEventListener("click",function(){set(r.getAttribute("data-theme")==="light"?"dark":"light",true)})})();

/* header shadow */
(function(){var h=$(".top");if(!h)return;function f(){h.classList.toggle("scrolled",window.scrollY>8)}f();addEventListener("scroll",f,{passive:true})})();

/* run a callback once an element is on screen */
function whenSeen(el,cb,th){
  if(!el)return;
  if(!("IntersectionObserver" in window)){cb();return}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){io.disconnect();cb()}})},{threshold:th||.25});
  io.observe(el);
}
/* toggle a callback while visible */
function whileSeen(el,on,off){
  if(!el)return;
  if(!("IntersectionObserver" in window)){on();return}
  new IntersectionObserver(function(es){es.forEach(function(e){e.isIntersecting?on():off()})},{threshold:.1}).observe(el);
}

/* =========================================================
   Trial calculator: filament cost only (weight x price per kg) + profit margin
   ========================================================= */
(function(){
  var lab=$("#lab");if(!lab)return;
  var D={price:10,w:150,h:6,m:40};
  var S=JSON.parse(JSON.stringify(D));
  var el=function(id){return document.getElementById(id)};
  var cur={oc:1.5,on:.6,op:2.1},raf={};
  function calc(){var c=S.w/1000*S.price,p=c*S.m/100;return {cost:c,profit:p,price:c+p}}
  function money(v){return "$"+v.toFixed(2)}
  function tween(id,to){
    var n=el(id);
    if(RM){cur[id]=to;n.textContent=money(to);return}
    var from=cur[id],t0=null;
    cancelAnimationFrame(raf[id]);
    (function step(t){
      if(!t0)t0=t;
      var k=Math.min((t-t0)/420,1),e=1-Math.pow(1-k,3);
      cur[id]=from+(to-from)*e;n.textContent=money(cur[id]);
      if(k<1)raf[id]=requestAnimationFrame(step);
    })(performance.now());
  }
  function fillRange(r){var p=(r.value-r.min)/(r.max-r.min)*100;r.style.setProperty("--p",p+"%")}
  function render(){
    var c=calc();
    tween("oc",c.cost);tween("on",c.profit);tween("op",c.price);
    el("ow").textContent=S.w+" g";
    el("oh").textContent=S.h+(AR?" ساعة":" h");
    el("om").textContent=S.m+"%";
    ["w","h","m"].forEach(function(k){fillRange(el("r"+k))});
    scene.shape();
  }
  /* ---- scene ---- */
  var scene=(function(){
    var svg=el("sc");if(!svg)return {shape:function(){},paint:function(){}};
    var NS="http://www.w3.org/2000/svg",N=34,L=[],sx=1,sy=1,H=118,BASE=164;
    var lay=el("lay"),car=el("car"),gan=el("gan"),fil=el("fil");
    for(var i=0;i<N;i++){var r=document.createElementNS(NS,"rect");r.setAttribute("rx","1");r.style.fill="var(--fil)";r.style.opacity=i%2?".86":"1";lay.appendChild(r);L.push(r)}
    var p=RM?1:0,phase=0,hold=0,last=0,k=-1,running=false,tt=0;
    function widthAt(i){var t=i/(N-1);return (34+24*Math.sin(Math.PI*Math.pow(t,.75))-10*t*t+3*Math.sin(t*14))*1.75*sx}
    function shape(){
      sx=.72+.28*Math.sqrt(S.w/1000);sy=.55+.45*Math.min(1,S.h/30);
      var h=H*sy,lh=h/N;
      for(var i=0;i<N;i++){var w=widthAt(i);L[i].setAttribute("x",(100-w/2).toFixed(2));L[i].setAttribute("width",w.toFixed(2));L[i].setAttribute("y",(BASE-(i+1)*lh).toFixed(2));L[i].setAttribute("height",(lh+.5).toFixed(2))}
      k=-1;paint();
    }
    function paint(){
      var h=H*sy,lh=h/N,n=Math.min(N,Math.floor(p*N)+(p>=1?0:1));
      if(n!==k){for(var i=0;i<N;i++)L[i].style.display=i<n?"":"none";k=n}
      var top=BASE-Math.max(n,0)*lh,w=n>0?widthAt(Math.max(n-1,0)):30;
      var x=100+Math.sin(tt*5.2)*(w/2-4);
      var show=p<1;
      car.setAttribute("transform","translate("+(x-13).toFixed(1)+","+(top-20).toFixed(1)+")");
      car.style.opacity=show?1:0;
      gan.setAttribute("transform","translate(0,"+(top-14).toFixed(1)+")");fil.setAttribute("d","M100 -2C100 44 "+x.toFixed(1)+" "+(top-72).toFixed(1)+" "+x.toFixed(1)+" "+(top-19).toFixed(1));fil.style.opacity=show?1:0;gan.style.opacity=show?1:0;
    }
    function frame(t){
      if(!running)return;
      var dt=Math.min((t-last)/1000,.05);last=t;tt+=dt;
      if(phase===0){p+=dt/7;if(p>=1){p=1;phase=1;hold=0}}
      else{hold+=dt;if(hold>2.4){p=0;phase=0;k=-1}}
      paint();requestAnimationFrame(frame);
    }
    function start(){if(RM||running)return;running=true;last=performance.now();requestAnimationFrame(frame)}
    function stop(){running=false}
    whileSeen(svg,start,stop);
    return {shape:shape,paint:paint};
  })();

  $$(".mat").forEach(function(b){
    b.addEventListener("click",function(){
      $$(".mat").forEach(function(x){x.setAttribute("aria-checked","false")});
      b.setAttribute("aria-checked","true");
      S.price=+b.dataset.p;lab.style.setProperty("--fil",b.dataset.c);render();
    });
  });
  [["rw","w"],["rh","h"],["rm","m"]].forEach(function(a){
    el(a[0]).addEventListener("input",function(){S[a[1]]=+this.value;render()});
  });
  el("reset").addEventListener("click",function(){
    S=JSON.parse(JSON.stringify(D));
    el("rw").value=D.w;el("rh").value=D.h;el("rm").value=D.m;
    $(".mat").click();
  });
  render();
})();

/* =========================================================
   App explorer (zoom into the real screenshot)
   ========================================================= */
(function(){
  var box=$("#xp");if(!box)return;
  var tabs=$$(".xp-tab",box),stage=$(".xp-stage",box),hl=$(".xp-hl",box);
  var auto=!RM&&window.innerWidth>980,idx=0,timer=null;
  var fr=$(".xp-frame",box),hp=fr.parentNode,hn=fr.nextSibling;
  function place(i){
    if(window.innerWidth<=980){tabs[i].insertAdjacentElement("afterend",fr);fr.style.gridColumn="1/-1";fr.style.margin="4px 0"}
    else if(fr.parentNode!==hp){hp.insertBefore(fr,hn);fr.style.gridColumn="";fr.style.margin=""}
  }
  window.addEventListener("resize",function(){place(idx)});
  function go(i){
    idx=i;
    tabs.forEach(function(t,j){t.setAttribute("aria-selected",j===i?"true":"false")});
    var t=tabs[i],x=+t.dataset.x,y=+t.dataset.y,w=+t.dataset.w,h=+t.dataset.h;
    if(!w){stage.style.transform="none";hl.style.opacity=0;return}
    var s=Math.min(3,.92/(w/100),.92/(h/100)),cx=(x+w/2)/100,cy=(y+h/2)/100;
    var tx=Math.max(1-s,Math.min(0,.5-cx*s)),ty=Math.max(1-s,Math.min(0,.5-cy*s));
    stage.style.transform="translate("+(tx*100)+"%,"+(ty*100)+"%) scale("+s+")";
    hl.style.left=x+"%";hl.style.top=y+"%";hl.style.width=w+"%";hl.style.height=h+"%";hl.style.opacity=1;
  }
  tabs.forEach(function(t,i){t.addEventListener("click",function(){auto=false;box.classList.remove("auto");clearInterval(timer);go(i);place(i);if(window.innerWidth<=980)setTimeout(function(){var h=(document.querySelector("header.top")||{}).offsetHeight||64;window.scrollTo({top:t.getBoundingClientRect().top+window.pageYOffset-h-10,behavior:"smooth"})},60)})});
  go(0);place(0);
  whenSeen(box,function(){
    if(!auto)return;
    box.classList.add("auto");
    timer=setInterval(function(){if(!auto){clearInterval(timer);return}go((idx+1)%tabs.length)},4200);
  },.4);
})();

/* =========================================================
   Feature tabs
   ========================================================= */
(function(){
  var tabs=$$(".ft-tab"),views=$$(".fp");if(!tabs.length)return;
  var current=0,fv=$(".ft-view"),home=fv&&fv.parentNode,homeNext=fv&&fv.nextSibling;
  function place(){
    if(!fv)return;
    if(window.innerWidth<=980){tabs[current].insertAdjacentElement("afterend",fv);fv.style.marginTop="12px"}
    else if(fv.parentNode!==home){home.insertBefore(fv,homeNext);fv.style.marginTop=""}
  }
  window.addEventListener("resize",place);
  function show(i){
    current=i;place();
    tabs.forEach(function(t,j){t.setAttribute("aria-selected",j===i?"true":"false")});
    views.forEach(function(v,j){
      v.hidden=j!==i;v.classList.remove("on");
      if(j===i)requestAnimationFrame(function(){requestAnimationFrame(function(){v.classList.add("on")})});
    });
  }
  tabs.forEach(function(t,i){t.addEventListener("click",function(){show(i);if(window.innerWidth<=980)setTimeout(function(){var h=(document.querySelector("header.top")||{}).offsetHeight||64;window.scrollTo({top:t.getBoundingClientRect().top+window.pageYOffset-h-10,behavior:"smooth"})},450)})});
  tabs.forEach(function(t,i){t.addEventListener("keydown",function(e){
    var n=e.key==="ArrowDown"||e.key==="ArrowRight"?1:e.key==="ArrowUp"||e.key==="ArrowLeft"?-1:0;
    if(!n)return;e.preventDefault();var j=(i+n+tabs.length)%tabs.length;tabs[j].focus();show(j);
  })});
  whenSeen($(".ft"),function(){show(current)},.2);
  show(0);

  /* invoice language */
  var paper=$("#paper"),W=I.inv||{};
  $$("#invl button").forEach(function(b){
    b.addEventListener("click",function(){
      $$("#invl button").forEach(function(x){x.setAttribute("aria-pressed",x===b?"true":"false")});
      var w=W[b.dataset.l];if(!w)return;
      paper.dir=b.dataset.l==="ar"?"rtl":"ltr";paper.lang=b.dataset.l;
      $$("[data-w]",paper).forEach(function(n){n.textContent=w[n.dataset.w]});
    });
  });
  /* compact layout */
  var fr=$("#fit"),fb=$("#fitbox"),fc=$("#fitcap");
  if(fr)fr.addEventListener("input",function(){
    var v=+fr.value;fb.style.setProperty("--fw",v+"%");fb.style.setProperty("--cols",v<62?1:v<82?2:3);
    fc.textContent=(I.fit||"")+" "+v+"%";
    fr.style.setProperty("--p",((v-fr.min)/(fr.max-fr.min)*100)+"%");
  });
})();

/* =========================================================
   Countries: pick one, currency / electricity / exchange rate follow
   ========================================================= */
(function(){
  var box=$("#cx");if(!box)return;
  var chips=$$(".ctries button",box);if(!chips.length)return;
  var out={code:$("#cxCode"),name:$("#cxName"),cur:$("#cxCur"),curn:$("#cxCurN"),kwh:$("#cxKwh"),rate:$("#cxRate"),ex:$("#cxEx")};
  function amt(n){var d=n>=100?0:2;return n.toLocaleString("en-US",{minimumFractionDigits:0,maximumFractionDigits:d})}
  function pick(b,focus){
    chips.forEach(function(x){var on=x===b;x.setAttribute("aria-checked",on?"true":"false");x.tabIndex=on?0:-1});
    var d=b.dataset,ap=d.ap==="1"?"\u2248 ":"";
    out.code.src=d.flag;out.name.textContent=d.n;
    out.cur.textContent=d.cur;out.curn.textContent=d.curn;
    out.kwh.textContent=d.kwh+" "+d.cur+" / kWh";
    out.rate.textContent="1 $ "+(ap?"\u2248":"=")+" "+d.rt+" "+d.cur;
    out.ex.textContent="$10 "+(ap?"\u2248":"=")+" "+amt(10*parseFloat(d.r))+" "+d.cur;
    if(!RM){box.classList.remove("pop");void box.offsetWidth;box.classList.add("pop")}
    if(focus)b.focus();
  }
  chips.forEach(function(b,i){
    b.addEventListener("click",function(){pick(b)});
    b.addEventListener("keydown",function(e){
      var n=e.key==="ArrowRight"||e.key==="ArrowDown"?1:e.key==="ArrowLeft"||e.key==="ArrowUp"?-1:0;
      if(!n)return;
      if(document.documentElement.dir==="rtl"&&(e.key==="ArrowLeft"||e.key==="ArrowRight"))n=-n;
      e.preventDefault();pick(chips[(i+n+chips.length)%chips.length],true);
    });
  });
})();

/* =========================================================
   Pricing: payment tabs + copy address
   ========================================================= */
(function(){
  var tp=$("#tabPP"),tc=$("#tabCR"),vp=$("#viewPP"),vc=$("#viewCR");if(!tp)return;
  function pick(c){tp.setAttribute("aria-selected",c?"false":"true");tc.setAttribute("aria-selected",c?"true":"false");vp.hidden=c;vc.hidden=!c}
  tp.onclick=function(){pick(false)};tc.onclick=function(){pick(true)};
  var cb=$("#copyBtn"),ad=$("#addr");
  function done(){cb.textContent=I.copied;setTimeout(function(){cb.textContent=I.copy},1800)}
  function fb(){var r=document.createRange();r.selectNodeContents(ad);var s=getSelection();s.removeAllRanges();s.addRange(r);try{if(document.execCommand("copy"))done()}catch(e){}}
  cb.onclick=function(){if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(ad.textContent.trim()).then(done,fb)}else fb()};
})();

/* =========================================================
   Activation steps: line fills as the section appears
   ========================================================= */
(function(){
  var s=$(".steps");if(!s)return;
  $$("li",s).forEach(function(li,i){li.style.setProperty("--d",(i*.22)+"s")});
  whenSeen(s,function(){s.style.setProperty("--prog",1);s.classList.add("go")},.35);
})();

/* =========================================================
   Latest version label
   ========================================================= */
(function(){
  var out=$("#ver");if(!out)return;
  function show(v){out.textContent=I.ver+" "+v+" · "}
  try{var c=sessionStorage.getItem("ver");if(c){show(c);return}}catch(e){}
  if(!window.fetch)return;
  fetch("https://api.github.com/repos/Pr0fes0rx/3d-print-calculator/releases/latest",{headers:{Accept:"application/vnd.github+json"}})
  .then(function(r){return r.ok?r.json():Promise.reject()})
  .then(function(j){var v=String(j.tag_name||"").replace(/^v/i,"");if(/^\d+(\.\d+)*/.test(v)){try{sessionStorage.setItem("ver",v)}catch(e){}show(v)}})
  .catch(function(){});
})();

/* =========================================================
   Contact widget
   ========================================================= */
(function(){
  var fab=$("#chatFab"),box=$("#chatBox");if(!fab)return;
  var msg=$("#chatMsg"),btn=$("#cs");
  function toggle(o){box.hidden=!o;fab.setAttribute("aria-expanded",o?"true":"false");if(o)$("#ce").focus()}
  fab.onclick=function(){toggle(box.hidden)};
  $("#chatX").onclick=function(){toggle(false)};
  document.addEventListener("keydown",function(e){if(e.key==="Escape"&&!box.hidden)toggle(false)});
  var fc=$("#footContact");if(fc)fc.onclick=function(e){e.preventDefault();toggle(true)};
  function say(k,err){msg.textContent=I[k];msg.className="chat-msg"+(err?" err":"")}
  $("#chatForm").onsubmit=function(e){
    e.preventDefault();
    var n=$("#cn").value.trim(),em=$("#ce").value.trim(),m=$("#cm").value.trim();
    if($("#cb").value)return;
    if(!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em)||!m){say("mBad",true);return}
    var subj="3D Print Calculator - message"+(n?" from "+n:"");
    btn.disabled=true;say("mSend");
    fetch("https://api.web3forms.com/submit",{method:"POST",headers:{"Content-Type":"application/json",Accept:"application/json"},
      body:JSON.stringify({access_key:I.key,subject:subj,name:n||em,email:em,message:m})})
    .then(function(r){return r.json()})
    .then(function(j){if(j.success){say("mOk");$("#chatForm").reset()}else say("mErr",true)})
    .catch(function(){say("mErr",true)})
    .then(function(){btn.disabled=false});
  };
})();
})();

/* download button -> real installer asset of the latest GitHub release */
(function(){
  var L="https://github.com/Pr0fes0rx/3d-print-calculator/releases/latest";
  function set(u){[].forEach.call(document.querySelectorAll('a[href="'+L+'"]'),function(a){a.href=u})}
  try{var c=sessionStorage.getItem("dl");if(c){set(c);return}}catch(e){}
  if(!window.fetch)return;
  fetch("https://api.github.com/repos/Pr0fes0rx/3d-print-calculator/releases/latest",{headers:{Accept:"application/vnd.github+json"}})
  .then(function(r){return r.ok?r.json():Promise.reject()})
  .then(function(j){var a=(j.assets||[]).filter(function(x){return /setup\.exe$/i.test(x.name)})[0];if(a){try{sessionStorage.setItem("dl",a.browser_download_url)}catch(e){}set(a.browser_download_url)}})
  .catch(function(){});
})();

/* contact box follows the mobile keyboard */
(function(){
  var box=document.getElementById("chatBox"),vv=window.visualViewport;if(!box||!vv)return;
  function fit(){
    if(box.hidden||window.innerWidth>860){box.style.bottom="";box.style.maxHeight="";return}
    var kb=window.innerHeight-vv.height-vv.offsetTop;
    box.style.bottom=Math.max(0,kb)+(kb>80?10:78)+"px";
    box.style.maxHeight=(vv.height-(kb>80?20:100))+"px";
  }
  vv.addEventListener("resize",fit);vv.addEventListener("scroll",fit);
  box.addEventListener("focusin",function(e){setTimeout(function(){fit();if(e.target.scrollIntoView)e.target.scrollIntoView({block:"nearest"})},300)});
  var fab=document.getElementById("chatFab");if(fab)fab.addEventListener("click",function(){setTimeout(fit,30)});
})();
