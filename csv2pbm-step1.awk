BEGIN { print "P1"; FS="," }
{ max_nf = max_nf < NF ? NF : max_nf }
END { printf("%d %d\n", max_nf, NR) }

