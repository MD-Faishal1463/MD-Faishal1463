import medical_data_visualizer as mdv

# Draw cat plot
cat_fig = mdv.draw_cat_plot()
cat_fig.savefig("catplot.png")

# Draw heat map
heat_fig = mdv.draw_heat_map()
heat_fig.savefig("heatmap.png")
