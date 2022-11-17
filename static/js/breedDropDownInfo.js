const dogDropDownData = dog_data;
var select = d3.select("#dogBreed")

dog_data.forEach((breedInfo)=>{
    select.append("option").text(breedInfo.breed)
});