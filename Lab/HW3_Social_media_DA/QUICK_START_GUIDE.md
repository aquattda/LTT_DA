#  Hng dn nhanh - Social Network Analysis

##  Hon thnh:  c d liu thc t!

D n  c setup vi **dataset thc t** t Stanford SNAP.

###  Dataset hin ti

**Facebook Social Circles**
-  **4,039 nodes** (ngi dng)
-  **88,234 edges** (kt ni bn b)
-  **Ngun**: Stanford Network Analysis Project (SNAP)
-  **Trch dn**: J. McAuley v J. Leskovec. "Learning to Discover Social Circles in Ego Networks." NIPS, 2012.

###  Files  c sn

```
data/
 social_network.gexf           File cho Gephi
 nodes.csv                     4,039 ngi dng
 edges.csv                     88,234 kt ni
 dataset_info.json             Thng tin metadata
 CITATION.txt                  Trch dn cho bo co
```

---

##  Bc tip theo - Chy phn tch

### 1. M Jupyter Notebook

```bash
cd D:\LTT_DA\Lab\HW3_Social_media_DA
jupyter notebook
```

### 2. Chy cc notebooks theo th t

####  Notebook 1: Network Overview (Phn 2)
- File: `notebooks/01_network_overview.ipynb`
- Ni dung:
  -  Tng quan mng (kch thc, mt )
  -  Phn phi bc (degree distribution)
  -  Kim nh Power Law
  -  Clustering coefficient
  -  Path length distribution

####  Notebook 2: Network Structure (Phn 3)
- File: `notebooks/02_network_structure.ipynb`
- Ni dung:
  -  7  o centrality (Degree, Closeness, Betweenness, Eigenvector, PageRank, HITS)
  -  Ma trn tng quan
  -  Top influential nodes
  -  Phn tch node types

####  Notebook 3: Community Detection (Phn 4)
- File: `notebooks/03_community_detection.ipynb`
- Ni dung:
  -  K-core decomposition
  -  4 thut ton community detection
  -  So snh modularity
  -  Thng k cng ng

### 3. Trc quan ha vi Gephi

1. **Ti Gephi**: https://gephi.org/users/download/
2. **M file**: `data/social_network.gexf`
3. **p dng layout**: ForceAtlas 2
4. **Ty chnh**:
   - Node size  Degree
   - Node color  Community
5. **Export**: PNG/SVG cho bo co

---

##  Vit bo co

###  QUAN TRNG: Trch dn dataset

M file: `data/CITATION.txt`

**Trch dn trong bo co:**

```
Ngun d liu:
Dataset: Facebook Social Circles
Ngun: Stanford Network Analysis Project (SNAP)
URL: https://snap.stanford.edu/data/

Trch dn:
J. McAuley and J. Leskovec. "Learning to Discover Social Circles 
in Ego Networks." In Proceedings of Neural Information Processing 
Systems (NIPS), 2012.
```

###  Cu trc bo co

S dng template: `reports/report_template.md`

**Cc phn chnh:**

1. **Gii thiu**
   - Dataset: Facebook Social Circles (4,039 nodes, 88,234 edges)
   - Mc tiu: Phn tch cu trc v cng ng trong mng x hi

2. **Phn 2: Tng quan v mng**
   - Thng k m t (t notebook 01)
   - Phn phi bc v Power Law
   - Clustering v path length

3. **Phn 3: Cu trc mng**
   - Centrality measures (t notebook 02)
   - Top influential nodes
   - Tng quan gia cc  o

4. **Phn 4: Cng ng**
   - K-core analysis (t notebook 03)
   - So snh thut ton community detection
   - c im cc cng ng

5. **Phn 5: Kt lun**
   - Tng kt insights
   -  ngha thc tin
   - Hn ch v hng pht trin

---

##  Kt qu mong i

Sau khi chy xong, bn s c:

###  Visualizations
- Degree distribution plots
- Centrality comparison charts
- Community structure diagrams
- Correlation heatmaps
- Network layouts from Gephi

###  Statistical Results
- Network metrics (density, diameter, clustering)
- Power law regression (, R, p-value)
- Centrality rankings
- Community modularity scores

###  Output Files
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

##  FAQ

### Q: Ti c cn API key khng?
**A:**  KHNG! Dataset  c ti sn t Stanford SNAP.

### Q: D liu ny c tht khng?
**A:**  C! y l mng Facebook thc t c s dng trong nghin cu khoa hc.

### Q: Lm sao trch dn trong bo co?
**A:** Xem file `data/CITATION.txt`  c thng tin y .

### Q: Ti c th dng dataset khc khng?
**A:**  C! Chy li `python scripts/data_collection.py` v chn:
- `twitter` - 81K nodes (ln hn)
- `github` - 37K nodes (developers)
- `email` - 1K nodes (nh hn)

### Q: Notebook bo li khng tm thy file?
**A:** Kim tra:
1. File `data/social_network.gexf` c tn ti khng?
2. ang chy notebook t folder `notebooks/` khng?
3. Th chy li: `python scripts/data_collection.py`

---

##  H tr

### Li thng gp

**1. Import error - networkx/pandas**
```bash
pip install -r requirements.txt
```

**2. Jupyter khng m c**
```bash
pip install notebook
jupyter notebook
```

**3. Graph disconnected warning**
-  Bnh thng! Script t ng dng largest component

**4. Community detection li**
```bash
pip install python-louvain
```

---

##  Tm tt

 D liu  sn sng (Facebook Social Circles - 4K nodes, 88K edges)  
 Dataset thc t t Stanford SNAP  
 File citation y  cho bo co  
 3 notebooks phn tch hon chnh  
 Template bo co c sn

** Bc tip theo:**
1. Chy notebooks (01  02  03)
2. Trc quan ha vi Gephi
3. Vit bo co (nh trch dn!)

** Trch dn dataset:** Xem `data/CITATION.txt`

---

 **Chc bn hon thnh bi tp tt!**
