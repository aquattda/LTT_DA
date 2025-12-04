# BO CO PHN TCH MNG X HI

**Sinh vin**: [H v tn]  
**MSSV**: [M s sinh vin]  
**Lp**: [Tn lp]  
**Ngy**: [Ngy np bo co]

---

## PHN 1: TNG QUAN  TI

### 1.1. Gii Thiu

[M t ngn gn v  ti, mc ch nghin cu]

**Loi mng c chn**: 
- [ ] Mng ca bn thn xy dng (bn b)
- [ ] Mng cng ng cng khai
- [ ] Mng truyn thng (tin nhn, comment)
- [ ] Mng ng hin din (hashtag co-occurrence)

**Kch thc mng**: [S nt] nt, [S cnh] cnh

### 1.2. Mc Tiu Nghin Cu

1. Phn tch cu trc tng quan ca mng x hi
2. Xc nh cc nt trung tm v nh hng trong mng
3. Pht hin v phn tch cc cng ng
4. nh gi cht lng phn vng cng ng

### 1.3.  Ngha Thc Tin

[Gii thch  ngha ca vic phn tch mng ny, ng dng trong thc t]

---

## PHN 2: PHN TCH TNG QUAN MNG

### 2.1. Ngun D Liu

**Ngun**: [M t ngun d liu: Facebook, Twitter, Instagram, v.v.]

**Phng php thu thp**: 
- [M t cch thu thp: API, web scraping, database cng khai, v.v.]
- Thi gian thu thp: [Thi gian]
- Cng c s dng: [Python, Beautiful Soup, Tweepy, v.v.]

**Cc bc tin x l**:
1. [Bc 1: Lm sch d liu]
2. [Bc 2: Loi b duplicate]
3. [Bc 3: X l missing values]
4. [Bc 4: Chun ha d liu]

### 2.2. Kiu  Th

**Loi  th**: 
- C hng / V hng: [Chn v gii thch]
- ng nht / Khng ng nht: [Chn v gii thch]
- C trng s / Khng trng s: [Chn v gii thch]

**Gii thch la chn**: [Gii thch ti sao chn kiu  th ny]

### 2.3. Thuc Tnh Nt v Cnh

**Thuc tnh nt**:
- [Thuc tnh 1]: [M t, v d: user_id, name, type]
- [Thuc tnh 2]: [M t, v d: followers_count]
- [Thuc tnh 3]: [M t]

**Thuc tnh cnh**:
- [Thuc tnh 1]: [M t, v d: weight (s lng interaction)]
- [Thuc tnh 2]: [M t, v d: interaction_type]

### 2.4. Thng K C Bn

| Ch s | Gi tr |
|--------|---------|
| S nt (Nodes) | [X] |
| S cnh (Edges) | [Y] |
| Mt  (Density) | [Z] |
| Lin thng | [C/Khng] |
| S thnh phn lin thng | [N] |

### 2.5. ng Knh v Bn Knh

- **ng knh (Diameter)**: [Gi tr]
  - *Gii thch*: Khong cch xa nht gia hai nt bt k l [X] bc.
  
- **Bn knh (Radius)**: [Gi tr]
  - *Gii thch*: Tn ti nt trung tm c khong cch xa nht n nt khc l [X] bc.

**Nhn xt**: [Phn tch  ngha ca ng knh v bn knh i vi mng]

### 2.6. H S Phn Cm (Clustering Coefficient)

| Loi | Gi tr |
|------|---------|
| H s phn cm ton cc (Global) | [X] |
| H s phn cm trung bnh cc b (Average Local) | [Y] |
| Gi tr nh nht | [Min] |
| Gi tr ln nht | [Max] |
|  lch chun | [Std] |

**Histogram**: [Chn hnh nh histogram phn phi h s phn cm]

**Nhn xt**: 
- H s phn cm [cao/thp] cho thy mng c xu hng [hnh thnh cc nhm cht ch / phn tn].
- [Thm phn tch su]

### 2.7.  Di ng i Trung Bnh

- ** di ng i trung bnh**: [Gi tr]
- ** di ngn nht**: [Min]
- ** di di nht**: [Max]

**Histogram**: [Chn hnh nh histogram phn phi  di ng i]

**Nhn xt**:
- Trung bnh cn [X] bc  i t mt nt n nt khc.
- y l c trng ca mng ["th gii nh" / "mng ngu nhin"].

### 2.8. Phn Phi Bc

**Thng k**:
- Bc trung bnh: [X]
- Bc trung v: [Y]
- Bc nh nht: [Min]
- Bc ln nht: [Max]
-  lch chun: [Std]

**Top 10 nt c bc cao nht**:
1. [Node 1]: [Degree]
2. [Node 2]: [Degree]
3. ...

