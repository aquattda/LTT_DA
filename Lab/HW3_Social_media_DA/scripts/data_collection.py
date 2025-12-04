"""
Data Collection Script for Social Network Analysis
Using Public Real-World Social Network Datasets

This script downloads and processes real social network datasets from public repositories.
These are actual social network data used in research papers.

Datasets available:
1. Facebook Social Circles (Stanford SNAP)
2. Twitter Social Network (Stanford SNAP)
3. GitHub Social Network (Stanford SNAP)
4. EU Email Communication Network
5. Wikipedia Voting Network

Author: [Your Name]
Date: November 2025
"""

import networkx as nx
import pandas as pd
import numpy as np
import json
from datetime import datetime
import time 
import urllib.request
import os
import gzip

# ============================================================================
# REAL-WORLD SOCIAL NETWORK DATASETS
# ============================================================================

DATASETS = {
    'facebook': {
        'name': 'Facebook Social Circles',
        'url': 'https://snap.stanford.edu/data/facebook_combined.txt.gz',
        'description': 'Facebook social circles from survey participants (Stanford SNAP)',
        'citation': 'J. McAuley and J. Leskovec. Learning to Discover Social Circles in Ego Networks. NIPS, 2012.',
        'nodes': 4039,
        'edges': 88234,
        'type': 'undirected'
    },
    'twitter': {
        'name': 'Twitter Social Network',
        'url': 'https://snap.stanford.edu/data/ego-Twitter.txt.gz',
        'description': 'Twitter ego network (Stanford SNAP)',
        'citation': 'J. McAuley and J. Leskovec. Learning to Discover Social Circles in Ego Networks. NIPS, 2012.',
        'nodes': 81306,
        'edges': 1768149,
        'type': 'directed'
    },
    'github': {
        'name': 'GitHub Developers Network',
        'url': 'https://snap.stanford.edu/data/github-social.txt.gz',
        'description': 'GitHub developers following network (Stanford SNAP)',
        'citation': 'Stanford Network Analysis Project (SNAP)',
        'nodes': 37700,
        'edges': 289003,
        'type': 'directed'
    },
    'email': {
        'name': 'EU Email Communication Network',
        'url': 'https://snap.stanford.edu/data/email-Eu-core.txt.gz',
        'description': 'Email communication network at a European research institution',
        'citation': 'H. Yin et al. Local Higher-order Graph Clustering. KDD, 2017.',
        'nodes': 1005,
        'edges': 25571,
        'type': 'directed'
    }
}


