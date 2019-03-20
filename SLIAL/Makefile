TEX:=$(shell ls *.tex)
OTHER = *~ *.aux *.dvi *.toc *.bbl *.blg *.gz *.out *.thm *.ps *.idx *.ilg *.ind

pdflatex: master.tex
	pdflatex --synctex=1 master.tex
	bibtex master.aux
	pdflatex --synctex=1 master.tex
	pdflatex --synctex=1 master.tex
	rm -f $(OTHER) $(PS)
clean:
	rm -f $(OTHER) $(PS)