#  D N  HON THNH - READY TO USE!

##  Tnh trng: SN SNG PHN TCH

###  Dataset thc t  c ti xung

**Facebook Social Circles from Stanford SNAP**
-  **4,039 nodes** (ngi dng Facebook)
-  **88,234 edges** (kt ni bn b)
-  **Ngun**: Stanford Network Analysis Project (SNAP)
-  **Loi**: Mng thc t c s dng trong nghin cu khoa hc
-  **Paper**: J. McAuley & J. Leskovec, NIPS 2012

---

##  Files  c sn

###  Data Files (trong `data/`)
```
 social_network.gexf          - Network file cho Gephi
 nodes.csv                    - 4,039 ngi dng
 edges.csv                    - 88,234 kt ni
 dataset_info.json            - Metadata
 CITATION.txt                 -  Thng tin trch dn cho bo co
 facebook_combined.txt.gz     - File gc t Stanford
```

###  Notebooks (trong `notebooks/`)
```
 01_network_overview.ipynb       - Phn 2: Tng quan
 02_network_structure.ipynb      - Phn 3: Cu trc & Centrality
 03_community_detection.ipynb    - Phn 4: Pht hin cng ng
```

###  Scripts (trong `scripts/`)
```
 data_collection.py              - Thu thp dataset t Stanford SNAP
```

###  Documentation
```
 README.md                       - Hng dn y 
 QUICK_START_GUIDE.md            - Hng dn nhanh
 reports/report_template.md      - Template bo co
```

---

##  CC BC TIP THEO

### 1 Chy Notebooks Phn Tch

```bash
# M Jupyter
cd D:\LTT_DA\Lab\HW3_Social_media_DA
jupyter notebook
```

**Chy theo th t:**
1. `notebooks/01_network_overview.ipynb` - Tng quan mng
2. `notebooks/02_network_structure.ipynb` - Centrality analysis
3. `notebooks/03_community_detection.ipynb` - Community detection

 **Thi gian**: ~5-10 pht mi notebook

### 2 Trc Quan Ha vi Gephi

1. Ti Gephi: https://gephi.org/
2. M file: `data/social_network.gexf`
3. p dng layout: **ForceAtlas 2**
4. Ty chnh:
   - Node size  theo Degree
   - Node color  theo Community
5. Export hnh nh cho bo co

### 3 Vit Bo Co

**Template c sn**: `reports/report_template.md`

** QUAN TRNG - Trch dn Dataset:**

M file: `data/CITATION.txt`

**Ghi trong bo co:**
```
Ngun d liu:
D liu s dng trong nghin cu l mng x hi Facebook t 
Stanford Network Analysis Project (SNAP), bao gm 4,039 ngi dng 
v 88,234 kt ni bn b thc t.

Trch dn:
[1] J. McAuley and J. Leskovec. "Learning to Discover Social Circles 
    in Ego Networks." In Proceedings of Neural Information Processing 
    Systems (NIPS), 2012.
[2] Stanford Network Analysis Project (SNAP). 
    https://snap.stanford.edu/data/
```

---

##  KT QU PHN TCH

Sau khi chy notebooks, bn s c:

### Phn 2: Network Overview
-  Thng k m t (size, density, diameter)
-  Degree distribution plot
-  Power Law regression (, R, p-value)
-  Clustering coefficient
-  Path length distribution

### Phn 3: Network Structure
-  7 Centrality measures:
  - Degree Centrality
  - Closeness Centrality
  - Betweenness Centrality
  - Eigenvector Centrality
  - PageRank
  - HITS (Hubs & Authorities)
-  Correlation matrix
-  Top influential nodes
-  Centrality comparison plots

### Phn 4: Community Detection
-  K-core decomposition
-  4 thut ton:
  - Greedy Modularity
  - Label Propagation
  - Louvain (best)
  - Girvan-Newman
-  Modularity comparison
-  Community size distribution
-  Community statistics