**Biu **: [Chn cc biu ]
- Linear scale histogram
- Log-log plot
- CCDF (Complementary Cumulative Distribution Function)

### 2.9. M Hnh Ha Phn Phi Bc

**Power Law Regression**:
- H s  (gamma): [Gi tr]
- R (Coefficient of determination): [Gi tr]
- P-value: [Gi tr]

**Kt lun**: 
- Phn phi bc [c/khng] tun theo lut ly tha (Power Law).
- Mng thuc loi [scale-free network / random network / small-world network].
- [Gii thch  ngha]

### 2.10. B Cc Mng (Gephi)

**Visualization**: [Chn hnh nh t Gephi]

**M t**:
- Layout s dng: [ForceAtlas 2 / Fruchterman Reingold / ...]
- Kch thc nt: [Theo degree / betweenness / ...]
- Mu sc nt: [Theo type / community / ...]
-  dy cnh: [Theo weight / ...]

**Nhn xt cu trc**: [M t cu trc quan st c t visualization]

---

## PHN 3: PHN TCH CU TRC MNG

### 3.1. Cc  o Trung Tm

#### 3.1.1. Degree Centrality

**Top 10 nt**:
1. [Node]: [Score] - [Gii thch vai tr]
2. ...

**Phn phi**: [Chn histogram]

**Nhn xt**: [Nhng nt c degree centrality cao ng vai tr g trong mng]

#### 3.1.2. Closeness Centrality

**Top 10 nt**:
1. [Node]: [Score]
2. ...

**Nhn xt**: [Nhng nt ny c kh nng lan truyn thng tin nhanh chng]

#### 3.1.3. Betweenness Centrality

**Top 10 nt**:
1. [Node]: [Score]
2. ...

**Nhn xt**: [Nhng nt ny ng vai tr cu ni quan trng]

#### 3.1.4. Eigenvector Centrality

**Top 10 nt**:
1. [Node]: [Score]
2. ...

**Nhn xt**: [Nhng nt ny c nh hng cao do kt ni vi cc nt quan trng]

### 3.2. PageRank v HITS (Mng C Hng)

#### 3.2.1. PageRank

**Top 10 nt**:
1. [Node]: [PageRank Score]
2. ...

**Nhn xt**: [Phn tch tm quan trng ca cc nt theo PageRank]

#### 3.2.2. HITS - Hub Scores

**Top 10 Hub**:
1. [Node]: [Hub Score]
2. ...

#### 3.2.3. HITS - Authority Scores

**Top 10 Authority**:
1. [Node]: [Authority Score]
2. ...

**Nhn xt**: [So snh hub v authority,  ngha trong mng]

### 3.3. Ma Trn Tng Quan

**Heatmap**: [Chn ma trn tng quan]

**Cc cp c tng quan cao**:
- [Measure 1]  [Measure 2]: [Correlation]
- [Measure 3]  [Measure 4]: [Correlation]

**Phn tch**:
- [Gii thch tng quan cao/thp gia cc  o]
- [Nhng  o no b sung thng tin cho nhau]

### 3.4. Sp Xp Theo Thuc Tnh

**Phn tch theo loi nt**: [Chn bng/biu  thng k centrality theo type]

**Top 20 nt quan trng nht (composite score)**:
1. [Node]: [Score]
2. ...

### 3.5. Phn Tch Tng ng Cu Trc

**Dendrogram**: [Chn dendrogram hierarchical clustering]

**Nhn xt**: 
- [Cc nhm nt c cu trc lng ging tng t]
- [Vai tr cu trc tng ng trong mng]

---

## PHN 4: PHN TCH CNG NG TRONG MNG

### 4.1. Phn Tch K-Core

**K-core cao nht**: [K]

**Phn phi k-core**:
| K-core | S nt | T l (%) |
|--------|--------|-----------|
| 1 | [X] | [Y%] |
| 2 | [X] | [Y%] |
| ... | ... | ... |
| [Max K] | [X] | [Y%] |

**Biu **: [Chn histogram phn phi k-core]

**Inner Core ([Max K]-core)**:
- S nt: [X]
- S cnh: [Y]
- Mt : [Z]
- H s phn cm TB: [W]

**Top 10 nt trong inner core**:
1. [Node]: Degree = [X]
2. ...

**Nhn xt**: [Vai tr ca inner core trong mng]

### 4.2. So Snh Cc Thut Ton Pht Hin Cng ng

#### Bng So Snh

| Thut ton | S cng ng | Modularity | Size TB | Coverage |
|------------|--------------|------------|---------|----------|
| Greedy Modularity | [X] | [Y] | [Z] | [W] |
| Label Propagation | [X] | [Y] | [Z] | [W] |
| Louvain | [X] | [Y] | [Z] | [W] |
| Girvan-Newman | [X] | [Y] | [Z] | [W] |

