// import data from matched_dog_data.js
const dogTableData = dog_data;

// Reference the HTML table using d3
var tdBreed = d3.select("td.breed");
var tdDescription = d3.select("td.description");
var tdTemperament = d3.select("td.temperament");
var tdHeight = d3.select("td.height");
var tdWeight = d3.select("td.weight");
var tdLife = d3.select("td.life");
var tdGroup = d3.select("td.group");
var tdGrooming = d3.select("td.grooming");
var tdShedding = d3.select("td.shedding");
var tdEnergy = d3.select("td.energy");
var tdTraining = d3.select("td.training");
var tdDemeanor = d3.select("td.demeanor");

function breedSelect() {
    // Grab breed from select label
    let chosenBreed = d3.select("#dogBreed").property("value");
    let selectedData = dogTableData;
    selectedData = selectedData.filter(row => row.breed === chosenBreed);
    tdBreed.text(selectedData[0].breed);
    tdDescription.text(selectedData[0].description);
    tdTemperament.text(selectedData[0].temperament);
    tdHeight.text(selectedData[0].avg_height);
    tdWeight.text(selectedData[0].avg_weight);
    tdLife.text(selectedData[0].avg_life_expectancy);
    tdGroup.text(selectedData[0].group);
    tdGrooming.text(selectedData[0].grooming_frequency_category);
    tdShedding.text(selectedData[0].shedding_category);
    tdEnergy.text(selectedData[0].energy_level_category);
    tdTraining.text(selectedData[0].trainability_category);
    tdDemeanor.text(selectedData[0].demeanor_category);    
};

// Code to listen for on change to happen
d3.selectAll("select").on("change", breedSelect);


