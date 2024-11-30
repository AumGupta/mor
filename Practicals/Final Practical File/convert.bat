cd "Practicals/Final Practical File"
jupyter nbconvert --to pdf main.ipynb
pdftk "main.pdf" cat 2-end output "24236761066(Om Gupta).pdf"
del main.pdf