#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE) #used to accept arguments at the command line

if ( args[1] == "--h") {
print("")
print("*********************************")
print("HELP MENU:")
print("*********************************")
print("")
print("Commands:                                  Info:")
print("--------------------------------------------------")
print("Rscript 0_summarize_csv.R --h       Help Menu")
print("--glance [infile] [outfile]         Quick glance at data")
print("--uni [infile] [outfile]            Univariate distributions")
print("--cor [infile] [outfile]            Correlation matrices")
print("--frq [infile] [outfile]            Frequency tables of categorical variables")
print("--mis [infile] [outfile]            Missing values report")
print("")
print("Current Directory is:")
print(getwd())
print("")
} 


#Example of file: /Users/jje/Documents/00__mytools/2_itsfriday/2_data/1_raw/Account Status History.csv
if ( args[1] == "--glance") {
print("glance")
df <- read.csv(args[2])
print("")
print("Head:")
print("--------------------------------------------------")
print(head(df))
print("Tail:")
print("--------------------------------------------------")
print(tail(df))
print("Summary:")
print("--------------------------------------------------")
print(summary(df))
print("")
} 
if ( args[1] == "--uni") {
print("uni")
}
if ( args[1] == "--cor") {
print("cor:")
}
if ( args[1] == "--frq") {
print("frq:")
}
if ( args[1] == "--mis") {
print("mis:")
}




