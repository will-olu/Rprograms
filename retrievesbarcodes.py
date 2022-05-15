import os


def combiningBarcodes():
    current_path = os.getcwd()
    folder = "/mouse_heart_GEO_data"
    barcodesRPF=open(current_path + folder + '/GSM3885061_RPFbarcodes.tsv.gz','r').readlines()
    barcodesLPF=open(curent_path + folder + '/GSM3885060_LPFbarcodes.tsv.gz','r').readlines()
    barcodesAVN=open(curent_path + folder + '/GSM3885059_AVNbarcodes.tsv.gz','r').readlines()
    barcodesSAN=open(curent_path + folder + '/GSM3885058_SANbarcodes.tsv.gz','r').readlines()
    filenames = [bacodesRPF, barcodesLPF, barcodesAVN, barcodesSAN]
    with open("barcodes.tsv.gz", "w") as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)


def combiningMatrices():
    current_path = os.getcwd()
    folder = "/mouse_heart_GEO_data"
    matrixRPF=open(current_path + folder +  "GSM3885061_RPFmatrix.mtx.gz", 'r').readlines()   
    matrixAVN=open(current_path + folder +  "GSM3885059_AVNmatrix.mtx.gz", 'r').readlines()
    matrixSAN=open(current_path + folder +  "GSM3885058_SANmatrix.mtx.gz", 'r').readlines()
    matrixLPF=open(current_path + folder +  "GSM3885060_LPFmatrix.mtx.gz", 'r').readlines()
    filenames = [matrixRPF, matrixAVN, matrixSAN, matrixLPF]
    with open("matrices.mtx.gz", "w") as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line infile:
                    outfile.write(line)
    
def combiningGenes():
    current_path = os.getcwd()
    folder = "/mouse_heart_GEO_data"
    genesRPF=open(current_path + folder +  "GSM3885061_RPFgenes.gz", 'r').readlines()   
    genesAVN=open(current_path + folder +  "GSM3885059_AVNgenes.gz", 'r').readlines()
    genesSAN=open(current_path + folder +  "GSM3885058_SANgenes.gz", 'r').readlines()
    genesLPF=open(current_path + folder +  "GSM3885060_LPFgenes.gz", 'r').readlines()
    filenames = [genesRPF, genesAVN, matrixSAN, matrixLPF]
    with open("genes.gz", "w") as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line infile:
                    outfile.write(line)




#GSM3885061_RPF      
#GSM3885059_AVN
#GSM3885058_SAN
#GSM3885060_LPF
