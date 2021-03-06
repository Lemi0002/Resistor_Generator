# Resistor_Generator
Repository containing scripts for automatically generating THT resistors with
color codes. Resistors with 4 and 5 color bands are being supported.
This script can scan any text file to filter out certain commands and
automatically generate appropriate resistor PNGs based on the given information.

## Dependencies
This code is dependent on some python modules. Execute following commands to
download the modules:

    pip install pypng

## Tool configuration
The following software versions were used to develop this software:

* VSCode: v1.66.2
* Python: v3.10.4

Versions of python modules:

* pypng: v0.0.21

## Capabilities
Resistor with 4 color bands:

| Band | Function   |
|:-----|:-----------|
| 1    | Digit 1    |
| 2    | Digit 2    |
| 3    | Multiplier |
| 4    | Tolerance  |

Resistor with 5 color bands:

| Band | Function   |
|:-----|:-----------|
| 1    | Digit 1    |
| 2    | Digit 2    |
| 3    | Digit 3    |
| 4    | Multiplier |
| 5    | Tolerance  |

Resistor color coding which is used by this generator:

![Resistor color code](Resources/Drawables/Resistor_Color_Code.PNG)

## Available console arguments
Following arguments can be passed to the script:

| Name                       | Parameters | Parameter description       |
|:---------------------------|:-----------|:----------------------------|
| --input, -i                | 1          | Input file                  |
| --outputPathAbsolute, -opa | 1          | Absolute path of the output |
| --help                     | 0          |                             |

### --input, -i
Specifies the file which shall be pared. This command can also be called
multiple times with different files.

Spaces within the given paths are not supported.

Parameters:

    P1: Path [string]

Example:

    -i Z:\Resistor_Generator\Test\Test1.md -i Z:\Resistor_Generator\Test\Test2.md

### --outputPathAbsolute, -opa
Specifies the absolute output path. If this path is set the output of all input
files is saved to the same location. Relative output path commands within the
input files will have no effect.

Spaces within the given paths are not supported.

Parameters:

    P1: Path [string]

Example:

    -opa Z:\Resistor_Generator\Test

### --help
If this arguments is set, a table with all available console arguments and file
commands will be printed to the console.

Parameters:

    None

Example:

    --help

## File command protocol
File commands refer to certain strings within any text file that is passed to
the python script by console arguments.

With the help of these available commands, the result of the output PNG can be
modified to any extent. There are default values set for every parameter that
can be modified. If the user wishes to modify any of these values one can do so
by using the appropriate command.

The output PNG will be generated after calling the "Specification" command.

Each command starts with a prefix in this case with "\_RG\_". After this prefix,
the actual command name must be specified. Depending on the command, a different
amount of parameters must be set. All of them must be separated by a semicolon
";". As a postfix a simple underscore "_" must be added.

Indication characters:

    Character start: "_RG_"
    Character end: "_"
    Character deliminator: ";"

File command templates:

    _RG_<Name>;<P1>_
    _RG_<Name>;<P1>;<P2>_
    _RG_<Name>;<P1>;<P2>;<P3>_


## Available file commands
These are the available file commands:

| Name                  | Parameters | Parameter description            |
|:----------------------|:-----------|:---------------------------------|
| Specification         | 2          | Value, Tolerance                 |
| OutputPathRelative    | 1          | Relative path of the output      |
| ImageSize             | 2          | Width, Height                    |
| BodyPosition          | 2          | X, Y                             |
| BodySize              | 2          | Width, Height                    |
| BodyColor             | 3          | Red, Green, Blue                 |
| LegSize               | 2          | Width, Height                    |
| LegColor              | 3          | Red, Green, Blue                 |
| CodeBarCount          | 1          | Code bar count                   |
| CodeBarClearanceSide  | 1          | Clearance body to code bar       |
| CodeBarClearance      | 1          | Clearance code bar to code bar   |
| BackgroundColor       | 3          | Red, Green, Blue                 |

### Specification
Specifies the actual resistor value and tolerance. The value must be entered in
Ohms and the tolerance in percents. Refer to the *Capabilities* chapter for more
information. Depending on the code bar count a different maximum value is
accepted.

The output PNG will be generated after calling this command. The output will be
named according to the following scheme:

    Resistor_<Value>_<Tolerance>.png

Parameters:

    P1: Value [0.1 - (99 or 999) * 10^9]
    P2: Tolerance [0.05 - 10]

Example:

    _RG_Specification;4700;1_

### OutputPathRelative
Specifies the relative location of the PNG output based on the path of the input
file where the specification command was found. This command will only have an
effect if no absolute output path was set by the command line arguments.

If no relative location is specified, the output will be saved to the directory
of the input file.

Parameters:

    P1: Path [string]

Example:

    _RG_OutputPathRelative;Output/Pictures_

### ImageSize
Specifies the image size of the output in pixel dimensions.

Parameters:

    P1: Width [unsigned int]
    P2: Height [unsigned int]

Example:

    _RG_ImageSize;41;9_

### BodyPosition
Specifies the location of the resistors body top left corner in pixel
coordinates.

Parameters:

    P1: X [int]
    P2: Y [int]

Example:

    _RG_BodyPosition;6;1_

### BodySize
Specifies the resistor body size in pixel dimensions.

Parameters:

    P1: Width [unsigned int]
    P2: Height [unsigned int]

Example:

    _RG_BodySize;29;7_

### BodyColor
Specifies the color of the resistor body.

Parameters:

    P1: Red [0 - 255]
    P2: Green [0 - 255]
    P3: Blue [0 - 255]

Example:

    _RG_BodyColor;100;204;180_

### LegSize
Specifies the resistor leg size in pixel dimensions.

Parameters:

    P1: Width [unsigned int]
    P2: Height [unsigned int]

Example:

    _RG_LegSize;5;3_

### LegColor
Specifies the color of the resistor legs.

Parameters:

    P1: Red [0 - 255]
    P2: Green [0 - 255]
    P3: Blue [0 - 255]

Example:

    _RG_LegColor;50;50;50_

### CodeBarCount
Specifies how many code bars will be drawn. Supported are 4 and 5 bar wide
resistors.

Parameters:

    P1: Count [4 - 5]

Example:

    _RG_CodeBarCount;5_

### CodeBarClearanceSide
Specifies the clearance between the two outermost code bars to the resistor
body sides in pixel dimensions. 

Parameters:

    P1: Clearance [unsigned int]

Example:

    _RG_CodeBarClearanceSide;2_

### CodeBarClearance
Specifies the minimal clearance between any adjacent code bars. The clearance
between the multiplier and the tolerance is always at least two times this size.
But it can get bigger as the value and multiplier bars are left aligned and the
tolerance bar is right aligned to the resistor body. The distance between the
multiplier and the tolerance is then being increased to match this alignment.

Parameters:

    P1: Clearance [unsigned int]

Example:

    _RG_CodeBarClearance;2_

### BackgroundColor
Specifies the color of the background color.

Parameters:

    P1: Red [0 - 255]
    P2: Green [0 - 255]
    P3: Blue [0 - 255]

Example:

    _RG_LegColor;255;255;255_
