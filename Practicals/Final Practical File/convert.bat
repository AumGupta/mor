cd "Practicals/Final Practical File"
jupyter nbconvert --to pdf main.ipynb
pdftk "main.pdf" cat 2-end output "21SGGCBSCS000037(Om Gupta).pdf"
del main.pdf