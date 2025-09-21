from medical_data_visualizer import draw_cat_plot, draw_heat_map

print("Testing Medical Data Visualizer...")
print("=" * 40)

try:
    print("Creating categorical plot...")
    cat_fig = draw_cat_plot()
    print("✅ Categorical plot saved as 'catplot.png'")
    
    print("Creating correlation heatmap...")
    heat_fig = draw_heat_map()
    print("✅ Heatmap saved as 'heatmap.png'")
    
    print("\n" + "=" * 40)
    print("🎉 SUCCESS! Both visualizations created!")
    print("Check your files for:")
    print("  - catplot.png")
    print("  - heatmap.png")
    
except FileNotFoundError:
    print("❌ ERROR: medical_examination.csv file not found!")
    print("Please make sure you have the dataset file.")
    
except Exception as e:
    print(f"❌ ERROR: {e}")
    print("Check that all required libraries are installed.")
    print("Run: pip install pandas seaborn matplotlib numpy")
