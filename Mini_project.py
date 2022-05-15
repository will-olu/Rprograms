import wget
url = 'https://www.ncbi.nlm.nih.gov/sra/SRX2896360'
url2 = 'https://www.ncbi.nlm.nih.gov/sra/SRX2896363'
url3 = 'https://www.ncbi.nlm.nih.gov/sra/SRX2896374'
url4 = 'https://www.ncbi.nlm.nih.gov/sra/SRX2896375'
filename = wget.download(url)
filename2 = wget.download(url2)
filename3 = wget.download(url3)
filename4 = wget.download(url4)

