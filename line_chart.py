import matplotlib.pyplot as plt
x = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

y_des_perf_original_ftask = [421677.9,307470.7,252819.8,220176.2,199502.3,191429.5,186350.8,189484.8,192360.6,193909.0,195809.8,197914.1,197640.5,195355.3,196127.9,194822.7,195087.7,195084.8,196544.5]

y_vga_lcd_original_ftask = [528171.4,370182.1,306499.6,269457.3,246895.6,237343.0,230434.3,237604.9,240142.0,245162.5,245395.4,247973.8,250517.3,248402.3,248389.8,248605.7,247355.4,249497.3,247840.0]

y_tv80_original_ftask = [20566.4,16400.9,13133.5,11477.1,11053.0,12821.4,11613.2,11443.5,13641.1,12645.1,12906.4,11734.2,16238.2,12647.9,15566.6,13310.0,17049.6,13861.8,11964.9]

y_wb_dma_original_ftask = [15951.8,12233.3,10001.1,8672.1,8322.3,10051.8,10778.7,11394.4,11505.1,11713.3,13078.9,10714.0,12375.8,11431.5,10423.3,8517.4,9949.8,9474.4,11101.4]

y_aes_core_original_ftask = [101356.8,74052.9,60201.5,52925.7,47541.1,45150.4,44011.1,42850.7,42679.6,42559.1,42240.2,42156.0,42132.7,42540.4,42553.2,42805.9,42279.4,42490.1,43550.6]

y_ac97_ctrl_original_ftask = [53538.3,37924.9,31673.6,27743.4,24881.1,24327.2,23156.6,22536.7,22508.7,22597.9,22753.2,22442.6,21947.4,24312.7,22402.5,23827.1,21902.8,22122.6,21460.8]

y_des_perf_original_btask = [44903.4,34618.4,30111.8,27218.5,25839.1,24817.4,25169.2,24608.7,24422.4,24131.3,24105.2,23929.9,23203.1,23009.3,22788.1,22365.7,22163.9,21819.1,21706.9]

y_vga_lcd_original_btask = [62947.3,48216.1,41506.6,38015.3,36202.0,34784.2,34216.5,34531.2,33620.4,33581.5,33187.9,32934.3,32618.5,31871.4,31770.3,31302.7,30885.1,30626.7,30437.0]

y_tv80_original_btask = [2123.3,1711.8,1557.1,1446.0,1434.9,1436.4,1394.6,1406.9,1451.3,1406.1,1459.1,1420.6,1428.6,1376.0,1379.8,1324.2,1325.7,1276.8,1257.7]

y_wb_dma_original_btask = [1576.1,1331.1,1236.2,1185.2,1171.1,1197.1,1144.5,1162.0,1211.9,1164.8,1139.3,1111.4,1148.0,1150.4,1101.9,1070.4,1048.4,1043.1,1089.4]

y_aes_core_original_btask = [10128.6,7556.7,6486.0,5844.9,5595.8,5374.0,5350.2,5289.9,5183.2,5186.9,5227.3,5148.2,5063.4,5000.9,4894.3,4832.5,4749.4,4706.1,4678.6]

y_ac97_ctrl_original_btask = [6553.9,5173.2,4509.2,4178.1,4048.7,3990.6,3809.2,3837.0,3872.1,3896.1,3878.5,3809.3,3768.4,3704.8,3661.3,3615.9,3610.9,3552.8,3547.3]

y_des_perf_pftask_only = [522142.3,400239.0,340489.1,302521.3,271906.6,255394.1,239186.2,240950.0,239991.5,241796.4,238930.1,236978.5,240316.7,249287.7,241335.1,242403.9,244203.3,237611.2,259888.6]

y_vga_lcd_pftask_only = [677114.0,540029.1,489602.2,449273.0,417613.5,405858.0,380951.6,396074.2,408844.2,373697.4,423019.0,405642.3,416527.6,407919.1,388740.4,380397.7,378421.4,372109.3,376242.8]

