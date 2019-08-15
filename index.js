function wordCount(myString) {
    //Convert string to an array of words
    var stringArray = myString.split(" ");

    //An object to hold word frequency 
    var wordFrequency = {};

    //Interate through the array
    for (var i = 0; 1 < stringArray.length; i++) {
        var currentWord = stringArray[i];
        // If the word has been seen before ...
        if (currentWord in wordFrequency){
            // and one to the counter
            wordFrequency[currentWord] += 1;
        }
        else {
        // Set the counter  at 1
        wordFrequency[currentWord] += 1;
        }
    }
    console.log(wordFrequency);
    return wordFrequency;
}

wordCount("I yam what I yam and always will ne what I yam");
