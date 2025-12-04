#  Cu Trc Project - Social Network Analysis

```
HW3_Social_media_DA/

  data/                              # D liu thc t t Stanford SNAP
    social_network.gexf              #  File chnh cho Gephi (4K nodes, 88K edges)
    nodes.csv                        # Danh sch 4,039 ngi dng
    edges.csv                        # 88,234 kt ni bn b
    dataset_info.json                # Metadata v dataset
    CITATION.txt                     #  Trch dn cho bo co
    facebook_combined.txt.gz         # File gc t Stanford

  notebooks/                         # Jupyter notebooks phn tch
    01_network_overview.ipynb       #  Phn 2: Tng quan mng
    02_network_structure.ipynb      #  Phn 3: Centrality & Structure
    03_community_detection.ipynb    #  Phn 4: Community Detection

  outputs/                           # Kt qu phn tch (auto-generated)
    network_summary.txt              # Thng k tng quan
    degree_distribution.png          # Biu  phn phi bc
    power_law_fit.png                # Kim nh Power Law
    centrality_comparison.png        # So snh cc  o centrality
    correlation_heatmap.png          # Ma trn tng quan
    community_sizes.png              # Phn phi kch thc cng ng
    top_nodes.csv                    # Top influential nodes
    community_stats.csv              # Thng k cng ng

  scripts/                          # Scripts thu thp d liu
    data_collection.py               # Script ti dataset t Stanford SNAP

  reports/                          # Templates v bo co
    report_template.md               # Template vit bo co

  Documentation/
    README.md                        #  Hng dn chi tit
    QUICK_START_GUIDE.md            #  Hng dn nhanh
    PROJECT_STATUS.md                #  Tnh trng project
    PROJECT_STRUCTURE.md             #  File ny

  requirements.txt                  # Python dependencies

```

##  Chi tit Data Files

### data/social_network.gexf
- **Format**: GEXF (Graph Exchange XML Format)
- **Size**: ~2.5 MB
- **Purpose**: Import vo Gephi  visualization
- **Content**: Full network vi 4,039 nodes v 88,234 edges

### data/CITATION.txt 
- **Purpose**: Thng tin trch dn CHO BO CO
- **Content**: 
  - Tn dataset: Facebook Social Circles
  - Source: Stanford SNAP
  - Citation: McAuley & Leskovec, NIPS 2012
  - URL: https://snap.stanford.edu/data/

### data/nodes.csv
- **Columns**: `id`, `name`, `degree`
- **Rows**: 4,039 ngi dng
- **Purpose**: Thng tin tng node

### data/edges.csv
- **Columns**: `source`, `target`, `weight`
- **Rows**: 88,234 kt ni
- **Purpose**: Danh sch cc cnh

##  Chi tit Notebooks

### 01_network_overview.ipynb (Phn 2)
**Ni dung phn tch:**
-  Thng k m t (size, density, diameter, radius)
-  Phn phi bc (degree distribution)
-  Kim nh Power Law (, R, p-value)
-  Clustering coefficient (local & global)
-  Path length distribution
-  Small-world properties

**Output files:**
- `outputs/degree_distribution.png`
- `outputs/power_law_fit.png`
- `outputs/clustering_analysis.png`

### 02_network_structure.ipynb (Phn 3)
**Ni dung phn tch:**
-  7  o centrality:
  - Degree Centrality
  - Closeness Centrality
  - Betweenness Centrality
  - Eigenvector Centrality
  - PageRank
  - HITS (Hubs & Authorities)
-  Ma trn tng quan gia cc centrality
-  Top influential nodes
-  Hierarchical clustering

**Output files:**
- `outputs/centrality_comparison.png`
- `outputs/correlation_heatmap.png`
- `outputs/top_nodes.csv`

### 03_community_detection.ipynb (Phn 4)
**Ni dung phn tch:**
-  K-core decomposition
-  4 thut ton community detection:
  - Greedy Modularity
  - Label Propagation
  - Louvain (best)
  - Girvan-Newman
-  So snh modularity
-  Thng k cng ng
-  Visualization

**Output files:**
- `outputs/community_sizes.png`
- `outputs/community_comparison.png`
- `outputs/community_stats.csv`

##  Workflow

### Bc 1: Setup ( hon thnh )
```bash
pip install -r requirements.txt
python scripts/data_collection.py  # Dataset  c sn
```

### Bc 2: Phn tch
```bash
jupyter notebook
```
Chy theo th t:
1. `01_network_overview.ipynb`
2. `02_network_structure.ipynb`
3. `03_community_detection.ipynb`

### Bc 3: Visualization
1. M Gephi
2. Import `data/social_network.gexf`
3. p dng layout ForceAtlas 2
4. Export hnh nh

### Bc 4: Bo co
1. S dng template: `reports/report_template.md`
2. Trch dn dataset t: `data/CITATION.txt` 
3. Thm visualizations t `outputs/`
4. Thm screenshots t Gephi

##  Files Quan Trng

| File | Mc ch | Trng thi |
|------|----------|------------|
| `data/CITATION.txt` |  Trch dn cho bo co |  Sn sng |
| `data/social_network.gexf` | File cho Gephi |  Sn sng |
| `notebooks/*.ipynb` | Phn tch |   cp nht |
| `outputs/` | Kt qu |  Auto-generate |
| `reports/report_template.md` | Template bo co |  Sn sng |

##  Checklist

### Hon thnh 
- [x] Dataset thc t  ti (Facebook Social Circles)
- [x] 3 notebooks  cp nht
- [x] Citation file  c
- [x] Project structure gn gng
- [x] Documentation y 

### Cn lm 
- [ ] Chy notebook 01
- [ ] Chy notebook 02
- [ ] Chy notebook 03
- [ ] Trc quan ha Gephi
- [ ] Vit bo co

##  Lu 

1. **Dataset**: D liu THC T t Stanford SNAP, khng phi synthetic
2. **Citation**: PHI trch dn theo file `data/CITATION.txt`
3. **Notebooks**:  c cp nht  load d liu t ng
4. **Outputs**: Folder `outputs/` s cha tt c kt qu phn tch
5. **Gephi**: Dng file `social_network.gexf`  visualization

##  Support

Nu gp li:
1. Check file `data/social_network.gexf` c tn ti khng
2. Chy li: `python scripts/data_collection.py`
3. Ci t li: `pip install -r requirements.txt`

---

 **Project  sn sng  phn tch!**
