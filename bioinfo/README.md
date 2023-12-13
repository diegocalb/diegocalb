
**Bioinfo** 

This is a bioinformatics project.

**Project structure**

bioinfo
├── data/: files with alignment info
|   ├── chromosomes.txt : length of each chromosome
|   ├── degs.csv : DEGs positions and colors for the plot
|   ├── full_bed_clean.csv : all probes positions
|   ├── total_reads_alignments.bed : alignments of all reads in bed format
|   ├── total_reads_alignments.sam : alignments of all reads in sam format
├── outputs/: folder with plots
├── helpers_final.py: functions for the analysis of this project
├── main.py: main file with the analysis
├── README.md: Readme file
├── requirements.txt: python packages needed for the project


**Introduction**

Sunflower is a crop of great economic importance, and one of its most devastating pathogens is the wet rot of the capitulum caused by the fungus Sclerotinia sclerotiorum. There is no genotype with absolute immunity; instead, all identified sources of resistance have been polygenic in nature. Therefore, breeding programs are based on the identification and stacking of favorable genes from different genotypes(1).

With this objective and given the absence of a reference genome, a microarray of oligonucleotides for sunflower based on public ESTs (Expressed Sequence Tags) was designed in 2012 (2). A total of 40,169 probes were designed, and this microarray was used for various studies, including the investigation of the plant-pathogen interaction between sunflower and S. sclerotiorum to identify potential resistance-conferring genes.

For this particular research project, data provided by a doctoral thesis will be used (3). The overall aim of the thesis was to study the transcriptional changes in resistant and susceptible sunflower lines at 0, 4, and 8 days post-inoculation with the pathogen to understand defense responses to S. sclerotiorum in the crop.

Among the results obtained in this thesis, 43 genes with contrasting expression patterns between the resistant and susceptible lines were identified. These were designated as candidate resistance genes and were associated with numerous functions known to play relevant roles in plant defense processes, such as oxidative stress detection, transcription factors, ubiquitination, peptidase inhibitors, membrane zinc ion transporters, amino acid synthesis, and cytoskeleton dynamics.

However, as of the current date, the genomic location of the sunflower ESTs used for microarray probe construction and the identified resistance genes from the previously mentioned thesis remains unknown.

**Objectives**

Since the sunflower genome was published in 2017 (4), this new source of information will be used to:

- Map within the sunflower genome all sequences used for microarray probe design and analyze their distribution.
- Map the location of genes identified as potential sources of resistance and analyze their distribution.

**Methods**

1. Sunflower genome acquisition → Build the index using the Burrows-Wheeler algorithm.
2. Align sequences against the indexed genome → Obtain the SAM file.
3. General mapping statistics.
4. Localization of Differentially Expressed Genes (DEGs).

**Bibliography**

1. Bert, P.F. et al., 2002. Comparative genetic analysis of quantitative traits in sunflower ( Helianthus annuus L.) 1. QTL involved in resistance to Sclerotinia sclerotiorum and Diaporthe helianthi. Tag Theoretical And Applied Genetics Theoretische Und Angewandte Genetik, 105(6–7), pp.985–993. Available at: http://www.ncbi.nlm.nih.gov/pubmed/12582925.
2. Fernandez, P. et al., 2012b. Development and validation of a high density sunflower microarray for functional studies on biotic and abiotic stresses. In Proceeding of the 18 International Sunflower Conference. Mar del Plata, Argentina.
3. Ehrenbolger, Guillermo Federico. "Identificación y caracterización funcional de genes candidatos para resistencia al patógeno Sclerotinia sclerotiorum en girasol mediante análisis transcriptómico". (2019). Tesis Doctoral, Universidad de Buenos Aires. Facultad de Ciencias Exactas y Naturales. 
(https://bibliotecadigital.exactas.uba.ar/download/tesis/tesis_n6711_Ehrenbolger.pdf)
4. Badouin, H., Gouzy, J., Grassa, C. et al. The sunflower genome provides insights into oil metabolism, flowering and Asterid evolution. Nature 546, 148–152 (2017). https://doi.org/10.1038/nature22380