y_tv80_pftask_only = [29305.7,29335.6,26421.5,25796.6,24686.2,24939.7,24509.6,26653.6,24894.2,25985.5,25580.3,27135.9,26644.5,26930.1,24204.3,37506.6,35791.2,34950.2,44707.8]

y_wb_dma_pftask_only = [19946.1,17903.5,15454.2,14114.0,13035.9,12602.8,12107.4,11749.7,12036.6,11305.7,11447.9,11524.6,11063.6,11385.8,11714.7,15727.3,13019.6,22944.1,24789.1]

y_aes_core_pftask_only = [150219.5,133718.0,122016.9,111729.8,104666.7,94075.3,90575.1,85112.5,82424.6,79238.3,74548.3,75418.0,71922.3,70985.0,67818.7,68631.1,69202.5,74182.5,77633.1]

y_ac97_ctrl_pftask_only = [66865.6,53960.2,48880.5,44694.4,41005.2,40615.3,37779.0,39611.7,40347.4,39858.9,38477.6,38628.1,37833.4,39396.1,41497.9,38828.8,39353.6,46342.9,54855.6]

y_des_perf_pbtask_only = [55143.8,56336.7,56863.9,54537.0,54742.7,54361.8,54385.1,54743.4,54583.6,54658.9,54625.1,54487.4,54827.4,54083.6,54479.7,53640.3,53758.2,53188.1,53021.3]

y_vga_lcd_pbtask_only = [82749.4,84656.9,84189.1,83213.4,86981.6,88523.9,89167.2,89332.3,89841.1,89468.8,93501.8,90061.0,91523.5,89050.3,88939.0,89360.3,89599.1,88693.2,90100.5]

y_tv80_pbtask_only = [2836.4,2793.9,2819.2,2839.2,2794.9,2666.5,2707.6,2617.2,2714.1,2685.3,2675.8,2744.6,2583.6,2716.8,2644.2,2657.9,2663.3,2655.7,2638.8]

y_wb_dma_pbtask_only = [1803.3,1810.6,1817.2,1799.6,1757.8,1757.6,1820.7,1845.2,1900.5,1843.8,1912.7,1982.0,1949.5,1863.3,1892.3,1838.9,1792.9,1908.9,1849.6]

y_aes_core_pbtask_only = [14656.4,14536.9,14578.3,14633.0,14649.9,14542.0,14678.7,14511.2,14715.1,14554.5,14546.9,14567.2,14340.8,14481.2,14401.8,14404.1,14253.6,14204.6,14233.3]

y_ac97_ctrl_pbtask_only = [8252.2,8283.5,8172.7,8102.8,8168.6,8002.1,8221.7,8030.9,8163.6,7922.4,8054.1,7909.4,7977.6,7932.6,8006.3,8105.0,7923.5,8196.6,7807.9]

y_des_perf_pbtask_only_schedule = [55905.0,61549.6,55937.3,56086.2,59283.8,58389.4,55750.1,56387.1,57511.0,57251.3,56996.8,55260.6,56681.5,55401.0,55817.8,55936.1,58248.0,56667.1,55238.4]

y_vga_lcd_pbtask_only_schedule = [98347.3,96249.8,94882.6,94091.4,95251.7,94639.4,98051.4,100711.5,98580.0,99171.5,103227.6,98311.0,102345.8,104526.2,100554.1,101762.9,100903.4,100097.7,103652.1]

y_tv80_pbtask_only_schedule = [2961.7,2947.9,2988.8,2957.1,3006.0,2829.1,2836.8,2754.6,2815.2,2814.1,2831.2,2800.1,2758.2,2691.0,2723.3,2737.5,2716.7,2679.9,2780.0]

y_wb_dma_pbtask_only_schedule = [1869.5,1895.5,1710.4,1812.0,1740.1,1771.4,1766.0,1852.6,1871.1,1870.1,1758.3,1758.2,1852.1,1867.0,1969.5,1733.4,1827.1,1750.1,1763.0]

