# Minecraft stack size calculator

Symlink ./main.py into your $PATH

eg: `$ sudo ln -s /path/to/repo/main.py /usr/local/bin/stackcalc`

Then:

```
$ stackcalc 125
0 SB +  1 st + 61

$ stackcalc 4000
2 SB +  8 st + 32
```

Alternatively, using a [Litematica](https://modrinth.com/mod/litematica) materials list export:

```
$ stackcalc ~/.minecraft/config/litematica/material_list_2025-03-12_15.55.29.txt
+--------------------------------------------------------------------+
| Material List for schematic 'desert-house-updown' (1 of 1 regions) |
+-------------------------+------------------------------------------+
| Item                    |                                    Total |
+-------------------------+------------------------------------------+
| Sandstone               |                                1 st + 61 |
| Smooth Sandstone Slab   |                                1 st + 27 |
| Cut Sandstone           |                                1 st + 25 |
| Smooth Sandstone        |                                       25 |
| Spruce Fence            |                                       25 |
| Spruce Button           |                                       22 |
| Campfire                |                                       21 |
| Cut Sandstone Slab      |                                       14 |
| Flower Pot              |                                       14 |
| Sandstone Wall          |                                       13 |
| Sandstone Slab          |                                       11 |
| Barrel                  |                                        8 |
| Bookshelf               |                                        8 |
| Lantern                 |                                        8 |
| Spruce Trapdoor         |                                        6 |
| Chest                   |                                        5 |
| Smooth Sandstone Stairs |                                        4 |
| Brewing Stand           |                                        3 |
| Composter               |                                        2 |
| Sandstone Stairs        |                                        2 |
| Anvil                   |                                        1 |
| Blast Furnace           |                                        1 |
| Cartography Table       |                                        1 |
| Cauldron                |                                        1 |
| Chiselled Sandstone     |                                        1 |
| Furnace                 |                                        1 |
| Grindstone              |                                        1 |
| Smoker                  |                                        1 |
+-------------------------+------------------------------------------+
| Item                    |                                    Total |
+-------------------------+------------------------------------------+
```