def download_real_dataset(dataset_name='facebook', output_dir='../data'):
    """
    Download real-world social network dataset
    
    Parameters:
    -----------
    dataset_name : str
        Dataset name: 'facebook', 'twitter', 'github', 'email'
    output_dir : str
        Output directory
    
    Returns:
    --------
    G : NetworkX Graph
        Social network graph
    metadata : dict
        Dataset metadata
    """
    if dataset_name not in DATASETS:
        raise ValueError(f"Unknown dataset. Choose from: {list(DATASETS.keys())}")
    
    dataset_info = DATASETS[dataset_name]
    os.makedirs(output_dir, exist_ok=True)
    
    print("="*70)
    print(f"DOWNLOADING: {dataset_info['name']}")
    print("="*70)
    print(f"Description: {dataset_info['description']}")
    print(f"Source: Stanford SNAP (https://snap.stanford.edu)")
    print(f"Approximate size: {dataset_info['nodes']:,} nodes, {dataset_info['edges']:,} edges")
    print(f"Type: {dataset_info['type']}")
    print(f"\nCitation for report:")
    print(f"  {dataset_info['citation']}")
    print("="*70)
    
    # Download file
    url = dataset_info['url']
    filename = url.split('/')[-1]
    filepath = os.path.join(output_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"\nDownloading from {url}...")
        try:
            urllib.request.urlretrieve(url, filepath)
            print(f"✓ Downloaded to {filepath}")
        except Exception as e:
            print(f"✗ Download failed: {e}")
            print("\nAlternative: Download manually from:")
            print(f"  {url}")
            print(f"  Save to: {filepath}")
            return None, None
    else:
        print(f"\n✓ File already exists: {filepath}")
    
    # Read and process data
    print("\nProcessing network data...")
    
    try:
        # Read gzipped file
        edges = []
        with gzip.open(filepath, 'rt') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split()
                    if len(parts) >= 2:
                        edges.append((int(parts[0]), int(parts[1])))
        
        # Create graph
        if dataset_info['type'] == 'directed':
            G = nx.DiGraph()
        else:
            G = nx.Graph()
        
        G.add_edges_from(edges)
        
        # Add node attributes
        print("\nAdding node attributes...")
        for node in G.nodes():
            G.nodes[node]['id'] = node
            G.nodes[node]['name'] = f'User_{node}'
            G.nodes[node]['degree'] = G.degree(node)
        
        # Add edge weights
        for u, v in G.edges():
            G.edges[u, v]['weight'] = 1
        
        print(f"\n✓ Network loaded successfully!")
        print(f"  Actual nodes: {G.number_of_nodes():,}")
        print(f"  Actual edges: {G.number_of_edges():,}")
        
        # Metadata
        metadata = {
            'dataset_name': dataset_info['name'],
            'description': dataset_info['description'],
            'citation': dataset_info['citation'],
            'source': 'Stanford Network Analysis Project (SNAP)',
            'url': 'https://snap.stanford.edu/data/',
            'type': dataset_info['type'],
            'nodes': G.number_of_nodes(),
            'edges': G.number_of_edges(),
            'download_date': datetime.now().isoformat()
        }
        
        return G, metadata
        
    except Exception as e:
        print(f"✗ Error processing file: {e}")
        return None, None


# ============================================================================
# DATASET SELECTION HELPER
# ============================================================================

def show_available_datasets():
    """Display available datasets"""
    print("\n" + "="*70)
    print("AVAILABLE REAL-WORLD DATASETS")
    print("="*70)
    
    for i, (key, info) in enumerate(DATASETS.items(), 1):
        print(f"\n{i}. {info['name']} ('{key}')")
        print(f"   {info['description']}")
        print(f"   Size: ~{info['nodes']:,} nodes, ~{info['edges']:,} edges")
        print(f"   Type: {info['type']}")
    
    print("\n" + "="*70)
    print("\nAll datasets from Stanford SNAP: https://snap.stanford.edu/data/")
    print("="*70)


# ============================================================================
# SAVE NETWORK DATA
# ============================================================================

