cap cd "C:\Users\Yin_d\Bordeaux-WIPO Dropbox\Shared\Chapter_2\Agbio\crops"
cap cd "C:\Users\Julio Raffo\Bordeaux-WIPO Dropbox\Shared\Chapter_2\Agbio\crops"

use "Patent_data\data\famid_idallclus.dta" 
gcollapse (count)clus_num=fam_id,by(cluster_type id_allclus_agbio)
merge 1:1 id_allclus_agbio using "clusters/idallclus_labels",keepusing(lat lng asciiname code3 )keep(match)nogen
compress 
ren id_allclus_agbio id_allclus
order id_allclus asciiname cluster_type
gegen clus_median=median(clus_num) if cluster_type ==62
replace clus_median =0 if cluster_type ==61
gen clus_abmedian=(clus_num >clus_median)
compress 
cd "../../Indicators/charts/chart 4.5/"
save "chart 4.5_agbio_cluster.dta",replace 



