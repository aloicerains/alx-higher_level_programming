#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let ch = 0;
      while (ch < this.height) {
        let cw = 0;
        let dspl = '';
        while (cw < this.width) {
          dspl = dspl.concat(c);
          cw++;
        }
        console.log(dspl);
        ch++;
      }
    }
  }
}
module.exports = Square;
