import {createLargeGraph} from './large-graph-data.js?v=11';
import {mountLargeGraph} from './large-graph.js?v=34';

const element=document.getElementById('large-network');
if(element){
 const graph=mountLargeGraph(element,createLargeGraph()),motion=matchMedia('(prefers-reduced-motion: reduce)'),toggle=document.getElementById('network-motion');
 let paused=motion.matches,intersecting=true;
 function refresh(){graph.setRunning(!paused&&intersecting&&!document.hidden);toggle.textContent=paused?'▷':'Ⅱ';toggle.setAttribute('aria-pressed',String(paused));toggle.setAttribute('aria-label',paused?'Retomar rotação da rede':'Pausar rotação da rede');}
 toggle.addEventListener('click',()=>{paused=!paused;refresh();});
 motion.addEventListener('change',()=>{paused=motion.matches;refresh();});
 document.addEventListener('visibilitychange',refresh);
 new IntersectionObserver(entries=>{intersecting=entries[0].isIntersecting;refresh();}).observe(element.parentElement);
 graph.setVisible(true);refresh();
}
