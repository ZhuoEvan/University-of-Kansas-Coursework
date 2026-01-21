//temperature.c
#include <stdio.h>

//New Line Function | Created by Me
void newLine() {
    printf("\n");
}

//Celsius to Fahrenheit Converter Function | Created by Me
float celsius_to_fahrenheit(float celsius) {
    return celsius * (9.0/5) + 32; //return the result of the conversion equation
}

//Fahrenheit to Celsius Converter Function | Created by Me
float fahrenheit_to_celsius(float fahrenheit) {
    return (fahrenheit - 32) * (5.0/9); //return the result of the conversion equation
}

//Celsius to Kelvin Converter Function | Created by Me
float celsius_to_kelvin(float celsius) {
    return celsius + 273.15; //return the result of the conversion equation
}

//Kelvin to Celsius Converter Function | Created by Me
float kelvin_to_celsius(float kelvin) {
    return kelvin - 273.15; //return the result of the conversion equation
}

//Categorize Temperature Function | Created by Me
void categorizeTemperature(float celsius) {
    if (celsius <= 0) {
        printf("Temperature category: Freezing\n"
            "Weather advisory: Stay Indoors.");
    } else if (celsius <= 10) {
        printf("Temperature category: Cold\n"
            "Weather advisory: Wear a jacket.");
    } else if (celsius <= 25) {
        printf("Temperature category: Comfortable\n"
            "Weather advisory: You should feel comfortable.");
    } else if (celsius <= 35) {
        printf("Temperature category: Hot\n"
            "Weather advisory: Bring Hydration.");
    } else {
        printf("Temperature category: Extreme Heat\n"
            "Weather advisory: Try to Stay Indoors or in Shade.");
    }
}

//Attach Temperature Unit | Created by Me
void unitAttach(int convert) {
    if (convert == 1) { //Celsius Unit
        printf("°C\n"); //Attach to same line
    } else if (convert == 2) { //Fahrenheit Unit
        printf("°F\n"); //Attach to same line
    } else { //Kelvin Unit
        printf("K\n"); //Attach to same line
    }
}

//Convert the Temperature Function | Created by Me
void convertTemp(float temp, int scale, int convert) {
    float newTemp = 0;
    float temporaryTemp = 0;
    if (scale == 1) { //Starting Temp is Celsius
        if (convert == 2) { //Convert to Fahrenheit
            newTemp = celsius_to_fahrenheit(temp);
        } else { //Convert to Kelvin
            newTemp = celsius_to_kelvin(temp);
        }
    } else if (scale == 2) { //Starting Temp is Fahrenheit
        if (convert == 1) { //Convert to Celsius
            newTemp = fahrenheit_to_celsius(temp);
        } else { //Convert to Kelvin
            temporaryTemp = fahrenheit_to_celsius(temp);
            newTemp = celsius_to_kelvin(temporaryTemp);
        }
    } else if (scale == 3) { //Starting Temp is Kelvin
        if (convert == 1) { //Convert to Celsius
            newTemp = kelvin_to_celsius(temp);
        } else { //Convert to Fahrenheit
            temporaryTemp = kelvin_to_celsius(temp);
            newTemp = celsius_to_fahrenheit(temporaryTemp);
        }
    }

    newLine(); //Empty Line
    printf("Converted temperature: %.2f", newTemp); //Print the converted temperature rounded to two decimal places | Used Google Gemini
    unitAttach(convert); //Attach the correct new Temperature Unit to converted temperature
    float categorizeTemp = 0;
    if (scale == 1) {
        categorizeTemperature(temp);
    } else if (scale == 2) {
        categorizeTemp = fahrenheit_to_celsius(temp);
        categorizeTemperature(categorizeTemp);
    } else {
        categorizeTemp = kelvin_to_celsius(temp);
        categorizeTemperature(categorizeTemp);
    }

}

//Valid Conversion Function | Created by Me
int validConvert(int scale, int convert) {
    if (scale == convert) { //Check if the value of scale and convert are the same
        return 0; //return False
    } else {
        return 1; //return True
    }
}

//Valid Kelvin Function | Created by Me
int validKelvin(float kelvin) {
    if (kelvin >= 0) { //Check if Kelvin is not negative
        return 1; //return True
    } else {
        return 0; //return False
    }
}

//Valid Function | Created by Me
int checkValid(float temp, int scale, int convert) {
    if (scale == 3) { //Validity Check for Kelvin Only
        if (validKelvin(temp) == 0) { //Check if temperature is negative
            printf("Error 001: Negative Kelvin\n");
            return 0; //return False
        }
    }
    if (validConvert(scale, convert) == 1) { //Check if conversion are valid
        return 1; //return True
    } else {
        printf("Error 002: Same Conversion\n");
        return 0; //return False
    }
}
//Main Function | Created by Me
int main() {
    float *temp; //Initialize a pointer to temp
    int currScale = 0; //Initialize a pointer to currScale
    int convertScale = 0; //Initialize a pointer to convertScale

    printf("Enter the temperature: "); //Input Message for entering temperature
    scanf("%f", temp); //Input for temperature
    printf("Choose the current scale (1) Celsius, (2) Fahrenheit, (3) Kelvin: "); //Input Message for entering current scale
    scanf(" %d", &currScale); //Input for current scale | stackOverflow
    printf("Convert to (1) Celsius, (2) Fahrenheit, (3) Kelvin: "); //Input Message for entering convert scale
    scanf(" %d", &convertScale); //Input for convert scale | stackOverflow
    if (checkValid(*temp, currScale, convertScale) == 1) {
        convertTemp(*temp, currScale, convertScale);
    } else { //Error Case
        printf("An Error had been Encountered\nProgram will Terminate\n"); //Terminate Program Message
    }
}