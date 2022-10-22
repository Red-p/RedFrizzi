## RedFrizzi
*Permette di cercare tracce di password relativamente a mail o domini su precedenti data breach.*
Se esistono risultati restituisce le iniziali delle password e l'hash della stessa in sha1<\br>
E' possibile generare il file da dare in pasto a john con l'opzione rf --john <nome_file>, dove <nome_file> contiene i risultati generati. </br>
</br>
</br>
launch : python3 redfrizzi_no_readlines.py/redfrizzi.py </br>
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

Al momento sono presenti due script: </br>
> redfrizzi_no_readlines.py: più indicato per file di grandi dimensioni ma più soggetto ad errori </br>
> redfrizzi.py: poco indicato per file di grandi dimensioni ma meno soggetto ad errori
