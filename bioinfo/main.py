# BIOINFORMATICS MAIN MODULE

from helpers_final import (
    find_max_min_position, reads_statistics,
    reads_per_chromosome, circular_plot)

#Constants
file = 'bioinfo/data/total_reads_alignment.sam'
file_genome = 'bioinfo/data/chromosomes.txt'
file_all_seq = 'bioinfo/data/full_bed_clean.csv'
file_deg_seq = 'bioinfo/data/degs.csv'
circular_plot_file = 'bioinfo/data/outputs/circular_plot.jpg'


# Statistics for the reads
percentages, repeats = reads_statistics(file)

#Max and min position of the genome coverage
find_max_min_position(file)

#Amount of reads per chromosome
reads_per_chromosome(file)

#Make a circular plot for chromosome coverage and DEGs location
circular_plot(file_genome, file_all_seq, file_deg_seq, circular_plot_file)
