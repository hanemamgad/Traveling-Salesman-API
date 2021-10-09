from flask import Flask, request, jsonify
import math
from sys import maxsize

app = Flask(__name__)

n_coordinates =[]
# points : [[x1,y1], [x2,y2],...,n]

@app.route('/travelingsalesman', methods=['POST'])
def get_coordinates():
    coordinates = request.json['points']
    global n_coordinates
    n_coordinates = coordinates
    distance, path = get_travel_path(coordinates)

    return jsonify({'Shortest distance': distance, 'Shortest path': path})

def get_travel_path(coordinates):
    root_point = coordinates[0]
    min_path = 0
    visited = []
    visited.append(0)
    main_point = root_point
    for point_index in range(len(coordinates[1:])):
        chosen_point, distance = get_shortest_distance(visited, coordinates, main_point)
        visited.append(chosen_point)
        min_path += distance
        main_point = coordinates[chosen_point]
    min_path += math.sqrt(((main_point[0] - root_point[0]) ** 2) + ((main_point[1] - root_point[1]) ** 2))
    path = []
    for i in visited:
        path.append(coordinates[i])
    return min_path, path



def get_shortest_distance(visited, coordinates, point):
    chosen_point = 0
    distance = maxsize
    for i in range(len(coordinates)):
        if i not in visited:
            new_distance = calculate_distance(coordinates[i], point)
            distance = min(distance, new_distance)
            if distance == new_distance:
                chosen_point = i
    return chosen_point, distance

def calculate_distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

if __name__ == '__main__':
    app.run(debug=True)




