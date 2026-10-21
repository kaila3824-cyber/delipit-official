import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';

const read = (name) => readFileSync(new URL(`../${name}`, import.meta.url), 'utf8');
const index = read('index.html');
const page = read('operator-disclosure.html');
const info = read('safe-information.html');

function formHarness({request = '', hash = '#contact', valid = true, success = true, reject = false} = {}) {
  const fields = {
    product: {value:'DELIPIT SAFE'}, inquiry_type:{value:'一般問い合わせ'},
    subject:{value:'initial'}, email:{value:'example@example.com'}
  };
  const status = {textContent:'', className:''};
  const submit = {disabled:true,textContent:'送信する'};
  const accordion = {open:false};
  const form = {
    elements:{namedItem: name => fields[name]}, reset(){this.resetCalled=true;},
    reportValidity:() => valid,
    addEventListener(type,cb){ if(type==='submit') this.onSubmit=cb; }
  };
  let calls=[];
  const script = [...index.matchAll(/<script>([\s\S]*?)<\/script>/g)].at(-1)[1];
  const context = {
    document:{getElementById:id=>({delipitContactForm:form,contactSubmit:submit,contactStatus:status})[id], querySelector:()=>accordion},
    location:{search:request ? `?request=${request}`:'', hash}, URLSearchParams, FormData: class {constructor(f){assert.equal(f,form)}},
    fetch:async (url,options)=>{calls.push({url,options});if(reject)throw Error('offline');return {ok:success,json:async()=>({success})}}
  };
  vm.runInNewContext(script,context);
  return {form,fields,status,submit,accordion,calls,send:async()=>form.onSubmit({preventDefault(){}})};
}

test('request route opens form and selects its distinct category',()=>{
  const operator=formHarness({request:'operator'});
  assert.equal(operator.accordion.open,true);
  assert.equal(operator.fields.inquiry_type.value,'運営者情報の開示請求');
  assert.equal(formHarness({request:'privacy'}).fields.inquiry_type.value,'個人情報の開示・訂正・削除等');
  assert.equal(formHarness().fields.inquiry_type.value,'一般問い合わせ');
});
test('success is only receipt acknowledgement and payload uses category',async()=>{
  const h=formHarness({request:'operator'});await h.send();
  assert.equal(h.calls.length,1);assert.equal(h.calls[0].url,'https://api.web3forms.com/submit');
  assert.match(h.fields.subject.value,/DELIPIT SAFE／運営者情報の開示請求/);
  assert.match(h.status.textContent,/回答が完了したことを示すものではありません/);
  assert.equal(h.form.resetCalled,true);assert.equal(h.submit.disabled,false);
});
test('validation and network errors do not report success',async()=>{
  const invalid=formHarness({valid:false});await invalid.send();assert.equal(invalid.calls.length,0);assert.match(invalid.status.textContent,/必須項目/);
  const offline=formHarness({reject:true});await offline.send();assert.match(offline.status.textContent,/送信できませんでした/);assert.equal(offline.form.resetCalled,undefined);
  const failed=formHarness({success:false});await failed.send();assert.equal(failed.status.className,'contact-status error');
});
test('public routes and minimal intake',()=>{
  for(const type of ['一般問い合わせ','個人情報の開示・訂正・削除等','運営者情報の開示請求','不具合報告','使い方について']) assert.ok(index.includes(`value="${type}"`));
  for(const product of ['DELIPIT','DELIPIT SAFE']) assert.ok(index.includes(`value="${product}"`));
  for(const link of ['index.html?request=operator#contact','index.html?request=privacy#contact','safe-terms.html','safe-privacy.html']) assert.ok(page.includes(link));
  assert.ok(index.includes('operator-disclosure.html'));assert.ok(info.includes('operator-disclosure.html'));
  assert.ok(index.includes('name="email"'));assert.ok(index.includes('name="name"'));
  assert.doesNotMatch(index, /name="(?:identity_document|backup|passphrase|address|phone)"/i);
  assert.match(page,/未承認・未施行/);assert.match(page,/有料の購入申込は受け付けていません/);
});
