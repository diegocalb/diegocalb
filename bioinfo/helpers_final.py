import pysam
import matplotlib.pyplot as plt
import seaborn as sns
import pycircos
from collections import defaultdict
import random


def reads_statistics(file):
    """Statistics of the reads alignments

    Parameters
    ----------
    file : str
        Path of the SAM file

    Returns
    -------
    dict
        Dict with percentages of each flag
    dict
        Dict with counts of each read
    """
    #Load BAM file
    with pysam.AlignmentFile(file, "rb") as sam:
        total_reads = 0
        flag_counts = {}
        freq_name_reads = {}

        for read in sam:
            total_reads += 1
            flag = read.flag
            flag_counts[flag] = flag_counts.get(flag, 0) + 1
            read_name = read.query_name
            freq_name_reads[read_name] = freq_name_reads.get(read_name, 0) + 1

    #Percentages of each flag
    percentages = {flag: count / total_reads * 100 for flag, count in flag_counts.items()}
    
    #Repeat for each read
    repeat_name_reads = {name_read: freq for name_read, freq in freq_name_reads.items()}# if frecuencia > 1}
    sorted_repeat_name_reads = dict(sorted(repeat_name_reads.items(), key=lambda item: item[1], reverse=True))

    flag = list(percentages.keys())
    counts = list(percentages.values())

    # Graficar los datos
    plt.figure(figsize=(15, 8))
    plt.subplot(1,2,1)
    sns.barplot(flag, counts)
    plt.xlabel('Flag', fontsize=14)
    plt.ylabel('Reads percentages', fontsize=14)
    plt.title('Percentages of each flag', fontsize=16)

    quant = list(sorted_repeat_name_reads.values())
    plt.subplot(1,2,2)
    sns.histplot(quant)
    plt.xlabel('Amount of repeats', fontsize=14)
    plt.ylabel('Amount of reads', fontsize=14)
    plt.title('Frequency of reads', fontsize=16)

    plt.show()
    return percentages, sorted_repeat_name_reads


def find_max_min_position(sam_file):
    """Find the maximun and minimum position of the whole coverage

    Parameters
    ----------
    sam_file : str
        Path of SAM file
    """
    # Start min and max position with extreme values
    min_position = float('inf')
    max_position = float('-inf')

    with pysam.AlignmentFile(sam_file, "rb") as sam:
        for read in sam:
            if not read.is_unmapped:  # Ignore unmapped reads
                start_position = read.reference_start
                end_position = read.reference_end

                # Update max and min positions
                min_position = min(min_position, start_position)
                max_position = max(max_position, end_position)

    print (f'Minimun position: {min_position}. Maximum position: {max_position}')

def reads_per_chromosome(sam_file):
    """_summary_

    Parameters
    ----------
    sam_file : str
        Path of the SAM file
    """
    reads_per_chrom = {}

    with pysam.AlignmentFile(sam_file, "rb") as sam:
        for read in sam:
            if not read.is_unmapped:   # Ignore unmapped reads
                chromosome = sam.get_reference_name(read.reference_id)
                reads_per_chrom[chromosome] = reads_per_chrom.get(chromosome, 0) + 1

    reads_per_chrom = dict(sorted(reads_per_chrom.items(), key=lambda item: item[0], reverse=False))

    chromosomes = list(reads_per_chrom.keys())
    reads_amount = list(reads_per_chrom.values())

    sns.barplot(chromosomes, reads_amount)
    plt.xlabel('Chromosome')
    plt.ylabel('Number of reads')
    plt.title('Number of reads per chromosome')
    plt.xticks(rotation=90)
    plt.show()

def sam_to_bed(input_sam, output_bed):
    with pysam.AlignmentFile(input_sam, 'r') as samfile, open(output_bed, 'w') as bedfile:
        for read in samfile:
            bedfile.write(f"{read.reference_name}\t{read.reference_start}\t{read.reference_end}\n")

def sam_to_bam(input_sam, output_bam):
    with pysam.AlignmentFile(input_sam, 'r') as samfile, pysam.AlignmentFile(output_bam, 'wb', header=samfile.header) as bamfile:
        for read in samfile:
            bamfile.write(read)


def circular_plot(file_genome, file_all_seq, file_deg_seq, circular_plot_file):
    """Circular plot for mapping sequences

    Parameters
    ----------
    file_genome : str
        Path of the genome in bed format
    file_all_seq : str
        Path of the sequences alignments in csv format
    file_deg_seq : str
        Path of the DEGs sequences alignments in csv format
    circular_plot_file : str
        Output path for the plot
    """
    Garc    = pycircos.Garc
    Gcircle = pycircos.Gcircle

    circle = Gcircle()
    with open(file_genome) as f:
        f.readline()
        for line in f:
            line   = line.rstrip().split(" ") 
            name   = line[5]
            length = int(line[4]) 
            arc    = Garc(arc_id=name, size=length, interspace=3, 
                        raxis_range=(800,880), labelposition=90, label_visible=True)
            circle.add_garc(arc)
    circle.set_garcs()
    circle.figure

#    values_all   = [] 
    arcdata_dict = defaultdict(dict)
    with open(file_all_seq) as f:
        f.readline()
        for line in f:
            line  = line.rstrip().split(",")
            name  = line[4]     
            start = int(line[2])
            end   = int(line[3]) 
            width = end-start 
            if name not in arcdata_dict:
                arcdata_dict[name]["positions"] = []
                arcdata_dict[name]["values"] = [] 
            arcdata_dict[name]["positions"].append(start) 
            arcdata_dict[name]["values"].append(10)
    #        values_all.append(10)

    #vmin, vmax = min(values_all), max(values_all)

    for key in arcdata_dict:  
        circle.scatterplot(key, data=arcdata_dict[key]["values"], positions=arcdata_dict[key]["positions"], 
                        #rlim=[vmin-0.05*abs(vmin), vmax+0.05*abs(vmax)], 
                        raxis_range=(700,780), facecolor="orangered", spine=True, markersize=1)

#    values_all   = [] 
    arcdata_dict = defaultdict(dict)
    with open(file_deg_seq) as f:
        f.readline()
        for line in f:
            line  = line.rstrip().split(",")
            name  = line[4]     
            start = int(line[2])
            end   = int(line[3]) 
            color = line[6]
            if name not in arcdata_dict:
                arcdata_dict[name]["positions"] = []
                arcdata_dict[name]["values"] = [] 
                arcdata_dict[name]["colors"] = []
            arcdata_dict[name]["positions"].append(start) 
            arcdata_dict[name]["values"].append(random.randint(1,30))
            arcdata_dict[name]["colors"].append(color)
    #        values_all.append(10)

    #vmin, vmax = min(values_all), max(values_all)

    for key in arcdata_dict:  
        circle.scatterplot(key, data=arcdata_dict[key]["values"], positions=arcdata_dict[key]["positions"], 
                        #rlim=[vmin-0.05*abs(vmin), vmax+0.05*abs(vmax)], 
                        raxis_range=(500,680), facecolor=arcdata_dict[key]["colors"], spine=True, 
                        markersize=20)

    plt.savefig(circular_plot_file)