y_aes_core_pbtask_only_schedule = [17883.6,17713.8,17796.2,17639.8,17990.4,17891.3,17751.8,17521.7,17630.0,17765.4,17638.2,18053.6,17626.2,17591.9,17580.5,17591.2,17591.8,17539.8,17523.6]

y_ac97_ctrl_pbtask_only_schedule = [10249.0,10149.6,10189.0,10184.4,10170.4,10090.1,10034.5,10022.1,10149.9,10172.7,10033.2,10010.8,10221.0,10344.2,10025.6,10015.7,9927.0,9869.2,10092.8]

y_des_perf_2queue_pftask_only = [490430.3,352070.8,299058.9,263287.1,236920.6,223586.77777777778,211491.3,217026.1,215818.4,219888.6,221259.2,217482.9,220038.1,219371.7,216865.0,216294.7,216612.7,215920.5,217931.6]

y_vga_lcd_2queue_pftask_only = [606003.5,445268.2,372493.6,328865.8,292188.1,275146.7,268288.6,268598.7,271404.2,269664.7,275223.4,273490.5,276661.3,273618.8,275004.1,275007.2,276564.4,274240.2,275060.9]

y_fix_thread_des_perf_2queue_pftask_only = [465815.3,359219.6,301950.9,267580.1,243248.5,227481.7,214835.6,232110.5,227802.7,226137.6,218233.7,217357.2,213799.5,211652.6,219999.6,225216.9,225911.9,224365.6,221371.88888888888]

y_fix_thread_vga_lcd_2queue_pftask_only = [580694.6,441067.1,367765.6,328216.6,296416.55555555556,281719.7,269521.3,292805.7,286760.1,285753.7,277427.3,278385.5,270966.3,277264.5,281272.3,284827.9,285193.8,284469.7,282761.1]

# -------------------------- fix_thread = 8, ftask comparison vga_lcd-----------------------------------

# Create the first figure and plot the first chart
fig_fix_thread_vga_lcd_ftask = plt.figure()
y_fix_thread_vga_lcd_2queue_pftask_only = [val/1000 for val in y_fix_thread_vga_lcd_2queue_pftask_only]
plt.plot(x, y_fix_thread_vga_lcd_2queue_pftask_only, 's-', color='green', label = 'partitioned ftask + 2queue_schedule')
plt.legend()
plt.xticks(x, x)
plt.xlabel('#partition')
plt.ylabel('runtime(ms)')
plt.title('ftask_vga_lcd, #threads = 8')

# -------------------------------------------------------------------------------------

# -------------------------- fix_thread = 8, ftask comparison des_perf-----------------------------------

# Create the first figure and plot the first chart
fig_fix_thread_vga_lcd_ftask = plt.figure()
y_fix_thread_des_perf_2queue_pftask_only = [val/1000 for val in y_fix_thread_des_perf_2queue_pftask_only]
plt.plot(x, y_fix_thread_des_perf_2queue_pftask_only, 's-', color='green', label = 'partitioned ftask + 2queue_schedule')
plt.legend()
plt.xticks(x, x)
plt.xlabel('#partition')
plt.ylabel('runtime(ms)')
plt.title('ftask_des_perf, #threads = 8')

# -------------------------------------------------------------------------------------

# -------------------------- ftask comparison vga_lcd-----------------------------------

# Create the first figure and plot the first chart
fig_vga_lcd_ftask = plt.figure()
y_vga_lcd_original_ftask = [val/1000 for val in y_vga_lcd_original_ftask]
y_vga_lcd_pftask_only = [val/1000 for val in y_vga_lcd_pftask_only]
y_vga_lcd_2queue_pftask_only = [val/1000 for val in y_vga_lcd_2queue_pftask_only]
plt.plot(x, y_vga_lcd_original_ftask, 'x-', color='red', label = 'original ftask')
plt.plot(x, y_vga_lcd_pftask_only, 'o-', color='blue', label = 'partitioned ftask')
plt.plot(x, y_vga_lcd_2queue_pftask_only, 's-', color='green', label = 'partitioned ftask + 2queue_schedule')
plt.legend()
plt.xticks(x, x)
plt.xlabel('#thread(=#partition)')
plt.ylabel('runtime(ms)')
plt.title('ftask_vga_lcd')

