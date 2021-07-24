let path = "data.json";

let response = d3.json(path);

console.log(response);


function build(sample) {
    
    let path = "data.json"
    // Read the json data
    d3.json(path).then(info => {
        console.log(info);
    
    let idInfo = info.data.filter(obj => obj.id == sample);
    console.log(idInfo);
    console.log(idInfo[0]);
    console.log(idInfo[0]['name']);

    let result = idInfo[0];

    console.log(Object.keys(result));
    console.log(result["songs"]);

    let panel = d3.select("#sample-metadata");

    panel.html("");

    for (i=0; i<10; i++){
        console.log(result["songs"][i]);
    }


       //Object.entries(result).forEach(([key,detail]) => {
       //    panel.append("p").text(`${key}: ${detail}`);
       //})
    
    


    }
)};

function sorter(year) {

    let path = "data.json";

    let response = d3.json(path);
    
    let fil = response.filter(obj => obj.id == year);

    console.log(fil);

};