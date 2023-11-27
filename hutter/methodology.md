
# Team Sherlock Project Methodology

- This approach is a way to address the issue of updating the codebase to a modern language using GPT or another similar language model without sending the entire codebase to the language model at once. To be able to port the codebase the AI needs to understand the entirety of the codebase, which can be done either by sending the entire codebase to the language model at once or by breaking the codebase up into parts. Breaking the codebase up into parts is most likely required because language models have a limited input size and in the rare case where they don’t have a limited input size if a crash or any kind of error were to occur all progress would be lost. 

# Steps for modernizing each file in codebase  
- Iterate through every file in code base and add to the database the file name and location of the file in the file tree.

- Iterate through every function in each file and store the CBASIC function code encoded as base64 in the database with metadata describing the function (input, output, and if the function calls other non-native functions in the codebase).

- Iterate through all the functions stored in the database that don’t call other non-native functions and decode the function code and send it to GPT to be converted to a modern language then store the now modernized code in the database as base64 with the metadata about the function (input, output, and a description of the function).

- Iterate through all the functions that call non-native functions in the code base and decode the function from base6 and send it to GPT along with the metadata for all the non-native functions that this function calls then store it encoded as base64 to the database with metadata describing the function (input, output, and a description of the function).

- Iterate through the database where the file names and file locations in file tree is located and for every file iterate through the functions that are within that file and assemble a new modernized source code file using the modernized functions that are stored as base64 in the database. The newly generated file can be sent to GPT again to organize the code and rename variables.

# Important points
- The purpose of the metadata for every function that is stored in the database serves the purpose of allowing GPT to understand the non-native functions that are being called by other functions so that the entire code base doesn’t need to be passed to GPT at once. The metadata also serves as a secondary purpose of allowing us to generate documentation for every function in the CBASIC codebase as well as the modernized codebase.  

- The process of going from CBASIC function to a modern language function can be done in two ways. 
    - A language model can be retrained to understand CBASIC and the CBASIC code can go directly to a modern language.
    - The vocabulary of the language can be defined and using simple code the CBASIC functions can be converted to pseudocode that GPT can understand which can then be converted to a modern language.

- Special attention needs to be given to variable names so that collision doesn’t occur. This could be done by either storing the variables from the codebase in the database or through specialized prompts to generate new variable names that won’t collide with one another.
  
# Organization of the database
- TBD
