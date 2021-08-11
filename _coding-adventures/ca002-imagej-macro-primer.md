---
title: "Primer to ImageJ Macro language"
excerpt: "Basic syntax and functionalitites of ImageJ1 macro scripting"
---
### ImageJ and Fiji Is Just ImageJ (FIJI)
[ImageJ](https://imagej.nih.gov/ij/) is a free-to-use open-source image analysis extremely versatile software that since its release in 1997, has become one of the most popular tool for all kinds of image analysis tasks.

[FIJI](https://imagej.net/software/fiji/downloads) (it's just ImageJ) it's an ImageJ version that comes with several plugins already installed and makes it easy to install new ones. Over the years ImageJ and particularly FIJI has become enriched with plugins, algorithms, and code snippets for image analysis in all scientific fields.

Personally I've encountered ImageJ / FIJI at the beginning of my PhD but I never had the chance to really get familiar with the software for more than a few clicks here and there through the menu interface. Which is a pity because being an image analysis staple, there is a good chance you will find an existing implementation of whatever you need to do already ready-to-go for you.

So recently I decided to take the excellent course by EPFL on [Image Processing and Analysis for Life Scientists](https://www.edx.org/course/image-processing-and-analysis-for-life-scientists), which, for me didn't introduce many new concepts that the ones I had to already encounter in my PhD, but has a good primer on ImageJ use and programming. So I decided to write a summary blog post to illustrate ImageJ programming native language most important features.

### ImageJ Macro language
ImageJ was mostly written in Java and myself as a Python programmer didn't really want to take the time and effort to learn a new programming language to be able to interface with the software. Because let's be honest, after a few days spent clicking through menus and windows, both my hand and my brain was tired and annoyed.

Luckily, ImageJ comes with its own Macro programming language which is actually fairly similar to Python language. Here I will write the basics of ImageJ1 language as a personal reminder for the future.

First of all let's create a new Script through the Plugins->New->Macro menu entry.

#### Important considerations
- The most difficult and frustrating thing I found in ImageJ programming, is that you are _coding as if you would be clicking through the windows and menus_. The clearest example of this, is that to modify or work on an image, you cannot do it **directly** referring to the image "object" but you would first **need to activate the image window** (either by ID or title) and then work on it. This is the same with things like Results and ROIs in the ROI manager.
- You should include a ; at the end of every line in ImageJ macro language. The compiler will actually not complain if you don't but in certain cases, especially when dealing with flow control, an error will pop up.
- The actual code is written in the **Macro window**, but the results of printing statements will actually come up into the **Log window**.
- You can actually run a wide variety of different languages including Java, Python and R if you have them properly installed from the same Macro window.
- Press CTRL+R to run the code
- Go to Help->Macro Functions... to get the full list of available functions and system variables (it will be very important!).

#### Variables, Strings and Arrays

Variables in ImageJ can basically be:

1. Boolean
2. Numeric
3. String
4. Arrays

Interestingly variables and typeless, meaning that they can be whatever you want them to be and you can re-define the same variable multiple times with different types as you could do in Python. Variables are always stored as **64-bit double-float precision**, so float and integer numbers are always stored as double-float variables; while boolean variable will be always stored as either 0 (false) or 1 (true).

Here a brief summary on how to define variables:

````
var1 = 5;
var2 = 3.0;

var3 = true;

str1 = "this is a string";
arr1 = newArray(3)  //empty array with length 3;
arr2 = newArray("this", "is", "an", "example") //array with length 4 filled with strings;

print(var2); // will return 3
print(var3); // will return 1
````

#### Arrays
Arrays are basically equivalent to Python lists: _ordered one-dimensional sequences of objects_. These objects can be either numbers or strings as seen above.

After you defined an array as a variable you can do the following:

````
// Arrays are 0-indexed
// You can assign single values indexing as you would do in Python
arr1[0] = 100
arr1[1] = 200
arr1[2] = 300

// Oddily you cannot use the usual print function, use instead
Array.print(arr1) // will return 100, 200, 300

// You cannot use the function lengthOf(), use instead
print(arr1.length) // will return 3
````

#### Conditionals

The classical IF-THEN-ELSE statements work pretty much as you would expect. If the IF-ELSE conditions is defined in one line the {} block is not needed.

Here's an example with a string evaluation of the image title to check for a specific format.

````
run("Blobs (25K)"); // run any macro or plugin that already exists
title = getTitle(); // title of the currently active image window
if (endsWith(title, ".gif")) {
    showMessage("This is a GIF file");
} else {
    showMessage("This is NOT a GIF file");
}
````

#### Loops
The traditional FOR and WHILE loops are available in ImageJ and work as you would expect.

Here's an example in which we want to change the Fluorescent Cells sample image to more color-blind-friendly LUTs.

````
run("Fluorescent Cells"); // open sample image
img_id = getImageID(); // get image ID
selectImage(img_id); // activate image window

getDimensions(width, height, channels, slices, frames); // doesn't return anything simply assign to those variables the dimensions of the image

luts_array = newArray("Magenta","Yellow","Cyan"); // create an array with the 3 LUTs I want to appy

for (i = 1; i <= channels; i++) { // here I start the loop from 1 because the SetSlice because the first channel is 1 not 0
    setSlice(i);
    run(luts_array[i-1]); // I have to subtract 1 to index for indexing Array
}
````

You can do the same as above using a WHILE loop instead.

````
i = 1;
while (i <= channels) {
    setSlice(i);
    run(luts_array[i-1]);
    i += 1;
}
````

#### Functions
Functions can be defined very similarly to Python, with the bonus difference that functions can be defined **after** its first use. So if you want you can dump all your function definitions at the end of the script and keep the workflow clean.

````
run("Fluorescent Cells");
img_id = getImageID();
luts_array = newArray("Magenta","Yellow","Cyan");

ApplyLUTtoSlice(img_id, luts_array)

// FUNCTION DEFINITIONS
function ApplyLUTtoSlice(img_id, lut_array) { 
    selectImage(img_id);
    getDimensions(width, height, channels, slices, frames);
    for (i = 1; i <= channels; i++) {
        setSlice(i);
        run(luts_array[i-1]);   
}
````

The tricky part of functions in ImageJ is to find out what functions or macros are already available!

Although the auto-filling function of the editor is generally quite good, it only prompts the first functions of the list completely forgetting to show you the alphabetically-later functions. As a consequence, already existing functions are actually relatively hard to find, unless you go to the website full of Macro functions and spend some time CTRL+F finding your way to what you need.

Anything that would run through the normal Menus, for example opening sample images or applying LUTs (as seen above) use the _run()_ command. So how do you know what command you should write instead the _run()_ brackets? Well, as far as I could see, the easiest way it to use the Macro Recorder and simply check what it should be! You can access it via Plugins->Macros->Record...

This is quite frustrating for me as there doesn't seem to be an easier way to find what command you should run unless you are first clicking through the menus with the Macro recorder open.