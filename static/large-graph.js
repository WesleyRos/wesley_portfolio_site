import {agroCategories} from './large-graph-data.js?v=11';
export function mountLargeGraph(element,data){
 const expand=document.getElementById('network-expand'),stage=element.parentElement;
 let fitDefault=()=>{};
 let graph=null,visible=false,running=false,fitted=false,zoomBase=null,selectedNode=null,hovering=false,dragging=false;
 const categories=new Map(agroCategories.map(([id,name])=>[id,name]));
 const escapeText=value=>String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
 function nodeLabel(node){return `<div class="agro-node-tooltip"><span>${escapeText(categories.get(node.type)||'Visão integrada')}</span><strong>${escapeText(node.label)}</strong><small>${node.context?'Contexto ilustrativo · ':''}Clique para explorar as relações</small></div>`;}
 function updateRotation(){if(graph)graph.controls().autoRotate=running&&!hovering&&!dragging;}
 function resize(){if(graph&&visible){graph.width(stage.clientWidth).height(stage.clientHeight);}}
 try{
  element.hidden=false;
  graph=new window.ForceGraph3D(element,{controlType:'orbit',rendererConfig:{antialias:true,alpha:true,preserveDrawingBuffer:true}}).width(stage.clientWidth).height(stage.clientHeight).backgroundColor('rgba(0,0,0,0)').showNavInfo(false).graphData(data).nodeLabel(nodeLabel).nodeVal(n=>n.hub?4:n.context?1:1.2).nodeColor('color').nodeRelSize(1.6).nodeResolution(5).nodeOpacity(1).linkLabel('label').linkColor(l=>l.cross?'#c6b9ee':'#7f8da5').linkOpacity(.3).linkWidth(.35).enablePointerInteraction(true).enableNodeDrag(true).warmupTicks(0).cooldownTicks(60);
  graph.d3Force('charge').strength(-12);graph.d3Force('link').distance(12);
  graph.camera().fov=45;graph.camera().updateProjectionMatrix();
  graph.cameraPosition({x:0,y:0,z:400});graph.onEngineStop(()=>{if(!fitted){fitDefault();}});graph.controls().autoRotate=true;graph.controls().autoRotateSpeed=.35;graph.controls().enableZoom=true;graph.controls().enablePan=true;graph.controls().zoomSpeed=1.1;graph.controls().minDistance=20;graph.controls().maxDistance=12000;
  const zoomLevel=document.getElementById('network-zoom-level');
  function distance(){return graph.camera().position.distanceTo(graph.controls().target);}
  function updateZoom(){const d=distance();if(zoomBase&&Number.isFinite(d)&&d>0)zoomLevel.textContent=`${Math.round(100*zoomBase/d)}%`;}
  function zoom(factor){
   fitted=true;const target=graph.controls().target,camera=graph.camera().position,d=distance();
   if(!Number.isFinite(d)||d<=0)return;
   if(zoomBase===null)zoomBase=d;
   const next=Math.max(20,Math.min(12000,d*factor)),ratio=next/d;
   graph.cameraPosition({x:target.x+(camera.x-target.x)*ratio,y:target.y+(camera.y-target.y)*ratio,z:target.z+(camera.z-target.z)*ratio},{x:target.x,y:target.y,z:target.z},0);
   graph.controls().update();updateZoom();
  }
  fitDefault=()=>{if(!graph)return;graph.zoomToFit(0,12);zoomBase=distance();zoom(1/1.75);updateMarker();};
  graph.controls().addEventListener('change',()=>{updateZoom();updateMarker();});
  document.getElementById('network-zoom-in').addEventListener('click',()=>zoom(.8));
  document.getElementById('network-zoom-out').addEventListener('click',()=>zoom(1.25));
  stage.addEventListener('keydown',event=>{if(event.key==='+'||event.key==='='){event.preventDefault();zoom(.8);}else if(event.key==='-'||event.key==='−'){event.preventDefault();zoom(1.25);}});

  const lookup=new Map(data.nodes.map(n=>[n.id,n]));
  function updateMarker(){const marker=document.getElementById('network-selected-node');if(!selectedNode){marker.hidden=true;return;}const point=graph.graph2ScreenCoords(selectedNode.x,selectedNode.y,selectedNode.z);marker.hidden=point.x<0||point.y<0||point.x>stage.clientWidth||point.y>stage.clientHeight;marker.style.left=point.x+'px';marker.style.top=point.y+'px';marker.textContent=selectedNode.label;marker.dataset.label=selectedNode.label;marker.style.borderColor=selectedNode.color;}
  graph.onEngineTick(updateMarker);
  function inspect(node){selectedNode=node;graph.nodeVal(n=>n.id===node.id?100:n.hub?4:n.context?1:1.2);updateMarker();
   const insight=document.getElementById('agro-insight');insight.hidden=false;insight.querySelector('strong').textContent=node.label;insight.querySelector('p').textContent=node.description;document.getElementById('network-title').textContent=node.label;
   document.getElementById('network-description').textContent=node.description;
   const list=document.getElementById('agro-relations');list.replaceChildren();
   data.links.filter(l=>(l.source.id||l.source)===node.id||(l.target.id||l.target)===node.id).forEach(l=>{const li=document.createElement('li');li.textContent=l.label;list.append(li);});
   document.getElementById('agro-topic').value=node.id;
  }
  const category=document.getElementById('agro-category'),topic=document.getElementById('agro-topic');
  agroCategories.forEach(([id,name])=>category.add(new Option(name,id)));
  data.nodes.filter(n=>!n.context).forEach(n=>topic.add(new Option(n.label,n.id)));
  category.addEventListener('change',()=>{graph.nodeColor(n=>category.value==='all'||n.type===category.value?n.color:'#252733');if(category.value!=='all')inspect(lookup.get(category.value));});
  topic.addEventListener('change',()=>{const n=lookup.get(topic.value);if(n)inspect(n);});
  document.getElementById('agro-reset').addEventListener('click',()=>{fitted=false;zoomBase=null;document.getElementById('network-zoom-level').textContent='175%';data.nodes.forEach(n=>{delete n.fx;delete n.fy;delete n.fz;});graph.d3ReheatSimulation();fitDefault();fitted=false;});
  graph.onNodeHover(node=>{hovering=!!node;updateRotation();}).onNodeClick(inspect).onLinkClick(l=>{document.getElementById('network-title').textContent='Relação entre fatores';document.getElementById('network-description').textContent=l.label;});
  graph.onNodeDrag(()=>{dragging=true;updateRotation();}).onNodeDragEnd(node=>{node.fx=node.x;node.fy=node.y;node.fz=node.z;document.getElementById('network-interaction-status').textContent=`${node.label}: ponto reposicionado.`;dragging=false;updateRotation();});

 }catch(error){element.textContent='A rede 3D precisa de WebGL. Escolha outra visualização acima.';console.error('Não foi possível iniciar o grafo 3D:',error);}
 window.addEventListener('resize',resize);
 document.getElementById('network-open-project').addEventListener('click',()=>expand.click());
 expand.addEventListener('click',async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await stage.requestFullscreen();}catch{element.textContent='Seu navegador não permitiu ampliar a visualização.';}});
 document.addEventListener('fullscreenchange',()=>{expand.textContent=document.fullscreenElement?'Fechar ampliação ↙':'Ampliar ↗';if(graph)graph.controls().enableZoom=true;resize();if(graph)requestAnimationFrame(fitDefault);});
 return{setVisible(value){visible=value;element.hidden=!value;expand.hidden=!value;document.querySelector('.agro-explorer').hidden=!value;if(!value)document.getElementById('agro-insight').hidden=true;resize();},setRunning(value){running=value;if(graph){updateRotation();graph.resumeAnimation();}},highlight(type){if(graph)graph.nodeColor(n=>type==='all'||n.type===type?n.color:'#24212c');}};
}
