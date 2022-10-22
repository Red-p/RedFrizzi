## RedFrizzi
*Permette di cercare tracce di password relativamente a mail o domini su precedenti data breach.*
Se esistono risultati restituisce le iniziali delle password e l'hash della stessa in sha1<\br>
E' possibile generare il file da dare in pasto a john con l'opzione rf --john <nome_file>, dove <nome_file> contiene i risultati generati. </br>
</br>
</br>
options:
</br>
Usage: [rf -options]
</br>
> -t <target> : Enter the target name
> -f < input_filename> : Load target names from file
> -o <output_filname> : Print response to <output_file>
> --john <inputfile>: Create outputfile for John using <inputfile>
> --init : Set API Key
> --clear : Reset terminal
