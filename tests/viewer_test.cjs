// Integration test with DOM/canvas stubs; does not replace a real-browser visual check.
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const listeners={},frames=[];let draws=0;
const context=new Proxy({},{get:(o,k)=>k in o?o[k]:(()=>{draws++;})});
const elements={};
for(const id of ['tv','pad','status','modeLabel','reset','mode','debug'])elements[id]={width:id==='tv'?960:854,height:id==='tv'?540:480,dataset:{},getContext:()=>context};
const sandbox={console,document:{getElementById:id=>elements[id]},navigator:{getGamepads:()=>[]},addEventListener:(name,handler)=>listeners[name]=handler,requestAnimationFrame:fn=>frames.push(fn),Image:class {set src(value){this.width=1280;this.height=1040;queueMicrotask(()=>this.onload());}}};
sandbox.window=sandbox;vm.createContext(sandbox);
const sceneDataPath='preview/scene-data.js';
if(fs.existsSync(sceneDataPath)){
    vm.runInContext(fs.readFileSync(sceneDataPath,'utf8'),sandbox);
}else{
    sandbox.SCENE={width:80,height:65,spawn:[1032,248],collision:new Uint8Array(80*65)};
    sandbox.ASSETS={ground:'test-ground',front:'test-front',avatar:'test-avatar'};
}
vm.runInContext(fs.readFileSync('preview/viewer.js','utf8'),sandbox);
function step(t){assert(frames.length);frames.shift()(t);}
function key(type,key){listeners[type]({key,repeat:false,preventDefault(){}});}
(async()=>{
    await new Promise(resolve=>setImmediate(resolve));
    step(1000);const start={x:sandbox.PROTOTYPE.x,y:sandbox.PROTOTYPE.y};
    key('keydown','ArrowDown');
    for(let i=1;i<=20;i++)step(1000+i*16);
    key('keyup','ArrowDown');assert(sandbox.PROTOTYPE.y>start.y);
    elements.mode.onclick();step(1340);assert.equal(sandbox.PROTOTYPE.mode,1);
    elements.reset.onclick();step(1360);assert.equal(sandbox.PROTOTYPE.x,start.x);assert.equal(sandbox.PROTOTYPE.y,start.y);
    assert(sandbox.PROTOTYPE.blocked(-1,0));assert(sandbox.PROTOTYPE.blocked(1280,0));
    key('keydown','ArrowDown');listeners.blur();step(1380);assert.equal(sandbox.PROTOTYPE.y,start.y);
    assert(draws>0);assert(elements.status.textContent.includes('80 × 65'));
    console.log('PASS: movement, reset, second-screen switch, boundaries, blur and draw dispatch (DOM stubs).');
})().catch(error=>{console.error(error);process.exitCode=1;});
