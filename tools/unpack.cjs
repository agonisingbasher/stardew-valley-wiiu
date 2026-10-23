const fs = require('node:fs');
const path = require('node:path');
const xnb = require('xnb/dist/xnb.cjs');

async function unpack(source, destination) {
  // Copy to an offset-zero typed array: pooled Node Buffers break xnb's header reader.
  const input = new Uint8Array(fs.readFileSync(source));
  const outputs = await xnb.unpackToFiles(input, {fileName:path.basename(source)});
  fs.mkdirSync(path.dirname(destination), {recursive:true});
  for (const {extension, data} of outputs) {
    const bytes = typeof data === 'string' ? data : Buffer.from(data instanceof Blob ? await data.arrayBuffer() : data);
    fs.writeFileSync(destination + '.' + extension, bytes);
  }
}

(async () => {
  const root = path.resolve(__dirname, '..');
  for (const name of process.argv.slice(2)) {
    await unpack(path.join(root,'work/packed', name+'.xnb'), path.join(root,'work/unpacked', name));
  }
})().catch(error => {console.error(error.stack);process.exitCode=1;});
