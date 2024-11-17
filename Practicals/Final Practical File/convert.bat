cd "Practicals/Final Practical File"
jupyter nbconvert --to pdf main.ipynb
pdftk "main.pdf" cat 2-end output "Final Practical File - Om Gupta.pdf"
del main.pdf