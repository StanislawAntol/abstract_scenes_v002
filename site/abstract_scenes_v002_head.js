var restrictInputStr = decode(gup("restrictInput"));

if (restrictInputStr == "") {
    restrictInput = true;
} else {
    if (restrictInputStr != "0") {
        restrictInput = true;
    } else {
        restrictInput = false;
    }
}

// Maybe want to parse list of scene types in the future
var sceneTypeList = [];
var sceneTypeStr = decode(gup("sceneType"));

if (sceneTypeStr == "") {
    sceneType = "Living";
} else {
    sceneType = sceneTypeStr;
}

var numScenesStr = decode(gup("numScenes"));
var numScenes;
if (numScenesStr == "") {
    // Default "demo" settings
    numScenes = 3;
    sceneTypeList = ["Living", "Park", "Living"];
} else {
    numScenes = Number(numScenesStr);

    for (var i = 0; i < numScenes; i++) {
        sceneTypeList.push(sceneType);
    }
}

curSceneType = sceneTypeList[0];
var titleStr;
if (curSceneType == "Park") {
    titleStr = curSceneType
} else {
    titleStr = "Living/Diving Room";
}
    
var randInitStr = decode(gup("randInit"));
var randInit = true;
if (randInitStr == "") {
    randInit = true;
} else {
    if ( randInitStr == "0") {
        randInit = false;
    } else {
        randInit = true;
    }
}

// ===========================================================
// Functions to help parse the URL query string for AMT data
// ===========================================================
function gup(name) {
    var regexS = "[\\?&]" + name + "=([^&#]*)";
    var regex = new RegExp(regexS);
    var tmpURL = window.location.href;
    var results = regex.exec(tmpURL);
    if (results == null) {
        return "";
    } else {
        return results[1];
    }
}

function decode(strToDecode) {
    var encoded = strToDecode;
    return unescape(encoded.replace(/\+/g, " "));
}

function get_random_int(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

function zero_pad(num, numZeros) {
    var n = Math.abs(num);
    var zeros = Math.max(0, numZeros - Math.floor(n).toString().length );
    var zeroString = Math.pow(10,zeros).toString().substr(1);
    if( num < 0 ) {
        zeroString = '-' + zeroString;
    }

    return zeroString+n;
}
