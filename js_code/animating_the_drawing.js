let fourierCoefficients;
let myData;

const xhr = new XMLHttpRequest();
xhr.open('GET', '../coefficients.json', false);
xhr.send();

if (xhr.status === 200) {
  myData = JSON.parse(xhr.responseText);
  console.log(myData); // to verify the array is loaded properly
} else {
  console.error('Error fetching coefficients:', xhr.status);
}

fourierCoefficients = Object.values(myData)[0];

time = 0;
drawx = [];
drawy = [];

let freqArray = [];
for (let i = 0; i < Math.round(fourierCoefficients.length / 2); i++) {
  if (i == 0) {
    freqArray.push(0);
  } else {
    freqArray.push(Math.sin(Math.PI / 2) * i);
    freqArray.push(Math.sin((3 * Math.PI) / 2) * i);
  }
}
console.log(freqArray);
console.log(fourierCoefficients);

/********** DRAWING SECTION **********/

function setup() {
  createCanvas(1880, 972);
}

function draw() {
  background("#000000");
  translate(940, 486);

  const scaleCoeff = 4;

  let intiX = 0;
  let initY = 0;

  let x = 0;
  let y = 0;

  for (let k = 0; k < fourierCoefficients.length; k++) {
    let frequency = freqArray[k];

    intiX = x;
    initY = y;

    x +=
      scaleCoeff *
      (math.re(math.complex(fourierCoefficients[k])) *
        cos(2 * Math.PI * frequency * time) +
        math.im(math.complex(fourierCoefficients[k])) *
          sin(2 * Math.PI * frequency * time));
    y +=
      scaleCoeff *
      (-1 *
        math.im(math.complex(fourierCoefficients[k])) *
        cos(2 * Math.PI * frequency * time) +
        math.re(math.complex(fourierCoefficients[k])) *
          sin(2 * Math.PI * frequency * time));

    fill("#E9D2C0");
    stroke("#E9D2C0");
    line(x, y, intiX, initY);
    ellipse(x, y, 5);
  }
  drawx.unshift(x);
  drawy.unshift(y);

  beginShape();
  noFill();
  for (let i = 0; i < drawx.length; i++) {
    vertex(drawx[i], drawy[i]);
  }
  endShape();

  point_limit = 30000;

  if (drawx.length > point_limit) {
    drawx.pop();
  }
  if (drawy.length > point_limit) {
    drawy.pop();
  }

  time += 0.002;
}
