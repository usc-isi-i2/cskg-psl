#!/bin/bash

python create_sameas.py

kgtk lift --columns-to-lift node1 node2 --lift-suffix=      --input-file cskg.tsv      --label-file output/sameas.tsv      --label-select-value connected_component  > output/cskg_merged.tsv

python create_path_pairs.py

kgtk paths --max_hops 2 --statistics-only -i output/cskg_merged.tsv --path_file pairs.tsv --directed > paths.tsv
