import quality_metrics as qm

ref_path = "../example_images/original/Buildings.0001.png"
vgl_path = "../example_images/decompressed/Buildings.001_jpg.png"

print(qm.psnr(vgl_path, ref_path))
print(qm.mssim(vgl_path, ref_path))
print(qm.niqe(vgl_path))
