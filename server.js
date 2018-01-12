const { exec } = require('child_process');
exec('python test.py -P elo.jp2"', (error, stdout, stderr) => {
  if (error) {
    console.error(`exec error: ${error}`);
    return;
  }

  let resPy = JSON.parse(stdout);
  if (resPy.hasOwnProperty('in')) {
      console.log(`Python spoke: "${resPy.in}"`);
  }
  if (resPy.hasOwnProperty('error')) {
      console.log(`Python error: "${resPy.error}"`);
  }

});
