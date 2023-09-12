#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  constructor (size) { super(size, size); }

  charPrint (c) {
    if (!c) { c = 'X'; }
    for (let j = 0; j < this.height; j++) { console.log(c.repeat(this.width)); }
  }
};