**Biu  so snh**: [Chn bar charts so snh cc metrics]

#### Phn Tch Tng Thut Ton

**1. Greedy Modularity Optimization**:
- u im: [...]
- Nhc im: [...]
- Ph hp vi: [...]

**2. Label Propagation**:
- u im: [...]
- Nhc im: [...]
- Ph hp vi: [...]

**3. Louvain Algorithm**:
- u im: [...]
- Nhc im: [...]
- Ph hp vi: [...]

**4. Girvan-Newman**:
- u im: [...]
- Nhc im: [...]
- Ph hp vi: [...]

### 4.3. nh Gi Cht Lng - Modularity

**Thut ton tt nht**: [Tn thut ton]
- Modularity: [Gi tr]
- Coverage: [Gi tr]

**Gii thch Modularity**:
- [Gi tr] [> 0.3 / > 0.5 / > 0.7] cho thy cu trc cng ng [yu/r rng/rt mnh]
- [Phn tch  ngha]

### 4.4. Phn Tch Chi Tit Cng ng

**Thng k**:
- Tng s cng ng: [X]
- Kch thc nh nht: [Y] nt
- Kch thc ln nht: [Z] nt
- Kch thc trung bnh: [W] nt
- Kch thc trung v: [V] nt

**Top 10 cng ng ln nht**:

| Cng ng | Kch thc | Mt  | Avg Clustering |
|-----------|------------|--------|----------------|
| 1 | [X] | [Y] | [Z] |
| 2 | [X] | [Y] | [Z] |
| ... | ... | ... | ... |

**Biu **: [Chn pie chart phn b nt trong cc cng ng]

### 4.5. Kt Ni Gia Cc Cng ng

**Thng k cnh**:
- Cnh ni b (intra-community): [X] ([Y%])
- Cnh lin cng ng (inter-community): [Z] ([W%])

**Ma trn kt ni**: [Chn heatmap ma trn kt ni gia top communities]

**Nhn xt**: 
- [Phn tch mc  tch bit gia cc cng ng]
- [Cc cng ng no c kt ni cht vi nhau]

### 4.6. Visualization Cng ng

**Hnh nh**: [Chn visualization mng vi mu cng ng]

**Top 6 cng ng**: [Chn hnh nh tng cng ng ring bit]

**M t**:
- [c im cu trc ca mi cng ng ln]
- [Cc nt trung tm trong mi cng ng]

---

## PHN 5: KT LUN

### 5.1. Tng Kt Cc Pht Hin Chnh

**1. Cu trc tng quan**:
- Mng c [X] nt v [Y] cnh
- c trng: [Scale-free / Small-world / Random network]
- H s phn cm [cao/thp] cho thy [...]
-  di ng i trung bnh [ngn/di] phn nh [...]

**2. Cc nt trung tm**:
- Cc nt quan trng nht theo cc tiu ch khc nhau
- [Node X] c vai tr [...]
- [Node Y] ng vai tr cu ni quan trng

**3. Cu trc cng ng**:
- Pht hin [X] cng ng vi modularity = [Y]
- Cc cng ng c kch thc v c im khc nhau
- [M t c trng cc cng ng chnh]

### 5.2.  Ngha v ng Dng

**Trong mng x hi ny**:
- [Gii thch  ngha ca cc pht hin]
- [ng dng thc t: marketing, influence spreading, v.v.]

** xut**:
- [ xut chin lc da trn phn tch]
- [Cch tn dng cc nt trung tm v cng ng]

### 5.3. Hn Ch v Hng Pht Trin

**Hn ch**:
- [Hn ch v d liu]
- [Hn ch v phng php]
- [Hn ch v thi gian/ti nguyn]

**Hng pht trin**:
- M rng kch thc mng
- Thu thp d liu theo thi gian (temporal network)
- p dng cc thut ton nng cao khc
- Phn tch su hn v c trng tng cng ng

---

## PH LC

### A. Code v Scripts

[Link n repository hoc nh km code]

### B. D Liu

[M t chi tit v dataset, link ti (nu c)]

### C. Cc Biu  v Hnh nh B Sung

[Cc hnh nh khng c a vo phn chnh]

---

## TI LIU THAM KHO

1. Newman, M. E. J. (2010). *Networks: An Introduction*. Oxford University Press.
2. Barabsi, A.-L. (2016). *Network Science*. Cambridge University Press.
3. Fortunato, S. (2010). Community detection in graphs. *Physics Reports*, 486(3-5), 75-174.
4. [Thm cc ti liu tham kho khc]

---

**Ngy hon thnh**: [Ngy/Thng/Nm]  
**Ch k sinh vin**: _____________________
