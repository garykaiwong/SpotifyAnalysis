let path = "data.json";

let response = d3.json(path);

console.log(response);


function init() {

    let path = "data.json";
    data = d3.json(path);
    console.log(data);

    let dropdown = d3.select("#selDataset");

        // Read json data
     d3.json("data.json").then((data) =>{
         let name = data.data;

            name.forEach((person) =>{
                dropdown.append("option").text(person["id"]).property("value", person["id"]);
            })

            let sample = name[0]['id'];
            console.log(sample);

            build(sample);
     });

}

    

function build(sample) {
    
    let path = "data.json"
    // Read the json data
    d3.json(path).then(info => {
        console.log(info);
    
    let idInfo = info.data.filter(obj => obj.id == sample);
    console.log(idInfo);
    //console.log(idInfo[0]);
    //console.log(idInfo[0]['name']);

    let result = idInfo[0];
    console.log(result);

    //console.log(Object.keys(result));
    //console.log(result["songs"]);

    let panel = d3.select("#sample-metadata");

    panel.html("");

    for (i=0; i<10; i++){
        let song = result["songs"][i];
        let artist = result["artists"][i].replace("[", "").replace("]", "").replace("'", '').replace("'", '').replace("'", "").replace("'", "");
        console.log(song);
        console.log(artist);
        panel.append("p").text(`${song} by ${artist}`);
    }

    //Object.entries(result).forEach(([key,detail]) => {
    //       panel.append("p").text(`${key}: ${detail}`);
    //   })
    }
)};


function optionChanged(thing){

    build(thing);
   
}

init();
