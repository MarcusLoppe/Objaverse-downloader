# Objaverse Annotations

This repo contains captions and property-specific annotations for 764K objects
from the Objaverse 1.0 [1] dataset. We include the following outputs generated
by PaLI-X [2] and aggregated using our Score-Based Multi-Probe Aggregation
(SBMPA) method:

1.  Captions: aggregated across 8 views per object.
2.  Type annotations: aggregated across 8 views and 4 questions per object.
3.  Material annotations: aggregated across 8 views per object.

The csv files contain the most likely response from each aggregated output
distribution. We also include the associated probability. The files use a
semicolon delimiter. Please see [our paper](https://arxiv.org/abs/2311.17851)
for more details.

## Citing this work

To cite this work, please use:

```
@article{kabra2023evaluating,
  title={Evaluating VLMs for Score-Based, Multi-Probe Annotation of 3D Objects},
  author={Kabra, Rishabh and Matthey, Loic and Lerchner, Alexander and Mitra, Niloy J},
  journal={arXiv preprint arXiv:2311.17851},
  year={2023}
}
```

## References

1.  Deitke, M., Schwenk, D., Salvador, J., Weihs, L., Michel, O., VanderBilt, E., Schmidt, L., Ehsani, K., Kembhavi, A., & Farhadi, A. (2023). Objaverse: A universe of annotated 3d objects. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 13142-13153).

2. Chen, X., Djolonga, J., Padlewski, P., Mustafa, B., Changpinyo, S., Wu, J., Ruiz, C. R., Goodman, S., Wang, X., Tay, Y., Shakeri, S., Dehghani, M., Salz, D., Lucic, M., Tschannen, M., Nagrani, A., Hu, H., Joshi, M., Pang, B., Montgomery, C., Pietrzyk, P., Ritter, M., Piergiovanni, A., Minderer, M., Pavetic, F., Waters, A., Li, G., Alabdulmohsin, I., Beyer, L., Amelot, J., Lee, K., Steiner, A. P., Li, Y., Keysers, D., Arnab, A., Xu, Y., Rong, K., Kolesnikov, A., Seyedhosseini, M., Angelova, A., Zhai, X., Houlsby, N., & Soricut, R. (2023). PaLI-X: On Scaling up a Multilingual Vision and Language Model. arXiv preprint arXiv:2305.18565.


## License and disclaimer

Copyright 2023 DeepMind Technologies Limited

All software is licensed under the Apache License, Version 2.0 (Apache 2.0);
you may not use this file except in compliance with the Apache 2.0 license.
You may obtain a copy of the Apache 2.0 license at:
https://www.apache.org/licenses/LICENSE-2.0

All other materials are licensed under the Creative Commons Attribution 4.0
International License (CC-BY). You may obtain a copy of the CC-BY license at:
https://creativecommons.org/licenses/by/4.0/legalcode

Unless required by applicable law or agreed to in writing, all software and
materials distributed here under the Apache 2.0 or CC-BY licenses are
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the licenses for the specific language governing
permissions and limitations under those licenses.

This is not an official Google product.
