# Social Network Analysis - Facebook Data

Phan tich mang xa hoi Facebook voi du lieu thuc te tu Stanford SNAP.

---

## Tinh Trang: SAN SANG

- Dataset: Facebook Social Circles (4,039 nodes, 88,234 edges)
- Source: Stanford SNAP (du lieu thuc te)
- Notebooks: 3 notebooks da cap nhat
- Citation: File trich dan day du

---

## Bat Dau Nhanh

### 1. Cai dat thu vien
```bash
pip install -r requirements.txt
```

### 2. Chay phan tich
```bash
jupyter notebook
```

**Chay theo thu tu:**
1. `notebooks/01_network_overview.ipynb` - Tong quan mang
2. `notebooks/02_network_structure.ipynb` - Centrality analysis
3. `notebooks/03_community_detection.ipynb` - Community detection

### 3. Truc quan hoa voi Gephi
1. Tai Gephi: https://gephi.org/
2. Mo file: `data/social_network.gexf`
3. Ap dung layout: ForceAtlas 2
4. Export hinh anh

### 4. Viet bao cao
- Template: `reports/report_template.md`
- Trich dan: Xem `data/CITATION.txt`

---

## Dataset

**Facebook Social Circles** (Stanford SNAP)
- 4,039 nguoi dung
- 88,234 ket noi ban be
- Nguon: https://snap.stanford.edu/data/
- Citation: McAuley & Leskovec, NIPS 2012

**File quan trong:**
- `data/social_network.gexf` - File cho Gephi
- `data/CITATION.txt` - Trich dan cho bao cao

---

## Cau Truc

```
HW3_Social_media_DA/
 data/                    # Du lieu (4K nodes, 88K edges)
    social_network.gexf # File Gephi
    CITATION.txt        # Trich dan
 notebooks/              # 3 notebooks phan tich
    01_network_overview.ipynb
    02_network_structure.ipynb
    03_community_detection.ipynb
 outputs/                # Ket qua (auto-generated)
 scripts/                # Data collection script
 reports/                # Template bao cao
```

---

##  Trch Dn Cho Bo Co

** QUAN TRNG**: M file `data/CITATION.txt`

**Ghi trong bo co:**
```
Ngun d liu:
Dataset: Facebook Social Circles
Source: Stanford Network Analysis Project (SNAP)
Citation: J. McAuley and J. Leskovec. "Learning to Discover 
          Social Circles in Ego Networks." NIPS, 2012.
URL: https://snap.stanford.edu/data/
```

---

##  Kt Qu Phn Tch

Sau khi chy notebooks, bn s c:

### Phn 2: Network Overview
- Thng k m t (size, density, diameter)
- Degree distribution & Power Law
- Clustering coefficient
- Path length distribution

### Phn 3: Network Structure  
- 7 Centrality measures (Degree, Closeness, Betweenness, etc.)
- PageRank & HITS
- Correlation analysis
- Top influential nodes

### Phn 4: Community Detection
- K-core decomposition
- 4 algorithms (Louvain, Label Propagation, etc.)
- Modularity comparison
- Community statistics

**Output folder**: `outputs/` cha tt c charts v CSV files

---

##  Visualization

### Trong Notebooks
- Degree distribution plots
- Centrality comparison charts
- Community structure diagrams
- Correlation heatmaps

### Trong Gephi
1. Import `data/social_network.gexf`
2. Layout: ForceAtlas 2
3. Node size: Degree
4. Node color: Community
5. Export: PNG/SVG

---

##  FAQ

**Q: Dataset c tht khng?**  
 C! Mng Facebook thc t t nghin cu NIPS 2012.

**Q: Cn API key khng?**  
 KHNG! Dataset  ti sn.

**Q: Lm sao trch dn?**  
 Xem file `data/CITATION.txt`

**Q: Notebook bo li?**  
 Chy: `python scripts/data_collection.py`

---

##  Documentation

- `README.md` - File ny (overview)
- `QUICK_START_GUIDE.md` - Hng dn nhanh chi tit
- `PROJECT_STRUCTURE.md` - Cu trc project y 
- `PROJECT_STATUS.md` - Tnh trng v checklist

---

##  Checklist

### Setup 
- [x] Dataset ti xong
- [x] Notebooks cp nht
- [x] Citation file sn sng

### Phn tch 
- [ ] Chy notebook 01
- [ ] Chy notebook 02  
- [ ] Chy notebook 03
- [ ] Check outputs/

### Visualization 
- [ ] Gephi visualization
- [ ] Export hnh nh

### Bo co 
- [ ] c template
- [ ] Trch dn dataset
- [ ] Thm visualizations
- [ ] Hon thnh

---

##  H tr

**Li import libraries:**
```bash
pip install -r requirements.txt
```

**Li khng tm thy file:**
```bash
python scripts/data_collection.py
```

**Li Jupyter:**
```bash
pip install notebook jupyter
```

---

##  Files Quan Trng Nht

1. `data/CITATION.txt` -  **Trch dn cho bo co**
2. `data/social_network.gexf` - File Gephi
3. `notebooks/01_*.ipynb` - Phn tch phn 2
4. `notebooks/02_*.ipynb` - Phn tch phn 3
5. `notebooks/03_*.ipynb` - Phn tch phn 4

---

 **Project sn sng! Bt u vi: `jupyter notebook`** 

---

 **Ghi nh**: Lun trch dn dataset t `data/CITATION.txt` trong bo co!
