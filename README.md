# sample_curly_ena

This script is designed to be used to as a way of querying the ENA portal api by offering a list of accessions

USAGE:

python3 advanced_curly.py -i input_file -it sample -qt analysis

Options:
    
    -i --> specify name of input file. Must be in same working directory as the script. Input file should be a line seperated list of accessions
    -it --> specify the type of input accession. e.g. sample, run etc.
    -qt --> specify the data type queried. e.g. analysis, read_run (for reads). A full list of the types of data to query is listed below and also in the ENA portal API docs.
    
    
Query_types:
  
  Please use this vocab list when specifying the data types you wish to query! These are the tested query types. Please ensure your input query type can be queried against these.
  
  Runs = read_run
  Analyses = analysis
  Experiment = read_experiment
