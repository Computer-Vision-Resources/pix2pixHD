### Using labels only
# python test.py --name pose2human_640p_g4_HW --dataroot /home/cristobal/p2p-haotian/table-tennis-data/JZ --label_nc 0 --no_instance --loadSize 640 --batchSize 1 --how_many 1

python convert.py --name pose2human_640p_g4_HW --loadSize 640 --label_nc 0 --no_instance