### Output Files
```
outputs/
 network_summary.txt
 degree_distribution.png
 centrality_comparison.png
 community_sizes.png
 top_nodes.csv
 community_stats.csv
```

---

##  CU TRC BO CO

### Phn 1: Gii thiu
- Dataset: Facebook Social Circles (SNAP)
- Mc tiu: Phn tch cu trc v cng ng
- Phng php: Network analysis

### Phn 2: Tng quan v mng
- Thng k m t
- Phn phi bc
- Power Law analysis
- Clustering
- Small-world properties

### Phn 3: Phn tch cu trc
- Centrality measures
- Top influential nodes
- Correlation analysis
- Node importance ranking

### Phn 4: Pht hin cng ng
- K-core analysis
- Community detection algorithms
- Modularity comparison
- Community characteristics

### Phn 5: Kt lun
- Tng kt insights
- c im mng x hi Facebook
-  ngha thc tin
- Hn ch v hng pht trin

---

##  FAQ

### Q: Dataset ny c tht khng?
**A:**  **C!** y l mng Facebook thc t t Stanford SNAP, c s dng trong paper NIPS 2012.

### Q: Ti c cn API key khng?
**A:**  **KHNG CN!** Dataset  c ti sn t Stanford.

### Q: Lm sao trch dn trong bo co?
**A:** Xem file `data/CITATION.txt` - c y  thng tin citation.

### Q: C th dng dataset khc khng?
**A:**  **C!** Chy: `python scripts/data_collection.py`
- `facebook` - 4K nodes (recommended)
- `twitter` - 81K nodes
- `github` - 37K nodes
- `email` - 1K nodes

### Q: Notebooks chy c ngay khng?
**A:**  **C!** Ch cn: `jupyter notebook` v chy tng cell.

---

##  CHECKLIST HON THNH

nh du khi hon thnh:

### Phn tch
- [ ] Chy notebook 01 - Network Overview
- [ ] Chy notebook 02 - Network Structure
- [ ] Chy notebook 03 - Community Detection
- [ ] Kim tra output files trong `outputs/`

### Visualization
- [ ] M `social_network.gexf` trong Gephi
- [ ] p dng layout ForceAtlas 2
- [ ] Ty chnh node size & color
- [ ] Export hnh nh cht lng cao

### Bo co
- [ ] c template: `reports/report_template.md`
- [ ] Trch dn dataset t `data/CITATION.txt`
- [ ] Vit Phn 2: Network Overview
- [ ] Vit Phn 3: Network Structure
- [ ] Vit Phn 4: Community Detection
- [ ] Vit Phn 5: Kt lun
- [ ] Thm visualizations v charts
- [ ] Kim tra li citation

---

##  TI LIU THAM KHO

### Dataset
- **Stanford SNAP**: https://snap.stanford.edu/data/
- **Original Paper**: McAuley & Leskovec, NIPS 2012

### Algorithms
- **NetworkX Docs**: https://networkx.org/documentation/stable/
- **Community Detection**: Newman (2006), Blondel et al. (2008)
- **Centrality**: Freeman (1978), Page et al. (1999)

### Tools
- **Gephi**: https://gephi.org/
- **Jupyter**: https://jupyter.org/
- **Python**: https://www.python.org/

---

##  TM TT

 **Dataset**: Facebook Social Circles (4K nodes, 88K edges) - THC T  
 **Ngun**: Stanford SNAP - UY TN  
 **Notebooks**: 3 notebooks phn tch hon chnh - SN SNG  
 **Citation**: File CITATION.txt y  - READY  
 **Template**: Bo co c sn - EASY  

** Bc tip theo:**
1. Chy 3 notebooks
2. Trc quan ha vi Gephi
3. Vit bo co (nh trch dn!)

** File quan trng nht:** `data/CITATION.txt`

---

 **Chc bn hon thnh xut sc!** 
