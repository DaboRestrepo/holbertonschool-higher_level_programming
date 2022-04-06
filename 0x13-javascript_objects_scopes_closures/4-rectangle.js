#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w && h && w >= 0 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row + '');
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    const doubleW = this.width * 2;
    const doubleH = this.height * 2;
    this.width = doubleW;
    this.height = doubleH;
  }
}
module.exports = Rectangle;
