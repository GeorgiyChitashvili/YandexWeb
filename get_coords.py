def get_cords(json_response):
    envelope = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["boundedBy"]
    boundary = (envelope['Envelope']['lowerCorner'].split(), envelope['Envelope']['upperCorner'].split())

    delta_x = str(abs(float(boundary[0][0]) - float(boundary[1][0])))
    delta_y = str(abs(float(boundary[0][1]) - float(boundary[1][1])))

    return f'{delta_x},{delta_y}'
