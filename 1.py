import mapnik
m = mapnik.Map(1200,800)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#ff14ff')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Red'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Mellyn',s)
ds = mapnik.Shapefile(file="ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Mellyn')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'cbx.JPEG', 'JPEG')
print "rendered image to 'cbx.JEPG' "