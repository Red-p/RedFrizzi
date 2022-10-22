## RedFrizzi
*Permette di cercare tracce di password relativamente a mail o domini su precedenti data breach.* </br>
</br>
Se esistono risultati restituisce le iniziali delle password e l'hash della stessa in sha1 <\br>
E' possibile generare il file da dare in pasto a john con l'opzione rf --john <nome_file>, dove <nome_file> contiene i risultati generati. </br>
</br>
options:
</br>
Usage: [rf -options]
</br>
> -t <target> : Enter the target name </br>
> -f < input_filename> : Load target names from file </br>
> -o <output_filname> : Print response to <output_file> </br>
> --john <inputfile>: Create outputfile for John using <inputfile> </br>
> --init : Set API Key </br>
> --clear : Reset terminal </br>

Lo script utilizza le API di https://breachdirectory.org, quindi è necessario ottenere l'API Key per accedere alle API. Ottenuta la key è possibile settarla utilizzando il comando rf --init <api_key> oppure modificando direttamente il file env. </br>