# -------------------------------------------------------------------------------------

# -------------------------- btask comparison vga_lcd-----------------------------------

# Create the first figure and plot the first chart
fig_vga_lcd_btask = plt.figure()
y_vga_lcd_original_btask = [val/1000 for val in y_vga_lcd_original_btask]
y_vga_lcd_pbtask_only = [val/1000 for val in y_vga_lcd_pbtask_only]
y_vga_lcd_pbtask_only_schedule = [val/1000 for val in y_vga_lcd_pbtask_only_schedule]
plt.plot(x, y_vga_lcd_original_btask, 'x-', color='red', label = 'original btask')
plt.plot(x, y_vga_lcd_pbtask_only, 'o-', color='blue', label = 'partitioned btask')
plt.plot(x, y_vga_lcd_pbtask_only_schedule, 's-', color='green', label = 'partitioned btask + levellist_scheduled')
plt.legend()
plt.xticks(x, x)
plt.xlabel('#thread(=#partition)')
plt.ylabel('runtime(ms)')
plt.title('btask_vga_lcd')

# -------------------------------------------------------------------------------------


# -------------------------- ftask comparison des_perf-----------------------------------

# Create the first figure and plot the first chart
fig_des_perf_ftask = plt.figure()
y_des_perf_original_ftask = [val/1000 for val in y_des_perf_original_ftask]
y_des_perf_pftask_only = [val/1000 for val in y_des_perf_pftask_only]
y_des_perf_2queue_pftask_only = [val/1000 for val in y_des_perf_2queue_pftask_only]
plt.plot(x, y_des_perf_original_ftask, 'x-', color='red', label = 'original ftask')
plt.plot(x, y_des_perf_pftask_only, 'o-', color='blue', label = 'partitioned ftask')
plt.plot(x, y_des_perf_2queue_pftask_only, 's-', color='green', label = 'partitioned ftask + 2queue_schedule')
plt.legend()
plt.xticks(x, x)
plt.xlabel('#thread(=#partition)')
plt.ylabel('runtime(ms)')
plt.title('ftask_des_perf')

# -------------------------------------------------------------------------------------

# -------------------------- btask comparison des_perf-----------------------------------

# Create the first figure and plot the first chart
fig_des_perf_btask = plt.figure()
y_des_perf_original_btask = [val/1000 for val in y_des_perf_original_btask]
y_des_perf_pbtask_only = [val/1000 for val in y_des_perf_pbtask_only]
y_des_perf_pbtask_only_schedule = [val/1000 for val in y_des_perf_pbtask_only_schedule]
plt.plot(x, y_des_perf_original_btask, 'x-', color='red', label = 'original btask')
plt.plot(x, y_des_perf_pbtask_only, 'o-', color='blue', label = 'partitioned btask')
plt.plot(x, y_des_perf_pbtask_only_schedule, 's-', color='green', label = 'partitioned btask + levellist_scheduled')
plt.legend()
plt.xticks(x, x)
plt.xlabel('#thread(=#partition)')
plt.ylabel('runtime(ms)')
plt.title('btask_des_perf')

# -------------------------------------------------------------------------------------



# -------------------------- ftask comparison tv80-----------------------------------

# Create the first figure and plot the first chart
fig_tv80_ftask = plt.figure()
plt.plot(x, y_tv80_original_ftask, color='red', label = 'original')
plt.plot(x, y_tv80_pftask_only, color='blue', label = 'partitioned')
plt.legend()
plt.xticks(x, x)
plt.xlabel('#thread(=#partition)')
plt.ylabel('runtime(ms)')
plt.title('ftask_tv80')

# -------------------------------------------------------------------------------------

# -------------------------- btask comparison tv80-----------------------------------

