let express = require('express');
let router = express.Router();
// https: //github.com/petranb2/Node_Python
const {
    spawn
} = require('child_process')


/* GET RC page. */
router.get('/', function (req, res, next) {
    // let result = doThings();
    app().then((result) => {
        console.log(`post: ${result}`)
        res.render('rc', {
            title: 'RC',
            pageData: `${result}`
        });

    });
});


function doThings() {
    let dataToSend
    let largeDataSet = []
    // spawn new child process to call the python script
    const python = spawn('python', ['../scripts/test.py'])

    // // collect data from script
    python.stdout.on('data', function (data) {
        // console.log('Pipe data from python script ...')
        //dataToSend =  data;
        largeDataSet.push(data)
        // console.error(`${data}`);
    })

    // // in close event we are sure that stream is from child process is closed
    python.on('close', (code) => {
        // console.log(`child process close all stdio with code ${code}`)
        // send data to browser
        // res.send(largeDataSet.join(''))
        dataToSend = largeDataSet.join('')
        console.log(dataToSend);
        console.log(`pre: ${dataToSend}`)
        return dataToSend;
    })
}

async function operation() {
    return new Promise(function (resolve, reject) {
        let dataToSend
        let largeDataSet = []
        // spawn new child process to call the python script
        const python = spawn('python', ['../scripts/test.py'])

        // // collect data from script
        python.stdout.on('data', function (data) {
            // console.log('Pipe data from python script ...')
            //dataToSend =  data;
            largeDataSet.push(data)
            // console.error(`${data}`);
        })

        // // in close event we are sure that stream is from child process is closed
        python.on('close', (code) => {
            // console.log(`child process close all stdio with code ${code}`)
            // send data to browser
            // res.send(largeDataSet.join(''))
            dataToSend = largeDataSet.join('')
            console.log(dataToSend);
            console.log(`pre: ${dataToSend}`)
            // return dataToSend;
            resolve(dataToSend) // successfully fill promise
        })

        // may be a heavy db call or http request?
    })
}

async function app() {
    var a = await operation() // a is 5
    return a;
}

// app()



module.exports = router;