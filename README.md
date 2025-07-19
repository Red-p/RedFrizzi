## RedFrizzi
*A tool to search for password traces related to emails or domains in past data breaches.* </br>
</br>
If results are found, it returns the initial characters of the passwords and their SHA-1 hashes. </br>
It is possible to generate a file to be used with John the Ripper using the option rf --john <filename>, where <filename> contains the generated results. </br>
</br>
options:
</br>
Usage: [rf -options]
</br>

-t <target> : Enter the target name </br>
-f <input_filename> : Load target names from file </br>
-o <output_filename> : Print response to <output_file> </br>
--john <inputfile> : Create output file for John using <inputfile> </br>
--init : Set API Key </br>
--clear : Reset terminal </br>

</br>
The script uses the APIs provided by https://breachdirectory.org, so you need to obtain an API Key to access the API.
Once you have the key, you can set it using the command rf --init <api_key> or by editing the .env file directly. </br>