# Create the first figure and plot the first chart
fig_tv80_btask = plt.figure()
plt.plot(x, y_tv80_original_btask, color='red', label = 'original')
plt.plot(x, y_tv80_pbtask_only, color='blue', label = 'partitioned')
plt.plot(x, y_tv80_pbtask_only_schedule, color='green', label = 'partitioned + scheduled')
plt.legend()
plt.xticks(x, x)
plt.xlabel('#thread(=#partition)')
plt.ylabel('runtime(ms)')
plt.title('btask_tv80')

# -------------------------------------------------------------------------------------



# -------------------------- ftask comparison wb_dma-----------------------------------

# Create the first figure and plot the first chart
fig_wb_dma_ftask = plt.figure()
plt.plot(x, y_wb_dma_original_ftask, color='red', label = 'original')
plt.plot(x, y_wb_dma_pftask_only, color='blue', label = 'partitioned')
plt.legend()
plt.xticks(x, x)
plt.xlabel('#thread(=#partition)')
plt.ylabel('runtime(ms)')
plt.title('ftask_wb_dma')

# -------------------------------------------------------------------------------------

# -------------------------- btask comparison wb_dma-----------------------------------

# Create the first figure and plot the first chart
fig_wb_dma_btask = plt.figure()
plt.plot(x, y_wb_dma_original_btask, color='red', label = 'original')
plt.plot(x, y_wb_dma_pbtask_only, color='blue', label = 'partitioned')
plt.plot(x, y_wb_dma_pbtask_only_schedule, color='green', label = 'partitioned + scheduled')
plt.legend()
plt.xticks(x, x)
plt.xlabel('#thread(=#partition)')
plt.ylabel('runtime(ms)')
plt.title('btask_wb_dma')

# -------------------------------------------------------------------------------------



# -------------------------- ftask comparison aes_core-----------------------------------

# Create the first figure and plot the first chart
fig_aes_core_ftask = plt.figure()
plt.plot(x, y_aes_core_original_ftask, color='red', label = 'original')
plt.plot(x, y_aes_core_pftask_only, color='blue', label = 'partitioned')
plt.legend()
plt.xticks(x, x)
plt.xlabel('#thread(=#partition)')
plt.ylabel('runtime(ms)')
plt.title('ftask_aes_core')

# -------------------------------------------------------------------------------------

# -------------------------- btask comparison aes_core-----------------------------------

# Create the first figure and plot the first chart
fig_aes_core_btask = plt.figure()
plt.plot(x, y_aes_core_original_btask, color='red', label = 'original')
plt.plot(x, y_aes_core_pbtask_only, color='blue', label = 'partitioned')
plt.plot(x, y_aes_core_pbtask_only_schedule, color='green', label = 'partitioned + scheduled')
plt.legend()
plt.xticks(x, x)
plt.xlabel('#thread(=#partition)')
plt.ylabel('runtime(ms)')
plt.title('btask_aes_core')

# -------------------------------------------------------------------------------------




# -------------------------- ftask comparison ac97_ctrl-----------------------------------

# Create the first figure and plot the first chart
fig_ac97_ctrl_ftask = plt.figure()
plt.plot(x, y_ac97_ctrl_original_ftask, color='red', label = 'original')
plt.plot(x, y_ac97_ctrl_pftask_only, color='blue', label = 'partitioned')
plt.legend()
plt.xticks(x, x)
plt.xlabel('#thread(=#partition)')
plt.ylabel('runtime(ms)')
plt.title('ftask_ac97_ctrl')

# -------------------------------------------------------------------------------------

# -------------------------- btask comparison ac97_ctrl-----------------------------------

# Create the first figure and plot the first chart
fig_ac97_ctrl_btask = plt.figure()
plt.plot(x, y_ac97_ctrl_original_btask, color='red', label = 'original')
plt.plot(x, y_ac97_ctrl_pbtask_only, color='blue', label = 'partitioned')
plt.plot(x, y_ac97_ctrl_pbtask_only_schedule, color='green', label = 'partitioned + scheduled')
plt.legend()
plt.xticks(x, x)
plt.xlabel('#thread(=#partition)')
plt.ylabel('runtime(ms)')
plt.title('btask_ac97_ctrl')

# -------------------------------------------------------------------------------------















# Display the figures
plt.show()


