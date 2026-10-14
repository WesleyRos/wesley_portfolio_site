import {describe,it,expect} from 'vitest';
import {createLargeGraph,agroCategories} from '../static/large-graph-data.js';
describe('Mapa conceitual do agronegócio',()=>{
 it('inclui nove categorias e temas únicos e explicados',()=>{const {nodes}=createLargeGraph();expect(agroCategories).toHaveLength(9);expect(nodes).toHaveLength(1200);expect(nodes.filter(n=>n.context).every(n=>n.description.includes('Não contém medições'))).toBe(true);expect(new Set(nodes.map(n=>n.id)).size).toBe(nodes.length);expect(new Set(nodes.map(n=>n.label)).size).toBe(nodes.length);for(const n of nodes){expect(n.description.length).toBeGreaterThan(30);expect(Number.isFinite(n.x+n.y+n.z)).toBe(true);}});
 it('cria relações válidas e explicadas sem duplicatas',()=>{const {nodes,links}=createLargeGraph();const ids=new Set(nodes.map(n=>n.id)),seen=new Set();for(const l of links){expect(ids.has(l.source)&&ids.has(l.target)).toBe(true);expect(l.source).not.toBe(l.target);const key=[l.source,l.target].sort().join(':');expect(seen.has(key)).toBe(false);seen.add(key);expect(l.label.length).toBeGreaterThan(10);}expect(links.filter(l=>l.cross).length).toBeGreaterThan(15);});
 it('conecta câmbio e fertilizantes como relação qualitativa',()=>{const {nodes,links}=createLargeGraph();const a=nodes.find(n=>n.label==='Câmbio'),b=nodes.find(n=>n.label==='Fertilizantes');expect(links.find(l=>l.source===a.id&&l.target===b.id)?.label).toContain('pode alterar');});
 it('é reproduzível',()=>expect(createLargeGraph()).toEqual(createLargeGraph()));
});
