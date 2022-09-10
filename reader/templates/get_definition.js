let dictionary = 
{
    fetchData: function(word)
    {
        api_key = "d98bcc41-7387-4462-97a6-a380a51bbcc6";

        url_part_1 = "https://www.dictionaryapi.com/api/v3/references/learners/json/";
        url_part_2 = word;
        url_part_3 = "?key=" + api_key;
        final_url = url_part_1 + url_part_2 + url_part_3;
        fetch
        (
            final_url
        )
        .then((response) => response.json())
        .then((data) => this.checkIfValid(data));
    },

    checkIfValid: function(data)
    {
        if(data.length == 0)
        {
            document.getElementById("part_of_speech").innerHTML = "Error: Not a valid word";
        }
        else
        {
            this.displayData(data);
        }
    },
    
    displayData: function(data)
    {
        var all_data = JSON.parse(data);
        definition_section = all_data['meta']['app-shortdef'];
        part_of_speech = definition_section['fl'];
        definition = definition_section['def'];

        document.getElementById("part_of_speech").innerHTML = part_of_speech;
        document.getElementById("definitions").innerHTML = definition;
    },

    get_info: function(word) 
    {
        this.fetchData(word);
    },
}


var all_words = document.querySelectorAll(".word")
document.write("hello");
for (i = 0; i < all_words.length; ++i) 
{
    var word = all_words[i].innerHTML;
    all_words[i].addEventListener("click", function () 
    {
        dictionary.get_info(word);
    });
}