def save_network(G, metadata, output_dir='../data'):
    """
    Save network and metadata in multiple formats
    
    Parameters:
    -----------
    G : NetworkX Graph
        Network to save
    metadata : dict
        Dataset metadata for citation
    output_dir : str
        Output directory
    """
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"\nSaving network to {output_dir}/...")
    
    # 1. GEXF (for Gephi)
    gexf_file = f"{output_dir}/social_network.gexf"
    nx.write_gexf(G, gexf_file)
    print(f"✓ Saved GEXF: {gexf_file}")
    
    # 2. CSV files (nodes and edges)
    nodes_data = []
    for node in G.nodes():
        node_dict = {'id': node}
        node_dict.update(G.nodes[node])
        nodes_data.append(node_dict)
    
    nodes_df = pd.DataFrame(nodes_data)
    nodes_file = f"{output_dir}/nodes.csv"
    nodes_df.to_csv(nodes_file, index=False, encoding='utf-8-sig')
    print(f"✓ Saved nodes: {nodes_file}")
    
    edges_data = []
    for u, v in G.edges():
        edge_dict = {'source': u, 'target': v}
        edge_dict.update(G.edges[u, v])
        edges_data.append(edge_dict)
    
    edges_df = pd.DataFrame(edges_data)
    edges_file = f"{output_dir}/edges.csv"
    edges_df.to_csv(edges_file, index=False, encoding='utf-8-sig')
    print(f"✓ Saved edges: {edges_file}")
    
    # 3. Metadata JSON (for report citation)
    metadata_file = f"{output_dir}/dataset_info.json"
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    print(f"✓ Saved metadata: {metadata_file}")
    
    # 4. Citation text file
    citation_file = f"{output_dir}/CITATION.txt"
    with open(citation_file, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write("DATASET INFORMATION FOR REPORT\n")
        f.write("="*70 + "\n\n")
        f.write(f"Dataset: {metadata['dataset_name']}\n")
        f.write(f"Description: {metadata['description']}\n")
        f.write(f"Source: {metadata['source']}\n")
        f.write(f"URL: {metadata['url']}\n")
        f.write(f"Type: {metadata['type']}\n")
        f.write(f"Nodes: {metadata['nodes']:,}\n")
        f.write(f"Edges: {metadata['edges']:,}\n")
        f.write(f"Downloaded: {metadata['download_date']}\n\n")
        f.write("="*70 + "\n")
        f.write("CITATION (for report)\n")
        f.write("="*70 + "\n\n")
        f.write(f"{metadata['citation']}\n\n")
        f.write("Stanford Network Analysis Project (SNAP)\n")
        f.write("https://snap.stanford.edu/data/\n")
    print(f"✓ Saved citation: {citation_file}")
    
    print(f"\n✓ All files saved successfully!")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function"""
    
    print("="*70)
    print("REAL-WORLD SOCIAL NETWORK DATA COLLECTION")
    print("="*70)
    print("\nThis script downloads real social network datasets from Stanford SNAP")
    print("These are actual networks used in published research papers.")
    
    # Show available datasets
    show_available_datasets()
    
    # Ask user to choose
    print("\nWhich dataset do you want to use?")
    print("Enter: facebook, twitter, github, or email")
    print("(Recommendation: 'facebook' for balanced size and analysis)")
    
    choice = input("\nYour choice: ").strip().lower()
    
    if choice not in DATASETS:
        print(f"\n✗ Invalid choice. Please choose from: {list(DATASETS.keys())}")
        print("Defaulting to 'facebook' dataset...")
        choice = 'facebook'
    
    # Download and process dataset
    G, metadata = download_real_dataset(choice, output_dir='../data')
    
    if G is not None and metadata is not None:
        # Save network
        save_network(G, metadata, output_dir='../data')
        
        # Print summary
        print("\n" + "="*70)
        print("NETWORK SUMMARY")
        print("="*70)
        print(f"Dataset: {metadata['dataset_name']}")
        print(f"Nodes: {G.number_of_nodes():,}")
        print(f"Edges: {G.number_of_edges():,}")
        print(f"Density: {nx.density(G):.4f}")
        print(f"Type: {'Directed' if G.is_directed() else 'Undirected'}")
        
        if not G.is_directed():
            print(f"Connected: {nx.is_connected(G)}")
            if not nx.is_connected(G):
                largest_cc = max(nx.connected_components(G), key=len)
                print(f"Largest component: {len(largest_cc)} nodes ({len(largest_cc)/G.number_of_nodes()*100:.1f}%)")
        
        print("\n" + "="*70)
        print("CITATION INFO (use in your report)")
        print("="*70)
        print(f"\nDataset: {metadata['dataset_name']}")
        print(f"Source: {metadata['source']}")
        print(f"Citation: {metadata['citation']}")
        print(f"URL: {metadata['url']}")
        print("\nSee data/CITATION.txt for full citation information")
        print("="*70)
        
        print("\n✓ Data collection completed!")
        print("\nNext steps:")
        print("1. Check data/CITATION.txt for report citation")
        print("2. Run the analysis notebooks:")
        print("   - notebooks/01_network_overview.ipynb")
        print("   - notebooks/02_network_structure.ipynb")
        print("   - notebooks/03_community_detection.ipynb")
    else:
        print("\n✗ Failed to download/process dataset")
        print("\nTroubleshooting:")
        print("1. Check your internet connection")
        print("2. Try downloading manually from: https://snap.stanford.edu/data/")
        print("3. Place the file in ../data/ folder")


if __name__ == "__main__":
    main()
