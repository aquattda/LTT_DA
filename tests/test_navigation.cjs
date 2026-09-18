// Unit-level DOM doubles; this does not replace an actual browser scroll test.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { resolve } = require('node:path');
const vm = require('node:vm');
const script = readFileSync(resolve(__dirname, '../Do_An/walmart_eda_model/navigation.js'), 'utf8').replace('__NAVIGATION_REVISION__', '1');

for (const selector of ['[data-testid="stMain"]', 'section.main', null]) {
  test(`navigation scrolls main and document after render (selector: ${selector})`, () => {
    const frames = [];
    const calls = [];
    const target = name => ({ scrollTo: options => calls.push([name, options.top, options.left, options.behavior]) });
    vm.runInNewContext(script, {
      requestAnimationFrame: callback => frames.push(callback),
      document: {
        querySelector: requested => requested === selector ? target('main') : null,
        scrollingElement: target('document'),
      },
      window: target('window'),
    });
    assert.deepEqual(calls, []);
    frames.shift()();
    assert.deepEqual(calls, []);
    frames.shift()();
    const names = selector ? ['main', 'document', 'window'] : ['document', 'window'];
    assert.deepEqual(calls, names.map(name => [name, 0, 0, 'instant']));
    assert.equal(frames.length, 0);
  });
}

test('a repeated navigation script cannot scroll again on a filter rerender', () => {
  const frames = [];
  let calls = 0;
  const context = vm.createContext({
    requestAnimationFrame: callback => frames.push(callback),
    document: { querySelector: () => null, scrollingElement: null },
    window: { scrollTo: () => { calls += 1; } },
  });
  vm.runInContext(script, context);
  while (frames.length) frames.shift()();
  assert.equal(calls, 1);
  vm.runInContext(script, context);
  assert.equal(frames.length, 0);
  assert.equal(calls, 1);
  vm.runInContext(script.replace('const revision = 1;', 'const revision = 2;'), context);
  while (frames.length) frames.shift()();
  assert.equal(calls, 2);
});
