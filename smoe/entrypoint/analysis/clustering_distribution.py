"""
python -m smoe.entrypoint.analysis.clustering_distribution -d resources/clustering_samples
"""

import argparse
from pathlib import Path

from smoe.utils.io import load_jsonlines
from smoe.utils.visualization.barh import barh


def main(args):
    data_dir = Path(args.data_dir)

    for file in data_dir.glob("*.jsonl"):
        cluster_idx = file.stem
        source_to_num = {
            "arxiv": 0,
            "books": 0,
            "c4": 0,
            "commoncrawl": 0,
            "github": 0,
            "stackexchange": 0,
            "wikipedia": 0,
        }
        data = load_jsonlines(file)
        for ins in data:
            source = ins["file"].split("-")[0]
            source_to_num[source] += 1
        barh(
            source_to_num,
            title=f"Cluster {cluster_idx}",
            save_filepath=f"results/analysis/cluster_{cluster_idx}.png",
        )
        print(f"Done: {file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data_dir", required=True)
    args = parser.parse_args()
    main(args)
