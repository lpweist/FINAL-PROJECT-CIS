import folium


def plotmap(iss_decoded):
  map = folium.Map([iss_decoded.sublat, iss_decoded.sublong], zoom_start=4)
  folium.Marker(
      location=[iss_decoded.sublat, iss_decoded.sublong],
      tooltip="Click me!",
      popup="ISS location",
      icon=folium.Icon(color="green"),
  ).add_to(map)
  map.save("map.html")

  return 1
